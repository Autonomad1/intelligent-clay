# Example: Brand Strategist

**Test prompt (verbatim):**
> "I'm a freelance brand strategist. I charge $15K for a 6-week engagement that ends in a brand guide. Help me modularize this."

**Run conditions:** Real run of the `intelligent-clay` skill on a fresh agent with the skill loaded as the only directive. No editorialization or post-processing — this is the verbatim output.

---

# Intelligent Clay — Brand Strategy Engagement

## Part 1 — Atomic Decomposition

**Deliverables**
- Brand audit document (current state assessment)
- Competitive landscape map (5 / 10 / 15 competitors profiled)
- Customer/stakeholder interview synthesis report
- Positioning statement (single page)
- Messaging hierarchy (tagline, elevator pitch, boilerplate, value props)
- Brand voice & tone guide (principles + do/don't examples)
- Naming recommendation (product, feature, or sub-brand)
- Visual identity direction (mood boards, not full system)
- Brand guide PDF (the flagship artifact)
- One-page brand summary (executive cheat sheet)
- Launch/rollout playbook (how to operationalize the guide)

**Time blocks**
- 60-min kickoff workshop
- 45-min stakeholder interview (per person)
- 30-min customer interview (per person)
- 90-min positioning workshop (live, with leadership)
- 60-min messaging workshop
- 45-min review/feedback session (per round)
- 60-min handoff session with internal team or external designer

**Access tiers**
- Email-only response (48-hr turnaround)
- Slack/Loom async (24-hr turnaround)
- Voxer + scheduled weekly call
- Direct line during business hours

**Support levels**
- Single-pass delivery (no revisions)
- 1 round of revisions per deliverable
- 2 rounds of revisions per deliverable
- Async review of internal team's work for 30 / 60 / 90 days post-engagement
- Office hours retainer (2 hrs/month for 3 months)

**Customizations**
- Industry depth (generalist vs. vertical-specialized research)
- Number of stakeholder interviews (3 / 6 / 10)
- Number of customer interviews (0 / 5 / 10)
- B2B vs. B2C framing
- Solo founder vs. leadership-team engagement model
- Internal-only guide vs. agency-handoff-ready guide

---

## Part 2 — Configuration Architecture

**Depth** — How thorough the inputs are
- Levels: Light (3 stakeholder interviews, 0 customer) / Standard (6 stakeholder, 5 customer) / Deep (10 stakeholder, 10 customer + competitive deep-dive)

**Breadth** — How much of the brand system is covered
- Levels: Verbal-only (positioning + messaging + voice) / Verbal + Visual Direction (adds mood boards & visual principles) / Full System (adds naming + rollout playbook)

**Pace** — Calendar duration
- Levels: Sprint (2 weeks) / Standard (6 weeks) / Deep (10 weeks)
- Dependency: Sprint pace is invalid with Deep depth (cannot run 10 customer interviews in 2 weeks); Sprint requires Light depth.

**Format** — How the work is delivered
- Levels: Async (Loom + docs, no live workshops) / Hybrid (kickoff + positioning live, rest async) / Live-led (all workshops live)
- Dependency: Async format invalid with Deep depth (synthesis requires live calibration).

**Support** — Access and revisions
- Levels: Single-pass / Standard (1 revision round + email) / High-touch (2 revision rounds + Slack + 60-day async review)

**Add-ons** (atomic, à la carte)
- Naming sprint (+1 deliverable)
- Customer interview pack of 5 (+ depth without changing tier)
- Designer-handoff session (60-min + annotated guide)
- 90-day office-hours retainer
- Executive one-pager
- Launch/rollout playbook (if not already in Breadth)

**Invalid combinations to block**
- Sprint pace + Deep depth
- Async format + Deep depth
- Verbal-only breadth + Naming add-on (naming requires at least Verbal + Visual)

---

## Part 3 — Tiered Packages + Build-Your-Own

### Lite — "Positioning Sprint" — $6,500
- **Configuration:** Depth: Light / Breadth: Verbal-only / Pace: Sprint (2 wks) / Format: Async / Support: Single-pass
- **Positioning line:** For early-stage founders who need a defensible positioning statement and core messaging fast — not a full brand guide.
- **Pricing logic:** Anchored against the cost of a bad positioning bet (months of wasted launch spend) and roughly 40% of the flagship — clearly the entry point.

### Core — "Brand Guide" — $15,000 *(current flagship)*
- **Configuration:** Depth: Standard / Breadth: Verbal + Visual Direction / Pace: Standard (6 wks) / Format: Hybrid / Support: Standard (1 revision round)
- **Positioning line:** For funded startups and growth-stage teams who need a complete brand guide their internal team or agency can execute against.
- **Pricing logic:** Anchored against typical agency brand engagements ($25-50K) — positioned as the senior-strategist-only version at roughly half the price.

### Premium — "Brand System + Embed" — $32,000
- **Configuration:** Depth: Deep / Breadth: Full System (incl. naming + rollout playbook) / Pace: Deep (10 wks) / Format: Live-led / Support: High-touch (2 revisions + 60-day async review)
- **Positioning line:** For Series A+ companies rebranding or launching a new product line, where the strategist stays embedded through rollout.
- **Pricing logic:** Anchored against the cost of a brand consultancy retainer ($40-75K) plus the saved cost of a separate naming engagement ($10-15K). Sum-of-parts feels like ~$45K; tier prices at a discount.

---

### Build-Your-Own Framework

**Base price:** $6,500 (Lite configuration)

**Per-dimension upgrades (additive):**
- Depth: Light → Standard +$3,500 / Standard → Deep +$5,000
- Breadth: Verbal-only → +Visual +$2,500 / +Visual → Full System +$4,500
- Pace: Sprint → Standard +$0 / Standard → Deep +$2,000 (calendar premium)
- Format: Async → Hybrid +$1,500 / Hybrid → Live-led +$3,000
- Support: Single-pass → Standard +$1,500 / Standard → High-touch +$3,500

**Add-ons (flat):**
- Naming sprint: +$4,000
- Customer interview pack (5): +$2,500
- Designer-handoff session: +$1,200
- 90-day office-hours retainer: +$3,600
- Executive one-pager: +$800
- Launch/rollout playbook (standalone): +$2,500

**Floor:** $6,500 — below this, the engagement isn't worth the context-switching cost.

**Ceiling:** $28,000 — above this, route to Premium or a custom scope conversation; configurator should not silently sell something that needs hand-holding.

**Dependencies the configurator must enforce:**
- Block: Sprint pace + Standard or Deep depth
- Block: Async format + Deep depth
- Block: Naming add-on when Breadth = Verbal-only
- Require: Live-led format if Depth = Deep
- Note: Sum-of-parts at Premium configuration intentionally exceeds $32K — the tier is the discount.
