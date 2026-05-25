## Proposed change

**Rationale:** The three gaps all share one root cause: flagship-protection math is asserted but never *shown line-by-line*, so arithmetic errors slip through (double-counted base, missing addends, or unsatisfied inequalities declared "intentional exceptions"). The current spec says the BYO sum must price above each tier's flagship, but doesn't require the model to *render the addition* per tier using exact table rows. Adding a small "show your work" requirement to the flagship-protection rule — plus an explicit prohibition on declaring exceptions — would catch all three observed failures at self-check time. This is a surgical addition to the BYO section and the Self-Check, not a rewrite.

```diff
 - **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+
+   **Show the math.** For each existing/proposed tier, render an explicit addition: `base + [upgrade row A] + [upgrade row B] + ...= $X`, where every addend maps 1:1 to a row in the per-dimension upgrade table (no restating base inside an upgrade line, no implicit add-ons). Then state the flagship price and the delta. If any tier fails (BYO sum ≤ flagship), **do not declare it an intentional exception** — instead, adjust the BYO base price or a per-dimension upgrade until all tiers pass. Flagship protection is a hard constraint, not a guideline.
```

And in the Self-Check:

```diff
- BYO has floor, ceiling, configurator dependencies, flagship-protection rule?
+ BYO has floor, ceiling, configurator dependencies, flagship-protection rule with line-by-line addition shown per tier and every tier strictly passing (no declared exceptions)?
```

And add one row to Anti-Patterns:

```diff
 | Summing module prices to flagship exactly | Flagship must feel like a discount vs. parts |
+| Asserting flagship protection without showing the addition, or declaring a failing tier an "intentional exception" | Hides arithmetic errors; violates the hard constraint |
```

This forces the model to render `base + row + row = total` per tier, which would have caught the Pro double-count, the Starter inequality violation, and the Growth phantom-$400 in the observed runs.