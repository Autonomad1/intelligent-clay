## Proposed change

**Rationale:** The recurring failure is shipping a blueprint that *acknowledges* a flagship-protection violation or BYO-sum ambiguity rather than resolving it. The current spec states the rule but doesn't require the model to *show its work* and *iterate before shipping*. A small addition — an explicit arithmetic-reconciliation step inside the Self-Check, plus a hard rule that the deliverable must not contain unresolved violations — closes the gap without expanding scope. It also forces every atom in a tier's config to be classified as **included** or **add-on** so the BYO sum is computable.

```diff
### Part 3 — Three Tiers + Build-Your-Own
...
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Config-inclusion rule:** every dimension level and every listed component in a tier's configuration must be explicitly marked **[included]** or **[add-on, +$X]**. No "optional" without a price and a side. Ambiguous items make the BYO-sum uncomputable and are disallowed.
+ **Show-the-math requirement:** for each tier, print the BYO-sum reconciliation line:
+ > *BYO-equivalent: base $X + [dim upgrades itemized] = $Y vs. flagship $Z → discount $Z−$Y (must be negative; flagship < BYO sum).*
```

```diff
## Self-Check Before Responding

- Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?
+ Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? Every tier component marked included vs. add-on? **BYO-sum reconciliation line printed for each tier, and every tier's flagship prices strictly below its BYO sum?** BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?
+
+ **Hard stop:** if reconciliation reveals a violation (flagship ≥ BYO sum, or an ambiguous "optional" component), fix it before shipping — either lower the flagship, raise the offending upgrade, or reclassify the component. Do not ship a blueprint that flags its own violation in prose.
```