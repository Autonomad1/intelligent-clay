# Existing-tier overlay mode

The default mode of Intelligent Clay produces three fresh tiers (Lite/Core/Premium) plus BYO. **But when the user already has productized tiers and is asking for a BYO option without breaking them, switch to overlay mode.**

This was first observed in a real run (SEO agency: Starter $2K / Growth $5K / Pro $10K, wanting to add BYO without cannibalization). The agent invented the right pattern in-context; this reference codifies it as a standard mode.

## When to use overlay mode

Trigger on phrases like:

- "Add BYO to my existing tiers"
- "I have $X / $Y / $Z tiers — don't break them, but give me a custom option"
- "We're already productized; we want à-la-carte alongside"
- "Without cannibalizing our existing packages"

If the user describes existing tiers and wants modular addition: overlay mode.

## How overlay mode differs from default

| Element | Default mode | Overlay mode |
|---------|--------------|--------------|
| Tier production | Generate three fresh tiers (Lite/Core/Premium) | **Preserve existing tiers exactly — same names, same prices, same configurations** |
| BYO position | Anchored on a fresh Lite | Anchored **below** the cheapest existing tier |
| Tier count | 3 + BYO | N existing + BYO (where N is whatever the user already has) |
| Output Part 3 | "Three Tiers + BYO" | "Existing Tiers (preserved) + BYO Overlay" |
| Flagship protection | BYO sum > each tier's price | **Same rule, but explicitly demonstrated for each existing tier** — show the BYO-summed equivalent of each existing tier and confirm the existing tier still wins on price |

## Step-by-step: producing overlay output

1. **Capture existing tiers verbatim** — name, price, included features. Do not rename, reprice, or restructure them, even if you'd have done it differently in default mode.

2. **Atomic decomposition (Part 1)** — same as default: list the smallest standalone components across the existing tier collection. Don't fight the user's existing groupings; just list the atoms.

3. **Configuration architecture (Part 2)** — same table format. Dimensions and levels should naturally span the existing tier configurations (i.e., the existing tiers should be expressible as specific points in the dimension space).

4. **BYO base price** — usually 50–80% of the cheapest existing tier. The intent is to capture buyers who want *less than the entry tier* (e.g., tracking-only, no calls), not buyers who want *something between the entry and middle tier* (those should still buy the entry tier).

5. **BYO upgrade pricing** — set per-dimension upgrade prices such that the BYO sum to reach each existing tier's configuration is **5–20% higher** than that tier's price. This is the flagship-protection rule applied to each existing tier individually.

6. **BYO ceiling** — set the ceiling at ~5% below the highest existing tier's price. Any configuration above the ceiling auto-routes to the highest tier (or to a custom-quote conversation), preventing BYO from undercutting the flagship.

7. **Closing section: "How this protects existing tiers"** — explicitly walk the user through:
   - BYO base ($X) gives less than entry tier — does not cannibalize.
   - BYO sum to reach mid tier ($Y) > mid tier price — mid tier wins on price.
   - BYO sum to reach top tier ($Z) > top tier price — top tier wins on price.
   - Ceiling routes to top tier — no BYO can exceed the flagship.

This closing section is **mandatory in overlay mode**. It's the section that gives the user confidence the BYO won't break what they've already built.

## Example: SEO agency overlay (compressed)

**Existing tiers (preserved):** Starter $2K · Growth $5K · Pro $10K

**BYO base:** $1,500 (tracking + monthly report + email — less than Starter on every dimension).

**BYO summed equivalents:**
- Starter config in BYO: ~$2,000 *(matches; clean indifference point — Starter wins on simplicity)*
- Growth config in BYO: ~$5,800 *(Growth at $5K wins on price; protects mid-tier)*
- Pro config in BYO: ~$11,500 *(Pro at $10K wins on price; protects flagship)*

**BYO ceiling:** $9,500 — any configuration above auto-routes to Pro.

**Result:** BYO captures the "I want Growth-but-async" buyer the user is currently losing, without giving anyone an incentive to swap out of an existing tier.

## Pitfalls to avoid

- **Don't rename existing tiers**, even if "Pro" feels like a weak name. The user's brand is the user's brand.
- **Don't reprice existing tiers** to "round numbers" or to fit the BYO math. Adjust BYO; never adjust existing.
- **Don't suggest the user retire any existing tier**, even if BYO obviates it. That's a strategic call, not a structural one.
- **Don't skip the "How this protects existing tiers" section** — it's the entire reason the user invoked overlay mode.
