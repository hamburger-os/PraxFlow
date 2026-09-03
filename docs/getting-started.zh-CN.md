# PraxFlow 入门与使用指南

[English](getting-started.md) · [简体中文](getting-started.zh-CN.md)

PraxFlow 是一组可移植的 Agent Skills，用来给已经很有能力的 Coding Agent 增加更稳定的工程纪律。它不替代 Coding Agent、本地工具、MCP Server、Build System 或项目自己的文档。

这份指南重点回答四个问题：**PraxFlow 为什么存在、应该安装哪些 package、怎么安装、安装之后应该怎样使用。**

## 基本原理

现代 Coding Agent 通常已经会读取仓库、修改文件、运行命令、搜索代码并生成实现。很多可靠性问题并不是“它不会执行”，而是发生在执行动作之上的判断层：

- 还没有理解到足够程度就开始修改；
- 把一个“看起来合理”的解释当成已经成立的事实；
- 本来可以通过调查仓库解决的问题，却直接问用户；
- 修改范围超过已经建立的因果边界；
- 用很弱或不相关的验证就宣称任务完成；
- 有价值的项目知识随着当前上下文结束而丢失。

PraxFlow 用四个概念处理这些问题：

| 概念 | 作用 |
| --- | --- |
| **Workflow** | 针对一类工程目标的端到端认知闭环。 |
| **Skill** | 可以在多个 Workflow 中复用的认知方法。 |
| **Protocol** | 横跨 Workflow / Skill 的证据、决策、变更范围、验证和知识规则。 |
| **Capability** | 当前项目或环境真正能执行的动作，例如 build、test、deploy、flash、browser、serial、database。 |

最重要的分层是：

> PraxFlow 决定 **什么时候、为什么** 需要某项工程动作；具体项目和 Agent 环境决定 **怎么执行** 这项动作。

完整概念模型见 [`concepts.zh-CN.md`](concepts.zh-CN.md)。

## 先选择 Workflow

对大多数非简单任务，先根据用户的目标选择 Workflow。

| 目标 | Workflow | 什么时候使用 |
| --- | --- | --- |
| 新增或明显改变行为 | `develop-feature` | 任务需要理解现有系统、收敛设计、控制范围、实现、Review 和验证。 |
| 修复错误行为 | `fix-bug` | 需要明确期望与实际行为、建立因果解释、修复根因并验证回归。 |
| 理解陌生项目或系统 | `understand-project` | 当前目标是建立解释或工作模型，而不是修改代码。 |
| 审查一个已有变更 | `review-change` | 需要根据意图、真实改动范围、契约和证据输出高信噪比 Review。 |

这些 Workflow 刻意保留不同认知结构。`fix-bug` 不是换了名字的 `develop-feature`，`review-change` 也不应该默认演化成“顺便把代码改掉”。

## 再按需要安装可复用 Skills

Workflow 在相关 Skill 已安装且适用时，会复用下面这些认知方法：

| Skill | 它主要改变 Agent 的什么行为 |
| --- | --- |
| `survey` | 帮助 Agent 判断先看哪里，以及调查应该扩展到多远。 |
| `trace` | 跨调用、数据、状态、事件、异步边界和生命周期还原行为路径。 |
| `grill` | 先调查可以自己解决的事实，只把真正重要的选择升级给用户。 |
| `diagnose` | 比较多个因果假设，并选择高信息量验证，而不是锁死第一个合理解释。 |
| `plan-change` | 在高成本编辑前限定解决目标所需的最小因果变更边界。 |

`plan-change` 在 v0.1 中仍然是 provisional。如果真实 Eval 证明它没有比普通 Agent planning 带来足够增益，PraxFlow 会删除它，而不是为了目录对称保留。

### 实际推荐组合

新增功能可以从下面这组开始：

```text
develop-feature
survey
trace
grill
plan-change
diagnose
```

Debug 可以使用：

```text
fix-bug
survey
trace
diagnose
plan-change
```

理解项目可以使用：

```text
understand-project
survey
trace
```

Review 可以使用：

```text
review-change
survey
trace
diagnose
```

这些是推荐组合，不是硬编码 dependency manifest。PraxFlow v0.1 刻意保持组合模型简单；Workflow 的规则是：相关 Skill **when available** 时使用它。

## 安装 PraxFlow

### 推荐方式：Agent Skills 生态 Installer

大多数用户直接运行：

```bash
npx skills@latest add hamburger-os/PraxFlow
```

然后在交互界面里选择需要的 Workflow、Cognitive Skills、可选 Domain Pack，以及目标 Coding Agent。

如果已经明确知道要安装哪些 package：

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

GitHub CLI 也提供 Agent Skill 安装能力：

```bash
gh skill install hamburger-os/PraxFlow
```

不同客户端的安装位置和发现行为可能变化。PraxFlow 当前维护的兼容性说明见 [`../adapters/README.md`](../adapters/README.md)。

### 高级方式：PraxFlow 内置确定性 Installer

以下情况更适合 Clone 仓库：

- 希望确定性安装整套 Core；
- 正在开发 PraxFlow 本身；
- 需要自定义输出目录；
- 需要显式安装 Domain Pack；
- 需要 Dry Run 或更明确的冲突控制。

```bash
git clone https://github.com/hamburger-os/PraxFlow.git
cd PraxFlow
```

内置工具要求 Python 3.10 或更高版本。

把 Core Workflows + Core Skills 安装到 Codex-compatible 项目：

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/project
```

额外安装嵌入式 Reference Domain Pack：

```bash
python3 scripts/install.py \
  --target codex \
  --scope project \
  --dest /path/to/project \
  --pack praxflow-embedded
```

## 安装以后怎么使用

Agent Skills 客户端通常会先把已安装 Skill 的 `name` 和 `description` 暴露给模型。当任务与某个 package 匹配时，Agent 可以激活它；部分客户端也支持用户显式选择或调用 Skill。

PraxFlow **不要求用户学习一套新的命令语言**。

例如普通的 feature 请求仍然可以这样写：

> 给 WebSocket client 增加断线重连。保持现有 public API 不变，并使用项目已有测试验证 reconnect 行为。

当 `develop-feature` 和相关 Skills 可用时，PraxFlow 的价值不在于让用户改变需求表达方式，而在于让 Agent 改变工作方法：先建立必要的现状和约束证据，再处理真正重要的设计选择，限定改动范围，然后实现、Review、验证。

Debug 也一样，可以直接描述问题，而不是替 Agent 指定根因：

> 网络中断后，服务偶尔显示 connected，但不再收到事件。请定位原因、修复并验证回归。

当 `fix-bug` 和 `diagnose` 可用时，Agent 应该先明确 expected vs observed，证据不足时保留多个因果解释，并通过有区分度的检查逐步排除，而不是看到第一段可疑代码就直接修。

如果你的客户端支持显式 Skill 选择，也可以在你明确希望使用某种方法时选中对应 PraxFlow package。具体 UI 或调用语法属于客户端，而不是 PraxFlow Core 的一部分。

## 一个好的 PraxFlow 执行应该是什么样

PraxFlow 生效的表现应该是 **更有纪律，但不是所有任务都变得更繁琐**。

你通常应该看到 Agent：

- 先调查可调查的项目事实，再提出无法避免的问题；
- 在重要场景中区分 observation、source、inference、assumption、unknown 和 conflict；
- 把人的注意力留给真正重要的决策，而不是普通事实确认；
- 只建立当前目标真正需要的项目理解，不无限扩展阅读范围；
- 追求最小 **因果变更**，而不是机械追求最小 diff；
- 对重要 Debug 假设和 Review finding 主动尝试反证；
- 让验证强度与风险和最终结论相匹配；
- 只沉淀稳定、可复用的项目知识，不保存全部临时推理过程。

你**不应该**期待每个小任务都生成 spec 文件、每次都要求批准、每次都跑最重的完整测试、或者激活全部 Skills。比例原则本身就是 PraxFlow 方法论的一部分。

## Domain Pack 是什么

Domain Pack 在不复制 Core Workflow 的前提下，增加领域特定的 Evidence、Review 和 Verification 策略。

目前第一个 Reference Pack 是：

```text
praxflow-embedded
```

它增加嵌入式开发中特别重要的规则，例如：

- Datasheet、Errata、正式标准、SDK 文档、Reference Implementation 的证据权威性；
- ISR / Thread 边界；
- DMA / Cache 一致性；
- Alignment / ABI；
- Memory Lifetime；
- Timing；
- Error Path；
- 从静态检查、Build 到 Deploy/Flash、Target Execution、Device Observation 的验证策略。

当一个领域存在反复出现、而通用软件工程规则不足以覆盖的推理风险时，适合使用 Domain Pack。

Domain Pack 不应该保存某一个项目的 build command、credential、device address 或架构事实。这些属于消费 PraxFlow 的具体项目。

## Agent Skills 标准与 PraxFlow 自己的约定

一个符合 Agent Skills 开放格式的最小 Skill 是：

```text
skill-name/
└── SKILL.md
```

规范还约定了常见的可选资源目录，例如：

```text
scripts/
references/
assets/
```

同时也允许额外文件。

PraxFlow 自己选择下面这个 canonical **repository source layout**：

```text
skills/<package-name>/SKILL.md
```

这里一定要区分：顶层 `skills/` 扁平 catalog 是 **PraxFlow 的分发约定**。Agent Skills Specification 本身并没有要求所有仓库必须使用一个名为 `skills/` 的顶层目录，也没有规定所有客户端必须使用同一个安装目录。

同样，PraxFlow 不会默认在每个 Skill package 里增加给人看的 README。人类的原理说明、教程、示例和使用方式集中在 `docs/`；package 内的 `references/` 用于 Agent 执行时按需加载。

## 如果你在开发 PraxFlow 本身

运行：

```bash
python3 scripts/validate.py
```

涉及 package format 的变更还应该通过 CI 使用的 Agent Skills reference validator。

贡献规范见 [`../CONTRIBUTING.md`](../CONTRIBUTING.md)。

## 下一步

- 阅读 [`concepts.zh-CN.md`](concepts.zh-CN.md) 了解完整概念模型。
- 阅读 [`../adapters/README.md`](../adapters/README.md) 了解客户端安装路径和兼容性边界。
- 阅读 [`../case-studies/`](../case-studies/) 查看真实工程案例。
- 阅读 [`roadmap.zh-CN.md`](roadmap.zh-CN.md) 查看项目当前阶段和后续 Eval 方向。
