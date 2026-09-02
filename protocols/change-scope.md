# Change Scope Protocol

The Change Scope Protocol keeps implementation aligned with the actual cause and goal of the task.

## Core rule: minimal causal change

Prefer the smallest change that addresses the established goal or cause without unnecessary collateral work.

This is deliberately **not** the same as “smallest diff.” A one-line patch that hides a symptom can be worse than a slightly larger change that fixes the underlying lifecycle, ownership, or contract issue.

## Before editing

For non-trivial changes, establish a change boundary that answers the relevant subset of:

- which components/files are expected to change;
- which public interfaces or data formats may change;
- which state transitions or data flows may change;
- which resources, dependencies, or permissions may change;
- what compatibility requirements exist;
- what must explicitly remain untouched;
- how the change will be verified.

The boundary should be as detailed as needed to catch a wrong direction before expensive editing starts.

## During editing

Treat unexplained scope expansion as a signal to stop and reassess.

Examples:

- a bug fix suddenly requires a public API redesign;
- a feature implementation starts renaming unrelated modules;
- a local behavior change starts reorganizing directory structure;
- new dependencies appear without being part of the accepted design.

Possible explanations include:

- the original plan was incomplete;
- the assumed root cause was wrong;
- a hidden architectural constraint was discovered;
- the agent is performing opportunistic cleanup.

Only the first three may justify expanding scope, and consequential expansion may require a Decision Gate.

## No opportunistic refactoring by default

Do not combine unrelated cleanup with a task merely because the agent noticed it.

If unrelated technical debt materially blocks the task, surface it and explain why it is causally required. Otherwise leave it for separate work.

## Preserve contracts intentionally

Do not assume a contract only means a formal public API. Relevant contracts may include:

- data layout and persistence format;
- error semantics;
- ordering guarantees;
- timing behavior;
- idempotency;
- resource ownership;
- thread/interrupt context;
- CLI behavior;
- configuration keys;
- protocol compatibility.

If a contract must change, make that change explicit in the active design/decision artifact.

## Bug-fix rule

For a bug fix, the target is a **causal repair**:

1. establish a supported cause or sufficiently strong causal model;
2. change the mechanism responsible for the failure;
3. avoid masking the observable symptom without addressing the mechanism;
4. verify the original failing condition and relevant regression surface.

## Review rule

Review should compare declared intent with actual change scope. Unexplained expansion is itself a review concern even when individual edits appear locally correct.
