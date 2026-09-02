# PraxFlow Concepts

PraxFlow separates methodology from packaging and environment execution. This document is the conceptual reference for v0.1.

## Workflow

A Workflow is an end-to-end cognitive loop for a class of goals. It defines meaningful phases, branching, human checkpoints, failure paths, and completion criteria.

A Workflow is not merely a list of Skills. Different task types can reuse the same Skills while requiring different cognitive structures.

Examples:

- `develop-feature`: intent → understand → clarify → design → plan → execute → review → verify.
- `fix-bug`: symptom → expected behavior → characterize → diagnose → causal fix → regression verification.
- `understand-project`: question → orient → survey → trace → provisional model → explain.
- `review-change`: intent → scope → inspect → challenge findings → report high-signal issues.

## Skill

A Skill is a reusable cognitive method used in more than one Workflow.

A Core Skill should be worth activating independently because it improves *how* the agent reasons, not because it names an ordinary action the agent can already perform.

Examples:

- `survey`: establish where to look and how far to explore.
- `trace`: reconstruct a behavior across calls, events, data, state, async boundaries, and lifecycles.
- `grill`: converge an under-specified problem by investigating before asking and escalating only consequential choices.
- `diagnose`: compare causal hypotheses and design high-information experiments.
- `plan-change`: bound the causal impact of a change before high-cost editing begins.

## Protocol

A Protocol is a cross-cutting rule set that applies across Workflows and Skills.

Protocols are not intended to be invoked as standalone commands. They define how claims, decisions, changes, verification, and durable knowledge should be handled.

Core protocols:

- **Evidence** — how claims are grounded and conflicts are surfaced.
- **Decisions** — what the agent may resolve autonomously and what requires human judgment.
- **Change Scope** — how to minimize collateral change without confusing minimal diff with correct causal repair.
- **Verification** — how completion claims are supported by proportionate external evidence.
- **Knowledge** — what should be persisted beyond ephemeral model context.

## Capability

A Capability is a concrete action available in the current environment.

Examples:

- `build`
- `test`
- `lint`
- `deploy`
- `flash`
- `read-serial`
- `ssh-target`
- `open-browser`
- `query-database`

Capabilities are project- or environment-specific. PraxFlow Core should not hard-code the command that implements them.

The separation is:

```text
Methodology decides WHEN and WHY an action is needed.
Capabilities define HOW the current environment performs it.
```

## Skill Package vs conceptual Skill

The Agent Skills open format uses a directory with `SKILL.md` as a portable distribution unit. PraxFlow uses that format for multiple conceptual types.

Therefore:

```text
develop-feature/SKILL.md
```

is technically an Agent Skill package but conceptually a PraxFlow **Workflow**.

Likewise:

```text
trace/SKILL.md
```

is both an Agent Skill package and a PraxFlow **Skill**.

PraxFlow records the conceptual type in `metadata.praxflow-type`.

## Domain Pack

A Domain Pack enriches Core behavior without copying Core Workflows.

A pack may add:

- evidence authority and conflict policy,
- domain-specific review concerns,
- verification strategy,
- genuinely domain-specific cognitive Skills.

A pack must not contain project-specific commands, credentials, architecture facts, or deployment targets.

## Working artifacts

Different Workflows create different artifacts. PraxFlow does not force every task through a universal `write-spec` Skill.

Examples:

- `develop-feature` may create a compact change spec.
- `fix-bug` creates a failure model and causal fix plan.
- `understand-project` creates a provisional working model.
- `review-change` creates a review contract and findings.

Artifacts exist to support reasoning, alignment, or handoff. They are not automatically durable documentation.

## Ephemeral context vs project knowledge

Temporary reasoning belongs in the active working context. Stable, reusable facts and decisions may be promoted into project-owned documentation.

Do not persist:

- exploratory dead ends,
- temporary hypotheses,
- a transcript of every interaction,
- transient tool output.

Consider persisting:

- stable architecture facts,
- durable constraints,
- consequential decisions,
- important invariants,
- recurring project capabilities,
- failure modes that materially affect future engineering.

## v0.1 non-goals

PraxFlow v0.1 does not define:

- a Workflow DSL,
- a custom runtime,
- a marketplace,
- a universal model-selection policy,
- a replacement for MCP/tools,
- a universal project documentation format,
- a generic `implement` Skill,
- a generic `verify` Skill.

These can be reconsidered only when real usage produces evidence that the current structure is insufficient.
