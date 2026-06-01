## Proposed change

**Rationale:** The most load-bearing gap across runs is Part 3's rendering: tiers are collapsed into a 3-column table that flattens the spec's three named sub-fields (Configuration / Positioning line / Pricing logic), and the flagship-protection rule is stated only abstractly — never demonstrated. These two failures compound: when tiers are a table, there's no room to show the BYO-sum inequality that proves the flagship wins on price. Fixing the rendering format forces the inequality to surface. This single edit addresses gaps #1 and #3 directly and creates the structural slot where token consistency (gap #2) becomes visually obvious.

### Diff

````diff
 ### Part 3 — Three Tiers + Build-Your-Own

-Three packages. Not two. Not five. Use Lite/Core/Premium, or rename in the brand's vocabulary (Foundation/Signature/Elite, Studio Lite/Core/Premium). For each tier:
-
-- **Configuration** — level on each dimension
-- **Positioning line** — one sentence: who it's for, what they get
-- **Pricing logic** — what the price is anchored against (see Pricing-Anchor Rule below)
+Three packages. Not two. Not five. Use Lite/Core/Premium, or rename in the brand's vocabulary (Foundation/Signature/Elite, Studio Lite/Core/Premium).
+
+**Render each tier as a named block, NOT a table row.** Tables flatten the three sub-fields into cells and consistently cause the positioning line to collapse into a fragment. Required format per tier:
+
+> **Tier name — $price (or token)**
+> **Configuration:** level on each dimension (one line per dimension or compact inline)
+> **Positioning:** one full sentence — who it's for, what they get, why this tier
+> **Pricing logic:** what the price is anchored against (see Pricing-Anchor Rule)
+
+Use the *same* token scheme across all three tiers and BYO (e.g., +$A / +$B / +$C). Do not mix concrete anchors with tokens within a single blueprint unless one tier is genuinely $0/free — in which case state that exception explicitly.

 Then a **Build-Your-Own framework**:

 - **Base price** (typically Lite) + **per-dimension upgrade pricing**
 - **Floor** (minimum viable) and **Ceiling** (above which auto-route to Premium or custom)
 - **Dependencies the configurator must enforce**
-- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount. **Demonstrate this with a worked inequality for the Core tier**, e.g., `base + depth↑ + breadth↑↑ + support↑ ≈ 1.25–1.4 × $B > $B`. Abstract assertion is insufficient; show the sum.
````

Also update Self-Check to add: *"Tiers rendered as named blocks with all three sub-fields present? Flagship-protection inequality shown numerically for Core?"*