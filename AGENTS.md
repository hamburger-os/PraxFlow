# PraxFlow Maintainer Guidance

This repository defines an opinionated, portable engineering methodology for AI agents. Keep the conceptual model small and test abstractions against real workflows before adding new nouns.

## Source-of-truth model

PraxFlow has four first-class concepts:

- **Workflow**: an end-to-end cognitive loop for a class of goals.
- **Skill**: a reusable cognitive method used by multiple workflows.
- **Protocol**: cross-cutting behavioral and information rules.
- **Capability**: a concrete action supplied by the current project/environment.

Agent Skills (`SKILL.md`) are the distribution format. Do not confuse an Agent Skill package with the PraxFlow conceptual type `Skill`.

All installable PraxFlow packages share one canonical repository root:

```text
skills/<package-name>/SKILL.md
```

This is a **PraxFlow repository convention**, not a requirement of the Agent Skills specification. The specification defines what belongs inside a Skill directory; clients and repositories decide where Skill directories live. Do not create separate canonical `workflows/` or `packs/` trees. Conceptual type belongs in `metadata.praxflow-type`.

## Documentation audiences and language

Keep documentation separated by its primary consumer.

### AI-facing material

Use English by default for material that is loaded or followed by agents:

- `AGENTS.md` and equivalent agent instructions;
- `skills/*/SKILL.md`;
- package-local `references/`;
- package-local scripts, templates, and agent-facing resource text.

Optimize this material for precise agent behavior, progressive disclosure, and portability rather than tutorial-style prose.

### Human maintainer material

Use Simplified Chinese by default for documentation whose main purpose is repository design, maintenance, release operation, or project administration for the primary maintainer. Examples include release procedures, repository settings, and internal design notes.

Do not translate code identifiers, package names, commands, frontmatter keys, or normative external terminology when translation would make them harder to verify.

### Community and user material

Public user documentation may be English or bilingual. Major user entry points should provide an English version and a Simplified Chinese counterpart when practical.

User documentation should explain:

- what the mechanism is;
- why it exists and the basic reasoning behind it;
- when to use it and when not to;
- how to install and use it;
- what behavior or output to expect;
- important limitations or compatibility boundaries.

Keep human tutorials under `docs/` rather than duplicating them inside every installable package.

### Skill package documentation boundary

Do **not** add `README.md` to each `skills/<name>/` package by default. Agent Skills requires `SKILL.md`; `scripts/`, `references/`, `assets/`, and other files are optional supporting resources. A README is legal extra content but has no special role in the Agent Skills specification or activation model.

Add package-local supporting documentation only when an agent needs it at runtime, normally under `references/`. Put human-oriented explanations, examples, and tutorials under `docs/`.

When documenting format or discovery behavior, distinguish explicitly between:

1. **Agent Skills specification requirements** — the portable package format and its defined fields/conventions;
2. **PraxFlow repository conventions** — for example the canonical source catalog at `skills/*/SKILL.md` and `metadata.praxflow-type`;
3. **client conventions or behavior** — for example `.agents/skills/`, `.claude/skills/`, installer flags, and vendor-specific extensions.

Do not describe a PraxFlow or client convention as if it were mandated by the Agent Skills specification.

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

- `name` must match its parent directory;
- use lowercase ASCII letters, digits, and single hyphens only;
- `description` must explain both purpose and trigger conditions;
- use `metadata` for PraxFlow-specific conceptual type and version;
- keep main instructions concise; move on-demand detail to `references/`;
- keep package identity and resources self-contained under `skills/<name>/`.

PraxFlow deliberately publishes its source catalog as immediate children of `skills/` so common repository installers can discover packages without PraxFlow-specific recursion. Treat that layout as a PraxFlow interoperability choice, not as a universal Agent Skills filesystem requirement.

Do not rely on vendor-specific frontmatter in Core packages unless it is optional and compatibility-safe. Optional root-level catalog metadata may improve presentation, but must not become required for package identity, discovery, or runtime behavior.

## Domain packs

A Domain Pack may enrich:

- evidence policy;
- review policy;
- verification strategy;
- domain-specific cognitive skills.

It must not duplicate Core workflows or encode project-specific commands and architecture facts.

A Domain Pack is packaged under `skills/` exactly like every other installable Agent Skill unit; `metadata.praxflow-type: "pack"` preserves its PraxFlow conceptual role.

## Project capabilities

Build commands, test commands, deployment targets, serial ports, credentials, device addresses, environment URLs, and similar details belong to the consuming project, not PraxFlow Core.

## Validation

Run before considering a repository change complete:

```bash
python3 scripts/validate.py
```

Also inspect changed `SKILL.md` descriptions for trigger overlap and conceptual duplication. Passing syntax validation is not sufficient.

Distribution-related changes must additionally preserve zero-special-case discovery from PraxFlow's flat `skills/*/SKILL.md` source catalog. CI smoke-tests an external Agent Skills installer for this reason.

## Documentation changes

When the conceptual model changes, update at least:

- `README.md`;
- `README.zh-CN.md`;
- `docs/concepts.md`;
- `docs/concepts.zh-CN.md`;
- affected packages under `skills/`;
- `docs/roadmap.md` and `docs/roadmap.zh-CN.md` if scope changes.

When public installation or usage behavior changes, update both user guides:

- `docs/getting-started.md`;
- `docs/getting-started.zh-CN.md`.

When distribution behavior changes, also update `adapters/README.md`, installer/validator tests, and release guidance when relevant.

Prefer deletion and consolidation over adding another abstraction.
