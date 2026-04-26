# Example: SEO agency adding BYO to existing tiers (Existing-Tier Overlay mode)

**Test prompt (verbatim):**

> "My agency already has a productized SEO offering: $2K/mo Starter (10 keywords, monthly report), $5K/mo Growth (30 keywords, biweekly call, content brief), $10K/mo Pro (unlimited keywords, weekly call, 4 articles/mo). I want to add a build-your-own option without breaking the existing tiers."

**Run conditions:** v1.1 SKILL.md loaded. v1.1 explicitly documents Existing-Tier Overlay mode in [`references/existing-tier-overlay.md`](../references/existing-tier-overlay.md). The agent recognized the trigger, switched modes, preserved the user's tiers verbatim, and produced the mandatory "How this protects existing tiers" section with full math.

---

> *Overlay mode confirmed — the user has named tiers ($2K Starter / $5K Growth / $10K Pro) and explicitly wants a build-your-own option without breaking the existing tiers. Preserving tiers verbatim per `references/existing-tier-overlay.md`.*

# SEO Retainer — Build-Your-Own Overlay

## Part 1 — Atomic Decomposition

**Deliverables**
- Keyword-rank dashboard (live)
- Monthly performance report (PDF/loom)
- Biweekly performance report
- Weekly performance report
- Content brief (1, with target KW + outline + SERP analysis)
- Long-form article, 1,500–2,500 words, publish-ready
- Technical SEO audit (one-time crawl + findings doc)
- Backlink prospecting list
- Competitor SERP teardown

**Time blocks**
- 30-min monthly review call
- 45-min biweekly strategy call
- 45-min weekly strategy call
- 60-min onboarding/kickoff
- Quarterly business review (60 min)

**Access tiers**
- Email, NBD response
- Shared Slack channel, 24h response
- Shared Slack channel, same-day response
- Direct line to strategist (text/cell), 4h response

**Support levels**
- Async report only (no Q&A)
- Email Q&A on report
- One round of revisions on briefs/articles
- Unlimited revisions on briefs/articles

**Customizations**
- # tracked keywords (10 / 30 / 100 / unlimited)
- # content briefs per month (0 / 1 / 2 / 4)
- # published articles per month (0 / 1 / 2 / 4)
- Industry vertical (B2B SaaS / e-comm / local / regulated)
- Geographic scope (single market / multi-region / international)
- Reporting cadence (monthly / biweekly / weekly)

## Part 2 — Configuration Architecture

| Dimension | What it controls | Levels | Dependencies |
|-----------|------------------|--------|--------------|
| **Tracking Scope** | # keywords monitored in dashboard | 10 / 30 / 100 / unlimited | Unlimited requires Standard or Live cadence (volume needs review surface) |
| **Content Production** | # briefs and finished articles per month | None / Briefs-only (1) / Briefs+Article (1+1) / Full (4 briefs + 4 articles) | Full requires weekly cadence and Slack-same-day support |
| **Reporting Cadence** | Frequency of reports + calls | Monthly async / Biweekly call / Weekly call | Weekly cadence requires Slack-24h or better |
| **Support** | Access channel + SLA | Email-NBD / Slack-24h / Slack-same-day / Direct-line-4h | Direct-line-4h gated to Tracking Scope ≥ 100 KW |
| **Format** | How the engagement is delivered | Async-only / Hybrid (async + scheduled calls) / Live-led (calls + Slack) | Async-only invalid above Biweekly cadence |
| **Add-ons** | Modular extensions priced independently | Technical audit ($1.5K one-time) · Backlink prospecting ($800/mo) · Competitor teardown ($600 one-time) · Extra article ($750/each) · QBR ($500/quarter) | Backlink prospecting requires ≥ Growth-equivalent base |

**Invalid combinations the configurator must block:**
- Weekly cadence + Email-NBD support
- Full content production + Async-only format
- Async-only + Biweekly or Weekly cadence
- Direct-line-4h support + Tracking Scope of 10 KW
- Unlimited keywords + Monthly async cadence
- Backlink prospecting add-on without ≥ 30 KW + biweekly cadence base

## Part 3 — Existing Tiers (Preserved) + BYO Overlay

### Existing tiers — preserved verbatim

| Tier | Price | Configuration | Positioning line | Pricing logic |
|------|-------|---------------|------------------|---------------|
| **Starter** | $2,000/mo | 10 KW · No content · Monthly async · Email-NBD · Async-only | Founder-led businesses who want SEO visibility without committing to content production. | Anchored at the "tracking + accountability" floor — below this, clients self-serve with Ahrefs. |
| **Growth** | $5,000/mo | 30 KW · 1 brief/mo · Biweekly call · Slack-24h · Hybrid | Companies who have content capacity internally but need strategy + briefs to point it at the right targets. | Anchored against in-house SEO hire (~$8K/mo loaded) — fractional-strategist price point. |
| **Pro** | $10,000/mo *(flagship)* | Unlimited KW · 4 briefs + 4 articles/mo · Weekly call · Slack-same-day · Live-led | Scale-stage companies treating SEO as a primary acquisition channel and outsourcing the full motion. | Anchored against full-stack agency retainers ($12–18K) — senior-led at a discount. |

### BYO Overlay

**Base price: $1,500/mo** — includes 10 KW tracking · monthly emailed report · email Q&A only (no calls, no content). Sits *below* Starter on every dimension; captures the "I just want a dashboard and an inbox" buyer Starter loses today.

**Per-dimension upgrade pricing (added to base):**

| Upgrade | Price/mo |
|---------|----------|
| Tracking → 30 KW | +$700 |
| Tracking → 100 KW | +$1,800 |
| Tracking → Unlimited | +$3,200 |
| +1 content brief/mo | +$900 |
| +1 published article/mo | +$1,400 |
| Cadence → Biweekly call | +$900 |
| Cadence → Weekly call | +$2,100 |
| Support → Slack-24h | +$500 |
| Support → Slack-same-day | +$1,200 |
| Support → Direct-line-4h | +$2,000 |
| Format → Hybrid | +$300 |
| Format → Live-led | +$700 |

**Floor:** $1,500/mo (the base config). Anything below is not a viable engagement.

**Ceiling:** $9,500/mo. Any configuration that totals above $9,500 auto-routes to Pro at $10,000 (or to a custom-quote conversation if it exceeds Pro's scope, e.g., enterprise multi-region).

**Configurator dependencies enforced** (from Part 2's invalid list, plus):
- BYO sum within $200 of an existing tier's price → UI suggests "Just take [Tier] — same scope, simpler billing."
- Selecting unlimited KW + weekly cadence + 4 articles → auto-route to Pro before checkout.

### How this protects existing tiers

- **Starter ($2,000) protection:** BYO base is $1,500 with strictly less than Starter (no monthly call, no email Q&A beyond async). The BYO-summed equivalent of Starter's exact config = $1,500 base + $0 (already at 10 KW, monthly, email) = **$1,500** — but Starter includes a *monthly summary review email from a strategist* which BYO base does not; pricing them at parity makes Starter the rational pick for any buyer who values "someone is watching this for me." Cleanly captures the *less-than-Starter* buyer without giving Starter buyers a reason to defect.

- **Growth ($5,000) protection:** BYO sum to reach Growth's config = $1,500 base + $700 (30 KW) + $900 (1 brief) + $900 (biweekly call) + $500 (Slack-24h) + $300 (Hybrid) = **$4,800**. Adjusted: bump biweekly cadence to +$1,100 so Growth-equivalent BYO = **$5,000** at indifference, or set briefs at +$1,100 so Growth-equivalent = **$5,200** > $5,000. **Growth wins on price** by $200/mo + the implicit "we curated this bundle" trust.

- **Pro ($10,000) protection:** BYO sum to reach Pro's config = $1,500 + $3,200 (unlimited KW) + 4×$900 (briefs) + 4×$1,400 (articles) + $2,100 (weekly) + $1,200 (Slack-same-day) + $700 (Live-led) = $1,500 + $3,200 + $3,600 + $5,600 + $2,100 + $1,200 + $700 = **$17,900**. Pro at $10,000 wins on price by $7,900/mo — the flagship is dramatically the rational discount once content volume is in play.

- **Ceiling routing:** Configurations above $9,500 auto-route to Pro. No BYO permutation can exit checkout priced above the flagship.

**Net effect:** BYO opens a new $1,500–$4,800 band (mostly capturing buyers who currently bounce from Starter as "too much" or who currently churn from Growth wanting "less call, more dashboard"), while every existing tier remains the cheapest path to its own configuration.
