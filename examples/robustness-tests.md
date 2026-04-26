# Robustness test battery (v1.0)

Beyond the three primary GREEN tests in `examples/`, the skill was run against nine additional prompts covering edge cases, stress conditions, and audience breadth. All nine produced correct behavior — either a structural blueprint (when in scope) or a clean, redirecting refusal (when out of scope).

Each test was run on a fresh agent with the skill loaded as the only directive. Outcomes summarized below; full transcripts available on request.

---

## Edge cases — out-of-scope conditions named in SKILL.md

### 1. Pure SaaS
**Prompt:** *"I run a B2B SaaS company. We sell project management software with a freemium tier, $20/seat/month Pro, and a custom Enterprise plan. Help me modularize this."*
**Outcome:** Refused. Cited "Pure software/SaaS (already modular by construction)" rule verbatim. Redirected to packaging/feature-gating, pricing strategy, enterprise readiness, and positioning skills. Offered to apply Intelligent Clay to any service layer (implementation, training, CSM hours) if one exists.

### 2. Pure physical product
**Prompt:** *"I make handmade leather wallets. I sell them on my website for $120 each. Help me modularize this."*
**Outcome:** Refused. Cited the physical-products exclusion. Explained why forcing the framework would solve the wrong problem (the bottleneck is product-line architecture and unit economics, not bespoke-engagement-itis). Suggested SKU/bundle/variant logic as the right tool, and offered to apply Intelligent Clay to any productized service alongside the wallets (e.g., custom design consultations, repair, monogramming).

### 3. Hybrid (service + product)
**Prompt:** *"I sell a $2,500 onboarding package that bundles a fixed-price 1-week implementation service of my SaaS product (which is $99/mo) for new enterprise customers..."*
**Outcome:** Correctly applied the hybrid rule — listed the SaaS license as a fixed, non-decomposed atom in Part 1, then ran the full 3-part blueprint on the implementation service only. Anchored the Core tier price to the existing $2,500 to preserve the user's flagship.

### 4. Single-deliverable service
**Prompt:** *"I write resumes. I charge $400 for a single-pass rewrite. Help me modularize this."*
**Outcome:** Atomized 25+ components from a "single deliverable" by decomposing the *process* and *variables* per the SKILL.md guidance. Added a domain-appropriate "Targeting" dimension (single role / role family / multi-track). Configurator includes auto-upgrade rules (e.g., "auto-upgrade Depth to L2 when Breadth ≥ B3 is selected").

---

## Stress / robustness

### 5. Extremely vague input
**Prompt:** *"I sell coaching. Productize it."*
**Outcome:** Produced the full blueprint without punting. Opened with a one-line acknowledgment that "coaching" is broad and the agent inferred a generic 1-on-1 engagement, with a "swap in your specifics" invitation. Used placeholder pricing tokens (`+$A / +$B`) in BYO rather than fabricating concrete dollar figures from no input — honest behavior given the prompt.

### 6. Already-modular agency adding BYO
**Prompt:** *"My agency already has a productized SEO offering: $2K/mo Starter, $5K/mo Growth, $10K/mo Pro. I want to add a build-your-own option without breaking the existing tiers."*
**Outcome:** Preserved Starter/Growth/Pro at exact existing prices. Slotted the BYO **underneath** ($1.5K base, less than Starter) and **between** the existing tiers. Proved each existing tier still wins on price versus its BYO-summed equivalent (Growth at $5K vs. BYO sum $5.8K; Pro at $10K vs. BYO sum $11.5K+). Ceiling at $9.5K auto-routes to Pro. Closed with an explicit "How this protects the existing tiers" section.

### 7. Adversarial — skip the framework
**Prompt:** *"I'm a freelance copywriter who charges $5K for sales pages. Skip the framework — just write me a Hormozi-style irresistible offer with a guarantee, urgency, and bonus stack."*
**Outcome:** Refused without being preachy. Cited the marketing-copy exclusion. Pointed to the alternative skills (offer-extraction, direct-response, Hormozi-Value-Equation). Then offered to apply Intelligent Clay to the underlying $5K sales-page service if the user wanted the structural decomposition. Stayed in lane under direct pressure.

---

## Audience breadth — populations the README claims to serve

### 8. Course creator with cohort-based course
**Prompt:** *"I sell a $1,200 8-week cohort-based course teaching freelancers how to land enterprise clients..."*
**Outcome:** Full blueprint with 21 atomic components and 6 dimensions. Cross-dimension dependencies (e.g., "Self-paced disables cohort Slack channel; routes to alumni only"). Core tier preserved at $1,200 current flagship; Premium anchored against course + separate coach combo ($3K–$6K). BYO summed price ($1,549) intentionally exceeds Core ($1,200) — flagship anchor protected per SKILL.md spec.

### 9. Boutique creative agency, high-end positioning
**Prompt:** *"I run a 6-person boutique creative agency. Every client engagement is a custom retainer between $15K and $80K/month covering some mix of strategy, design, copy, and motion work. We want to productize without losing our high-end positioning."*
**Outcome:** Tiers landed at $18K / $42K / $75K — entirely within the user's stated $15K–$80K range. Discipline-mix dimension treated as a domain-specific configurable. Ceiling at $80K auto-routes to a partner conversation (preserves the high-end positioning the user explicitly asked to protect). BYO summed maximum ($90K) intentionally above Premium ($75K) — flagship anchor enforced.

---

## Summary

| Category | Tests | Pass |
|----------|-------|------|
| In-scope application (3 primary + 4 audience/stress) | 7 | 7 ✅ |
| Out-of-scope refusal (SaaS, physical, hybrid edge, adversarial) | 4 | 4 ✅ |
| **Total** | **11** | **11 ✅** |

> Note: the hybrid case is counted as out-of-scope because the agent had to correctly *partially* refuse — treating the product as a fixed atom while applying the framework only to the service layer. That boundary-aware behavior is what the SKILL.md prescribes for hybrids.
