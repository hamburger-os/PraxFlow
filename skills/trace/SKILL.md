---
name: trace
description: Reconstruct how a behavior actually flows through a codebase or technical system across calls, events, data transformations, state transitions, async boundaries, and resource lifecycles. Use when a bug, feature, review, or architecture question depends on the exact path rather than broad project structure.
license: MIT
metadata:
  praxflow-type: "skill"
  praxflow-version: "0.1"
---

# Trace

Trace one behavior end to end. Optimize for a trustworthy path, not maximum coverage.

## Choose the trace question

Name the specific thing being traced, for example:

- a request from entry to response;
- a UI action to backend effect;
- data from input/IRQ/message to consumer;
- a state transition and who causes it;
- creation → ownership → use → release of a resource;
- an error from origin to user-visible handling.

If the question is still “where should I look?”, use `survey` first when available.

## Method

### 1. Find an observable entry and outcome

Anchor the trace at concrete points whenever possible.

Examples:

```text
HTTP request -> response
button click -> device command
IRQ -> application event
login completion -> first authenticated request
allocation -> final release
```

### 2. Follow evidence, not naming conventions

At each hop, record the relevant evidence:

- caller/callee;
- event publisher/subscriber;
- queue or IPC boundary;
- state mutation;
- data transformation;
- ownership transfer;
- scheduling/thread/interrupt boundary;
- error translation.

Do not infer a hop merely because two modules have suggestive names.

### 3. Preserve important context changes

Highlight boundaries where reasoning assumptions can break:

- process/thread/ISR changes;
- sync → async transitions;
- serialization/deserialization;
- mutable shared state;
- retries/timeouts;
- caching;
- ownership or lifetime changes;
- external service/device calls.

### 4. Track state and data separately when necessary

A call chain alone can miss the cause of behavior.

For a complex path, maintain parallel questions:

```text
Control: who invokes whom?
Data: what value is passed/transformed?
State: what persistent state changes?
Context: on which thread/process/device does it run?
Ownership: who may use/release the resource?
```

### 5. Expand only when the path branches materially

Follow branches that can change the target behavior. Do not recursively explore unrelated callers or consumers.

When multiple possible paths exist, state the condition that selects each path.

### 6. Validate the reconstructed path

Before presenting a trace as established:

- search for alternate entry points;
- check guards/early returns;
- verify async callbacks or subscriptions are actually registered;
- inspect state conditions that can bypass a hop;
- note unresolved dynamic behavior that static inspection cannot establish.

## Output

Prefer an explicit path plus supporting notes:

```text
Entry
  -> Component A: reason/evidence
  -> async boundary
  -> Component B: state change
  -> Component C: result
```

Then add only the useful details:

- critical state transitions;
- data transformations;
- execution-context changes;
- ownership/lifecycle observations;
- unresolved branches or unknowns.

## Stop condition

Stop when the trace explains the behavior needed by the current task with no unresolved branch likely to change the next decision.

Do not turn a focused trace into a full architecture survey.
