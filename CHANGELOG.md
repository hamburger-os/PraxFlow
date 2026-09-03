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
- External Agent Skills CLI distribution smoke coverage that verifies PraxFlow's flat `skills/*/SKILL.md` source catalog and a real install result.
- `skills.sh.json` catalog grouping metadata for Workflows, Cognitive Skills, and Domain Packs.
- English and Simplified Chinese project READMEs.
- English and Simplified Chinese user guides covering principles, package selection, installation, practical usage, expected behavior, and format boundaries.
- Simplified Chinese counterpart for the conceptual reference and Roadmap.
- Documentation audience rules: English-first AI-facing package instructions, Chinese-first primary-maintainer operational docs, and English/bilingual community docs.
- Canonical PraxFlow banner and brand guidance.
- Mermaid diagrams for the Core model, workflow selection, Workflow feedback loops, Decision Gates, verification ladders, and embedded evidence/verification relationships.
- `evals/` methodology evaluation framework and scenario template.
- `case-studies/` with an explicitly qualitative MCP2518FD / RT-Thread retrospective.
- Release evidence checklist in `docs/releasing.md`.
- Recommended GitHub repository metadata and protection settings in `docs/repository-settings.md`.
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, Pull Request template, and structured Issue Forms.
- `.editorconfig` and `.gitignore` repository hygiene files.
- CI coverage for the Python 3.10 runtime floor, pinned Agent Skills reference validation, external catalog installation, cross-target built-in installer smoke tests, and Protocol/package synchronization.
- A stable `Validate PraxFlow` aggregate CI gate suitable for branch protection.

### Changed

- Refined the project model around four first-class concepts: Workflow, Skill, Protocol, and Capability.
- Treat Agent Skills as the distribution format rather than inventing a PraxFlow-specific Skill specification.
- Standardized PraxFlow's own canonical source catalog on `skills/<package-name>/SKILL.md`; removed separate `workflows/` and `packs/` package roots.
- Clarified that the flat top-level `skills/` source catalog is a **PraxFlow repository convention**, not a filesystem location mandated by the Agent Skills specification.
- Clarified the three compatibility layers: Agent Skills package-format requirements, PraxFlow repository conventions, and client-specific discovery/install behavior.
- Explicitly documented that `README.md` is not required or special inside an Agent Skill package; human tutorials stay under `docs/`, while package-local `references/` exist for agent runtime use.
- Moved Workflow packages and `praxflow-embedded` into `skills/` while preserving conceptual type through `metadata.praxflow-type`.
- Made ecosystem installation (`npx skills@latest add hamburger-os/PraxFlow`) the default first-run path; the Python installer is now the advanced/deterministic path.
- Removed the need for PraxFlow-specific repository-wide deep-search flags to discover first-class packages through the supported installer path.
- Updated the built-in validator and installer so physical source location is independent from PraxFlow conceptual type.
- Reworked Protocol/package synchronization around the single `skills/` source root.
- Removed early candidate abstractions such as generic `implement`, `verify`, `write-spec`, `sync-docs`, and `evidence-search` Core Skills.
- Reworked README information architecture around quick start, principles, the dedicated user guide, evidence, contribution, and security entry points.
- Separated qualitative case-study evidence from controlled eval claims to avoid retrospective metric invention.
- Clarified that repository-level Protocol documents are canonical maintainer references while portable packages embed their required operational guidance.
- Reduced README hero repetition and corrected the banner feedback-loop/pill overlap.
- Hardened forced installation by refusing canonical source directories and staging replacement copies before removing an existing installation.
- Documented Python 3.10+ as the supported runtime for PraxFlow's built-in tooling rather than a prerequisite for normal ecosystem installation.
- Clarified that native/plugin packaging is a client-specific managed distribution layer, while canonical PraxFlow packages remain portable Agent Skills sources.
- Made maintainer-focused release, repository-settings, and brand guidance Simplified-Chinese-first while keeping commands, identifiers, and public English brand text stable.

### Design notes

- The flat `skills/*/SKILL.md` layout is deliberate **for PraxFlow**: package taxonomy lives in metadata and optional catalog presentation, while the source repository stays easy for common installers to consume.
- The Agent Skills specification defines the internal Skill package format; client implementations and repositories choose where Skill directories live.
- `skills.sh.json` is non-normative presentation metadata; package identity and portability must not depend on it.
- `plan-change` remains provisional and may be removed if real-world evaluation shows that it does not add enough value beyond ordinary agent planning.
- A workflow DSL, runtime, registry, marketplace, and general-purpose domain expansion are deliberately out of scope for the current baseline.
- The first tagged release should remain a pre-release until representative real engineering evaluations are recorded.
