# Playwright tests

Two suites, one currently active, one a documented skeleton awaiting credentials.

## Active: `test_repo_pages.py`

Hits public GitHub URLs and verifies:

- README renders with a v1.x status badge
- `SKILL.md` is publicly fetchable from `raw.githubusercontent.com`
- Every `references/*.md` linked from SKILL.md is reachable
- The `self-iterate.yml` workflow file exists on `main`
- The Actions tab surfaces the workflow
- `v1.0` and `v1.1` tags are visible

No authentication required. Catches accidental privatization, branch
push failures, and broken release tagging.

Run locally:

```bash
pip install pytest playwright
playwright install chromium
pytest tests/playwright/test_repo_pages.py
```

Run in CI: handled by `.github/workflows/test.yml`.

## Deferred: claude.ai skill discovery

Would automate `claude.ai`, send the 13 test prompts from
`tests/prompts.yaml`, and assert the `intelligent-clay` skill is invoked
on each — testing the *real* discovery path users hit, not the
API-injected path the self-iteration loop uses.

**Why deferred:**

1. **Authentication.** `claude.ai` requires Google/Apple OAuth or email
   magic-link login plus 2FA. Automating this end-to-end is brittle and
   account-bound. The clean approach is a one-time interactive login
   captured to `auth.json` via `playwright codegen`, then reused — but
   that auth state expires and is owner-specific.
2. **Cloudflare bot protection.** Headless Chromium gets challenged.
   `playwright-extra` + `puppeteer-extra-plugin-stealth` mitigates but
   doesn't eliminate the issue.
3. **DOM volatility.** The `claude.ai` UI changes faster than the skill
   does. Skill-banner detection logic would break monthly.

**To enable** (when the value justifies the cost):

1. Run `playwright codegen https://claude.ai` once locally, log in, save
   the storage state to `tests/playwright/.auth/claude-ai.json`.
2. Add `tests/playwright/.auth/` to `.gitignore` (already done).
3. Set repo secret `PLAYWRIGHT_AUTH_STATE` containing the JSON contents
   for CI.
4. Build `test_skill_discovery.py` reading from that state.

Until then, skill discovery is validated manually: roughly once per
release, run a couple of test prompts in `claude.ai` and confirm the
`intelligent-clay` banner appears in the response.

## Local-only artifacts

Don't commit:

- `tests/playwright/.auth/` (auth states)
- `tests/playwright/screenshots/` (captures from failed runs)

Both already in `.gitignore`.
