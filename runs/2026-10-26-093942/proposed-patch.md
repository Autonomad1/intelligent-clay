## Proposed change

**Rationale:** The most common and highest-leverage gap pattern across both runs is **flagship-protection failures in Part 3** — BYO base prices sitting at or below adjacent tier prices, upgrade tables that don't arithmetically reconstruct above flagships, and narrative "fixes" that leave two conflicting price tables in the output. The current spec states the flagship-protection rule but doesn't require the model to *show its work* or produce a single authoritative price list. A short, mandatory reconstruction check — done once, before emitting the final tables — would catch all four already-modular-overlay pricing bugs and force the model to iterate internally rather than patch narratively. Pairing it with an explicit "one authoritative table" rule prevents the mid-output rewrite pattern.

```diff
### Part 3 — Three Tiers + Build-Your-Own

...
- **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+ **Flagship-protection rule:** the BYO sum to reach each tier's configuration must price *above* that tier's flagship — flagships must remain the rational discount.
+
+ **Mandatory reconstruction check (do silently, before emitting Part 3):**
+ For every tier T, compute `BYO_base + Σ(upgrades needed to match T's configuration)` and confirm it exceeds T's price by a visible margin (≥10%). Also confirm the BYO base itself sits *below* the cheapest tier by a visible margin. If either check fails, **revise the BYO base or upgrade prices and recompute** — do not emit, then "fix." The output must contain exactly **one** upgrade price table and **one** reconstruction row per tier; conflicting or superseded tables are a hard failure.
+
+ Render the reconstruction as a compact proof row in the tier table:
+
+ | Tier | Price | BYO reconstruction | Margin |
+ |---|---|---|---|
+ | Lite | $X | base $Y | — (base < Lite by Z%) |
+ | Core *(flagship)* | $X | base + up1 + up2 = $Y | +Z% above flagship ✓ |
+ | Premium | $X | base + up1..upN = $Y | +Z% above flagship ✓ |
+
+ In **existing-tier overlay mode**, this check runs against every preserved tier; if any tier cannot be protected without restructuring upgrades, flag it explicitly and propose a structural fix (raise BYO base, cap configuration ceiling, or add a managed-fee floor) — never a narrative handwave.
```

This adds ~150 words, keeps the edit surgical, and directly addresses 4 of the 10 observed gaps while reinforcing the existing flagship-protection rule rather than restating it.