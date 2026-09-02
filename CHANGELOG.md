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

### Changed

- Refined the project model around four first-class concepts: Workflow, Skill, Protocol, and Capability.
- Treat Agent Skills as the distribution format rather than inventing a PraxFlow-specific Skill specification.
- Removed early candidate abstractions such as generic `implement`, `verify`, `write-spec`, `sync-docs`, and `evidence-search` Core Skills.

### Design notes

- `plan-change` remains provisional and may be removed if real-world evaluation shows that it does not add enough value beyond ordinary agent planning.
- A workflow DSL, runtime, registry, marketplace, and general-purpose domain expansion are deliberately out of scope for the current baseline.
