# Example: Change Management Consultant

**Test prompt (verbatim):**
> "I'm a consultant who does change management for mid-market companies. Each engagement is custom. Productize this."

**Run conditions:** Real run of the `intelligent-clay` skill on a fresh agent. The skill produced 24 atomic components, 6 dimensions with explicit dependencies, and a 3-tier + BYO framework with EBITDA-anchored pricing for the flagship.

---

### Part 1 — Atomic Decomposition

- 60-min stakeholder interview (single)
- 90-min executive sponsor alignment session
- Current-state organizational assessment doc
- Change readiness diagnostic (survey + scored report)
- Stakeholder map / influence matrix
- Resistance risk register
- Communications plan document
- Single broadcast comms artifact (email template, town hall script, FAQ)
- Manager enablement playbook
- Frontline training module (90-min, single topic)
- Train-the-trainer session (half-day)
- Change champion network design doc
- Adoption metrics dashboard (KPIs + tracking spec)
- Pulse survey instrument (single deployment)
- Weekly steering committee call (60 min)
- Bi-weekly working session with PMO (90 min)
- Async Slack/Teams office hours (per week, fixed cap)
- Email-only review turnaround (48-hr SLA)
- Async deliverable review (per artifact, 2 revisions)
- On-call escalation line (per month)
- Post-go-live retrospective workshop (half-day)
- 30/60/90-day adoption check-in call
- Sustainment coaching call (per leader, 45 min)
- Industry-specific case library reference pack
- Methodology overlay selection (Prosci ADKAR / Kotter / hybrid)

### Part 2 — Configuration Architecture

**Depth — how thorough the diagnostic and design phase is**
- Levels: Light (5 interviews, 1 readiness survey) / Standard (12 interviews, survey + 2 focus groups) / Deep (25+ interviews, survey + focus groups + ethnographic observation)
- Dependency: Deep depth required if org headcount > 1,500 or > 3 business units in scope

**Breadth — how much of the change lifecycle is covered**
- Levels: Diagnostic-only / Diagnostic + Plan / Plan + Enablement / Full lifecycle (Diagnostic → Plan → Enablement → Sustainment)
- Dependency: Sustainment cannot be selected without Enablement

**Pace — engagement duration**
- Levels: Sprint (4 weeks) / Standard (10 weeks) / Extended (6 months)
- Dependency: Sprint pace invalid with Deep depth or Full-lifecycle breadth

**Format — how delivery happens**
- Levels: Async-led (docs + recorded modules + email review) / Hybrid (mostly async + key live sessions) / Live-led (on-site or live-virtual throughout)
- Dependency: Live-led required if executive sponsor sessions exceed 4

**Support — access level during engagement**
- Levels: Scheduled-only (booked sessions, 48-hr email) / + Async office hours (Slack/Teams, weekly cap) / + On-call retainer (named escalation line, same-day)
- Dependency: On-call retainer requires Pace = Standard or Extended

**Add-ons — extensions on top of base**
- Train-the-trainer
- Change champion network build
- Adoption dashboard build
- Pulse survey series (3-pack)
- 30/60/90 sustainment check-ins
- Executive 1:1 coaching block (per leader)
- Methodology overlay (ADKAR or Kotter formalization)
- Dependency: Pulse series and Sustainment check-ins require Breadth ≥ Plan + Enablement

### Part 3 — Tiered Packages + Build-Your-Own

**Lite — "Change Readiness Sprint"**
- Configuration: Depth = Light, Breadth = Diagnostic-only, Pace = Sprint (4 wks), Format = Async-led, Support = Scheduled-only, Add-ons = none
- Positioning: For mid-market leaders who suspect a change initiative will stall and need a fast, evidence-based read on readiness, risks, and the right intervention shape — before committing budget.
- Pricing logic: Anchored against the cost of one failed change rollout (commonly 1–3% of payroll in lost productivity for a 500-person org); priced as a fraction of a single quarter of that loss.

**Core — "Change Program Blueprint"**
- Configuration: Depth = Standard, Breadth = Diagnostic + Plan, Pace = Standard (10 wks), Format = Hybrid, Support = + Async office hours, Add-ons = Methodology overlay
- Positioning: For mid-market companies with a confirmed change in motion (system implementation, restructure, M&A integration) that need a credentialed plan, comms architecture, and manager playbook ready to execute.
- Pricing logic: Anchored against the loaded cost of a 10-week internal change PMO (typically 1.5–2 FTEs at director level + tooling); priced at parity-or-below to make insourcing economically irrational.

**Premium — "Full-Lifecycle Change Partner"**
- Configuration: Depth = Deep, Breadth = Full lifecycle, Pace = Extended (6 mo), Format = Live-led, Support = + On-call retainer, Add-ons = Train-the-trainer + Champion network + Adoption dashboard + 30/60/90 check-ins
- Positioning: For mid-market executives leading a high-stakes transformation (ERP, post-merger ops, org redesign) where adoption failure is existential and they need a partner embedded from diagnosis through sustainment.
- Pricing logic: Anchored against the EBITDA-at-risk of the underlying transformation (typically 5–15% of the program's projected value capture); priced as insurance against adoption shortfall.

**Build-Your-Own Framework**
- Base price: Lite configuration (Diagnostic-only, Light depth, Sprint, Async-led, Scheduled-only)
- Per-dimension upgrade pricing:
  - Depth: Light → Standard (+50% of base) / Standard → Deep (+75% of base)
  - Breadth: + Plan (+1.0× base) / + Enablement (+1.25× base) / + Sustainment (+0.5× base)
  - Pace: Sprint = included / Standard (+15%) / Extended (+30%) — pace is a multiplier on engagement load, not a discount
  - Format: Async-led = included / Hybrid (+20%) / Live-led (+40%)
  - Support: Scheduled = included / + Async office hours (+10%) / + On-call retainer (+25%)
  - Add-ons: each priced as a fixed module (Train-the-trainer, Champion network, Dashboard, Pulse 3-pack, 30/60/90, Exec coaching block, Methodology overlay)
- Floor: Must include at least Diagnostic-only Breadth at Light depth — no à-la-carte add-ons without a base engagement
- Ceiling: Any configuration with Deep depth + Full lifecycle + On-call retainer must route to Premium (or scoped custom); the configurator should not let BYO exceed Premium without explicit override
- Dependencies the configurator must enforce:
  - Sprint pace blocked when Depth = Deep or Breadth = Full lifecycle
  - Sustainment blocked unless Enablement is selected
  - On-call retainer blocked when Pace = Sprint
  - Pulse series and 30/60/90 check-ins blocked unless Breadth ≥ Plan + Enablement
  - Live-led format auto-selected when executive sponsor sessions > 4
- Pricing rule: the sum of à-la-carte upgrades to reach the Premium configuration should land ~15–20% above Premium's flagship price, so the Premium tier remains the rational choice for buyers who want everything.
