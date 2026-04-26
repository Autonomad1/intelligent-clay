# Dimensions reference

The six standard dimensions used in Part 2 (Configuration Architecture) of the Intelligent Clay blueprint, plus guidance on when to invent domain-specific dimensions.

## The six standard dimensions

| Dimension | What it controls | Common levels |
|-----------|------------------|---------------|
| **Depth** | How thorough the work is — # interviews, # iterations, # revisions, # research artifacts | Light · Standard · Deep |
| **Breadth** | How much scope is covered — verbal vs. visual, single-topic vs. whole-life, single-system vs. integrated | Often three named tiers describing what's included |
| **Pace** | Calendar duration and cadence | Sprint · Standard · Deep / Extended |
| **Format** | How the work is delivered | Async · Hybrid · Live-led |
| **Support** | Access and responsiveness — channels, SLAs, revisions, office hours | Email-NBD · Slack-24h · Direct-line-4h, plus revision counts |
| **Add-ons** | Modular extensions on top of any base configuration | List of à-la-carte items, each priced independently |

Use only the dimensions that fit. Some offerings have natural Pace dimensions but no meaningful Breadth dimension; others reverse it. Don't force all six.

## When to invent a domain-specific dimension

Add a new dimension when the user's offering has a configurable variable that **doesn't map cleanly onto any of the six**, but materially changes the price/scope/positioning of the engagement.

Tests:
1. Does varying this control change what the customer gets, not just how it's delivered?
2. Could a customer reasonably want one level over another for non-budget reasons?
3. Would two of the six standard dimensions duplicate this if you tried to express it through them?

If yes to any of these — invent the dimension.

## Examples from real runs

| Domain | Invented dimension | Why standard six didn't fit |
|--------|--------------------|-----------------------------|
| Boutique creative agency | **Discipline Mix** (strategy / design / copy / motion — choose any subset) | Breadth is about *scope within one craft*, not *which crafts* are active |
| Resume writer | **Targeting** (single role / role family / multi-track) | Specific to job-search artifacts; not Depth, not Breadth |
| SEO retainer | **Tracking Scope** (10 KW / 30 / 100 / unlimited) | A unit-count variable native to the domain |
| Fitness coaching | **Form-check volume** (0 / 4 / unlimited per month) | Quantitative add-on volume that needs its own gating |
| Change management | **Methodology overlay** (ADKAR / Kotter / hybrid) | A categorical choice, not a level on a scale |

Naming the dimension well matters — readers should understand what it controls without reading the levels.

## Common dependency patterns

- **Pace × Depth conflicts:** Sprint pace usually invalid with Deep depth (no time for thorough work).
- **Format × Breadth requirements:** Multi-stakeholder breadth usually requires Live or Hybrid format (async can't coordinate live alignment).
- **Support × Cadence requirements:** High-touch support (Slack same-day, on-call) usually requires Standard or Extended pace (not viable on Sprint).
- **Add-on prerequisites:** Specialist add-ons (compliance overlay, executive coaching, peaking blocks) usually require a baseline depth or breadth — gate them.
- **Cross-channel mismatches:** Async-only access incompatible with weekly live calls, or with same-day SLA.

When a dimension's level is unsafe without another dimension's level, state it explicitly in the Dependencies column rather than relying on the configurator UI to figure it out.
