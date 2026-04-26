---
name: intelligent-clay
description: Use when productizing, modularizing, packaging, or repackaging a service — turning consulting, coaching, agency, freelance, or done-for-you offerings into configurable, tiered, build-your-own products. Triggers on phrases like "too custom to scale", "add tiers", "build-your-own version", "turn my service into a product", "modularize my offering", or "scale without doing more 1-on-1 work".
version: 1.2
---

# Intelligent Clay

Services are clay. This skill produces ONE thing: the **structural blueprint** for productizing a service. Not marketing copy, not positioning, not a roadmap. Structure only.

## When to Use

Apply when the user describes a service-based offering they want to modularize, package, productize, or make build-your-own.

**Out of scope (refuse + redirect):**
- Pure SaaS / software (already modular)
- Pure physical products (use SKU/bundle logic instead)
- Marketing copy or positioning (use offer-extraction or Dunford-style skills)
- Product roadmap / discovery (use a PM skill)

**Modes:**
- **Default mode** — fresh productization. Output: 3 tiers (Lite/Core/Premium, or renamed in the offering's vocabulary) + BYO.
- **Existing-tier overlay mode** — user already has tiers and wants BYO without breaking them. Preserve existing tiers exactly; slot BYO **underneath** the cheapest and **between** existing tiers; prove each existing tier still wins on price vs. its BYO-summed equivalent. See [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
- **Hybrid offerings** (service + product) — decompose the service portion only; the product is one fixed atom.
- **Single-deliverable services** ("I write resumes") — atomize by *process steps* and *variables* (turnaround, depth, format, revision count).

## Required Output (always 3 parts, in order)

### Part 1 — Atomic Decomposition

Flat bullet list, grouped by atom type. Each atom must pass: *could a customer buy just this and get value?* Phases ("Discovery") are bundles, not atoms; "60-min stakeholder interview" is.

- **Deliverables** — artifacts produced
- **Time blocks** — sessions, calls, sprints, with duration
- **Access tiers** — channels and response time
- **Support levels** — revisions, office hours, async review
- **Customizations** — variables (industry focus, depth, pace, etc.)

### Part 2 — Configuration Architecture (always a table)

Render as a table, one row per dimension:

| Dimension | What it controls | Levels | Dependencies |
|-----------|------------------|--------|--------------|

Standard dimensions: Depth, Breadth, Pace, Format, Support, Add-ons. Definitions and standard levels in [`references/dimensions.md`](references/dimensions.md). **Invent domain-specific dimensions** when the standard six don't capture a key configurable — examples that emerged from real runs: "Discipline Mix" (creative agency), "Targeting" (resume writer), "Tracking Scope" (SEO retainer).

Below the table: **Invalid combinations the configurator must block** as a flat bullet list.

### Part 3 — Three Tiers + Build-Your-Own

Three packages. Not two. Not five. Use Lite/Core/Premium, or rename in the brand's vocabulary (Foundation/Signature/Elite, Studio Lite/Core/Premium). For each tier:

- **Configuration** — level on each dimension
- **Positioning line** — one sentence: who it's for, what they get
- **Pricing logic** — what the price is anchored against (see Pricing-Anchor Rule below)

Then a **Build-Your-Own framework**:

- **Base price** (typically Lite) + **per-dimension upgrade pricing**
- **Floor** (minimum viable) and **Ceiling** (above which auto-route to Premium or custom)
- **Dependencies the configurator must enforce**
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.

### Pricing-Anchor Rule

| Input quality | Anchor approach |
|---------------|-----------------|
| User gave concrete prices | Use $ figures; anchor each tier against them |
| Domain norms are well-known **at the named sub-niche level** (exec coaching, brand strategy, SEO retainers, technical resume writing) | Use $ figures from those benchmarks |
| Generic category only ("coaching", "consulting", "design", "marketing") with no sub-niche named | Treat as vague — use placeholder tokens |
| Truly vague input | Use placeholder tokens (`+$A`, `+$B`, `+$C`) — do not fabricate |

**Bright line:** "coaching" alone is vague; "executive coaching for Series B founders" is anchored. When in doubt, use tokens and offer to re-anchor once the niche is named. Never invoke norms for the parent category to justify specific dollar figures.

**Vague-input preamble:** When using placeholder tokens, open with a one-line assumption stub, not a complaint. Format:

> *Assuming [generic-but-plausible reading of the offering]; will re-anchor with $ figures once you name [the specific variable that would unlock norms].*

Do not lampshade the vagueness ("you've given me almost nothing", "this is hard to answer") — infer, stub, produce.

## Inline Example (compressed)

**Input:** "$15K, 6-week brand strategy engagement ending in a brand guide."

**Part 1 (excerpt):**
- *Deliverables:* brand audit · positioning statement · voice guide · brand guide PDF · naming recommendation
- *Time blocks:* 60-min kickoff · 45-min stakeholder interview · 90-min positioning workshop
- *Customizations:* # interviews (3/6/10), B2B vs B2C, internal-only vs agency-handoff-ready

**Part 2 (excerpt):**

| Dimension | What it controls | Levels | Dependencies |
|---|---|---|---|
| Depth | Interview thoroughness | Light / Standard / Deep | Sprint pace blocked at Deep |
| Breadth | Brand-system scope | Verbal-only / +Visual / Full system | Naming add-on requires +Visual |
| Pace | Calendar | Sprint (2w) / Standard (6w) / Deep (10w) | — |

**Part 3 (excerpt):**

| Tier | Price | Anchor |
|---|---|---|
| Lite — Positioning Sprint | $6,500 | ~40% of flagship; cost-of-bad-positioning entry point |
| Core — Brand Guide *(flagship)* | $15,000 | Senior-strategist-only at half typical agency engagements ($25–50K) |
| Premium — Brand System + Embed | $32,000 | Below consultancy retainer + naming sum-of-parts (~$45K) |

BYO: $6,500 base + per-dimension upgrades; floor $6,500; ceiling $28,000 routes to Premium; configurator blocks Sprint+Deep, Async+Deep, Naming without Visual.

## Anti-Patterns

| Failure | Why it's wrong |
|---------|----------------|
| Five tiers instead of three + BYO | Decision paralysis; undermines anchor |
| Skipping Part 2 entirely | Most common naive failure |
| Listing phases as atoms | Phases are bundles, not atoms |
| Marketing/positioning advice | Out of scope; refer to other skills |
| Asking clarifying questions before producing | Infer, produce, then offer to refine |
| Summing module prices to flagship exactly | Flagship must feel like a discount vs. parts |

## Self-Check Before Responding

Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?

## Memory Integration (Optional)

If `claude-mem` (or equivalent persistent memory) is available, **before** producing the blueprint, query for past runs in the same domain. If 2+ similar past runs exist, prepend a one-line memory preamble:

> *Memory note: I've seen N similar offerings ([verticals]). Load-bearing dimensions historically: [list]. Applying as starting hypotheses; will diverge where this offering differs.*

**After** producing the blueprint, save the run as a tagged observation (`intelligent-clay:run`) with domain, vertical, dimensions used, invented dimensions, anchor strategy, and notable dependencies. Full schema and integration spec in [`references/memory-integration.md`](references/memory-integration.md).

If memory is unavailable, omit the preamble silently. Never fail or refuse because memory isn't there.

## Optional Follow-Up Menu

After delivering, offer **one** based on context:

- **Scope/deliverable language** drafting for any tier
- **Configurator output mode** — re-emit Parts 2 and 3 as JSON/YAML for paste into Typeform/Webflow/custom builder. See [`references/configurator-output.md`](references/configurator-output.md)
- **Edge-case stress-test** — apply dimensions to a concrete extreme scenario the user names
- **Highest-leverage atom** identification — which 1–2 atoms, if standardized, unlock the most BYO velocity
- **Pricing validation** — sanity-check each tier's anchor against the user's competitive set
