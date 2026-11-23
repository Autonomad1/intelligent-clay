## Proposed change

**Rationale:** The dominant failure pattern across runs is shipping a flagship-protection *violation* with an acknowledgment or deferred fix, rather than resolving it before delivery. The spec says BYO sums must price *above* each tier's flagship, but the skill lacks (a) an explicit requirement to *show the proof arithmetic inline* and (b) a hard gate forbidding delivery when the proof fails. Models currently treat the rule as aspirational and narrate the gap instead of iterating upgrade prices until it's satisfied. The fix: require a visible proof table and add an explicit "do not ship" instruction with the remediation lever (raise per-dimension upgrade prices, bundle atoms into tiers, or both).

### Diff

**OLD** (end of Part 3, the Flagship-protection bullet):

```
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
```

**NEW:**

```
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
- **Flagship-protection proof (required, inline):** render a table showing, for each tier: `BYO atom list → BYO sum → flagship price → discount ($ and %)`. Every row must show a positive discount (BYO sum > flagship).
- **Do-not-ship gate:** if any tier fails the proof (BYO sum ≤ flagship, or near-parity <5% discount), you MUST resolve it *before* delivering the blueprint. Do not ship with a parenthetical acknowledgment, a "required adjustment" note, or a ceiling-routing substitute. Remediation levers, in order of preference:
  1. Raise per-dimension upgrade prices until BYO sums clear each flagship by ≥10%.
  2. Bundle one or more atoms *into* the failing tier (removing them from BYO-reachable configuration) so the BYO-equivalent requires strictly more.
  3. Lower the flagship price (last resort; only if upgrade prices would become implausible vs. anchors).
  Re-run the proof table after remediation. Iterate until all tiers pass. Only then deliver.
- **Arithmetic hygiene:** show the BYO sum as a single transparent addition (`base + upgrade₁ + upgrade₂ + …= total`). Do not stack alternative line items (e.g., "biweekly +$800; weekly adds another +$800") inside one sum — pick the atom that matches the tier's configuration and show that line only.
```

Also add to **Self-Check Before Responding**:

```
Flagship-protection proof table rendered inline with positive discounts for all tiers? No tier shipped with an acknowledged violation or deferred fix?
```

And add to **Anti-Patterns**:

| Shipping a flagship-protection violation with a note | Spec requires resolution before delivery, not acknowledgment |
| Substituting ceiling-routing for flagship-protection | Different mechanism; doesn't preserve flagship-as-discount |