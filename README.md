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

**Input:** "I'm a freelance brand strategist charging $15K for a 6-week engagement."

**Atomic decomposition:**
- Discovery interviews (3 × 60min)
- Competitor audit (deliverable)
- Positioning workshop (1 × 3hr)
- Brand guide draft (deliverable)
- Revision rounds (2 included)
- Implementation handoff call (1 × 60min)

**Configuration architecture:**
- *Depth*: number of discovery interviews (1, 3, or 5)
- *Breadth*: brand guide scope (verbal-only, verbal + visual, full system)
- *Pace*: 3-week sprint vs. 6-week standard vs. 12-week deep
- *Support*: workshop-only vs. workshop + revisions vs. ongoing retainer

**Tiered packages:**
- **Clay Lite** ($4K) — 1 interview, verbal positioning only, async delivery
- **Clay Core** ($12K) — 3 interviews, verbal + visual, 6-week pace, 1 revision
- **Clay Custom** ($15K+) — full configurator with add-ons

---

## Project structure

```
intelligent-clay/
├── SKILL.md           # The main skill file
├── README.md          # You are here
├── LICENSE
└── references/
    ├── decomposition-patterns.md
    ├── configuration-dimensions.md
    └── tiering-logic.md
```

---

## Status

🚧 **Early draft** — actively iterating. Feedback, issues, and pull requests welcome.

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
