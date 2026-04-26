# Memory integration — autonomous self-improvement

Intelligent Clay can use a persistent memory layer to learn from every run, surface relevant past blueprints, and propose improvements to itself over time. This reference describes both the mechanism and the integration points.

## Why memory

Without memory, every run is naive: the skill produces a blueprint from first principles, no matter how many times it's seen the same domain. With memory, the skill can:

- **Retrieve similar past offerings** — "I've seen 4 SEO retainer productizations before; the dimensions that proved load-bearing were Tracking Scope, Reporting Cadence, Content Production."
- **Apply learned dependencies** — pricing patterns, common dependency conflicts, dimension inventions that worked.
- **Self-improve** — when the user corrects an output, that correction becomes a future input.

## Substrate: claude-mem

Intelligent Clay uses [claude-mem](https://github.com/anthropics/claude-mem) as the memory substrate when available in the user's environment. claude-mem provides:

- A persistent observation database that survives across sessions
- Tag-based retrieval (`mem-search`)
- Knowledge-base building (`knowledge-agent`) — turns accumulated observations into queryable expertise

Falls back gracefully when claude-mem is not installed.

## Integration points

### 1. Ingest after every run

After producing a blueprint, save the run as a tagged observation:

```
tag: intelligent-clay:run
fields:
  domain: <consultant | coach | agency | freelancer | course-creator | other>
  vertical: <free-text label, e.g., "brand strategy", "SEO retainer">
  input_summary: <1-line summary of the user's offering>
  dimensions_used: [<list of dimensions, including any domain-specific>]
  invented_dimensions: [<dimensions outside the standard 6>]
  tier_count_pattern: <"3+BYO" | "existing+BYO-overlay">
  flagship_anchor: <how each tier was priced — "$ figures" | "% of base" | "placeholders">
  notable_dependencies: [<the most non-obvious dependencies the agent enforced>]
  user_corrections: <captured if the user pushes back; default empty>
```

### 2. Retrieve before producing

At the top of every blueprint, the skill should query:

```
mem-search "intelligent-clay:run domain:{inferred_domain} vertical:{inferred_vertical}"
```

If 2+ similar past runs exist, surface a brief preamble:

> *Memory note: I've seen N similar offerings ([list of verticals]). Patterns that proved load-bearing: [dimensions], [dependencies]. Applying those as starting hypotheses; will diverge where this offering differs.*

This is a one-line preamble — not a regurgitation of past outputs. The blueprint that follows is still freshly produced.

### 3. Build a knowledge base periodically

Roughly every 25 runs (or weekly if usage is steady), invoke `claude-mem:knowledge-agent` with the prompt:

> "Build a 'Productization Brain' from observations tagged `intelligent-clay:run`. Compile patterns: which domains use which dimensions, which dependency types recur, which pricing anchors hold up across runs."

The output is a queryable knowledge base the skill (and the user) can consult.

### 4. Self-improvement loop

The autonomous improvement loop runs via [`.github/workflows/self-iterate.yml`](../.github/workflows/self-iterate.yml). It:

1. Reads recent runs from claude-mem (via the GitHub-side equivalent: a JSONL log committed to `runs/`).
2. Identifies patterns: dimensions invented repeatedly across runs (candidates for promotion to standard), dependencies missed at first that the user corrected (candidates for explicit anti-pattern entries), tier-naming conventions that emerged organically (candidates for renaming guidance).
3. Drafts a SKILL.md patch addressing the pattern.
4. Opens a PR titled `chore(skill): self-iterate v{N+1} — {summary}`.
5. The user reviews and merges (or closes).

This loop is **gated by human review** — the PR mechanism ensures no autonomous edit lands without a person validating it. That's intentional. Autonomous editing of the skill itself, without a gate, would risk drift.

## Falling back without claude-mem

If claude-mem is not installed, the skill operates without the preamble. The GH Action loop is the only persistent improvement mechanism, and it relies on the JSONL `runs/` log committed by the user (or, eventually, by an autonomous harness).

The skill should never fail or refuse work because memory is unavailable — memory is an enhancement, not a requirement.

## Privacy note

The user's offering descriptions are personal/business sensitive. claude-mem observations are local to the user's environment by default. The GH Action only reads from `runs/` logs the user has explicitly committed; it never reads claude-mem directly. Users running real client offerings through the skill should review what they commit before pushing.
