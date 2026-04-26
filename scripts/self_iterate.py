#!/usr/bin/env python3
"""Autonomous self-iteration loop for Intelligent Clay.

Run weekly via .github/workflows/self-iterate.yml, or manually:

    ANTHROPIC_API_KEY=sk-... python3 scripts/self_iterate.py

What it does:
  1. Loads the test prompts from tests/prompts.yaml.
  2. For each prompt, calls Claude with the current SKILL.md loaded as system
     instructions and captures the model's blueprint output.
  3. Asks Claude (in a second pass) to score each output against the skill's
     own self-check criteria — flagging any gaps where the output deviates
     from spec.
  4. Aggregates the gap analysis across all prompts and asks Claude to
     propose a SKILL.md patch addressing the most common gap.
  5. Writes the patch proposal to a file the GH Action then turns into a PR.

The PR is gated by human review — no autonomous edit lands without a person
merging it. That's intentional. Autonomous editing without a gate would risk
drift.

Outputs (written under runs/<timestamp>/):
  - blueprints.jsonl   — one line per prompt, with input + output
  - gap-analysis.json  — per-prompt gap scores
  - proposed-patch.md  — the SKILL.md improvement Claude wants to make
  - summary.md         — human-readable summary for the PR body

Requires: anthropic>=0.40, pyyaml.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
    from anthropic import Anthropic
except ImportError as e:
    sys.exit(
        f"Missing dependency: {e.name}. Install with: pip install anthropic pyyaml"
    )

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = REPO_ROOT / "SKILL.md"
PROMPTS_YAML = REPO_ROOT / "tests" / "prompts.yaml"
RUNS_DIR = REPO_ROOT / "runs"
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-7")
MAX_TOKENS = 4096


def load_inputs() -> tuple[str, list[dict]]:
    skill = SKILL_MD.read_text()
    with PROMPTS_YAML.open() as f:
        prompts = yaml.safe_load(f)["prompts"]
    return skill, prompts


def run_prompt(client: Anthropic, skill: str, prompt: dict) -> str:
    """Run one test prompt with the current SKILL.md as system instructions."""
    system = (
        "You are simulating Claude Code with the `intelligent-clay` skill loaded. "
        "Apply this skill verbatim to the user's prompt. Return ONLY the response "
        "the user would see — no process commentary.\n\n"
        f"---\nSKILL.md content:\n\n{skill}"
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": prompt["prompt"]}],
    )
    return msg.content[0].text


def score_output(client: Anthropic, skill: str, prompt: dict, output: str) -> dict:
    """Ask Claude to score the output against the skill's self-check."""
    system = (
        "You are a strict reviewer scoring a blueprint against the Intelligent "
        "Clay skill spec. Identify any gap where the output deviates from spec. "
        "Be specific: name the section, name the gap, suggest a one-line fix.\n\n"
        f"---\nSKILL.md:\n\n{skill}\n\n"
        f"---\nExpected mode: {prompt['expected_mode']}\n"
        f"Notes: {prompt.get('notes', '(none)')}"
    )
    review_prompt = (
        f"Test prompt id: {prompt['id']}\n"
        f"Category: {prompt['category']}\n\n"
        f"User input:\n{prompt['prompt']}\n\n"
        f"Skill output:\n{output}\n\n"
        "Return JSON only, no prose:\n"
        '{"id": "...", "passed": bool, "gaps": ["...", ...], '
        '"suggested_fixes": ["...", ...]}'
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": review_prompt}],
    )
    text = msg.content[0].text.strip()
    # Strip markdown fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


def propose_patch(client: Anthropic, skill: str, gap_analysis: list[dict]) -> str:
    """Aggregate gaps and ask Claude to propose a SKILL.md patch."""
    failing = [g for g in gap_analysis if not g.get("passed")]
    if not failing:
        return ""  # nothing to propose

    aggregated_gaps = "\n".join(
        f"- [{g['id']}] {gap}"
        for g in failing
        for gap in g.get("gaps", [])
    )
    aggregated_fixes = "\n".join(
        f"- [{g['id']}] {fix}"
        for g in failing
        for fix in g.get("suggested_fixes", [])
    )

    system = (
        "You are proposing a minimal patch to SKILL.md that addresses recurring "
        "gaps observed across many runs. Output a unified-diff-style markdown "
        "describing the change, focusing on the most-common pattern. Don't "
        "rewrite the whole skill; surgical edits only."
    )
    user = (
        f"Current SKILL.md:\n\n{skill}\n\n"
        f"---\nGaps observed across runs:\n{aggregated_gaps}\n\n"
        f"---\nSuggested fixes (for context):\n{aggregated_fixes}\n\n"
        "Propose ONE surgical change to SKILL.md that addresses the most common "
        "gap pattern. Return: a heading like '## Proposed change', a one-paragraph "
        "rationale, then a diff-style block showing OLD → NEW for the section "
        "you'd edit. Mark the heading clearly. Keep it under 400 words."
    )
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2048,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return msg.content[0].text


def main() -> int:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "ANTHROPIC_API_KEY not set. Skipping self-iteration run "
            "(this is normal in PRs from forks; no secret exposure).",
            file=sys.stderr,
        )
        return 0

    client = Anthropic()
    skill, prompts = load_inputs()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    run_dir = RUNS_DIR / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)

    blueprints_path = run_dir / "blueprints.jsonl"
    gap_path = run_dir / "gap-analysis.json"
    patch_path = run_dir / "proposed-patch.md"
    summary_path = run_dir / "summary.md"

    gap_analysis: list[dict] = []
    with blueprints_path.open("w") as bf:
        for prompt in prompts:
            print(f"  running: {prompt['id']}", file=sys.stderr)
            try:
                output = run_prompt(client, skill, prompt)
                bf.write(json.dumps({"id": prompt["id"], "output": output}) + "\n")
                score = score_output(client, skill, prompt, output)
                gap_analysis.append(score)
            except Exception as e:  # noqa: BLE001
                print(f"  ERROR on {prompt['id']}: {e}", file=sys.stderr)
                gap_analysis.append(
                    {"id": prompt["id"], "passed": False,
                     "gaps": [f"Run failed: {e}"], "suggested_fixes": []}
                )

    gap_path.write_text(json.dumps(gap_analysis, indent=2))

    patch = propose_patch(client, skill, gap_analysis)
    patch_path.write_text(patch or "_No gaps observed; no patch proposed._\n")

    pass_count = sum(1 for g in gap_analysis if g.get("passed"))
    total = len(gap_analysis)
    summary = (
        f"# Self-iteration run — {timestamp}\n\n"
        f"**Pass rate:** {pass_count}/{total}\n\n"
        f"**Detail:** [`gap-analysis.json`]({gap_path.name})\n\n"
        f"**Proposed patch:** [`proposed-patch.md`]({patch_path.name})\n"
    )
    summary_path.write_text(summary)
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
