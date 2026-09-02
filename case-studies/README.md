# PraxFlow Case Studies

Case studies show how PraxFlow behaves in real engineering work. They are not marketing testimonials and should not hide failures.

## Evidence standard

A useful case study distinguishes:

- **Observed** — what the agent/project/tools actually did;
- **Sourced** — facts backed by project or external references;
- **Inferred** — interpretation derived from evidence;
- **Unknown** — relevant information not established.

Do not invent metrics after the fact. If a run was not controlled, label it qualitative.

## Recommended structure

```markdown
# Case Study: ...

## Context
## Engineering goal
## Why this task is difficult
## Available evidence and capabilities
## PraxFlow packages used
## Workflow
## Important decisions
## Failures / corrections
## Verification
## What PraxFlow helped with
## What it did not solve
## Lessons for the methodology
## Reproducibility / artifacts
```

## First reference case

The planned first reference case is an embedded MCP2518FD / RT-Thread driver workflow because it exercises:

- unfamiliar-project understanding;
- hardware-authoritative evidence;
- errata handling;
- reference implementation comparison;
- design convergence;
- bounded implementation;
- review;
- build/deploy capability;
- target/device verification.

A retrospective write-up is useful, but it must not be presented as a controlled eval unless baseline runs and artifacts are actually preserved. Quantitative claims should come from [`../evals/`](../evals/), not be reconstructed from memory.
