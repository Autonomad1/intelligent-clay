# Example: Brand Strategist

**Test prompt (verbatim):**
> "I'm a freelance brand strategist. I charge $15K for a 6-week engagement that ends in a brand guide. Help me modularize this."

**Run conditions:** v1.1 SKILL.md loaded. The agent followed the skill verbatim — table format for Part 2, math-verified flagship protection in the BYO framework, and explicit anchoring against current $15K flagship.

---

# Brand Strategy Engagement — Productization Blueprint

## Part 1 — Atomic Decomposition

**Deliverables**
- Brand audit (competitive landscape + internal brand perception synthesis)
- Audience/segment map (1-pager per priority segment)
- Positioning statement (single canonical sentence + rationale memo)
- Messaging hierarchy (tagline · primary message · 3 pillar messages · proof points)
- Voice & tone guide (principles + do/don't examples)
- Naming recommendation (brand, sub-brand, or product)
- Visual direction brief (mood, not execution — handed to designer)
- Brand guide PDF (compiled artifact)
- Internal rollout deck (talking points for the team)
- Agency/handoff package (specs + exportable assets bundle)

**Time blocks**
- 60-min kickoff
- 45-min stakeholder interview (per stakeholder)
- 45-min customer interview (per customer)
- 90-min positioning workshop
- 60-min messaging workshop
- 60-min voice workshop
- 30-min mid-engagement checkpoint
- 60-min final presentation
- 30-min post-delivery office hours (per session)

**Access tiers**
- Async-only (Loom + email, 48hr response)
- Scheduled-only (booked calls inside the engagement window)
- Direct line (Slack Connect / WhatsApp during engagement, 4hr response)

**Support levels**
- 1 revision round per deliverable
- 2 revision rounds per deliverable
- Unlimited revisions inside engagement window
- 30-day post-delivery async review
- 90-day embed (monthly check-in calls)

**Customizations**
- Number of stakeholder interviews (3 / 6 / 10)
- Number of customer interviews (0 / 3 / 6)
- B2B vs. B2C vs. hybrid
- Internal-only vs. agency-handoff-ready
- Single-brand vs. portfolio (master brand + sub-brands)
- Industry vertical depth (generalist vs. specialist research add-on)

---

## Part 2 — Configuration Architecture

| Dimension | What it controls | Levels | Dependencies |
|---|---|---|---|
| Depth | Research thoroughness (interviews + audit rigor) | Light (3 stakeholder, 0 customer) / Standard (6+3) / Deep (10+6) | Sprint pace blocked at Deep |
| Breadth | Brand-system scope | Verbal-only (positioning + messaging + voice) / +Visual direction / Full system (incl. naming) | Naming requires Breadth ≥ +Visual |
| Pace | Calendar | Sprint (2w) / Standard (6w) / Extended (10w) | Sprint blocks Deep depth and Unlimited revisions |
| Format | Deliverable polish | Working docs / Branded PDF guide / Guide + rollout deck + handoff package | Handoff package requires Breadth = Full system |
| Support | Revisions + access | 1 round / 2 rounds / Unlimited within window | Unlimited blocked on Sprint |
| Continuity | Post-delivery presence | None / 30-day async / 90-day embed | 90-day embed requires Format ≥ Branded PDF |
| Portfolio Scope | Brands covered | Single brand / Master + 1 sub-brand / Master + 2-3 sub-brands | Each additional sub-brand multiplies Depth minimums |

**Invalid combinations the configurator must block**
- Sprint pace + Deep depth
- Sprint pace + Unlimited support
- Naming add-on without Breadth ≥ +Visual
- Agency-handoff-ready format without Full system breadth
- 90-day embed on Working-docs format
- Portfolio Scope > Single brand on Sprint pace
- Customer interviews > 0 without Standard or Deep depth

---

## Part 3 — Three Tiers + Build-Your-Own

| Tier | Configuration | Positioning line | Price | Pricing logic |
|---|---|---|---|---|
| **Lite — Positioning Sprint** | Depth: Light · Breadth: Verbal-only · Pace: Sprint (2w) · Format: Working docs · Support: 1 round · Continuity: None · Portfolio: Single | For early-stage founders who need a defensible positioning statement and core messaging fast — not a brand guide. | **$6,500** | ~43% of flagship; priced against the cost of a bad positioning bet (one wasted ad month). Sits well below the $15K anchor so it never cannibalizes Core. |
| **Core — Brand Guide** *(flagship)* | Depth: Standard · Breadth: +Visual direction · Pace: Standard (6w) · Format: Branded PDF guide · Support: 2 rounds · Continuity: None · Portfolio: Single | For Series A/B teams ready to operationalize a brand — the guide their next designer, marketer, and agency will all build from. | **$15,000** | User's current anchor. Senior-strategist-only delivery at half the cost of a typical $25–50K agency engagement; the rational default. |
| **Premium — Brand System + Embed** | Depth: Deep · Breadth: Full system (incl. naming) · Pace: Extended (10w) · Format: Guide + rollout deck + handoff package · Support: Unlimited within window · Continuity: 90-day embed · Portfolio: Single or Master+1 | For funded teams launching/relaunching a brand who need naming, a full handoff-ready system, and a strategist on-call through rollout. | **$32,000** | Below sum-of-parts (Core $15K + naming ~$8K + embed ~$12K + handoff ~$5K = ~$40K) and below the floor of consultancy retainers (~$45K+). |

### Build-Your-Own framework

**Base price:** $6,500 (Lite configuration)

**Per-dimension upgrade pricing:**
- Depth: Light → Standard **+$3,500** · Standard → Deep **+$5,000**
- Breadth: Verbal → +Visual **+$2,500** · +Visual → Full system (naming) **+$5,500**
- Pace: Sprint → Standard **+$1,500** · Standard → Extended **+$2,500**
- Format: Working docs → Branded PDF **+$1,500** · Branded PDF → Guide + deck + handoff **+$3,500**
- Support: 1 round → 2 rounds **+$1,500** · 2 rounds → Unlimited **+$3,000**
- Continuity: 30-day async **+$2,500** · 90-day embed **+$9,000**
- Portfolio: +1 sub-brand **+$6,000** each

**Floor:** $6,500 (Lite). Below this, refuse — output isn't defensible.
**Ceiling:** $28,000. Above this, auto-route to Premium ($32K flagship is cheaper than the BYO equivalent).

**Configurator-enforced dependencies:**
- Block Sprint+Deep, Sprint+Unlimited, Sprint+Portfolio>1
- Block Naming without Breadth ≥ +Visual
- Block Handoff format without Full system breadth
- Block 90-day embed on Working-docs format
- Block customer interviews unless Depth ≥ Standard

**Flagship-protection check (verified):**
- BYO to reach Core config: $6,500 + $3,500 (Std depth) + $2,500 (+Visual) + $1,500 (Std pace) + $1,500 (PDF) + $1,500 (2 rounds) = **$16,500** > $15,000 flagship ✓
- BYO to reach Premium config: $6,500 + $3,500 + $5,000 + $2,500 + $5,500 + $2,500 + $1,500 + $3,500 + $1,500 + $3,000 + $9,000 = **$44,000** > $32,000 flagship ✓

Flagships remain the rational discount.
