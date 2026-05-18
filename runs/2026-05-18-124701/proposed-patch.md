## Proposed change

**Rationale:** The dominant failure pattern across these runs is *diagnosing-but-not-fixing*: the model correctly identifies a flagship-protection violation in its own output, then ships the broken numbers anyway with a note. The spec already says BYO sums "must price *above*" each tier, but it doesn't tell the model what to *do* when its first pass fails the check — so the model treats the rule as descriptive (flag it) rather than prescriptive (iterate until satisfied). A single rule promoting flagship-protection from a static constraint to an iterate-until-pass step, plus an explicit "no shipping known violations" gate in self-check, should close the loop. Bonus: this also nudges the model to fill in the Savings column with real deltas (since it now has to compute them to verify the rule).

```diff
--- SKILL.md (Part 3, Build-Your-Own framework)
+++ SKILL.md
@@
 - **Dependencies the configurator must enforce**
-- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *meaningfully above* that tier's flagship (target ≥10–15% premium, not rounding-error close) — flagships must remain the rational discount.
+
+**Flagship-protection is iterative, not advisory.** After drafting prices, compute each tier's BYO-equivalent sum and the savings delta. If any tier fails (BYO ≤ flagship, or delta <10%), you MUST adjust per-dimension upgrade prices or the base upward and re-emit the corrected tables — do not ship a pricing table you have flagged as violating the rule. Always render the "Savings vs. BYO" column with concrete $ figures, never "—".
```

```diff
--- SKILL.md (existing-tier overlay mode bullet)
+++ SKILL.md
@@
-- **Existing-tier overlay mode** — user already has tiers and wants BYO without breaking them. Preserve existing tiers exactly; slot BYO **underneath** the cheapest and **between** existing tiers; prove each existing tier still wins on price vs. its BYO-summed equivalent. See [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
+- **Existing-tier overlay mode** — user already has tiers and wants BYO without breaking them. Preserve existing tiers exactly; slot BYO **underneath** the cheapest (state the sub-cheapest base price explicitly and justify it as the overlay floor) and **between** existing tiers; add a one-line **pricing anchor** to each existing tier (what benchmark it wins against); prove each existing tier still wins by ≥10% vs. its BYO-summed equivalent, iterating prices until it does. See [`references/existing-tier-overlay.md`](references/existing-tier-overlay.md).
```

```diff
--- SKILL.md (Self-Check)
+++ SKILL.md
@@
-Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?
+Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift? **Computed BYO-sum for each tier and confirmed ≥10% savings vs. flagship? If any tier failed, iterated and re-emitted — never ship a table you've flagged as violating the rule.**
```