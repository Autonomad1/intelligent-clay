"""Static validation of SKILL.md.

Verifies the file the entire repo orbits around is well-formed: YAML
frontmatter parses, required fields are present, the description follows
the documented "Use when..." convention, required H2 sections exist, and
word count sits inside the documented sanity range.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = REPO_ROOT / "SKILL.md"
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)

REQUIRED_FRONTMATTER_FIELDS = {"name", "description", "version"}
REQUIRED_SECTIONS = {
    "When to Use",
    "Required Output",
    "Pricing-Anchor Rule",
    "Anti-Patterns",
    "Self-Check Before Responding",
}
WORD_COUNT_MIN = 500
WORD_COUNT_MAX = 1500


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL_MD.read_text()


@pytest.fixture(scope="module")
def parsed(skill_text: str) -> tuple[dict, str]:
    match = FRONTMATTER_PATTERN.match(skill_text)
    assert match, "SKILL.md must start with YAML frontmatter delimited by ---"
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    return frontmatter, body


def test_frontmatter_parses(parsed):
    frontmatter, _ = parsed
    assert isinstance(frontmatter, dict), "Frontmatter must parse to a dict"


def test_frontmatter_has_required_fields(parsed):
    frontmatter, _ = parsed
    missing = REQUIRED_FRONTMATTER_FIELDS - set(frontmatter.keys())
    assert not missing, f"Missing required frontmatter fields: {missing}"


def test_name_format(parsed):
    """Skill names must be letters/numbers/hyphens only — no spaces or special chars."""
    frontmatter, _ = parsed
    name = frontmatter["name"]
    assert re.fullmatch(r"[a-z0-9-]+", name), (
        f"name must match [a-z0-9-]+, got: {name!r}"
    )


def test_description_starts_with_use_when(parsed):
    """Per writing-skills CSO guidance, description should start with 'Use when'."""
    frontmatter, _ = parsed
    description = frontmatter["description"]
    assert description.lower().startswith("use when"), (
        "description must start with 'Use when' to focus on triggering conditions"
    )


def test_description_under_max_length(parsed):
    """Frontmatter total has a 1024-char ceiling per agentskills.io spec."""
    frontmatter, _ = parsed
    description = frontmatter["description"]
    # Soft cap at 800 to leave room for other fields within 1024 total.
    assert len(description) < 800, (
        f"description is {len(description)} chars; keep under 800 for safety "
        "within the 1024-char frontmatter ceiling"
    )


def test_version_is_semver_like(parsed):
    frontmatter, _ = parsed
    version = str(frontmatter["version"])
    assert re.fullmatch(r"\d+\.\d+(\.\d+)?", version), (
        f"version should look like 1.0 or 1.0.0, got: {version!r}"
    )


def test_required_sections_present(parsed):
    _, body = parsed
    headings = re.findall(r"^##+\s+(.+?)$", body, re.MULTILINE)
    headings_normalized = [h.strip() for h in headings]
    for required in REQUIRED_SECTIONS:
        matches = [h for h in headings_normalized if required in h]
        assert matches, (
            f"Required section '{required}' not found. Headings present: "
            f"{headings_normalized}"
        )


def test_three_part_output_documented(parsed):
    """Part 1, Part 2, Part 3 must all be documented as required output."""
    _, body = parsed
    for n in (1, 2, 3):
        pattern = rf"Part\s+{n}\s*[—\-]"
        assert re.search(pattern, body), (
            f"Part {n} of the required output structure is missing"
        )


def test_word_count_in_range(skill_text):
    word_count = len(skill_text.split())
    assert WORD_COUNT_MIN <= word_count <= WORD_COUNT_MAX, (
        f"SKILL.md word count is {word_count}; expected "
        f"{WORD_COUNT_MIN}-{WORD_COUNT_MAX} for the v1.x format"
    )


def test_table_format_mandated_for_part_2(parsed):
    """v1.1 mandates a table format for Part 2. Verify the rule is stated."""
    _, body = parsed
    # The rule appears in the Part 2 heading or its body
    part_2_match = re.search(
        r"Part\s+2.+?(?=Part\s+3|\Z)", body, re.DOTALL
    )
    assert part_2_match, "Part 2 section not found"
    part_2_section = part_2_match.group(0).lower()
    assert "table" in part_2_section, (
        "Part 2 must explicitly mention table format (v1.1 requirement)"
    )


def test_pricing_anchor_rule_three_levels(parsed):
    """The Pricing-Anchor Rule is a 3-row table covering input quality."""
    _, body = parsed
    heading_idx = body.find("Pricing-Anchor Rule")
    assert heading_idx != -1, "Pricing-Anchor Rule heading not found"
    # Slice from the heading to the next H2 (exactly two #'s + space, not H3+)
    section = body[heading_idx:]
    next_h2 = re.search(r"\n## [^#]", section)
    if next_h2:
        section = section[: next_h2.start()]
    table_rows = [
        line for line in section.splitlines()
        if line.startswith("|") and "---" not in line
    ]
    # header row + at least 3 data rows = 4 minimum
    assert len(table_rows) >= 4, (
        f"Pricing-Anchor Rule table must have 3+ data rows; got "
        f"{max(0, len(table_rows) - 1)}"
    )


def test_optional_followup_menu_exists(parsed):
    """v1.1 introduces the 5-option follow-up menu."""
    _, body = parsed
    assert "Follow-Up" in body or "follow-up" in body.lower(), (
        "Optional follow-up menu section is missing"
    )


def test_referenced_files_exist(parsed):
    """Every references/*.md file linked from SKILL.md must exist."""
    _, body = parsed
    refs = re.findall(r"references/[\w-]+\.md", body)
    for ref in set(refs):
        path = REPO_ROOT / ref
        assert path.exists(), f"Referenced file does not exist: {ref}"
