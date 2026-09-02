# PraxFlow Maintainer Guidance

This repository defines an opinionated, portable engineering methodology for AI agents. Keep the conceptual model small and test abstractions against real workflows before adding new nouns.

## Source-of-truth model

PraxFlow has four first-class concepts:

- **Workflow**: an end-to-end cognitive loop for a class of goals.
- **Skill**: a reusable cognitive method used by multiple workflows.
- **Protocol**: cross-cutting behavioral and information rules.
- **Capability**: a concrete action supplied by the current project/environment.

Agent Skills (`SKILL.md`) are the distribution format. Do not confuse a Skill Package with the PraxFlow conceptual type `Skill`.

## v0.1 Core

Workflows:
- `develop-feature`
- `fix-bug`
- `understand-project`
- `review-change`

Skills:
- `survey`
- `trace`
- `grill`
- `diagnose`
- `plan-change` (provisional; remove it if its implementation proves trivial)

Protocols:
- `evidence`
- `decisions`
- `change-scope`
- `verification`
- `knowledge`

Reference domain pack:
- `praxflow-embedded`

## Design discipline

Before adding a new Core Skill, verify all of the following:

1. It solves a recurring and well-bounded cognitive problem.
2. It is independently reusable in multiple workflows.
3. It contains a non-obvious method, not merely an instruction to perform an ordinary agent action.
4. It has meaningful entry conditions, process, stop conditions, and outputs.
5. It is not inherently domain-, project-, model-, or tool-specific.
6. Removing the package would materially reduce agent reliability or consistency.

Do not create Core Skills for ordinary execution verbs such as implement, edit, run, build, test, verify, reproduce, or write-docs unless real evidence shows a reusable cognitive method exists beyond the platform's native ability.

## Reasoning principles

- Extract principles from prior practices; do not preserve old prescriptions merely because they already exist in a guide.
- Treat project models as provisional and goal-directed.
- Keep assumptions visible.
- Surface authoritative conflicts instead of silently choosing a source.
- Prefer minimal causal change over minimal textual diff.
- Use proportionate external verification before claiming completion.
- Ask humans for consequential decisions, not facts the agent can investigate.
- A valid review may contain zero findings.
- A plausible first hypothesis is not a root cause.

## Agent Skills compatibility

Every installable package must contain `SKILL.md` with Agent Skills-compatible YAML frontmatter:

- `name` must match its parent directory.
- lowercase ASCII letters, digits, and hyphens only.
- `description` must explain both purpose and trigger conditions.
- use `metadata` for PraxFlow-specific conceptual type and version.
- keep main instructions concise; move domain detail to `references/`.

Do not rely on vendor-specific frontmatter in Core packages unless it is optional and compatibility-safe.

## Domain packs

A Domain Pack may enrich:

- evidence policy,
- review policy,
- verification strategy,
- domain-specific cognitive skills.

It must not duplicate Core workflows or encode project-specific commands and architecture facts.

## Project capabilities

Build commands, test commands, deployment targets, serial ports, credentials, device addresses, environment URLs, and similar details belong to the consuming project, not PraxFlow Core.

## Validation

Run before considering a repository change complete:

```bash
python3 scripts/validate.py
```

Also inspect changed `SKILL.md` descriptions for trigger overlap and conceptual duplication. Passing syntax validation is not sufficient.

## Documentation changes

When the conceptual model changes, update at least:

- `README.md`
- `docs/concepts.md`
- affected Workflow/Skill/Protocol packages
- `docs/roadmap.md` if scope changes

Prefer deletion and consolidation over adding another abstraction.
