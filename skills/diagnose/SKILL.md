---
name: diagnose
description: Diagnose technical failures by establishing expected versus observed behavior, characterizing the failure, generating competing causal hypotheses, designing discriminating experiments, updating hypotheses from evidence, and stopping only when a sufficiently supported cause or bounded next test is established. Use for bugs, CI failures, runtime anomalies, performance regressions, deployment failures, or device/system faults.
license: MIT
metadata:
  praxflow-type: "skill"
  praxflow-version: "0.1"
---

# Diagnose

Do not patch the first suspicious location. Improve the causal model until the next action is supported by evidence.

## Method

### 1. Establish expected versus observed behavior

First determine what should happen and what actually happened.

Expected behavior may come from:

- an accepted requirement/spec;
- tests;
- public/API contracts;
- standards or domain references;
- previously verified behavior;
- an explicit user decision.

If expected behavior itself is unclear and consequential, resolve that before declaring a bug.

### 2. Characterize the failure

Find conditions that increase information value:

- when it happens and when it does not;
- deterministic versus intermittent;
- input/state/timing/environment dependence;
- first known bad version or change when available;
- impact radius;
- correlated logs, metrics, traces, core dumps, or device observations.

A precise failure signature is often more valuable than reading more code.

### 3. Reproduce when feasible; capture when not

Prefer a controlled reproduction, but do not require reproduction as dogma.

If reproduction is impractical, obtain the strongest available failure record such as:

- logs/trace;
- core dump;
- metrics;
- production observation;
- captured input;
- hardware/device output;
- user-reported conditions with explicit uncertainty.

### 4. Localize before theorizing broadly

Use targeted project understanding to narrow:

```text
system -> subsystem -> path -> state/lifecycle boundary -> condition
```

Use `survey` or `trace` when available and useful.

### 5. Generate competing hypotheses

When the cause is not established, keep more than one plausible explanation alive when evidence permits.

For each candidate, ask:

- what evidence already supports it?
- what evidence contradicts it?
- what observable result would be expected if it were true?

Do not mechanically invent a fixed number of hypotheses. The purpose is to resist premature fixation.

### 6. Design a discriminating experiment

Prefer the cheapest targeted action that distinguishes plausible hypotheses.

Good experiments are:

- high-information;
- reversible or low-risk;
- narrowly tied to the uncertainty;
- observable;
- interpretable under both positive and negative outcomes.

Examples:

- add one targeted state/log probe instead of broad logging;
- run the same path with one state variable controlled;
- compare known-good and failing inputs;
- temporarily disable one mechanism to test causality;
- trace whether a callback/event actually fires before inspecting its internals.

### 7. Update the hypothesis set

After every useful experiment:

- discard contradicted explanations;
- strengthen supported ones without overstating certainty;
- refine overly broad hypotheses;
- identify the next highest-information uncertainty.

Do not keep editing around a hypothesis that evidence has contradicted.

### 8. Establish cause before causal repair

Treat a cause as sufficiently established when it:

- explains the important observed symptoms;
- is consistent with available evidence;
- predicts relevant conditions/boundaries;
- and, when feasible, an intervention affecting the proposed mechanism changes the failure behavior.

If a full root cause cannot be established, stop with a bounded next experiment rather than fabricating certainty.

## Containment

If continued operation can cause consequential damage, data loss, security exposure, physical risk, or expanding production impact, prioritize containment before deep diagnosis.

Containment is not the final fix. Preserve enough evidence for later diagnosis when possible.

## Output

For active debugging, keep a compact working model:

```markdown
## Expected vs observed
...

## Failure signature
...

## Hypotheses
- H1 — supported/contradicted/untested: ...
- H2 — ...

## Best next experiment
...

## Evidence update
...

## Current cause / remaining uncertainty
...
```

Do not expose unnecessary internal narration. Show the evidence and reasoning needed for the engineer to understand or act on the diagnosis.

## Stop condition

Stop when either:

1. a sufficiently supported cause exists for a bounded causal fix; or
2. the next discriminating experiment is clear but cannot be executed with available capabilities.
