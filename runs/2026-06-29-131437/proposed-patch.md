## Proposed change

**Rationale:** The recurring failure is treating a concrete price *range* (e.g., "$15K–$80K/mo") as vague input and defaulting to placeholder tokens plus an "Assuming..." preamble. The Pricing-Anchor Rule's first row already covers this ("User gave concrete prices"), but a range apparently reads as ambiguous to the model — it's not a single figure, so it gets demoted to "vague." The fix is to make the rule explicitly name *ranges and bands* as concrete input, and to add a hard requirement that tier prices land inside any user-supplied band. This is a two-line surgical edit to the Pricing-Anchor Rule table and the bright-line note immediately below it.

```diff
 ### Pricing-Anchor Rule

 | Input quality | Anchor approach |
 |---------------|-----------------|
-| User gave concrete prices | Use $ figures; anchor each tier against them |
+| User gave concrete prices, ranges, or bands (e.g., "$15K–$80K/mo") | Use $ figures; anchor each tier against them; **every tier price must land inside the stated range**, with Lite near the floor, Premium near the ceiling, Core between |
 | Domain norms are well-known **at the named sub-niche level** (exec coaching, brand strategy, SEO retainers, technical resume writing) | Use $ figures from those benchmarks |
 | Generic category only ("coaching", "consulting", "design", "marketing") with no sub-niche named | Treat as vague — use placeholder tokens |
 | Truly vague input | Use placeholder tokens (`+$A`, `+$B`, `+$C`) — do not fabricate |

-**Bright line:** "coaching" alone is vague; "executive coaching for Series B founders" is anchored. When in doubt, use tokens and offer to re-anchor once the niche is named. Never invoke norms for the parent category to justify specific dollar figures.
+**Bright line:** "coaching" alone is vague; "executive coaching for Series B founders" is anchored. A **price range counts as anchored input** — do not demote a range to vague just because it isn't a single figure. When in doubt, use tokens and offer to re-anchor once the niche is named. Never invoke norms for the parent category to justify specific dollar figures.

-**Vague-input preamble:** When using placeholder tokens, open with a one-line assumption stub, not a complaint. Format:
+**Vague-input preamble:** When using placeholder tokens (and *only* then — never when the user supplied $ figures or a range), open with a one-line assumption stub, not a complaint. Format:
```

This closes the loop: ranges are explicitly concrete, tier prices must fall inside them (making the flagship-protection math verifiable), and the preamble is gated to token-only outputs so it can't leak into anchored runs.