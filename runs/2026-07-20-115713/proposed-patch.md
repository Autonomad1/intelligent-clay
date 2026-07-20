## Proposed change

**Rationale:** The dominant failure pattern across runs is Part 3 delivery hygiene: flagship-protection math is shown as visible scratch-work, self-corrections, "optional fixes," or tied/violating numbers that should have been resolved *before* rendering. The skill states the rule but doesn't enforce that resolution happens silently, pre-delivery. A surgical fix is to (a) elevate flagship-protection from a bullet inside Part 3 into an explicit pre-render gate in the Self-Check, and (b) add a "no visible scratch-work" clause. This addresses 4 of the 8 observed gaps directly (both flagship-protection violations, the inline `(wait, Signature is…)` aside, and the "optional fix" framing) and reinforces one anti-pattern already listed.

```diff
### Part 3 — Three Tiers + Build-Your-Own
...
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *strictly above* that tier's flagship — flagships must remain the rational discount. This is a hard gate, not a preference:
+ - Run the sum for **every** tier before rendering Part 3.
+ - If any tier ties or loses, adjust base price, per-dimension upgrades, or tier config **silently** until all tiers pass, then render only the final numbers.
+ - Never deliver a "recommended fix," "acceptable exception," or tied result. Never show self-correction, scratch-work, or parenthetical reversals ("wait, actually…") in the final output.
+ - In overlay mode: BYO slots **between and above** existing tiers only. Any sub-cheapest zone must be framed as one-time/add-on inventory, not a monthly BYO config, so no BYO configuration prices at or below the cheapest existing tier.
+ - The BYO upgrade table and the flagship-protection math must be internally consistent: every upgrade referenced in the protection sum must appear in the BYO table at the same price, and vice versa.
```

And in **Self-Check Before Responding**, replace:

```diff
- BYO has floor, ceiling, configurator dependencies, flagship-protection rule?
+ BYO has floor, ceiling, configurator dependencies? Flagship-protection sum computed for every tier and strictly exceeds each flagship on first render (no ties, no "acceptable" violations, no visible fixes)? BYO upgrade table matches the protection math line-for-line?
```

This keeps the edit tight, converts a stated rule into a rendering gate, and explicitly forbids the two adjacent hygiene failures (scratch-work, table/math inconsistency) that co-occurred with the protection violations.