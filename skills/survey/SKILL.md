---
name: survey
description: Rapidly map the parts of an unfamiliar codebase or technical project that matter to the current goal. Use before deeper investigation when you need entry points, boundaries, relevant components, likely dependencies, existing docs/tests, and high-value unknowns without reading the whole repository.
license: MIT
metadata:
  praxflow-type: "skill"
  praxflow-version: "0.1"
---

# Survey

Build a **goal-directed provisional map** of the project. Do not attempt to understand the whole repository unless the user's goal genuinely requires it.

## Method

### 1. State the investigation goal

Translate the user's task into what you need to understand.

Examples:

- “fix first-request 401” → auth/session initialization and first authenticated request path;
- “add reconnect” → connection lifecycle, state machine, retry behavior, ownership;
- “review this migration” → changed schema, readers/writers, compatibility, rollback.

Do not widen the scope merely because more files are available.

### 2. Orient cheaply

Prefer low-cost structural evidence first:

- README and project docs relevant to the goal;
- top-level directories;
- build/package manifests;
- obvious entry points;
- tests near the target behavior;
- configuration and interfaces connected to the goal.

Use search rather than sequentially reading directories.

### 3. Locate likely boundaries

Identify the smallest set of components that plausibly participate in the target behavior.

Look for:

- entry points;
- ownership boundaries;
- module/service/process/thread boundaries;
- external dependencies;
- persistent state;
- public contracts;
- test seams;
- relevant project capabilities.

### 4. Build a provisional map

Separate what is observed from what is inferred.

A useful lightweight map may include:

```text
Relevant areas
Current behavior model
Known constraints
Important unknowns
Recommended next investigation
```

Do not present a provisional inference as established architecture.

### 5. Identify high-value unknowns

Ask: which unknown, if resolved, would most change the next engineering decision?

Prefer unknowns about:

- lifecycle or ownership;
- state transitions;
- data/control flow;
- interfaces and compatibility;
- concurrency/async boundaries;
- error paths;
- verification path.

### 6. Stop or deepen selectively

Stop when the map is sufficient for the current task.

If one behavior needs deeper reconstruction, use `trace` when available instead of widening the whole survey.

## Do not

- summarize every directory;
- read the entire repository by default;
- generate an architecture document just because you inspected the project;
- ask the user where code lives when you can search for it;
- treat directory names or README claims as authoritative when code evidence contradicts them.

## Output

Keep the result compact unless the user explicitly asks for a full architecture assessment.

Prefer:

```markdown
## Relevant areas
...

## Working model
...

## Constraints / evidence
...

## Unknowns
...

## Next investigation
...
```

The working model is allowed to be incomplete. Make important uncertainty visible rather than filling gaps with guesses.
