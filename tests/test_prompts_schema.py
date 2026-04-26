"""Schema validation for tests/prompts.yaml.

The autonomous self-iteration loop reads this file. Schema errors here
break the loop silently — these tests catch them before merge.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_YAML = REPO_ROOT / "tests" / "prompts.yaml"

REQUIRED_FIELDS = {"id", "category", "expected_mode", "prompt"}
VALID_CATEGORIES = {"primary", "edge", "stress", "breadth", "meta"}
VALID_MODES = {"produce", "refuse"}


@pytest.fixture(scope="module")
def prompts() -> list[dict]:
    with PROMPTS_YAML.open() as f:
        data = yaml.safe_load(f)
    assert "prompts" in data, "Top-level key 'prompts' missing"
    assert isinstance(data["prompts"], list), "'prompts' must be a list"
    return data["prompts"]


def test_prompts_not_empty(prompts):
    assert len(prompts) > 0, "tests/prompts.yaml has no prompts"


def test_each_prompt_has_required_fields(prompts):
    for prompt in prompts:
        missing = REQUIRED_FIELDS - set(prompt.keys())
        assert not missing, f"Prompt {prompt.get('id', '?')} missing fields: {missing}"


def test_prompt_ids_are_unique(prompts):
    ids = [p["id"] for p in prompts]
    duplicates = {i for i in ids if ids.count(i) > 1}
    assert not duplicates, f"Duplicate prompt ids: {duplicates}"


def test_prompt_ids_are_kebab_case(prompts):
    import re

    for prompt in prompts:
        pid = prompt["id"]
        assert re.fullmatch(r"[a-z0-9-]+", pid), (
            f"Prompt id must be kebab-case [a-z0-9-]+, got: {pid!r}"
        )


def test_categories_valid(prompts):
    for prompt in prompts:
        assert prompt["category"] in VALID_CATEGORIES, (
            f"Prompt {prompt['id']}: invalid category {prompt['category']!r}; "
            f"must be one of {VALID_CATEGORIES}"
        )


def test_expected_modes_valid(prompts):
    for prompt in prompts:
        assert prompt["expected_mode"] in VALID_MODES, (
            f"Prompt {prompt['id']}: invalid expected_mode "
            f"{prompt['expected_mode']!r}; must be one of {VALID_MODES}"
        )


def test_prompt_text_nontrivial(prompts):
    """Every prompt should have meaningful text — not empty, not a placeholder."""
    for prompt in prompts:
        text = prompt["prompt"].strip()
        assert len(text) >= 30, (
            f"Prompt {prompt['id']} is too short ({len(text)} chars); "
            "real prompts should be at least a couple of sentences"
        )
        assert not text.lower().startswith("todo"), (
            f"Prompt {prompt['id']} appears to be a TODO placeholder"
        )


def test_each_category_represented(prompts):
    """The loop is meaningful only if each category has at least one prompt."""
    categories_present = {p["category"] for p in prompts}
    missing = VALID_CATEGORIES - categories_present
    assert not missing, (
        f"No prompts for categories: {missing}. The self-iteration loop's "
        "coverage shrinks if any category is empty."
    )
