## Proposed change

**Rationale:** The dominant failure pattern is in existing-tier overlay mode: the flagship-protection check is hand-waved rather than line-by-line auditable. Specifically, (1) existing tiers aren't mapped onto Part 2 dimensions, so the BYO sum-check has nothing to sum against; (2) BYO floors get pinned at the cheapest tier rather than truly *underneath* it; (3) per-dimension prices aren't calibrated to clear flagship by a clear margin, leading to retroactive "proxy" fudges. All three collapse into a single fix: tighten the overlay-mode contract in SKILL.md so the structural requirement forces clean math. The reference file already covers the mechanics — the SKILL bullet just needs to be load-bearing enough to prevent shortcuts.

```diff
@@ ## When to Use, Modes ##
- **Existing-tier overlay mode** — user already has tiers and wants BYO without breaking them. Preserve existing tiers exactly; slot BYO **underneath** the cheapest and **between** existing tiers; prove each existing tier still wins on price vs. its BYO-summed equivalent. See [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
+ **Existing-tier overlay mode** — user already has tiers and wants BYO without breaking them. Requirements (all mandatory; no shortcuts):
+   1. **Map each existing tier onto Part 2 dimensions** in an explicit "Configuration (in dimension terms)" column — every dimension gets a level per tier, so the sum-check is line-by-line auditable.
+   2. **BYO floor must price strictly below the cheapest existing tier** (a real sub-tier configuration, not a routing redirect). If you can't construct a coherent sub-floor offering, say so explicitly rather than collapsing the floor onto the cheapest tier.
+   3. **Flagship-protection sum-check must use only real BYO line items** at their published per-dimension prices — no half-unit proxies, no "adjust by $X" retrofits. If the math ties or loses, **raise per-dimension prices upward** until every existing tier's BYO-equivalent clears its flagship by **≥15%**, then re-show the sum.
+   4. Show the sum-check arithmetic explicitly per tier: `base + dim1 + dim2 + ... = $Total vs $Flagship (margin: X%)`.
+   See [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
```

This makes the three recurring gaps structurally impossible to ship: missing dimension mapping, floor-equals-cheapest, and proxy-based protection math all become visible contract violations rather than judgment calls.