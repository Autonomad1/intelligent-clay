"""Static validation of every example transcript in examples/.

Each example is a real or representative run of the skill. We verify it
follows the documented 3-part structure so the docs stay honest as the
skill evolves.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = REPO_ROOT / "examples"

# robustness-tests.md is a meta summary, not a single blueprint, so it has
# different structural rules.
META_EXAMPLES = {"robustness-tests.md"}


def _example_files() -> list[Path]:
    return sorted(p for p in EXAMPLES_DIR.glob("*.md") if p.is_file())


@pytest.mark.parametrize("path", _example_files(), ids=lambda p: p.name)
def test_example_has_test_prompt_block(path: Path):
    text = path.read_text()
    if path.name in META_EXAMPLES:
        return  # meta files have a different structure
    assert "Test prompt" in text, (
        f"{path.name} must include a 'Test prompt' block citing the verbatim input"
    )


@pytest.mark.parametrize("path", _example_files(), ids=lambda p: p.name)
def test_example_has_three_parts(path: Path):
    text = path.read_text()
    if path.name in META_EXAMPLES:
        return
    for n in (1, 2, 3):
        pattern = rf"Part\s+{n}\s*[—\-]"
        assert re.search(pattern, text), (
            f"{path.name} must contain Part {n} heading"
        )


@pytest.mark.parametrize("path", _example_files(), ids=lambda p: p.name)
def test_part_2_uses_table(path: Path):
    text = path.read_text()
    if path.name in META_EXAMPLES:
        return
    # Pull out the Part 2 section
    part_2_match = re.search(
        r"Part\s+2.+?(?=Part\s+3|\Z)", text, re.DOTALL
    )
    assert part_2_match, f"{path.name}: Part 2 section not found"
    part_2 = part_2_match.group(0)
    pipe_lines = [ln for ln in part_2.splitlines() if ln.strip().startswith("|")]
    assert len(pipe_lines) >= 3, (
        f"{path.name}: Part 2 must use a table (got {len(pipe_lines)} table rows)"
    )


@pytest.mark.parametrize("path", _example_files(), ids=lambda p: p.name)
def test_part_3_has_byo(path: Path):
    """Part 3 must include BYO framework, not just the three tiers."""
    text = path.read_text()
    if path.name in META_EXAMPLES:
        return
    part_3_match = re.search(r"Part\s+3.+", text, re.DOTALL)
    assert part_3_match, f"{path.name}: Part 3 section not found"
    part_3 = part_3_match.group(0).lower()
    assert "build-your-own" in part_3 or "byo" in part_3, (
        f"{path.name}: Part 3 must include a Build-Your-Own framework"
    )


@pytest.mark.parametrize("path", _example_files(), ids=lambda p: p.name)
def test_part_3_has_floor_and_ceiling(path: Path):
    """The BYO framework must define Floor and Ceiling per spec."""
    text = path.read_text()
    if path.name in META_EXAMPLES:
        return
    part_3_match = re.search(r"Part\s+3.+", text, re.DOTALL)
    assert part_3_match, f"{path.name}: Part 3 section not found"
    part_3_lower = part_3_match.group(0).lower()
    assert "floor" in part_3_lower, f"{path.name}: BYO must define a Floor"
    assert "ceiling" in part_3_lower, f"{path.name}: BYO must define a Ceiling"
