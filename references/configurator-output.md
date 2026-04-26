# Configurator output mode

When the user wants to actually build a configurator UI (Typeform, Webflow, a custom builder, a SaaS like Pricing.io), re-emit Parts 2 and 3 of the blueprint as a structured machine-readable spec rather than prose.

## When to use

Offer this mode in the optional follow-up menu when:

- The user explicitly mentions building a checkout, configurator, or pricing page
- The user mentions a specific tool (Typeform, Tally, Webflow, Stripe, etc.)
- The blueprint has 6+ dimensions or many add-ons (manual UI build is unsafe without a spec)

## Output structure

Emit a single YAML document with three top-level keys: `dimensions`, `tiers`, `byo`. JSON is also acceptable; YAML is preferred because it's checkout-tool-friendly.

### YAML schema

```yaml
dimensions:
  - id: depth
    name: Depth
    description: Interview thoroughness and iteration count
    levels:
      - id: light
        name: Light
        description: 3 stakeholder interviews, 0 customer
        delta_price: 0
      - id: standard
        name: Standard
        description: 6 stakeholder, 5 customer
        delta_price: 3500
      - id: deep
        name: Deep
        description: 10 stakeholder, 10 customer + competitive deep-dive
        delta_price: 8500
  - id: breadth
    name: Breadth
    # ...

dependencies:
  - rule: block
    when: { depth: deep, pace: sprint }
    message: "Sprint pace cannot accommodate Deep depth"
  - rule: require
    when: { format: live_led }
    needs: { depth: deep }
  - rule: auto_upgrade
    when: { breadth: full_system }
    sets: { format: hybrid }

tiers:
  - id: lite
    name: "Lite — Positioning Sprint"
    price: 6500
    config:
      depth: light
      breadth: verbal_only
      pace: sprint
      format: async
      support: single_pass
    positioning: "For early-stage founders who need defensible positioning fast — not a full brand guide."
    pricing_anchor: "~40% of flagship; cost-of-bad-positioning entry point"
  - id: core
    # ...

byo:
  base_price: 6500
  base_config: lite
  add_ons:
    - id: naming_sprint
      name: Naming sprint
      price: 4000
      requires: { breadth: { gte: visual } }
    - id: customer_interviews_5
      name: Customer interview pack (5)
      price: 2500
  floor: 6500
  ceiling: 28000
  ceiling_action: route_to_premium
  flagship_protection_rule: "BYO sum to reach Premium config must price above $32,000"
```

## Mapping to common tools

| Tool | Mapping notes |
|------|---------------|
| **Typeform** | One question per dimension; use logic-jump rules to enforce dependencies. Add-ons are a multi-select. |
| **Tally** | Same pattern as Typeform. Native price-calculator field handles deltas. |
| **Webflow + Memberstack** | Dimensions become CMS collections; price calculator is JS that reads `delta_price` fields. |
| **Stripe Pricing Tables** | Tiers map directly. BYO doesn't fit — use Stripe Custom Pricing for that path. |
| **Custom (React/Vue)** | YAML can drive a generic configurator component. Dependencies enforced in form-state reducer. |

## Dependency rule grammar

Three rule types:

- **`block`** — these levels cannot coexist; configurator must prevent the combination.
- **`require`** — selecting level X *requires* level Y on another dimension.
- **`auto_upgrade`** — selecting level X automatically sets level Y on another dimension (often a UX nicety).

State all three rule types in the `dependencies` block; don't conflate them.

## Pricing-delta convention

`delta_price` is the *additional* cost of stepping from the previous level to this level on the same dimension. The first level on each dimension always has `delta_price: 0` (it's the base). The total price for a configuration is `base_price + sum(delta_price for each selected non-base level) + sum(price for each add-on)`.

This makes the configurator's price-calculation logic trivial and avoids accidental double-counting.
