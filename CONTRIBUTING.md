# Contributing to PraxFlow

PraxFlow is intentionally small. Contributions should improve demonstrated agent behavior, not increase the number of framework concepts.

## Before proposing a new Core Skill

A Core Skill should satisfy all of these:

1. It solves a recurring, well-bounded cognitive problem.
2. It is independently reusable in multiple Workflows.
3. It contains a non-obvious method beyond ordinary agent execution.
4. It has meaningful entry conditions, process, stop conditions, and output behavior.
5. It is not inherently tied to one domain, project, model, or client.
6. There is a plausible way to evaluate whether it improves agent reliability.

If the idea is simply “tell the agent to do X,” it probably belongs inside a Workflow phase or project capability rather than a new Skill.

## Before proposing a new Workflow

Show that the task class has a meaningfully different cognitive structure from existing Workflows.

A new Workflow should not be a renamed variant such as:

```text
backend-develop-feature
embedded-develop-feature
frontend-develop-feature
```

Use Domain Packs to enrich Core workflows instead.

## Domain Packs

A Domain Pack may define:

- evidence applicability/authority rules;
- domain review dimensions;
- verification strategy;
- genuinely domain-specific cognitive Skills.

Do not include:

- project-specific commands;
- credentials/hosts/ports;
- one project's architecture facts;
- copies of Core Workflows;
- model/token selection policy that only reflects one organization.

## Agent Skills format and PraxFlow repository layout

The Agent Skills specification defines the contents of an individual Skill directory. At minimum, a package contains `SKILL.md`; `scripts/`, `references/`, `assets/`, and other supporting files are optional.

PraxFlow additionally chooses one canonical **repository** source layout for interoperability and maintainability:

```text
skills/<package-name>/SKILL.md
```

This flat source catalog is a PraxFlow convention, not a requirement that the Agent Skills specification imposes on every repository or client. Do not create separate top-level `workflows/` or `packs/` source trees. Workflow / Skill / Pack is a PraxFlow conceptual classification, not a universal filesystem rule.

Each package must contain `SKILL.md` and follow the Agent Skills open specification.

At minimum for PraxFlow packages:

```yaml
---
name: package-name
description: Explain what it does and when to use it.
license: MIT
metadata:
  praxflow-type: "workflow | skill | pack"
  praxflow-version: "0.1"
---
```

`name` must match the directory name. `metadata.praxflow-type` must be one of `workflow`, `skill`, or `pack`.

Keep package resources self-contained. Put on-demand supporting material that agents need at runtime in `references/`, executable helpers in `scripts/`, and static resources in `assets/`. Prefer shallow relative references from `SKILL.md`.

Do **not** add a README to every Skill package by default. `README.md` is permitted as an extra file by the specification, but it has no special role in Skill discovery or activation. Human-oriented explanations, tutorials, principles, and usage examples belong under `docs/`; package-local documentation should exist because the agent needs it while executing the Skill.

The flat `skills/*/SKILL.md` source catalog is deliberate: PraxFlow taxonomy belongs in metadata and catalog presentation, while the repository stays easy for common Agent Skills tooling to consume without PraxFlow-specific recursive discovery.

## Documentation audiences

Keep the primary reader explicit.

- **AI-facing instructions and package resources:** English by default. This includes `AGENTS.md`, `skills/*/SKILL.md`, and package-local `references/`.
- **Primary-maintainer operational/design documentation:** Simplified Chinese by default when the document mainly exists to support repository maintenance.
- **Community and user documentation:** English or bilingual. Major user entry points should offer English and Simplified Chinese counterparts when practical.

User documentation should explain both principles and usage: what the mechanism does, why it exists, when to use it, how to install/invoke it, what behavior to expect, and important limitations.

When writing about compatibility, clearly distinguish:

1. Agent Skills specification requirements;
2. PraxFlow repository conventions;
3. client-specific conventions and vendor behavior.

Do not elevate a PraxFlow or client convention into a claim about the open specification.

## Protocol changes

Top-level `protocols/*.md` files are the maintainer source-of-truth for cross-cutting methodology. They are intentionally not installed as standalone packages; portable packages under `skills/` embed the operational guidance they need.

Because of that split, a Protocol-only runtime change is incomplete. If a Protocol changes, update at least one affected installable package under `skills/` in the same PR. CI enforces this coarse-grained sync rule so the maintainer reference cannot silently drift away from distributed behavior.

Purely editorial Protocol changes should normally avoid changing normative meaning. If an editorial change genuinely needs no package update, explain why in the PR and make the smallest package-side synchronization needed to keep the source-of-truth relationship explicit.

## Writing guidance

Prefer instructions that change agent behavior:

- how to distinguish facts from inference;
- how to choose the next investigation;
- when to stop;
- how to avoid confirmation bias;
- how to expose scope or verification gaps.

Avoid filler such as:

- “think carefully”;
- “write high-quality code”;
- generic best-practice lists without decision context;
- large checklists that apply to only a small subset of tasks.

## Evidence for changes

When changing methodology, explain the failure mode that motivated the change.

Strong contributions often include:

- a real task where the existing Skill/Workflow failed;
- before/after agent behavior;
- a minimal reproducible eval scenario;
- evidence that a proposed rule reduces noise, wrong changes, or unsupported conclusions.

## Validate

Run:

```bash
python3 scripts/validate.py
```

For normative Agent Skills conformance, also run the pinned/reference `skills-ref validate` check used by CI when package format or content changes. CI additionally exercises Python 3.10 compatibility, the built-in installer, external catalog installation, and Protocol/package synchronization.

A package-format or repository-distribution change is incomplete if PraxFlow's own validator passes but the supported external installer path cannot discover the intended `skills/<name>/SKILL.md` source catalog without a PraxFlow-specific workaround.

## Compatibility changes

Client-specific installation paths and extensions belong under `adapters/` and `scripts/install.py`.

Verify current vendor documentation before changing compatibility behavior. Do not turn vendor-specific extensions into Core requirements. Optional ecosystem metadata such as `skills.sh.json` may improve presentation, but canonical package identity must remain fully derivable from each package directory and its `SKILL.md`.

## Pull request scope

Keep methodology changes reviewable. Prefer one conceptual change per PR when possible.

If you add an abstraction, also state what existing complexity it removes or what observed failure it uniquely solves.
