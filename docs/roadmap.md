# PraxFlow Roadmap

PraxFlow should grow from tested workflows, not from speculative framework design.

## v0.1 — Methodology baseline

Goal: prove that a small set of cognitive Skills and cross-cutting Protocols materially improves software-engineering agent behavior across multiple clients.

Deliverables:

- four Core Workflows:
  - `develop-feature`
  - `fix-bug`
  - `understand-project`
  - `review-change`
- five Core cognitive Skills:
  - `survey`
  - `trace`
  - `grill`
  - `diagnose`
  - `plan-change`
- five Core Protocols:
  - evidence
  - decisions
  - change scope
  - verification
  - knowledge
- embedded Domain Pack as the first reference implementation
- portable installation for Agent Skills-compatible clients
- structural validation of all packages

Success criteria are behavioral, not file-count based:

- agents ask fewer avoidable questions because they investigate first;
- important factual claims expose provenance or uncertainty;
- debugging tests competing hypotheses rather than patching the first suspicious location;
- change plans expose scope expansion before editing;
- reviews contain fewer speculative/noise findings and actively try to falsify important findings;
- completion claims are supported by relevant external checks;
- embedded workflows consistently consult appropriate authoritative references and real target evidence when available.

## v0.2 — Real-project evaluation

Do not add a Workflow DSL yet.

Run the v0.1 packages against representative tasks in at least:

1. a conventional application/backend repository;
2. an embedded/RTOS repository;
3. a legacy or poorly documented repository.

Capture failure cases such as:

- Skill trigger overlap;
- unnecessary activation;
- Workflow instructions ignored or reordered in harmful ways;
- excessive questioning;
- evidence claims without traceable support;
- over-broad code changes;
- weak verification despite stronger capabilities being available;
- domain pack rules failing to affect the active Workflow.

Use these failures to revise packages before introducing new abstractions.

## v0.3 — Evals and conformance

Add repeatable evaluations for:

- trigger precision;
- question quality;
- assumption visibility;
- evidence provenance;
- diagnosis information gain;
- review precision/recall on curated changes;
- change-scope discipline;
- verification selection.

Where possible, compare:

```text
baseline agent
vs
agent + individual Skill
vs
agent + full Workflow
vs
agent + Workflow + Domain Pack
```

The goal is to establish which parts of PraxFlow actually cause quality improvements.

## v0.4 — Additional domain pack

Only after embedded has validated the pack mechanism, add a second materially different domain. Backend/distributed systems is a strong candidate because it introduces transaction, migration, idempotency, authorization, observability, and distributed-failure concerns.

A second pack should test whether the Domain Pack abstraction is genuinely reusable rather than embedded-specific.

## Workflow manifest decision gate

A machine-readable Workflow manifest is intentionally deferred.

Consider a manifest only when real Workflows demonstrate repeated needs that natural-language Skill Packages cannot reliably express, such as:

- explicit branches;
- resumable state;
- durable checkpoints;
- client-independent human approval gates;
- deterministic dependency resolution;
- eval instrumentation;
- static workflow validation.

If introduced, the manifest must be extracted from existing workflows rather than designed in isolation.

## Runtime decision gate

Do not build a PraxFlow runtime unless portable Agent Skills orchestration proves insufficient for important use cases.

A runtime is justified only if it solves observed problems that client agents cannot reasonably solve themselves.

## Long-term direction

PraxFlow may eventually extend beyond software engineering into research, product development, technical writing, and other evidence-sensitive knowledge work.

That is a direction, not a v0.1 claim.

The core methodology should earn generality through successful transfer, not through broad wording alone.
