# PraxFlow

**Engineering workflows for reliable AI agents.**

PraxFlow is an opinionated engineering methodology for AI agents, distributed as portable [Agent Skills](https://agentskills.io/). It is not a new agent runtime, a new Skill format, or a generic prompt collection.

The project focuses on a harder question:

> How should an AI agent investigate, reason, decide, change, review, and verify work so that capability becomes reliable engineering practice?

PraxFlow v0.1 deliberately starts with software engineering. Embedded development is the first reference domain because it stress-tests evidence quality, hard constraints, concurrency, build/deploy loops, and verification against the physical world.

## Core model

PraxFlow has four conceptual building blocks:

- **Workflow** — an end-to-end cognitive loop for a class of goals.
- **Skill** — a reusable cognitive method used by multiple workflows.
- **Protocol** — cross-cutting rules for evidence, decisions, change scope, verification, and durable knowledge.
- **Capability** — a concrete action provided by the current project or environment, such as build, test, deploy, flash, browser, serial, or database access.

Agent Skills are the **distribution format**. A PraxFlow Workflow or Skill is packaged as a standards-compatible `SKILL.md` directory. The conceptual type is recorded in metadata.

```text
User Goal
   |
   v
Workflow
   |
   +---- Skill
   +---- Skill
   +---- Skill
   |
Protocols
   |
   v
Project Capabilities
   |
   v
External Evidence
   |
   +---- feedback ----> Workflow
```

## v0.1 scope

### Workflows

| Package | Purpose |
| --- | --- |
| `develop-feature` | Turn a feature goal into a bounded design, implementation, review, and proportionate verification loop. |
| `fix-bug` | Move from symptom to expected behavior, characterization, competing hypotheses, causal fix, and regression verification. |
| `understand-project` | Build only the evidence-backed project model needed for the stated understanding goal. |
| `review-change` | Review a change against intent, contracts, impact, evidence, and domain-specific risks with high-signal findings. |

### Cognitive skills

| Package | Core question |
| --- | --- |
| `survey` | Where should I look first? |
| `trace` | How exactly does this behavior happen? |
| `grill` | What genuinely needs to be decided before work can proceed? |
| `diagnose` | Which causal explanation best fits the evidence, and how can I distinguish alternatives? |
| `plan-change` | What is the smallest causal change boundary that addresses the goal without collateral work? |

### Protocols

- `evidence.md` — distinguish observations, sources, inferences, assumptions, unknowns, and conflicts.
- `decisions.md` — resolve before asking; escalate consequential tradeoffs through decision gates.
- `change-scope.md` — prefer minimal causal change, not merely minimal diff.
- `verification.md` — completion claims require proportionate external verification.
- `knowledge.md` — persist stable reusable knowledge, not transient reasoning history.

### Reference domain pack

`packs/praxflow-embedded/` adds embedded-specific evidence policy, review concerns, and verification strategy without duplicating the Core workflows.

## Design principles

PraxFlow currently uses these working principles:

1. **Spec-driven when consequences justify it.** A design artifact is a working contract, not a ritual or a chat transcript.
2. **Evidence-first.** Model memory is not an authoritative source. Important claims should expose how they are known.
3. **Skill-guided.** Reusable methods belong in Skills; concrete environment actions belong in project capabilities.
4. **Reality-verified.** Do not equate generated output with completion. Use the strongest relevant and economical external verification available.
5. **Resolve before ask.** Investigate code, docs, evidence, and constraints before asking the user questions the agent can answer itself.
6. **Human at consequential decisions.** Human-in-the-loop should concentrate on irreversible, high-impact, policy, compatibility, and engineering tradeoffs—not every small step.
7. **Goal-directed understanding.** Read as broadly and deeply as the current goal requires; do not archify a repository by default.
8. **Challenge your own findings.** Debugging and review should actively seek evidence that can falsify the first plausible explanation.
9. **Extract principles, not prescriptions.** Tool-specific practices are implementation choices unless the underlying problem is truly universal.

## Repository layout

```text
PraxFlow/
├── workflows/                 # End-to-end workflow packages
├── skills/                    # Reusable cognitive skill packages
├── protocols/                 # Cross-cutting methodology
├── packs/                     # Domain packs; embedded is the first reference pack
├── adapters/                  # Installation and client notes
├── examples/                  # Project capability examples
├── scripts/                   # Installer and validator
├── docs/                      # Concepts and roadmap
├── AGENTS.md                  # Maintainer/agent instructions
└── CLAUDE.md                  # Claude Code entrypoint importing AGENTS.md
```

## Install

PraxFlow keeps canonical packages under `workflows/`, `skills/`, and `packs/`. The installer flattens selected packages into the discovery directory expected by the target client.

```bash
# Clone
 git clone https://github.com/hamburger-os/PraxFlow.git
 cd PraxFlow

# Install Core workflows + Core skills for a project
python3 scripts/install.py --target codex --scope project --dest /path/to/project

# Add the embedded domain pack
python3 scripts/install.py --target codex --scope project --dest /path/to/project --pack praxflow-embedded

# Claude Code
python3 scripts/install.py --target claude --scope project --dest /path/to/project --pack praxflow-embedded

# TRAE
python3 scripts/install.py --target trae --scope project --dest /path/to/project --pack praxflow-embedded
```

Current project-level discovery paths:

- **Codex:** `.agents/skills/`
- **TRAE:** `.agents/skills/`
- **Claude Code:** `.claude/skills/`

These paths are client behavior, not part of the PraxFlow methodology. See `adapters/README.md` before changing adapters.

You may also copy individual package directories manually, as long as each installed directory keeps its `SKILL.md` and supporting files together.

## Validate

```bash
python3 scripts/validate.py
```

The local validator checks the parts of the Agent Skills specification PraxFlow relies on: directory/name matching, required YAML frontmatter, allowed skill names, description presence/length, and duplicate package names. For normative validation, also use the Agent Skills reference validator (`skills-ref validate`).

## Project capabilities

PraxFlow does not encode project-specific build, test, deploy, flash, or debug commands in Core Skills. Put those facts in project-owned documentation or project-specific skills. See `examples/embedded-project/PROJECT_CAPABILITIES.md`.

The separation is intentional:

```text
PraxFlow says WHEN and WHY to verify.
The project says HOW to build/test/deploy/observe.
```

## Status

PraxFlow is pre-1.0 and intentionally opinionated. The v0.1 artifacts are hypotheses to be tested against real projects. Concepts may be removed or renamed when implementation shows that they are redundant.

## Compatibility references

- Agent Skills open specification: https://agentskills.io/specification
- Claude Code Skills: https://code.claude.com/docs/en/skills
- OpenAI Skills / Codex: https://learn.chatgpt.com/docs/build-skills
- TRAE changelog (project Skills support, including `.agents/skills`): https://www.trae.ai/changelog

## License

MIT. See `LICENSE`.
