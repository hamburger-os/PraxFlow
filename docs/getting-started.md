# Getting Started with PraxFlow

[English](getting-started.md) · [简体中文](getting-started.zh-CN.md)

PraxFlow is a set of portable Agent Skills that adds engineering discipline to capable coding agents. It does not replace your coding agent, tools, MCP servers, build system, or project documentation.

This guide explains the basic reasoning behind PraxFlow, how to choose packages, how to install them, and what to expect when using them.

## The basic idea

A coding agent often already knows how to edit files, run commands, search a repository, and produce code. Reliability problems usually happen one level above those actions:

- acting before understanding enough of the system;
- treating a plausible explanation as an established fact;
- asking the user questions that repository investigation could answer;
- changing more code than the established cause requires;
- claiming success after weak or irrelevant verification;
- losing important project knowledge between tasks.

PraxFlow addresses those problems with four concepts:

| Concept | Role |
| --- | --- |
| **Workflow** | An end-to-end reasoning loop for a class of engineering goals. |
| **Skill** | A reusable cognitive method that can be used across Workflows. |
| **Protocol** | Cross-cutting rules for evidence, decisions, change scope, verification, and knowledge. |
| **Capability** | A concrete action supplied by the project or environment, such as build, test, deploy, flash, browser, serial, or database access. |

The important separation is:

> PraxFlow decides **when and why** an engineering action is needed. Your project and agent environment decide **how** to perform it.

For the full model, see [`concepts.md`](concepts.md).

## Choose a Workflow first

For most non-trivial tasks, start from the Workflow that matches the user's goal.

| Goal | Workflow | Use it when… |
| --- | --- | --- |
| Add or materially change behavior | `develop-feature` | The task needs understanding, design choices, bounded implementation, review, and verification. |
| Fix incorrect behavior | `fix-bug` | You need to distinguish expected vs observed behavior, establish a cause, repair it, and verify regression behavior. |
| Understand an unfamiliar system | `understand-project` | The goal is explanation or a working model rather than a code change. |
| Review a proposed change | `review-change` | You want high-signal findings grounded in intent, actual scope, contracts, and evidence. |

Workflows are intentionally different cognitive loops. `fix-bug` is not just `develop-feature` with a different title, and `review-change` should not turn into an implementation task by default.

## Add reusable cognitive Skills

Workflows can use the following reusable Skills when they are installed and relevant:

| Skill | What it changes in agent behavior |
| --- | --- |
| `survey` | Helps the agent decide where to look first and how far to explore. |
| `trace` | Reconstructs a behavior across calls, data, state, events, async boundaries, and lifecycles. |
| `grill` | Investigates answerable facts before asking the user, then escalates only consequential choices. |
| `diagnose` | Compares causal hypotheses and chooses high-information checks instead of committing to the first plausible explanation. |
| `plan-change` | Bounds the smallest causal change surface before expensive editing starts. |

`plan-change` is provisional in v0.1. PraxFlow will remove it if real evaluation shows that it does not improve behavior beyond ordinary agent planning.

### Practical package combinations

A useful starting point is to install the Workflow you need plus the reusable Skills that support it.

For feature work:

```text
develop-feature
survey
trace
grill
plan-change
diagnose
```

For debugging:

```text
fix-bug
survey
trace
diagnose
plan-change
```

For project understanding:

```text
understand-project
survey
trace
```

For review:

```text
review-change
survey
trace
diagnose
```

These are recommendations, not hard dependency manifests. PraxFlow v0.1 deliberately keeps package composition simple; Workflows use supporting Skills **when available**.

## Install PraxFlow

### Recommended: Agent Skills ecosystem installer

For most users:

```bash
npx skills@latest add hamburger-os/PraxFlow
```

Choose the packages and target coding agents you want during the interactive flow.

If you already know the packages and target:

```bash
npx skills@latest add hamburger-os/PraxFlow \
  --skill develop-feature \
  --skill survey \
  --skill trace \
  --skill grill \
  --skill plan-change \
  --agent codex \
  --yes
```

GitHub CLI also provides Agent Skill installation:

```bash
gh skill install hamburger-os/PraxFlow
```

Exact target paths and client behavior can change over time. See [`../adapters/README.md`](../adapters/README.md) for the compatibility notes PraxFlow currently maintains.

### Advanced: built-in deterministic installer

Clone the repository when you need deterministic package selection, local source development, custom output directories, or explicit Domain Pack installation:

```bash
git clone https://github.com/hamburger-os/PraxFlow.git
cd PraxFlow
```

The built-in tooling requires Python 3.10 or newer.

Install the Core Workflows and Core Skills into a Codex-compatible project:

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/project
```

Add the embedded reference Domain Pack:

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/project \
  --pack praxflow-embedded
```

## How to use PraxFlow after installation

Agent Skills clients normally expose installed Skills to the model through their name and description. A relevant package can then be activated by the agent when the task matches it. Some clients also support explicit user selection or invocation.

You do not need to learn a PraxFlow-specific command language.

A normal feature request can remain normal:

> Add reconnect support to the WebSocket client. Preserve the existing public API and verify the reconnect behavior with the project's tests.

With `develop-feature` and supporting Skills available, the expected difference is **how the agent approaches the task**: it should first establish relevant behavior and constraints, surface consequential choices, bound the change, implement, review, and use appropriate external verification.

For debugging, you can similarly state the problem rather than prescribing the diagnosis:

> After a network interruption, the service sometimes reports connected but stops receiving events. Find the cause, fix it, and verify the regression.

With `fix-bug` and `diagnose`, the agent should distinguish expected and observed behavior, keep multiple causal explanations alive when evidence is incomplete, and avoid treating the first suspicious code location as the root cause.

If your client supports explicit Skill selection, you can select the relevant PraxFlow package when you specifically want that method applied. The exact UI or syntax belongs to the client, not PraxFlow.

## What good PraxFlow behavior should look like

PraxFlow is working when the behavior becomes more disciplined without turning every task into ceremony.

You should expect the agent to:

- investigate project facts before asking avoidable questions;
- distinguish observation, source, inference, assumption, unknown, and conflict when the distinction matters;
- ask for human judgment at consequential choices rather than routine facts;
- build only as much project understanding as the current goal requires;
- prefer the smallest established **causal** change instead of mechanically minimizing diff size;
- challenge important debugging hypotheses and review findings before presenting them as established;
- match verification strength to the risk and claim being made;
- persist only stable reusable project knowledge, not a transcript of temporary reasoning.

You should **not** expect every task to produce a specification file, request approval, run the strongest possible test suite, or activate every available Skill. Proportionality is part of the methodology.

## Domain Packs

A Domain Pack adds domain-specific evidence, review, and verification policy without copying the Core Workflows.

The first reference pack is:

```text
praxflow-embedded
```

It adds embedded-specific guidance for areas such as authoritative hardware references, ISR/thread boundaries, DMA/cache coherency, alignment, ABI, memory lifetime, timing, error paths, and target-level verification.

Use a Domain Pack when the domain creates recurring reasoning risks that are not sufficiently covered by general software-engineering rules.

Do not use a Domain Pack to store one project's build commands, credentials, device addresses, or architecture facts. Those belong to the consuming project.

## Agent Skills format: what is standard and what is PraxFlow-specific

An Agent Skill is a directory containing at minimum:

```text
skill-name/
└── SKILL.md
```

The open specification also defines conventional optional resource directories such as `scripts/`, `references/`, and `assets/`, and permits additional files.

PraxFlow chooses this canonical **repository** layout:

```text
skills/<package-name>/SKILL.md
```

That flat `skills/` catalog is a PraxFlow distribution convention. The Agent Skills specification itself does not require all repositories to use a top-level `skills/` directory, and it does not mandate one universal client installation location.

For the same reason, PraxFlow does not put a human README into every package. Human explanations stay in `docs/`; package-local references exist for agents to load when execution requires them.

## Validate a local PraxFlow checkout

If you are contributing to PraxFlow itself:

```bash
python3 scripts/validate.py
```

Package-format changes should also pass the Agent Skills reference validator used by CI.

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) for contribution rules.

## Next steps

- Read [`concepts.md`](concepts.md) for the full conceptual model.
- Read [`../adapters/README.md`](../adapters/README.md) for client installation paths and compatibility notes.
- Read [`../case-studies/`](../case-studies/) for concrete engineering evidence.
- Read [`roadmap.md`](roadmap.md) for project status and planned evaluation work.
