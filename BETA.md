# Intelligent Clay — Beta Program

The skill is publicly stable at v1.1, but the highest-leverage way to make it better is feedback from real consultants, coaches, and agencies running their actual offerings through it. The synthetic test battery catches *logic* gaps; only real domain practitioners catch *blindspot* gaps.

This document explains how the beta program works.

## What you get as a beta participant

- A direct line to the maintainer for blueprint reviews (turnaround within ~1 week).
- Your domain considered for explicit inclusion in the standard reference pack — if your vertical recurrently exposes a gap, your patterns become first-class.
- Co-authorship credit on the SKILL.md commit that addresses your feedback (your call — opt in or stay anonymous).
- Early access to v1.x features (configurator-output mode, claude-mem integration, vertical-specific reference packs) before they ship publicly.

## What we ask in return

1. **Run the skill on a real offering** — your own, or one you're advising on. Synthetic prompts won't help us; reality will.
2. **Capture the output** as-is, even if you disagree with parts.
3. **File a feedback issue** using the template at [`.github/ISSUE_TEMPLATE/beta-feedback.yml`](.github/ISSUE_TEMPLATE/beta-feedback.yml). Tell us:
   - What domain / what kind of offering
   - What the skill nailed
   - What it got wrong, missed, or oversimplified
   - The full output (or relevant excerpt)
4. **Stay engaged enough** to confirm whether a proposed fix actually addresses your concern. One round of follow-up is usually enough.

## What we don't ask

- We don't ask for public attribution unless you want it.
- We don't ask for the original client/offering details that would identify a third party — generalize them.
- We don't ask for promotion, social posts, or endorsements. The skill should earn its own keep.

## Privacy

- Run on real offerings means real numbers and real services. **Generalize before sharing.** Replace client names, identifying revenue specifics, and proprietary methodology details with neutral analogs.
- Anything you commit to a beta-feedback issue becomes public on GitHub. If sensitivity is a concern, email the maintainer at `disrupt@autonomad.ai` instead of opening a public issue.

## How feedback becomes skill improvements

1. Beta issue is filed.
2. Maintainer triages: is this a one-off (case-specific tuning) or a pattern (the skill has a real gap)?
3. Patterns become a `references/*.md` addition or an explicit anti-pattern in `SKILL.md`.
4. The next self-iteration GH Action run (or a manual one) validates the change against the test prompt battery.
5. PR opens; if you're a beta participant, you're tagged for review.
6. Merge ships in the next minor version. Your name lands in `CHANGELOG.md` if you opted in.

## How to apply

There's no formal application — open an issue with the template and label `beta-feedback`. Practical limit: roughly 5 active beta participants at a time, to keep response quality high. Slots reopen as cases close.

## Out of scope (don't expect)

- Custom configurator UI built for you (that's the Premium tier in [`examples/intelligent-clay-on-itself.md`](examples/intelligent-clay-on-itself.md)).
- Pricing strategy advice beyond the structural anchor logic the skill already provides.
- Ghostwriting your sales page (use offer-extraction or Dunford-style skills).
- Revenue-share, white-labeled forks, or commercial licensing — separate conversation.

## Maintainer

Autonomad — `disrupt@autonomad.ai`
