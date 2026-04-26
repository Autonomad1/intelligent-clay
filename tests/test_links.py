"""Markdown link checker.

Walks every .md file in the repo (excluding generated runs/) and verifies
that relative links resolve to existing files. External http(s) links are
not checked — that's a different concern.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"runs", ".github"}  # generated/ephemeral content not author-controlled
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _all_markdown_files() -> list[Path]:
    files = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.relative_to(REPO_ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def _collect_relative_links(path: Path) -> list[tuple[str, str]]:
    """Return (text, target) for each non-external link in the file."""
    text = path.read_text()
    out = []
    for match in LINK_PATTERN.finditer(text):
        link_text, target = match.group(1), match.group(2).strip()
        # Skip external links and anchors
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Strip any in-page anchor
        target_no_anchor = target.split("#", 1)[0]
        if not target_no_anchor:
            continue
        out.append((link_text, target_no_anchor))
    return out


@pytest.mark.parametrize(
    "path", _all_markdown_files(), ids=lambda p: str(p.relative_to(REPO_ROOT))
)
def test_relative_links_resolve(path: Path):
    broken: list[str] = []
    for text, target in _collect_relative_links(path):
        # Resolve the link relative to the file's directory
        candidate = (path.parent / target).resolve()
        if not candidate.exists():
            broken.append(f"  [{text}]({target}) -> {candidate}")
    assert not broken, (
        f"{path.relative_to(REPO_ROOT)} has broken relative links:\n"
        + "\n".join(broken)
    )
