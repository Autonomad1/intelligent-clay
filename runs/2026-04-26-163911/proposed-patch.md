## Proposed change

**Rationale:** The most load-bearing gap is the Pricing-Anchor Rule being silently overridden when the domain *sounds* familiar but isn't actually tight. "Coaching," "consulting," "design" feel like known domains, so the model invokes "domain norms" and fabricates figures — violating the spec's intent. The fix is to tighten the middle row of the Pricing-Anchor table so it requires a *named sub-niche* before invoking norms, and to add a one-line preamble convention that replaces the "you gave me nothing" lampshade with a productive assumption stub. This single edit addresses both the fabrication failure and the tone failure observed in vague-input runs, and is precedent-setting for any future vague domain (coaching, consulting, design, marketing).

```diff
 ### Pricing-Anchor Rule

 | Input quality | Anchor approach |
 |---------------|-----------------|
 | User gave concrete prices | Use $ figures; anchor each tier against them |
-| Domain norms are well-known (exec coaching, brand strategy, SEO retainers) | Use $ figures from those benchmarks |
-| Truly vague input | Use placeholder tokens (`+$A`, `+$B`) — do not fabricate |
+| Domain norms are well-known **at the named sub-niche level** (exec coaching, brand strategy, SEO retainers, technical resume writing) | Use $ figures from those benchmarks |
+| Generic category only ("coaching", "consulting", "design", "marketing") with no sub-niche named | Treat as vague — use placeholder tokens |
+| Truly vague input | Use placeholder tokens (`+$A`, `+$B`, `+$C`) — do not fabricate |
+
+**Bright line:** "coaching" alone is vague; "executive coaching for Series B founders" is anchored. When in doubt, use tokens and offer to re-anchor once the niche is named. Never invoke norms for the parent category to justify specific dollar figures.
+
+**Vague-input preamble:** When using placeholder tokens, open with a one-line assumption stub, not a complaint. Format:
+
+> *Assuming [generic-but-plausible reading of the offering]; will re-anchor with $ figures once you name [the specific variable that would unlock norms].*
+
+Do not lampshade the vagueness ("you've given me almost nothing", "this is hard to answer") — infer, stub, produce.
```

This also retroactively fixes the Pace/BYO consistency issue indirectly: when tiers are built from tokens rather than fabricated figures, the model is forced to be explicit about what each upgrade *costs* (+$B), which surfaces baseline contradictions like "Biweekly included in base" before they ship.