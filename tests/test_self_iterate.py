"""Unit tests for scripts/self_iterate.py.

The script orchestrates the autonomous self-iteration loop. We mock the
Anthropic client so tests run instantly with no API key required, and
exercise: missing-key graceful exit, gap aggregation, JSON-with-fences
robustness, no-failure short-circuit, and end-to-end run.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "self_iterate.py"


def _load_script_module(monkeypatch, fake_anthropic_client):
    """Load self_iterate.py as a module with a stubbed anthropic SDK."""
    # Stub the anthropic module before import
    fake_module = types.ModuleType("anthropic")
    fake_module.Anthropic = MagicMock(return_value=fake_anthropic_client)
    monkeypatch.setitem(sys.modules, "anthropic", fake_module)

    # Force a fresh import
    spec = importlib.util.spec_from_file_location("self_iterate", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["self_iterate"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fake_client():
    return MagicMock()


def _msg(text: str) -> MagicMock:
    """Build a fake anthropic response shaped like Messages API."""
    block = MagicMock()
    block.text = text
    return MagicMock(content=[block])


def test_no_api_key_exits_gracefully(monkeypatch, fake_client, capsys):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    module = _load_script_module(monkeypatch, fake_client)
    rc = module.main()
    assert rc == 0, "Should exit 0 when ANTHROPIC_API_KEY is missing"
    err = capsys.readouterr().err
    assert "ANTHROPIC_API_KEY not set" in err


def test_score_output_strips_markdown_fences(monkeypatch, fake_client):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    module = _load_script_module(monkeypatch, fake_client)

    payload = {"id": "x", "passed": True, "gaps": [], "suggested_fixes": []}
    fenced = f"```json\n{json.dumps(payload)}\n```"
    fake_client.messages.create.return_value = _msg(fenced)

    result = module.score_output(
        fake_client,
        skill="(skill body)",
        prompt={"id": "x", "category": "primary", "expected_mode": "produce",
                "prompt": "test", "notes": ""},
        output="(model output)",
    )
    assert result == payload


def test_propose_patch_short_circuits_on_all_pass(monkeypatch, fake_client):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    module = _load_script_module(monkeypatch, fake_client)

    all_passed = [
        {"id": "a", "passed": True, "gaps": [], "suggested_fixes": []},
        {"id": "b", "passed": True, "gaps": [], "suggested_fixes": []},
    ]
    result = module.propose_patch(fake_client, skill="(skill)", gap_analysis=all_passed)
    assert result == "", (
        "When all prompts pass, propose_patch must return empty string and not "
        "call the API"
    )
    fake_client.messages.create.assert_not_called()


def test_propose_patch_aggregates_failures(monkeypatch, fake_client):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    module = _load_script_module(monkeypatch, fake_client)

    fake_client.messages.create.return_value = _msg("## Proposed change\n...")
    failures = [
        {"id": "a", "passed": False, "gaps": ["bug 1"], "suggested_fixes": ["fix 1"]},
        {"id": "b", "passed": True, "gaps": [], "suggested_fixes": []},
        {"id": "c", "passed": False, "gaps": ["bug 2"], "suggested_fixes": ["fix 2"]},
    ]
    result = module.propose_patch(fake_client, skill="(skill)", gap_analysis=failures)
    assert result.startswith("## Proposed change")

    # Verify the user message included only the failing prompts' gaps
    call_args = fake_client.messages.create.call_args
    user_msg = call_args.kwargs["messages"][0]["content"]
    assert "bug 1" in user_msg
    assert "bug 2" in user_msg
    assert "[a]" in user_msg
    assert "[c]" in user_msg
    assert "[b]" not in user_msg, "Passing prompts shouldn't appear in the patch ask"


def test_main_end_to_end_with_two_prompts(monkeypatch, tmp_path, fake_client):
    """End-to-end: main() runs all prompts, scores, proposes patch, writes outputs."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    # Stand up a fake repo layout
    fake_skill = tmp_path / "SKILL.md"
    fake_skill.write_text("---\nname: test\nversion: 1.0\n---\n# fake\n")
    fake_tests = tmp_path / "tests"
    fake_tests.mkdir()
    fake_prompts = fake_tests / "prompts.yaml"
    fake_prompts.write_text(
        "prompts:\n"
        "  - id: a\n"
        "    category: primary\n"
        "    expected_mode: produce\n"
        "    prompt: test prompt a\n"
        "  - id: b\n"
        "    category: edge\n"
        "    expected_mode: refuse\n"
        "    prompt: test prompt b\n"
    )

    module = _load_script_module(monkeypatch, fake_client)

    # Point the module at our fake repo
    monkeypatch.setattr(module, "SKILL_MD", fake_skill)
    monkeypatch.setattr(module, "PROMPTS_YAML", fake_prompts)
    monkeypatch.setattr(module, "RUNS_DIR", tmp_path / "runs")

    # Three calls per prompt: blueprint + score; then 1 patch call.
    # 2 prompts * 2 = 4 + 1 patch = 5 calls
    score_a = json.dumps({"id": "a", "passed": True, "gaps": [],
                          "suggested_fixes": []})
    score_b = json.dumps({"id": "b", "passed": False, "gaps": ["missed redirect"],
                          "suggested_fixes": ["add explicit refusal example"]})

    fake_client.messages.create.side_effect = [
        _msg("# blueprint a"),
        _msg(score_a),
        _msg("# blueprint b (bad)"),
        _msg(score_b),
        _msg("## Proposed change\nclean up refusal section"),
    ]

    rc = module.main()
    assert rc == 0

    runs = list((tmp_path / "runs").iterdir())
    assert len(runs) == 1, "Exactly one run directory should be created"
    run_dir = runs[0]

    # Outputs landed
    assert (run_dir / "blueprints.jsonl").exists()
    assert (run_dir / "gap-analysis.json").exists()
    assert (run_dir / "proposed-patch.md").exists()
    assert (run_dir / "summary.md").exists()

    # Gap analysis matches what we fed
    parsed = json.loads((run_dir / "gap-analysis.json").read_text())
    assert len(parsed) == 2
    ids = {p["id"] for p in parsed}
    assert ids == {"a", "b"}

    # Patch was proposed since b failed
    patch = (run_dir / "proposed-patch.md").read_text()
    assert "Proposed change" in patch

    # Summary reports 1/2 pass rate
    summary = (run_dir / "summary.md").read_text()
    assert "1/2" in summary
