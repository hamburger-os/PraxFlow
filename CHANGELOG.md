# Changelog

All notable changes to PraxFlow will be documented in this file.

The project is pre-1.0. Until the first tagged release, the changelog tracks the evolving v0.1 baseline rather than promising API stability.

## Unreleased

### Added

- Four Core workflows: `develop-feature`, `fix-bug`, `understand-project`, and `review-change`.
- Five Cognitive Skills: `survey`, `trace`, `grill`, `diagnose`, and provisional `plan-change`.
- Five Core protocols covering evidence, decisions, change scope, verification, and durable knowledge.
- `praxflow-embedded` as the first reference domain pack.
- Cross-client installer support for Codex, Claude Code, and TRAE discovery paths.
- Package validator and GitHub Actions validation / installer smoke test.
- English and Simplified Chinese project READMEs.
- Canonical PraxFlow banner and brand guidance.
- Mermaid diagrams for the Core model, workflow selection, Workflow feedback loops, Decision Gates, verification ladders, and embedded evidence/verification relationships.
- `evals/` methodology evaluation framework and scenario template.
- `case-studies/` with an explicitly qualitative MCP2518FD / RT-Thread retrospective.
- Release evidence checklist in `docs/releasing.md`.
- Recommended GitHub repository metadata and protection settings in `docs/repository-settings.md`.
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, Pull Request template, and structured Issue Forms.
- `.editorconfig` and `.gitignore` repository hygiene files.
- CI coverage for the Python 3.10 runtime floor, pinned Agent Skills reference validation, cross-target installer smoke tests, and Protocol/package synchronization.
- A stable `Validate PraxFlow` aggregate CI gate suitable for branch protection.

### Changed

- Refined the project model around four first-class concepts: Workflow, Skill, Protocol, and Capability.
- Treat Agent Skills as the distribution format rather than inventing a PraxFlow-specific Skill specification.
- Removed early candidate abstractions such as generic `implement`, `verify`, `write-spec`, `sync-docs`, and `evidence-search` Core Skills.
- Reworked README information architecture around quick start, visual model, real evidence, contribution, and security entry points.
- Separated qualitative case-study evidence from controlled eval claims to avoid retrospective metric invention.
- Clarified that repository-level Protocol documents are canonical maintainer references while portable packages embed their required operational guidance.
- Reduced README hero repetition and corrected the banner feedback-loop/pill overlap.
- Hardened forced installation by refusing canonical source directories and staging replacement copies before removing an existing installation.
- Documented Python 3.10+ as the supported tooling runtime.
- Clarified that OpenAI plugin packaging is a client-specific reusable distribution layer, while canonical PraxFlow packages remain portable Agent Skills sources.

### Design notes

- `plan-change` remains provisional and may be removed if real-world evaluation shows that it does not add enough value beyond ordinary agent planning.
- A workflow DSL, runtime, registry, marketplace, and general-purpose domain expansion are deliberately out of scope for the current baseline.
- The first tagged release should remain a pre-release until representative real engineering evaluations are recorded.
