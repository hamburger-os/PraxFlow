# Knowledge Protocol

The Knowledge Protocol separates ephemeral working context from durable project knowledge.

## Core rule

Persist stable, reusable information outside transient model context when it is likely to matter to future work.

Do not turn every task into a documentation project.

## Ephemeral working context

Keep temporary material in the active task unless it becomes durable knowledge:

- exploratory notes;
- discarded hypotheses;
- intermediate search results;
- transient logs;
- temporary implementation options;
- conversational history;
- one-off command output.

These can be useful while reasoning and still be poor project documentation.

## Durable candidates

Consider persisting:

- stable architecture boundaries;
- component responsibilities that are not obvious from local code;
- durable constraints and invariants;
- consequential engineering decisions;
- compatibility requirements;
- recurring build/test/deploy/debug capabilities;
- important failure modes that future engineers must account for;
- external reference applicability (version, hardware revision, standard profile) when it affects future work.

## Promotion test

Before writing long-term documentation, ask:

1. Is this information expected to remain true beyond the current task?
2. Is it difficult or expensive to rediscover correctly?
3. Will future work benefit from knowing it early?
4. Is there an appropriate canonical location for it?

If the answer is mostly no, leave it in the task context.

## Avoid transcript persistence

A durable artifact should capture the stable conclusion, not the entire path used to reach it.

Prefer:

```text
Decision: preserve the existing wire format for backward compatibility.
Reason: deployed devices on version X cannot negotiate a new format.
```

Over a long chronological record of every alternative discussed.

## Documentation is evidence, not automatic truth

Existing project documentation can be stale. Treat docs as sourced evidence whose authority depends on ownership, recency, scope, and consistency with observed behavior.

When code and documentation disagree:

- do not silently overwrite one with the other;
- determine whether the disagreement represents stale docs, a regression, an incomplete implementation, or an unapproved behavior change;
- update the canonical artifact only after the intended state is established.

## Context continuity

Do not rely on one ever-growing conversation as the sole carrier of important task state.

When a task spans sessions, models, agents, or long periods, preserve stable state in artifacts that the next agent can re-read:

- accepted design;
- unresolved decisions;
- verified facts;
- current failure model;
- next bounded step.

The exact handoff mechanism is client-specific; the principle is not.
