# Example: Intelligent Clay on Itself (dogfood)

**Test prompt (verbatim):**

> "I'm building Intelligent Clay — a Claude Code skill that helps consultants, coaches, and agencies turn custom service offerings into modular, configurable, build-your-own products. It currently exists as one open-source MIT skill in a public GitHub repo, with reference docs, examples, a self-iteration GitHub Action, and an optional claude-mem memory integration. Right now everyone gets the same skill with no tiers, no paid add-ons, and no configurability. Productize the skill itself."

**Run conditions:** v1.1 SKILL.md loaded, all `references/*.md` available. The agent applied the framework to its own author. This is dogfood — if the skill can produce a credible blueprint of itself, it works on its own author.

---

## Part 1 — Atomic Decomposition

**Deliverables**
- `SKILL.md` core file (the productization engine itself — Parts 1/2/3 + Pricing-Anchor Rule + Anti-Patterns + Self-Check)
- `README.md` (positioning, install, usage, status)
- `LICENSE` (MIT)
- `references/dimensions.md` (six standard dimensions + invention guidance + dependency patterns)
- `references/configurator-output.md` (YAML/JSON spec + tool-mapping table + dependency grammar)
- `references/existing-tier-overlay.md` (overlay-mode spec + protection-section template)
- `references/memory-integration.md` (claude-mem schema + retrieval/ingest spec)
- `examples/brand-strategist.md` (full verbatim run)
- `examples/fitness-coach.md` (full verbatim run)
- `examples/change-management-consultant.md` (full verbatim run)
- `examples/robustness-tests.md` (9-test battery summary)
- Domain-specific worked example pack (per-vertical: agency, coach, freelancer, course creator)
- Anti-pattern gallery (real bad outputs + corrected versions)
- Pricing-anchor benchmark library (domain-by-domain $ ranges)

**Time blocks / live touchpoints**
- 30-min onboarding call ("walk me through your offering")
- 60-min blueprint live-build session (skill run with operator alongside)
- 90-min configurator-output workshop (YAML → Typeform/Webflow)
- 45-min pricing-anchor stress-test call
- Quarterly office-hours drop-in (group)
- 1-on-1 "your offering, my fingers on the keys" engagement (single seat)

**Access tiers**
- Public GitHub repo, file-an-issue (NBD)
- Discord/Slack community channel (~24h peer + maintainer)
- Private Slack Connect with maintainer (same-business-day)
- Direct-line / email priority (4h business-hour SLA)

**Support levels**
- Read-the-README self-serve
- One async blueprint review (markdown comments on the user's run)
- Three-run async review pack
- Live co-build (operator drives skill, user watches)
- Embedded productization partner (recurring monthly)

**Customizations / configurables**
- Vertical specialization (consulting / coaching / agency / freelancer / course / hybrid)
- Mode coverage (default-only / +existing-tier overlay / +hybrid / +single-deliverable)
- Reference-pack depth (3 standard refs / 4 / 4 + private vertical packs)
- Memory substrate (none / claude-mem / claude-mem + Productization Brain knowledge agent)
- Self-iteration cadence (off / monthly GH Action / weekly + human-gated PRs)
- Configurator-output formats (none / YAML / YAML + JSON + Typeform/Tally/Webflow recipes)
- Anti-pattern gallery access (off / read / contribute)
- Beta-program slot (none / observer / contributor / co-author)
- White-label / fork-and-rename rights (off / on)
- Attribution mode (MIT-attribution-appreciated / MIT-only / private fork)

**Add-ons (à-la-carte)**
- Scope/deliverable language drafting (per tier)
- Edge-case stress-test against a named scenario
- Highest-leverage-atom identification
- Pricing validation against competitive set
- Configurator JSON/YAML emit
- Custom domain-specific dimension authoring
- Vertical reference pack (one new vertical, written and merged)
- Self-iteration GH Action setup + tuning
- claude-mem install + Productization Brain seed
- "Bring my last 5 proposals" → batch atomization
- Co-branded fork (badge, vertical-tuned defaults)

---

## Part 2 — Configuration Architecture

| Dimension | What it controls | Levels | Dependencies |
|---|---|---|---|
| **Depth** | How much of the SKILL.md surface area is active | Core-only (default mode) / +Overlay + Hybrid + Single-deliverable / All modes + private vertical packs | Vertical packs require Depth ≥ Standard |
| **Breadth (Mode coverage)** | Which productization modes the skill handles cleanly | Default-only / Default + Overlay / Default + Overlay + Hybrid + Single-deliverable | Overlay mode requires `existing-tier-overlay.md` reference |
| **Support** | Human touchpoints around the skill | Self-serve / Community + 1 async review / Slack Connect + live co-build + office hours | Live co-build requires Support ≥ Standard |
| **Format** | How the user interacts with the offering | Repo-only (markdown) / Repo + configurator YAML emit / Repo + YAML + co-built configurator UI | Configurator UI requires `configurator-output.md` ref + Format ≥ Hybrid |
| **Memory & Self-Improvement** | Persistence and iteration loop | None / claude-mem ingest+retrieve / claude-mem + Productization Brain + GH Action self-iterate | Self-iterate requires memory substrate present |
| **Add-ons** | Modular extensions | Scope-language draft · Edge-case stress-test · Highest-leverage-atom · Pricing validation · Configurator emit · Custom dimension authoring · Vertical pack · GH Action setup · claude-mem seed · Batch-proposal atomization · Co-branded fork | Co-branded fork requires Licensing ≥ White-label |
| **Vertical Specialization** *(domain-specific)* | Which verticals the reference pack and benchmarks are tuned for | Generalist / 1 chosen vertical / 3 chosen verticals / Unlimited | Premium-only above 1 |
| **Beta-Program Participation** *(domain-specific)* | Role in the skill's evolution | None / Observer (read run-log) / Contributor (submit examples) / Co-author (PR rights + roadmap input) | Co-author requires Premium tier |
| **Licensing & Attribution** *(domain-specific)* | Reuse rights | MIT public / MIT + private fork / White-label fork (rename + remove attribution) | White-label requires Premium or BYO ceiling |

**Invalid combinations the configurator must block:**
- Self-iteration loop ON with Memory = None
- Configurator UI co-build with Format = Repo-only
- Vertical packs > 1 without Depth = All modes
- Co-branded fork with Licensing = MIT public
- Beta co-author with Support = Self-serve (no channel to coordinate)
- Live co-build with Format = Repo-only
- Overlay mode requested without `existing-tier-overlay.md` shipped (Breadth ≥ Default+Overlay required)
- Pricing-anchor benchmark library access at Lite (it's the moat)

---

## Part 3 — Three Tiers + Build-Your-Own

| Tier | Price | Configuration | Positioning | Pricing logic (anchor) |
|---|---|---|---|---|
| **Lite — Open Clay** | **$0** (MIT, public) | Depth: Core-only · Breadth: Default mode · Support: Self-serve (GitHub issues) · Format: Repo-only · Memory: None · Vertical: Generalist · Beta: None · Licensing: MIT public | For the curious solo operator who wants to try modularizing one offering without commitment. | Anchored at $0 deliberately — distribution + top-of-funnel. The skill itself is the lead magnet; conversion happens when someone runs it on a real $20K+ engagement and wants the operator's eyes on it. |
| **Core — Workshop Clay** *(flagship)* | **$1,500** one-time (or $150/mo for 12mo) | Depth: +Overlay + Hybrid + Single-deliverable · Breadth: Default + Overlay · Support: Community Slack + 1 async blueprint review · Format: Repo + configurator YAML emit · Memory: claude-mem ingest+retrieve · Vertical: 1 chosen · Beta: Observer · Licensing: MIT + private fork | For the consultant or boutique-agency owner productizing one offering and wanting a human pass on the output before they price it. | Anchored against a single bad pricing decision on a $15–50K engagement (the brand-strategist example). One mispriced tier costs ~$5–10K in margin; $1,500 to de-risk that is ~10–30% of the downside. Sits below a typical pricing-consultant engagement ($5–15K). |
| **Premium — Studio Clay** | **$6,500** one-time + $500/mo retainer | Depth: All modes + private vertical packs · Breadth: Full · Support: Slack Connect 4h SLA + live co-build + quarterly office hours · Format: Repo + YAML + co-built configurator UI · Memory: claude-mem + Productization Brain + GH Action self-iterate · Vertical: 3 chosen · Beta: Contributor (PR rights to examples) · Licensing: White-label fork | For agency owners and 7-figure consultants productizing 2–3 offerings, who want the configurator standing up in Typeform/Webflow and a private vertical pack written for their domain. | Anchored against a productization-consultancy engagement ($25–75K from firms like Productize & Scale, Helping Sells, etc.). Studio Clay does the structural work at <30% of that, plus ongoing self-iteration. Sum-of-parts for the components (live co-build $3K + vertical pack $2K + configurator UI $2.5K + retainer year $6K) ≈ $13.5K — flagship is a discount. |

### Build-Your-Own — "Hand-Pick Your Clay"

- **Base price:** $1,500 (Lite-equivalent productized output: one default-mode run, async)
- **Per-dimension upgrades:**
  - Depth → +Overlay/Hybrid/Single-deliverable: **+$400 each**
  - Breadth → Add Overlay mode: **+$600**
  - Support → Community + 1 async review: **+$500**; Slack Connect 4h: **+$2,000**; Live co-build session: **+$1,500**
  - Format → Configurator YAML emit: **+$750**; co-built configurator UI: **+$2,500**
  - Memory → claude-mem ingest/retrieve: **+$400**; Productization Brain knowledge agent seed: **+$1,200**; GH Action self-iterate: **+$800**
  - Vertical Specialization → +1 vertical pack: **+$1,500/each** (max 3 in BYO; 4+ auto-routes)
  - Beta → Observer: **+$0** (any tier); Contributor: **+$1,000**; Co-author: Premium-only
  - Licensing → Private fork: **+$500**; White-label fork: **+$3,000**
- **Add-ons (à la carte, any tier):**
  - Scope/deliverable language draft per tier: **+$300/tier**
  - Edge-case stress-test: **+$400**
  - Highest-leverage-atom call: **+$500**
  - Pricing validation against named competitors: **+$750**
  - Custom domain-specific dimension authored + merged: **+$1,000**
  - "Bring my last 5 proposals" batch atomization: **+$2,500**

- **Floor:** $1,500 (anything less is just Lite — auto-route to the free MIT repo)
- **Ceiling:** $6,000 — any BYO summed configuration ≥ $6,000 auto-routes to Premium ($6,500 one-time + retainer), because Premium includes the ongoing self-iteration loop and white-label rights that no BYO sum can replicate cleanly

- **Dependencies the configurator must enforce:**
  - Self-iterate add-on requires claude-mem level ≥ ingest/retrieve
  - Configurator UI add-on requires YAML emit selected
  - White-label fork requires BYO total ≥ ceiling (i.e., effectively Premium-only)
  - Vertical packs > 1 require Depth = All modes
  - Live co-build requires Support ≥ Slack Connect
  - Co-author Beta slot blocked in BYO (Premium-tier only)

- **Flagship-protection rule:** The BYO sum to reach Core's configuration must price *above* $1,500 and the BYO sum to reach Premium's configuration must price *above* $6,500. Worked check:
  - **Core-equivalent BYO:** $1,500 base + $400 (Overlay depth) + $400 (Hybrid) + $400 (Single-deliverable) + $600 (Breadth: Overlay) + $500 (1 async review) + $750 (YAML) + $400 (claude-mem) + $1,500 (1 vertical) + $500 (private fork) = **$6,950** vs Core at $1,500 — Core wins decisively (it's the rational discount).
  - **Premium-equivalent BYO:** Premium-equivalent sums to ~$15,000+ before retainer — the BYO ceiling of $6,000 prevents anyone from even attempting it; auto-route to Premium at $6,500 + $500/mo is the only path. Premium wins.

---

> *Meta-observation: the agent invented three domain-specific dimensions for this run — Vertical Specialization, Beta-Program Participation, and Licensing & Attribution — none of which exist in the standard six. v1.1's explicit "invent domain-specific dimensions when the standard six don't capture a key configurable" guidance fired correctly.*
