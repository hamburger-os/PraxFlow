---
name: plan-change
description: Bound the causal impact of a non-trivial software change before editing. Use after enough understanding exists to identify the intended mechanism, affected components, contracts, state/data-flow effects, non-goals, and verification path so wrong-direction or collateral changes are caught before implementation.
license: MIT
metadata:
  praxflow-type: "skill"
  praxflow-version: "0.1"
  praxflow-status: "provisional"
---

# Plan Change

Create a **change boundary**, not a generic todo list.

This Skill exists only while it provides non-trivial value beyond an agent's ordinary planning ability. Keep it focused on impact, contracts, and causal scope.

## Entry condition

Use when:

- the change is non-trivial or spans multiple files/components;
- public behavior, state, lifecycle, concurrency, persistence, dependencies, or resources may change;
- a wrong implementation direction would be expensive;
- a bug fix has an established causal model and is ready for repair.

Skip for obvious, low-risk edits where the plan would merely restate the task.

## Method

### 1. Restate the causal intent

State what mechanism or behavior must change and why.

For a feature:

```text
Current behavior -> desired behavior
```

For a bug:

```text
Established cause -> causal repair
```

If the mechanism is not understood well enough to state this, investigate or diagnose first.

### 2. Identify the expected change surface

List only areas that have a causal reason to change.

For each important area, explain why it belongs in scope.

Consider:

- files/components;
- public/private interfaces;
- state machines;
- data flow;
- ownership/lifetime;
- async/concurrency boundaries;
- persistence/data formats;
- dependencies/resources;
- configuration;
- tests/verification hooks.

### 3. Identify contracts and constraints

Make externally meaningful boundaries explicit when relevant:

- compatibility requirements;
- API/error semantics;
- data/protocol format;
- ordering/timing guarantees;
- memory/resource budgets;
- safety/security constraints;
- domain-pack rules;
- accepted human decisions.

### 4. State non-goals

Name tempting nearby work that should not be included.

Examples:

- no public API redesign;
- no unrelated naming cleanup;
- no directory reorganization;
- no replacement of an existing abstraction unless causally required.

Non-goals are useful when they prevent scope drift; do not invent ceremonial non-goals for tiny tasks.

### 5. Order implementation around risk

Prefer steps that expose wrong assumptions early.

Examples:

- change one underlying invariant before all callers;
- add/adjust a focused test before broad refactoring;
- separate compatibility migration from cleanup;
- validate a hardware/protocol assumption before writing the full path.

### 6. Define verification before editing

Identify the strongest relevant checks that should demonstrate success.

Do not hard-code project commands. Use available project capabilities.

For bug fixes, include:

- original failing condition;
- causal verification when feasible;
- nearby regression surface.

### 7. Reassess on scope expansion

If implementation discovers a need to change a new public contract, dependency, architecture boundary, or consequential resource assumption, stop and update the plan. Use a Decision Gate when the expansion changes an accepted tradeoff or boundary.

## Output

Prefer a concise plan:

```markdown
## Intent
...

## Change surface
- component/file — causal reason

## Contracts / constraints
...

## Non-goals
...

## Execution order
1. ...
2. ...

## Verification
...
```

## Stop condition

The plan is ready when an implementer can make the bounded change without rediscovering the core intent, hidden contract, or verification strategy.

Do not plan implementation line-by-line when the code itself is the cheaper and clearer representation.
