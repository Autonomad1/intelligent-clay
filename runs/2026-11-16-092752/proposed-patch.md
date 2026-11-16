## Proposed change

**Rationale:** All three gaps are the same failure: in existing-tier overlay mode, the BYO price grid is set without actually running the flagship-protection arithmetic against each existing tier. The model emits BYO per-dimension prices, then either (a) notes the violation and reframes it, or (b) hand-waves ("can't be replicated") instead of proving sum > tier. The fix is to make the proof a required, visible artifact — a small table showing each existing tier's config summed in BYO, with the delta — and to state the construction order (set BYO prices *so that* sums exceed tiers, not the other way around). This converts flagship-protection from a rule the model acknowledges into a computation it must show.

```diff
### Part 3 — Three Tiers + Build-Your-Own
...
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+
+ **Construction order (do not skip):** set tier prices first, then *reverse-engineer* BYO base + per-dimension upgrades so that summing each tier's configuration in BYO exceeds that tier's price. If the math doesn't close, raise BYO unit prices, add mandatory base components, or cap BYO below the tier's config — do not ship a BYO grid that undercuts a tier.
+
+ **Required proof table** (always render, both default and overlay modes):
+
+ | Tier | Tier price | BYO-summed equivalent | Delta | Protected? |
+ |------|-----------|----------------------|-------|-----------|
+
+ Delta must be positive for every row. If a tier's top configuration cannot be replicated in BYO at all (exclusivity, access, headcount), write "N/A — exclusivity" in the BYO column and name the non-replicable atom explicitly. Do not use "can't be replicated" as a substitute for the sum proof on tiers whose config *is* BYO-expressible.
+
+ **Overlap check (overlay mode):** the BYO floor slotted beneath the cheapest existing tier must sit strictly below that tier's price, AND no mid-range BYO configuration reachable from that floor may cross into the cheapest tier's price without triggering the flagship-protection delta above. State the BYO price range for each inter-tier slot and verify it against adjacent tier prices.
```