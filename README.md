# Intelligent Clay

> Take any service or offering and turn it into modular, configurable, customer-buildable shape.

**Intelligent Clay** is an open-source skill for [Claude](https://claude.ai) that helps service providers, consultants, coaches, and agencies transform their fixed offerings into modular, configurable products. If you've ever felt your service was "too custom to scale" or wanted to give customers a build-your-own version of what you do — this skill is for you.

The metaphor is clay: take something solid and make it shapeable.

---

## What it does

Give Intelligent Clay a description of your existing service or product, and it produces a three-part transformation:

1. **Atomic decomposition** — breaks your offering into its smallest standalone components (deliverables, time blocks, access tiers, support levels, customizations).
2. **Configuration architecture** — defines the dimensions on which customers can customize (depth, breadth, pace, format, support level, add-ons), including valid combinations and dependencies.
3. **Tiered package recommendations** — three suggested starter configurations (Lite / Core / Premium) plus a build-your-own framework, each with positioning language and pricing logic.

The output is the structural blueprint for productizing a service — not marketing copy, not a positioning statement, but the underlying architecture that makes both possible.

---

## Who it's for

- Solo consultants and coaches wanting to scale beyond 1-on-1 work
- Boutique agencies looking to productize bespoke engagements
- Freelancers ready to package their services into tiers
- Service-based founders building configurable offerings
- Course creators designing modular curricula

---

## How it's different from other skills

The Claude skills ecosystem already has strong coverage in adjacent areas:

- **Offer design and copy** (e.g., Kim Barrett's `offer-extraction`, Hormozi-influenced offer skills) — these focus on *how to sell* an offering
- **Product management frameworks** (e.g., Digidai PM skills, Dean Peters' Product-Manager-Skills) — these focus on *roadmap, discovery, and execution*
- **Positioning** (e.g., Dunford-style skills) — these focus on *who the offering is for and why it wins*

Intelligent Clay sits in a gap none of those fill: **structural decomposition and reconfiguration**. It's the LEGO-fication step that has to happen before any of those other skills become useful for a custom service.

---

## Installation

### Claude Code

```bash
# Clone into your skills directory
git clone https://github.com/Autonomad1/intelligent-clay ~/.claude/skills/intelligent-clay
```

Or via the plugin marketplace (if you publish it that way):

```bash
/plugin marketplace add Autonomad1/intelligent-clay
```

### Claude.ai

Upload the `.skill` file via Settings → Capabilities → Skills.

### Claude API

Reference the skill via the `/v1/skills` endpoint with the Code Execution beta header. See [Anthropic's Skills API documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

---

## Usage

Once installed, the skill triggers automatically when you describe a service productization need. Example prompts:

> "I'm a freelance brand strategist. I charge $15K for a 6-week engagement that ends in a brand guide. Help me modularize this."

> "I run a fitness coaching business — 1-on-1 only. I want a build-your-own version."

> "I'm a consultant who does change management for mid-market companies. Each engagement is custom. Productize this."

> "My service feels too custom to scale. Help me find the modular structure."

You can also invoke it directly:

> "Use Intelligent Clay on my offering: [description]"

---

## Example output (abbreviated)

> Excerpted from a real run of the skill on a fresh agent. Full transcripts for all three test prompts are in [`examples/`](examples/).

**Input:** "I'm a freelance brand strategist. I charge $15K for a 6-week engagement that ends in a brand guide. Help me modularize this."

**Atomic decomposition (excerpt):**
- *Deliverables:* Brand audit, competitive landscape map, positioning statement, messaging hierarchy, brand voice guide, naming recommendation, visual identity direction, brand guide PDF, one-page summary, launch playbook
- *Time blocks:* 60-min kickoff workshop · 45-min stakeholder interview · 30-min customer interview · 90-min positioning workshop · 60-min handoff session
- *Access tiers:* Email-only (48-hr) · Slack/Loom async (24-hr) · Voxer + weekly call · Direct line, business hours
- *Support levels:* Single-pass · 1 revision round · 2 revision rounds · 30/60/90-day async review · Office-hours retainer
- *Customizations:* Industry depth, # stakeholder interviews (3/6/10), # customer interviews (0/5/10), B2B vs B2C, internal-only vs agency-handoff-ready

**Configuration architecture (6 dimensions, with dependencies):**
- *Depth* — Light / Standard / Deep
- *Breadth* — Verbal-only / Verbal + Visual / Full System
- *Pace* — Sprint (2w) / Standard (6w) / Deep (10w) — *Sprint pace invalid with Deep depth*
- *Format* — Async / Hybrid / Live-led — *Async invalid with Deep depth*
- *Support* — Single-pass / Standard / High-touch
- *Add-ons* — Naming sprint, customer interview pack, designer handoff, retainer, executive one-pager — *Naming requires Breadth ≥ Verbal+Visual*

**Tiered packages + Build-Your-Own:**

| Tier | Price | Configuration (excerpt) | Pricing logic |
|------|-------|-------------------------|---------------|
| **Lite — Positioning Sprint** | $6,500 | Light · Verbal-only · Sprint · Async · Single-pass | Anchored against the cost of a bad positioning bet — ~40% of flagship to be a clear entry point |
| **Core — Brand Guide** *(current flagship)* | $15,000 | Standard · Verbal + Visual · Standard · Hybrid · 1 revision | Anchored against typical agency engagements ($25–50K) — senior-strategist-only at half the price |
| **Premium — Brand System + Embed** | $32,000 | Deep · Full System · Deep · Live-led · High-touch | Anchored against consultancy retainer + naming engagement (sum-of-parts ~$45K); tier prices at a discount |

**Build-your-own** uses Lite as the base, with per-dimension upgrade pricing (e.g., +$3,500 for Depth Light → Standard, +$2,500 for Breadth +Visual), a $6,500 floor, a $28,000 ceiling above which the configurator routes to Premium, and dependencies it must enforce (block Sprint+Deep, Async+Deep, Naming without Visual, etc.).

See [`examples/brand-strategist.md`](examples/brand-strategist.md) for the full output, and [`examples/fitness-coach.md`](examples/fitness-coach.md) and [`examples/change-management-consultant.md`](examples/change-management-consultant.md) for the other test runs.

---

## Project structure

```
intelligent-clay/
├── SKILL.md                                    # The main skill file
├── README.md                                   # You are here
├── LICENSE
└── examples/
    ├── brand-strategist.md                     # Real run on a $15K brand engagement
    ├── fitness-coach.md                        # Real run on 1-on-1 fitness coaching
    └── change-management-consultant.md         # Real run on mid-market change mgmt
```

---

## Status

✅ **Stable v1.0** — tested via TDD-for-skills against three test prompts (brand strategist, fitness coach, change-management consultant) with a baseline-vs-skill comparison. All three GREEN tests produce the full 3-part blueprint with explicit dimensions, dependencies, and a Lite/Core/Premium + BYO framework. See [`examples/`](examples/) for the verbatim outputs.

Feedback, issues, and pull requests welcome.

---

## Contributing

This is an open-source project. Contributions of all kinds are welcome:

- **Test cases** — share offerings you've run through the skill and how the output landed
- **Edge cases** — flag service types that don't decompose cleanly
- **Reference patterns** — submit decomposition patterns from your industry
- **Bug fixes and clarifications** to the SKILL.md itself

Open an issue or PR on GitHub.

---

## License

[MIT License](LICENSE) — free to use, modify, and redistribute. Attribution appreciated but not required.

---

## Author

Created by **Autonomad**.

If Intelligent Clay helps you productize your service, I'd love to hear about it — open an issue, send a PR with your story, or reach out at [disrupt@autonomad.ai](mailto:disrupt@autonomad.ai).

---

## Acknowledgments

- Built with [Anthropic's Claude](https://claude.ai) and the official [skill-creator](https://github.com/anthropics/skills) toolkit
- Inspired by every consultant who has ever stared at a custom proposal and thought "there has to be a better way to package this"
