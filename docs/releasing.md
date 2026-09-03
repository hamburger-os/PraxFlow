# PraxFlow 发布指南

本文主要供 PraxFlow 维护者使用，因此默认使用简体中文。代码标识、命令、package 名称和外部规范术语保持原样，方便核对。

PraxFlow 的 Release 应该反映已经验证过的方法论，而不是被日历节奏推动。

## Versioning

PraxFlow 当前处于 pre-1.0。概念模型稳定之前，使用 SemVer pre-release，例如：

```text
v0.1.0-alpha.1
v0.1.0-alpha.2
v0.1.0-beta.1
```

Pre-release 阶段允许 breaking methodology changes，但必须明确记录。

Tagged release 也是分发契约的一部分：Agent Skills installer 可以解析或固定 repository version，所以 package layout 和 installability 必须从 Release commit 本身验证，不能只假设 default branch 正常。

## Release Gate

创建 tag 之前检查：

- [ ] `python3 scripts/validate.py` 在最低支持 Python 版本上通过。
- [ ] `skills/*` 下每个 package 都通过 CI 固定版本的 Agent Skills reference validator。
- [ ] 每个 PraxFlow first-class package 都能从 canonical `skills/<name>/SKILL.md` source catalog 被支持的外部 Installer 直接发现，不依赖 PraxFlow-specific deep-search 或 client-specific source tree。
- [ ] External Agent Skills CLI distribution smoke test 在 Release checkout 上通过。
- [ ] Built-in installer 的跨 target 和 failure-mode smoke tests 通过。
- [ ] 顶层 Protocol 的运行时语义变更没有留下未同步的 `skills/` package。
- [ ] Release commit 上最终 `Validate PraxFlow` aggregate CI gate 为 green。
- [ ] `README.md` 与 `README.zh-CN.md` 描述同一个公开产品表面。
- [ ] `docs/concepts.md` 与 `docs/concepts.zh-CN.md` 的核心模型一致。
- [ ] `docs/getting-started.md` 与 `docs/getting-started.zh-CN.md` 的安装和使用方式一致。
- [ ] `CHANGELOG.md` 包含本次 Release 的变更和已知限制。
- [ ] 每个发生行为变化的 Core Workflow / Skill 都能关联到 observed failure mode、Eval 或具体工程理由。
- [ ] Client compatibility claims 已对照最新 Vendor 文档检查。
- [ ] Security-sensitive changes 已 Review。
- [ ] 如果 Core 行为有实质变化，至少有一个 representative end-to-end scenario 覆盖本次 Release。

如果当前 GitHub CLI 仍把 `gh skill publish` 标记为 preview，可在支持时使用 `gh skill publish --dry-run` 作为额外 Release 验证；不要让 preview-only 行为成为唯一 Gate。

## Distribution Invariants

Release 必须保持以下 invariants：

1. `skills/` 是 PraxFlow 唯一 canonical installable source root。
2. `skills/` 的每个 immediate child 都是 self-contained Agent Skills package，并且目录名与 `name` 一致。
3. Workflow / Skill / Pack 的 PraxFlow 概念类型由 `metadata.praxflow-type` 表达，而不是依赖 path depth。
4. `skills.sh.json` 只是 presentation metadata；删除它不能让 package 本身失去身份或可移植性。
5. Client-specific / managed plugin bundle 如果存在，只能是派生分发层，不能成为第二套手工维护的方法论来源。
6. 不要把 `skills/<name>/SKILL.md` 描述成 Agent Skills Specification 对所有 repository 的强制根目录结构；它是 PraxFlow 自己的 canonical repository convention。
7. 不默认给每个 package 添加人类 README。给人的教程和原理说明放在 `docs/`，package-local `references/` 只保留 Agent 执行时按需使用的内容。

## Alpha Release Criterion

第一个 `v0.1.0-alpha.1` 不应该仅仅因为仓库结构已经存在就发布。

建议最低证据：

1. 一次真实 `develop-feature` run；
2. 一次真实 `fix-bug` run；
3. 一次 unfamiliar-project understanding run；
4. 一次真实 change review；
5. 至少一次 Embedded-domain run，并实际使用 authoritative references 和 environment verification；
6. 对这些运行中发现的失败或限制有明确记录。

## Release Notes

Release notes 应回答：

- Agent behavior 发生了什么变化？
- 什么问题促成了这个变化？
- 哪些 packages 变化了？
- 什么证据支持这个变化？
- 哪些部分仍然 experimental？
- 安装或 compatibility 是否变化？

避免只把 commit list 当作 release notes。

## Release 之后

发布后：

- 从 `CHANGELOG.md` 链接 Release；
- 验证 Release archive 包含预期的 `skills/*` packages；
- 使用至少一个受支持的外部 Agent Skills Installer，从 tagged release 测试真实安装；
- 从 tagged checkout 测试 Built-in installer；
- 在 Client 支持时验证能够按名称 preview / select 一个具体 Skill；
- 新发现的 regression 持续记录在 Issues / Eval records 中。
