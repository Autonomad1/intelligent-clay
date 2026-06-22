## Proposed change

The most common pattern across the gaps is **token-based BYO arithmetic that can't actually be verified** — placeholder tokens get used without defined relative magnitudes, so the flagship-protection rule becomes an unprovable assertion rather than shown math. This is the load-bearing failure: the skill's whole pricing-integrity claim collapses when tokens are unscaled. Fixing this also forces the vague-input preamble to specify *what variable unlocks real numbers*, since the tokens are now structured objects rather than vibes. Surgical edit to the Pricing-Anchor Rule section:

```diff
 **Vague-input preamble:** When using placeholder tokens, open with a one-line assumption stub, not a complaint. Format:

-> *Assuming [generic-but-plausible reading of the offering]; will re-anchor with $ figures once you name [the specific variable that would unlock norms].*
+> *Assuming [generic-but-plausible reading]; will re-anchor with $ figures once you name [the specific variable that unlocks norms — typically buyer type, sub-niche, or engagement length].*

 Do not lampshade the vagueness ("you've given me almost nothing", "this is hard to answer") — infer, stub, produce.
+
+**Token scale (required when using placeholders):** Define relative magnitudes inline before Part 3, e.g. `+$a < +$b < +$c, roughly 1 : 4 : 16` (Lite-unit : Core-unit : Premium-unit). Without scaled tokens, flagship-protection math is unverifiable and the BYO framework fails its own check.
+
+**Show, don't assert, flagship protection.** For each tier, write the inequality explicitly using the scaled tokens:
+
+> *Core flagship = +$b; BYO-sum to reach Core config = +$a + 3(+$a) + … ≈ +$18a > +$b ✓*
+> *Premium flagship = +$c; BYO-sum to reach Premium config = [summed tokens] > +$c ✓*
+
+If the inequality doesn't hold, the tier configuration or BYO pricing is wrong — fix it before delivering.
```

And one matching addition to the Self-Check list:

```diff
-Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?
+Atoms truly atomic? Part 2 in table form with dependencies? Three tiers + BYO (or existing-tier overlay)? Each tier has configuration + positioning + pricing logic anchored, not just $? BYO has floor, ceiling, configurator dependencies, flagship-protection rule? **If tokens used: scale defined and each tier's flagship-protection inequality shown explicitly?** Domain-specific dimensions added if needed? Stayed structural — no marketing or positioning drift?
```

This turns "flagship must feel like a discount" from a slogan into checkable arithmetic in both anchored and tokenized runs.