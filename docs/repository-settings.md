# Recommended GitHub Repository Settings

This document records the repository settings PraxFlow should use for a polished public open-source project. These settings live in GitHub metadata and are intentionally kept separate from the methodology itself.

## About

### Description

Use:

> Composable, evidence-first engineering workflows for reliable AI agents — packaged as portable Agent Skills.

Keep the Description stable and vendor-neutral. Client compatibility belongs in Topics and adapters rather than the one-line positioning statement.

### Topics

Recommended Topics:

```text
agent-skills
ai-agents
coding-agents
llm-agents
agentic-workflows
ai-engineering
software-engineering
developer-tools
human-in-the-loop
codex
claude-code
trae
embedded-systems
```

Avoid generic discovery bait such as `awesome`, `automation`, or `prompt-engineering` unless the project's actual scope changes.

### Website

Leave the website field empty until PraxFlow has a real documentation site or stable project domain. Do not point it to a placeholder landing page.

## Social preview

Use a **1280 × 640** PNG derived from `assets/praxflow-banner.svg`.

The preview should contain:

- PraxFlow;
- `Engineering workflows for reliable AI agents`;
- `Composable · Evidence-first · Human-guided · Reality-verified`;
- the Goal → Workflow → Skills → Evidence feedback motif.

Do not add vendor logos.

GitHub path:

```text
Settings → General → Social preview → Edit
```

## General pull request settings

Recommended:

- **Allow squash merging:** on;
- **Allow merge commits:** off once contributions begin;
- **Allow rebase merging:** optional;
- **Always suggest updating pull request branches:** on when available;
- **Automatically delete head branches:** on.

Squash merging keeps methodology changes reviewable as one conceptual change while preserving detailed discussion in the pull request.

## Main branch protection

Once public contributions begin, protect `main` using a Ruleset or branch protection rule.

Recommended baseline:

- require a pull request before merging;
- require the `Validate PraxFlow` status check;
- require branches to be up to date when practical;
- block force pushes;
- block branch deletion;
- require code-owner review only if CODEOWNERS becomes meaningful with multiple maintainers.

Do not enable approval rules that create ceremony without an actual second maintainer.

## Security

Enable GitHub **Private vulnerability reporting** when available for the repository.

`SECURITY.md` intentionally asks reporters not to disclose exploitable vulnerabilities publicly. Once private reporting is enabled, keep the GitHub security UI as the preferred confidential channel.

## Discussions

Do not enable Discussions merely for completeness. Enable it when there is enough community traffic that usage questions, design discussion, and examples are creating noise in Issues.

Until then:

- use Issues for reproducible defects and methodology proposals;
- use Pull Requests for concrete changes;
- keep speculative discussion out of the issue tracker when it has no actionable engineering question.

## Releases

Do not publish a stable-looking `v0.1.0` only because the repository is organized.

Follow [`releasing.md`](releasing.md). The first public release should normally be a pre-release such as `v0.1.0-alpha.1` after representative real-world evaluations are recorded.
