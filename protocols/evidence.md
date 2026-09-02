# Evidence Protocol

The Evidence Protocol governs how PraxFlow treats claims. It is a reasoning discipline, not a retrieval engine.

## Objective

Important claims should expose enough provenance and uncertainty that an engineer can distinguish:

- what was directly observed,
- what a source states,
- what the agent inferred,
- what is currently assumed,
- what remains unknown,
- where relevant sources conflict.

The protocol does **not** require citation ceremony for every trivial statement. Apply it in proportion to the consequence of being wrong.

## Claim model

PraxFlow does not freeze a machine schema in v0.1, but agents should reason along three independent dimensions.

### Kind

What role does the claim play?

Typical kinds:

- **Observation** — an observed behavior or state.
- **Requirement** — behavior the system is expected to provide.
- **Constraint** — a boundary the work must respect.
- **Hypothesis** — a candidate explanation not yet established.
- **Decision** — an intentional choice among alternatives.
- **Conclusion** — a derived judgment such as a root cause or review finding.

Do not force every statement into these labels in user-visible output. The purpose is to prevent semantic mixing during reasoning.

### Basis

How was the claim obtained?

- **Observed** — read or measured directly from the current environment: code, command output, logs, test results, runtime state, device output, database result, etc.
- **Sourced** — stated by a traceable source such as a specification, project doc, issue, standard, vendor document, or official API documentation.
- **Inferred** — derived from one or more observations/sources through reasoning.
- **Assumed** — temporarily adopted without sufficient evidence so work can proceed.

Inference is not a source. An agent must not present “the source says X” when X is actually its own derivation from the source.

### Status

How should the claim currently be treated?

- **Supported** — adequate evidence exists for the current purpose.
- **Unverified** — plausible but not sufficiently tested or sourced.
- **Contradicted** — available evidence argues against it.
- **Conflicted** — relevant authoritative evidence disagrees.
- **Superseded** — once-valid information has been replaced by a newer decision/source/state.

`Unknown` is best treated as absence of a supported claim rather than something the agent must disguise with a guess.

## Rules

### 1. Keep assumptions visible

An assumption may be necessary. The failure is silently converting it into a fact.

High-impact assumptions should trigger one of:

- further investigation,
- source lookup,
- a discriminating experiment,
- a Decision Gate,
- an explicit unresolved note.

### 2. Preserve provenance

When a claim affects design, safety, compatibility, debugging, or review severity, retain enough provenance to re-check it.

Useful provenance includes:

- file + symbol/line region,
- document + section/page,
- command/test + result,
- runtime observation + conditions,
- user/owner decision + context.

### 3. Do not silently resolve authoritative conflicts

When relevant authoritative sources disagree:

1. identify the conflicting sources;
2. check version, scope, applicability, and authority;
3. resolve only when the evidence itself supports a resolution;
4. otherwise surface the conflict and use the Decisions Protocol.

A project requirement cannot redefine an external physical or protocol fact. A reference implementation cannot override a formal specification merely because it is executable code.

### 4. Source authority is domain-dependent

Core PraxFlow does not define a universal ranking such as “official docs always beat code.”

Authority depends on the question:

- What *should* the system do?
- What does the current implementation *actually* do?
- What does an external standard require?
- Which version or hardware revision applies?

Domain Packs may define an Evidence Policy for their domain.

### 5. Evidence collection is targeted

Do not gather evidence without a question. Prefer information that changes a decision, distinguishes hypotheses, bounds risk, or verifies completion.

### 6. Model memory is a lead, not authority

Model knowledge can suggest where to investigate, but consequential external facts should be checked against current, applicable evidence when practical.

## Output behavior

Use explicit labels such as `Observed`, `Assumption`, `Unknown`, or `Conflict` when the distinction materially helps the user. Do not clutter ordinary answers with labels that add no decision value.

The minimum standard is epistemic honesty: never make an inference look sourced, an assumption look observed, or a conflict look resolved.
