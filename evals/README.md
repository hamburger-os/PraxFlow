# PraxFlow Evaluations

PraxFlow is a methodology project. Its quality should be judged by observable agent behavior, not by how persuasive a `SKILL.md` sounds.

This directory defines lightweight evaluations for Core Workflows, Skills, and Protocol changes.

## What to evaluate

Use representative engineering tasks and compare outcomes with the smallest meaningful baseline. A baseline can be:

- the same agent without PraxFlow;
- the previous PraxFlow version;
- a Core-only run versus Core + Domain Pack;
- two competing methodology variants.

Do not claim statistical significance from a handful of runs. Small evals are diagnostic evidence, not scientific proof.

## Core dimensions

### Task outcome

- Was the requested engineering goal achieved?
- Did the final result satisfy stated acceptance criteria?

### Evidence discipline

- Were consequential facts grounded in observable or sourced evidence?
- Were assumptions visible?
- Were authoritative conflicts surfaced rather than silently resolved?

### Question quality

- Did the agent investigate answerable questions before asking the user?
- Were human questions concentrated on consequential choices?

### Scope discipline

- Did the change remain causally related to the task?
- Was unrelated refactoring or cleanup introduced?

### Diagnosis quality

For failure tasks:

- Were expected and observed behavior separated?
- Were plausible alternatives considered when the cause was unclear?
- Did experiments discriminate between hypotheses?
- Did the repair address a supported cause rather than only suppress a symptom?

### Review quality

- Are findings actionable and evidence-backed?
- Were important findings challenged against contrary evidence?
- How much low-value noise was produced?

### Verification quality

- Were completion claims backed by checks relevant to the changed behavior?
- Was stronger environment evidence used when risk justified it and capability existed?
- Were unperformed checks honestly reported as unperformed?

### Efficiency

Track when useful:

- unnecessary questions;
- irrelevant files read;
- unrelated files changed;
- repeated failed edit loops;
- verification cost;
- number of human decision points.

Efficiency is secondary to correctness, but avoid methodology that achieves reliability only through unbounded context or ritual.

## Eval record

Start from [`scenario-template.md`](scenario-template.md). Keep raw observations distinct from interpretation.

A useful result states:

```text
Observed behavior
→ evidence
→ interpretation
→ methodology change (if justified)
```

Do not turn one anecdote directly into a Core rule. Look for the underlying failure mode and test whether the proposed rule improves it without creating larger regressions.

## Initial v0.1 suite

The first useful suite should include at least:

| Scenario | Primary Workflow | Stress point |
| --- | --- | --- |
| Add a bounded feature to an existing project | `develop-feature` | investigation, decisions, scope, verification |
| Diagnose a non-obvious regression | `fix-bug` | causal reasoning and discriminating evidence |
| Explain an unfamiliar repository subsystem | `understand-project` | goal-directed exploration and stop conditions |
| Review a realistic patch with planted + non-issues | `review-change` | precision, falsification, noise control |
| Embedded driver behavior constrained by hardware references | Core + `praxflow-embedded` | authority, domain review, target evidence |

Keep scenarios reproducible and small enough to rerun as methodology changes.
