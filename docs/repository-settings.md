# GitHub Repository Settings 建议

本文主要供 PraxFlow 维护者使用，因此默认使用简体中文。它记录为了让 PraxFlow 作为公开 Open Source Project 保持清晰、可信和易维护，GitHub repository 应采用的设置。

这些设置属于 GitHub metadata / repository administration，不属于 PraxFlow 方法论本身。

## About

### Description

建议保持：

> Composable, evidence-first engineering workflows for reliable AI agents — packaged as portable Agent Skills.

Description 应稳定、简短、vendor-neutral。具体 Client compatibility 放在 Topics、README 和 adapters，而不是塞进一句定位描述里。

### Topics

建议 Topics：

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

除非项目真实范围变化，否则不要为了流量加入 `awesome`、`automation`、`prompt-engineering` 这类弱化定位的泛化标签。

### Website

在 PraxFlow 有正式文档站或稳定项目域名之前，Website 字段保持为空。不要指向临时 placeholder landing page。

## Social Preview

使用从 `assets/praxflow-banner.svg` 导出的 **1280 × 640** PNG。

Preview 建议包含：

- PraxFlow；
- `Engineering workflows for reliable AI agents`；
- `Composable · Evidence-first · Human-guided · Reality-verified`；
- Goal → Workflow → Skills → Evidence feedback 的视觉结构。

不要加入 Vendor Logo。

GitHub 路径：

```text
Settings → General → Social preview → Edit
```

## Pull Request 通用设置

建议：

- **Allow squash merging:** on；
- **Allow merge commits:** off；
- **Allow rebase merging:** optional；
- **Always suggest updating pull request branches:** on（可用时）；
- **Automatically delete head branches:** on。

Squash merging 比较适合 PraxFlow：一个方法论变更可以在 PR 讨论中保留完整过程，而 main history 最终仍然保持一个清晰的 conceptual change。

## `main` Branch Protection

使用 Ruleset 或 Branch Protection Rule 保护 `main`。

建议 baseline：

- merge 前要求 Pull Request；
- protected `main` 允许 **squash** merge；
- 要求 aggregate `Validate PraxFlow` status check；
- 实际可行时要求 branch up to date；
- 禁止 force push；
- 禁止 branch deletion；
- 只有未来真的出现多维护者 CODEOWNERS 流程时，再要求 code-owner review。

`Validate PraxFlow` aggregate job 应保持稳定：只有 Python compatibility / structural checks、Agent Skills reference validation、external distribution smoke test、Installer smoke tests、Protocol/package synchronization 都成功后它才成功。Branch protection 应依赖这个 aggregate context，而不是依赖容易变化的 matrix job name。

不要在目前只有一个主要维护者时增加没有实际 Review 价值的 approval ceremony。

## Security

Repository 支持时启用 GitHub **Private vulnerability reporting**。

`SECURITY.md` 已经要求不要公开披露可利用漏洞。启用 private reporting 后，把 GitHub Security UI 作为首选 confidential channel。

## Discussions

不要为了“看起来完整”而提前启用 Discussions。

只有当社区流量足够高，usage question、design discussion、example sharing 已经明显干扰 Issues 时，再考虑启用。

在此之前：

- Issues 用于 reproducible defect 和 methodology proposal；
- Pull Requests 用于 concrete change；
- 没有 actionable engineering question 的纯发散讨论不要占用 Issue tracker。

## Releases

不要因为 repository 结构已经整理完成，就发布一个看起来像 stable 的 `v0.1.0`。

按 [`releasing.md`](releasing.md) 的 Release Gate 执行。第一个公开 Release 应该通常是 `v0.1.0-alpha.1` 这类 pre-release，并且前提是已经记录 representative real-world evaluations。

## 定期复查

Repository administration 也属于会随 GitHub 产品变化的外部事实。修改这些建议之前，应重新检查当前 GitHub Settings / Rulesets / Security UI，而不是依赖旧截图或模型记忆。
