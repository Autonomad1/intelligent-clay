## Proposed change

The most load-bearing gap is **flagship-protection being diagnosed but not enforced**. Across runs, the model identifies that BYO sums fall below tier prices, then either rationalizes the violation or offers the user a choice of fixes. The spec already says flagships must remain the rational discount, but it doesn't tell the model what to *do* when the math fails on first pass — so it punts. The fix is to make flagship-protection an iterative constraint the model must resolve before shipping, not a check it merely reports. A single self-check line is too easy to satisfy with "I noted the issue."

```diff
--- SKILL.md (Part 3, Build-Your-Own framework)
+++ SKILL.md
@@
 - **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+- **Flagship-protection is a hard constraint, not a diagnostic.** Before shipping, compute the BYO-summed equivalent for each tier's configuration. If any tier's flagship ≥ its BYO sum, **fix it in the blueprint itself** — do not present the violation as an open question. Acceptable fixes (apply silently, pick the least disruptive):
+  1. Raise per-dimension BYO unit prices until every tier clears its sum by a visible margin (~10–20%).
+  2. Add an atom into the tier (e.g., bundle an extra deliverable) so the BYO equivalent rises.
+  3. Lower the flagship price if the anchor still holds.
+
+  Ship a single compliant table. Never output "Starter fails the rule; want me to fix it?" — that's the skill's job, not the user's.
```

And one matching tightening to the Self-Check:

```diff
--- SKILL.md (Self-Check Before Responding)
+++ SKILL.md
-BYO has floor, ceiling, configurator dependencies, flagship-protection rule?
+BYO has floor, ceiling, configurator dependencies, flagship-protection rule? **Did I actually sum BYO for each tier and confirm flagship < sum, or did I iterate until it does?**
```

This converts the rule from aspirational to operational: the model must do arithmetic, and if it fails, must repair the blueprint rather than narrate the failure. It also directly addresses the second observed gap (offering fixes as optional) by naming the anti-behavior explicitly. The other gaps (memory preamble framing, follow-up menu phrasing) are cosmetic by comparison and can wait.