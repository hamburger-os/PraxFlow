---
name: grill
description: Converge an under-specified technical goal or design by investigating first, separating facts from choices, recommending before asking, and escalating only the consequential decisions the user must make. Use before implementation when requirements, tradeoffs, constraints, or acceptance criteria are not sufficiently determined.
license: MIT
metadata:
  praxflow-type: "skill"
  praxflow-version: "0.1"
---

# Grill

Help the user make the decisions that actually require human judgment. Do not turn uncertainty into an interview questionnaire.

## Core behavior

```mermaid
flowchart LR
    I[Investigate] --> R[Resolve what evidence can resolve]
    R --> C[Identify real choices]
    C --> M[Recommend]
    M --> Q{Human decision necessary?}
    Q -->|No| N[Continue with bounded next step]
    Q -->|Yes| A[Ask one high-value question]
    A --> V[Converge decision]
    V --> N
```

## Method

### 1. Investigate before questioning

Use the available project, code, docs, tests, references, and environment to answer factual questions yourself.

Do not ask questions like:

- which file contains the current implementation;
- what the existing API returns;
- which thread creates a resource;
- whether a guard already exists;

when these can be inspected directly.

### 2. Separate facts, unknowns, and decisions

For each unresolved point, determine whether it is:

- an investigable fact;
- an external fact requiring a source;
- a temporary assumption;
- an engineering tradeoff;
- a business/product/policy choice;
- a high-impact boundary decision.

Only the last categories normally belong to the user.

### 3. Reduce the decision space

Before asking, establish relevant constraints and eliminate options that are inconsistent, unsupported, or unnecessarily costly.

Do not ask “How should this work?” when the evidence already narrows the choice to two meaningful alternatives.

### 4. Recommend before asking

For a real tradeoff, present:

- the decision;
- the important evidence/constraints;
- the plausible options;
- your recommendation;
- the consequence of choosing differently.

Use a small number of high-value questions per turn. Prefer one decisive question over a list of ten speculative questions.

### 5. Match human involvement to consequence

Low-risk, reversible choices can usually use a reasonable default.

Engineering tradeoffs that materially affect behavior or future constraints should be confirmed.

Irreversible, security-sensitive, compatibility-breaking, data-destructive, production-risk, or hardware-risk decisions must be explicit before execution.

### 6. Converge into stable task state

When a decision becomes stable, record it in the active task artifact if it affects implementation or verification.

Do not preserve the entire conversation. Preserve the decision and the relevant constraint/reason.

## Stop condition

Stop grilling when enough information exists to take the next bounded engineering step safely.

The objective is not complete certainty. It is enough resolved uncertainty to avoid building the wrong thing.

## Failure modes

Avoid:

- asking the user to investigate facts for you;
- presenting many options without a recommendation;
- asking confirmation after every minor step;
- continuing to ask questions after a safe default is available;
- silently choosing a consequential tradeoff;
- treating user speculation as observed fact.
