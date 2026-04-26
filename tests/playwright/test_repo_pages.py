"""Playwright smoke tests for the public-facing GitHub repo pages.

Verifies the README renders, key files are reachable, and the
self-iteration workflow + tags exist publicly. These tests catch
broken links or accidentally private content the static checkers
wouldn't notice.

Run locally:

    pip install pytest playwright
    playwright install chromium
    pytest tests/playwright/

Skipped automatically in CI if PLAYWRIGHT_BROWSERS_PATH is unset and
Chromium isn't installed (the CI workflow installs it explicitly).
"""

from __future__ import annotations

import os
import shutil
from typing import Iterator

import pytest

playwright = pytest.importorskip("playwright.sync_api")
from playwright.sync_api import Page, sync_playwright  # noqa: E402

REPO_URL = "https://github.com/Autonomad1/intelligent-clay"
RAW_BASE = "https://raw.githubusercontent.com/Autonomad1/intelligent-clay/main"


def _chromium_available() -> bool:
    """Best-effort: are Playwright browsers installed?"""
    if shutil.which("chromium") or shutil.which("chrome"):
        return True
    if os.environ.get("PLAYWRIGHT_BROWSERS_PATH"):
        return True
    # Fall back to trying — the test will skip via fixture if launch fails
    return True


pytestmark = pytest.mark.skipif(
    not _chromium_available(), reason="Playwright Chromium not available"
)


@pytest.fixture(scope="module")
def page() -> Iterator[Page]:
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
        except Exception as e:  # noqa: BLE001
            pytest.skip(f"Could not launch Chromium: {e}")
        context = browser.new_context(
            user_agent="intelligent-clay-tests/1.0 (+https://github.com/Autonomad1/intelligent-clay)"
        )
        page = context.new_page()
        yield page
        browser.close()


def test_repo_homepage_renders(page: Page):
    response = page.goto(REPO_URL, wait_until="domcontentloaded", timeout=30_000)
    assert response and response.status == 200, "Repo homepage must return 200"
    # README contents render server-side
    page.wait_for_selector("article.markdown-body", timeout=10_000)
    content = page.locator("article.markdown-body").inner_text()
    assert "Intelligent Clay" in content
    assert "Stable v1" in content, "Status badge should mention v1.x"


def test_skill_md_is_publicly_fetchable(page: Page):
    """The skill itself must be reachable without auth."""
    response = page.goto(f"{RAW_BASE}/SKILL.md", timeout=30_000)
    assert response and response.status == 200, (
        "SKILL.md must be publicly fetchable from raw.githubusercontent.com"
    )
    body = page.content()
    assert "intelligent-clay" in body
    assert "Atomic Decomposition" in body


def test_references_are_reachable(page: Page):
    """Each references/*.md the skill links to must be fetchable."""
    refs = [
        "dimensions.md",
        "configurator-output.md",
        "existing-tier-overlay.md",
        "memory-integration.md",
    ]
    for ref in refs:
        url = f"{RAW_BASE}/references/{ref}"
        response = page.goto(url, timeout=30_000)
        assert response and response.status == 200, f"Missing or private: {url}"


def test_workflow_file_is_present(page: Page):
    """The self-iteration workflow must exist on main."""
    url = f"{RAW_BASE}/.github/workflows/self-iterate.yml"
    response = page.goto(url, timeout=30_000)
    assert response and response.status == 200, "self-iterate workflow missing"
    body = page.content()
    assert "self-iterate" in body
    assert "ANTHROPIC_API_KEY" in body


def test_actions_page_lists_self_iterate(page: Page):
    """The Actions tab must surface the self-iterate workflow."""
    page.goto(f"{REPO_URL}/actions", wait_until="domcontentloaded", timeout=30_000)
    page.wait_for_load_state("networkidle", timeout=15_000)
    content = page.content()
    assert "self-iterate" in content, (
        "self-iterate workflow not visible on the Actions tab"
    )


def test_v1_tag_exists(page: Page):
    """v1.0 and v1.1 release tags must be public."""
    page.goto(f"{REPO_URL}/tags", wait_until="domcontentloaded", timeout=30_000)
    page.wait_for_load_state("networkidle", timeout=15_000)
    content = page.content()
    assert "v1.0" in content, "v1.0 tag missing"
    assert "v1.1" in content, "v1.1 tag missing"
