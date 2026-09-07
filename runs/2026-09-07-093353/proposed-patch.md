## Proposed change

**Rationale:** The dominant failure pattern is misclassifying concrete input as vague — leading to a cascade of downstream errors (unwarranted preamble, placeholder tokens instead of $ figures, unverifiable flagship-protection math, and in one case a "memory unavailable" line that violates silent-omit). The root cause is that the Pricing-Anchor Rule doesn't explicitly treat a **stated price range or budget band** as concrete. A price band like "$15K–$80K/mo" is concrete input — tiers should land inside it. Fixing this one classification rule, plus tightening the vague-input preamble trigger and the memory silent-omit language, prevents the whole cascade with minimal surface-area change.

```diff
--- SKILL.md (Pricing-Anchor Rule)
+++ SKILL.md (Pricing-Anchor Rule)
@@
 | Input quality | Anchor approach |
 |---------------|-----------------|
-| User gave concrete prices | Use $ figures; anchor each tier against them |
+| User gave concrete prices **or a price range/budget band** (e.g., "$15K–$80K/mo", "engagements run $8–25K") | Use $ figures; anchor each tier **inside the stated range** — Lite near the floor, Premium near the ceiling, Core between. Never fall back to tokens when a band is given. |
 | Domain norms are well-known **at the named sub-niche level** (exec coaching, brand strategy, SEO retainers, technical resume writing) | Use $ figures from those benchmarks |
 | Generic category only ("coaching", "consulting", "design", "marketing") with no sub-niche named | Treat as vague — use placeholder tokens |
 | Truly vague input | Use placeholder tokens (`+$A`, `+$B`, `+$C`) — do not fabricate |

 **Bright line:** "coaching" alone is vague; "executive coaching for Series B founders" is anchored. When in doubt, use tokens and offer to re-anchor once the niche is named. Never invoke norms for the parent category to justify specific dollar figures.

-**Vague-input preamble:** When using placeholder tokens, open with a one-line assumption stub, not a complaint. Format:
+**Vague-input preamble:** **Only** when actually using placeholder tokens (rows 3–4 above). If the user supplied concrete prices or a price band, skip the preamble entirely and go straight to Part 1. Format when used:

 > *Assuming [generic-but-plausible reading of the offering]; will re-anchor with $ figures once you name [the specific variable that would unlock norms].*

 Do not lampshade the vagueness ("you've given me almost nothing", "this is hard to answer") — infer, stub, produce.
+
+**BYO upgrade deltas** must also be expressed in $ (not tokens) whenever the tiers are in $, so flagship-protection math is verifiable in-output.
```

Also, in Memory Integration, tighten silent-omit:

```diff
-If memory is unavailable, omit the preamble silently. Never fail or refuse because memory isn't there.
+If memory is unavailable, omit the preamble silently — **do not** print "memory unavailable" or any equivalent notice. Never fail or refuse because memory isn't there.
```