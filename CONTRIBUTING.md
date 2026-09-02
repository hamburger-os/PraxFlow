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

## Agent Skills format

All installable packages live one directory below one of:

```text
workflows/
skills/
packs/
```

Each package must contain `SKILL.md` and follow the Agent Skills open specification.

At minimum:

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

`name` must match the directory name.

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

For normative Agent Skills conformance, also use the upstream `skills-ref` validator when available.

## Compatibility changes

Client-specific installation paths and extensions belong under `adapters/` and `scripts/install.py`.

Verify current vendor documentation before changing compatibility behavior. Do not turn vendor-specific extensions into Core requirements.

## Pull request scope

Keep methodology changes reviewable. Prefer one conceptual change per PR when possible.

If you add an abstraction, also state what existing complexity it removes or what observed failure it uniquely solves.
