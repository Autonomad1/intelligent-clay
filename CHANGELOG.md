# Changelog

All notable changes to Intelligent Clay are documented here. The skill follows [semantic versioning](https://semver.org/): major versions break the output format; minor versions add capability while preserving outputs from prior versions; patch versions fix wording and clarifications.

---

## [v1.1] — 2026-04-26

The "make it amazing" release. v1.1 keeps the v1.0 contract (3-part output: atomic decomposition / configuration architecture / tiered packages + BYO) and layers on consistency, dogfooding, and an autonomous self-improvement loop.

### Added

- **Inline example in SKILL.md.** A compressed before/after run on a brand-strategy engagement, kept inside the skill itself so agents see one concrete instance of correct output before producing their own.
- **Pricing-Anchor Rule.** Explicit guidance for when to use $ figures (user gave numbers, or domain norms are well-known) vs. placeholder tokens (`+$A`, `+$B`) when the input is genuinely vague. Prevents the skill from fabricating prices.
- **Existing-tier overlay mode.** Codified as a documented mode triggered by phrases like "without breaking my existing tiers" or "add BYO to my $X / $Y / $Z packages". Preserves existing tiers verbatim, slots BYO underneath/between, and demonstrates flagship protection mathematically. Spec lives in [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
- **Domain-specific dimensions.** Explicit permission (and tests for when) to invent dimensions outside the standard six — e.g., "Discipline Mix" for an agency, "Targeting" for a resume writer, "Tracking Scope" for an SEO retainer.
- **Memory integration via claude-mem.** Optional. When available, the skill saves each run as a tagged observation and queries similar past runs at the start of every blueprint. Spec in [`references/memory-integration.md`](references/memory-integration.md).
- **Configurator output mode.** Optional follow-up that re-emits Parts 2 and 3 as YAML/JSON for paste into Typeform, Webflow, or a custom builder. Schema and tool-mapping table in [`references/configurator-output.md`](references/configurator-output.md).
- **Optional follow-up menu.** Replaces the generic single-line closer with a five-option menu (scope drafting, configurator output, edge-case stress-test, highest-leverage atom, pricing validation).
- **Reference pack.** New top-level [`references/`](references/) directory: `dimensions.md`, `existing-tier-overlay.md`, `configurator-output.md`, `memory-integration.md`.
- **Autonomous self-iteration loop.** GitHub Action ([`.github/workflows/self-iterate.yml`](.github/workflows/self-iterate.yml)) runs every Monday: invokes Claude on the test-prompt battery, scores each output against spec, and opens a PR if a recurring gap is detected. Human-gated — every proposed SKILL.md change requires human review before merge.
- **Test prompt battery.** [`tests/prompts.yaml`](tests/prompts.yaml) — 13 prompts covering primary, edge, stress, breadth, and meta categories, used by both manual regression and the autonomous loop.
- **Beta program.** Documented in [`BETA.md`](BETA.md) with a structured issue template at [`.github/ISSUE_TEMPLATE/beta-feedback.yml`](.github/ISSUE_TEMPLATE/beta-feedback.yml).
- **Dogfood example.** [`examples/intelligent-clay-on-itself.md`](examples/intelligent-clay-on-itself.md) — the skill applied to its own offering. Produces a real Lite/Core/Premium tiering for the skill itself, including white-label rights at Premium.

### Changed

- **Part 2 (Configuration Architecture) now mandates a table.** Earlier outputs varied between bullets and tables; tables are objectively cleaner — table format is now the spec.
- **SKILL.md frontmatter** gained a `version` field for traceability.
- **README example section** points at full transcripts (`examples/*.md`) and includes an abbreviated table excerpt rather than constructed copy.
- **Status section** reflects v1.1 + 12-prompt validation surface (3 primary + 9 robustness + dogfood, all passing).

### Validated

- All 3 primary GREEN tests re-run against v1.1 — output quality improved (table format, explicit flagship-protection math, honest placeholder pricing on vague input).
- Existing-tier overlay test re-run — overlay mode triggered correctly, "How this protects existing tiers" section produced with full math.
- Skill-on-itself dogfood — produced a real tier framework for the skill, invented three domain-specific dimensions (Vertical Specialization, Beta-Program Participation, Licensing & Attribution).

---

## [v1.0] — 2026-04-26

Initial public release.

### Added

- `SKILL.md` with three-part required output (atomic decomposition / configuration architecture / tiers + BYO).
- Three primary test prompts run via TDD-for-skills: brand strategist, fitness coach, change-management consultant. All three GREEN passes are committed verbatim to `examples/`.
- 9-test robustness battery (edge cases, stress conditions, audience breadth) summarized in `examples/robustness-tests.md`.
- README, MIT license, public GitHub repo at https://github.com/Autonomad1/intelligent-clay.
