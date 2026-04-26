# Example: 1-on-1 Fitness Coach

**Test prompt (verbatim):**
> "I run a fitness coaching business — 1-on-1 only. I want a build-your-own version."

**Run conditions:** Real run of the `intelligent-clay` skill on a fresh agent. Notable: a baseline agent (without the skill) responded by asking 4 clarifying questions instead of producing structure. The skill-loaded agent inferred from context and produced the full blueprint below.

---

# Intelligent Clay Blueprint — 1-on-1 Fitness Coaching

## Part 1 — Atomic Decomposition

- 60-min initial assessment call (movement screen, goals, history, baseline metrics)
- Custom training program document (4-week block, PDF or app-delivered)
- Custom nutrition plan (macros + meal framework, not full meal plan)
- Full meal plan with grocery list (separate from macro framework)
- Weekly 1-on-1 coaching call (30 min, video)
- Bi-weekly 1-on-1 coaching call (30 min, video)
- Monthly progress review call (60 min, video, with plan recalibration)
- Form-check video review (async, per submission, 24-hr turnaround)
- Form-check video review (async, per submission, 48-hr turnaround)
- Voxer / WhatsApp daily messaging access
- Email-only async access (48-hr response SLA)
- Slack/Discord channel access (community + coach drop-ins)
- Weekly written check-in form + coach written response
- Workout log review (weekly, async written feedback)
- Body composition / progress photo review (bi-weekly)
- Wearable data review (Whoop, Garmin, Oura — weekly summary)
- Program rewrite (mid-cycle pivot if goals change)
- Pre-built program library access (templates by goal: hypertrophy, fat loss, strength, endurance)
- Recipe / meal-prep video library access
- Mobility / warm-up routine library access
- One-time supplement protocol consult (30 min)
- One-time injury / return-to-training consult (30 min)
- Travel / hotel-gym workout adaptation (per request)
- Race or event peaking block (4–8 week specialist plan)
- Quarterly InBody / DEXA interpretation session

## Part 2 — Configuration Architecture

| Dimension | What it controls | Levels |
|-----------|------------------|--------|
| **Depth** | Customization of training + nutrition | L1: template-matched / L2: customized program, macro framework / L3: fully bespoke program + full meal plan |
| **Pace of iteration** | How often the plan is re-tuned | Monthly / Bi-weekly / Weekly |
| **Coach access** | Channel + responsiveness | Async-only (email, 48-hr) / Voxer-style daily messaging / Voxer + scheduled calls |
| **Call cadence** | Live 1-on-1 time | None / Monthly 60-min / Bi-weekly 30-min / Weekly 30-min |
| **Form-check volume** | Async video reviews per month | 0 / 4 per month / unlimited (fair-use 12) |
| **Data review** | Inputs the coach actively monitors | Self-reported only / Logs + photos / Logs + photos + wearable |
| **Add-ons** | Specialist modules layered on | Event-peaking block, return-to-training consult, DEXA review, travel adaptations |

**Dependencies (configurator must enforce):**
- Weekly call cadence requires Voxer + scheduled calls access (not async-only).
- Depth L3 (fully bespoke + full meal plan) requires Bi-weekly or Weekly pace — bespoke plans go stale at monthly pace.
- Wearable data review requires Bi-weekly pace or faster (weekly data with monthly review is wasted).
- Unlimited form-checks requires Voxer-tier access (channel must exist for delivery).
- Event-peaking add-on requires Depth L2 minimum (cannot peak off a template).

**Invalid pairs:** Async-only access + Weekly calls; Monthly pace + Wearable review; Template depth + Event-peaking.

## Part 3 — Tiered Packages + Build-Your-Own

### Foundation — "Self-Driven with a Coach in the Wings"
- **Configuration:** Depth L1 (template-matched) · Monthly pace · Async email access (48-hr) · Monthly 60-min call · 0 form-checks · Self-reported data only
- **Positioning:** For the disciplined client who needs structure and expert guardrails, not hand-holding. One real call a month, a program that fits their goal, and a coach reachable by email.
- **Pricing logic:** Anchored against a quality group-coaching app subscription (~$50–80/mo) plus the marginal cost of one real coaching hour — should price meaningfully above app-only since there's a human, but well below 1-on-1 bespoke.

### Signature — "True 1-on-1, Without the Premium Ceiling"
- **Configuration:** Depth L2 (custom program + macro framework) · Bi-weekly pace · Voxer daily messaging · Bi-weekly 30-min calls · 4 form-checks/mo · Logs + photos reviewed
- **Positioning:** For the client who wants a coach who actually knows them — custom programming, regular live time, and a messaging line for the in-the-moment questions that matter.
- **Pricing logic:** Anchored against the prevailing 1-on-1 online coaching market rate (typically $300–600/mo). This is the "default 1-on-1 product" and should land mid-market — it's the comparison everyone makes.

### Elite — "Full Concierge"
- **Configuration:** Depth L3 (fully bespoke program + full meal plan) · Weekly pace · Voxer + scheduled calls · Weekly 30-min calls · Unlimited form-checks · Logs + photos + wearable · Includes 1 add-on/quarter (DEXA, peaking block, etc.)
- **Positioning:** For the client whose results justify a coach embedded in their week — wearable-informed, fully bespoke, and on-call. Replaces an in-person trainer + nutritionist for clients who travel or want privacy.
- **Pricing logic:** Anchored against the realistic alternative — an in-person personal trainer 3x/week ($400–600/mo) plus a registered dietitian retainer ($200–400/mo). Elite should price below that combined cost while delivering more continuity.

### Build-Your-Own
- **Base price:** Foundation configuration as the floor.
- **Per-dimension upgrade pricing:**
  - Depth L1 → L2: meaningful step (custom programming labor)
  - Depth L2 → L3: largest single step (full meal plan + bespoke is the heaviest deliverable)
  - Pace Monthly → Bi-weekly: moderate step; Bi-weekly → Weekly: moderate step
  - Access Async → Voxer: moderate step (this is where attention cost lives)
  - Calls: priced per call slot per month, declining marginal price after the second
  - Form-checks: priced per 4-pack; unlimited is a flat upgrade gated on Voxer access
  - Wearable review: small flat add-on, gated on Bi-weekly+
  - Specialist add-ons (peaking block, return-to-training, DEXA): one-time fees on top of any tier
- **Floor (minimum viable bundle):** Depth L1 + Monthly pace + Async access + 1 monthly call. Below this it's a template sale, not coaching.
- **Ceiling (route to Elite or custom quote):** Any BYO that combines Depth L3 + Weekly pace + Voxer + Weekly calls + Wearable review should auto-route to Elite — don't let BYO undercut the flagship.
- **Dependencies enforced by configurator:**
  - Block: Async-only + any Weekly cadence
  - Block: Monthly pace + Wearable review
  - Block: Template depth + Event-peaking add-on
  - Block: Unlimited form-checks without Voxer access
  - Require: Depth L3 implies Bi-weekly pace minimum
- **Pricing principle:** The sum of BYO modules to reach the Signature configuration should price ~10–15% above Signature, and the sum to reach Elite should price ~15–25% above Elite. The flagships must remain the rational choice for clients who want "the whole thing."
