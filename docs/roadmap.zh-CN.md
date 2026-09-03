# PraxFlow Roadmap

[English](roadmap.md) · [简体中文](roadmap.zh-CN.md)

PraxFlow 应该从经过真实验证的 Workflow 中成长，而不是从推测性的 Framework 设计中成长。

## v0.1 — 方法论基线

目标：证明一小组 Cognitive Skills 和横向 Protocols 能够在多个客户端中实质改善软件工程 Agent 的行为。

交付内容：

- 四个 Core Workflows：
  - `develop-feature`
  - `fix-bug`
  - `understand-project`
  - `review-change`
- 五个 Core Cognitive Skills：
  - `survey`
  - `trace`
  - `grill`
  - `diagnose`
  - `plan-change`
- 五个 Core Protocols：
  - evidence
  - decisions
  - change scope
  - verification
  - knowledge
- Embedded Domain Pack 作为第一个 reference implementation
- 一个 PraxFlow canonical source catalog：`skills/*/SKILL.md`
- 在 Agent Skills-compatible 客户端中实现可移植安装，不依赖 PraxFlow 专用 deep-discovery 规则
- 对所有 package 做结构验证，并通过外部 Installer smoke test 验证真实分发

成功标准应该是行为层面的，而不是文件数量：

- Agent 因为会先调查，所以减少可以避免的问题；
- 重要事实结论能够暴露来源或不确定性；
- Debug 会测试竞争性假设，而不是直接修改第一个可疑位置；
- Change plan 能在编辑开始前暴露范围扩张；
- Review 减少 speculative/noise findings，并主动尝试反证重要 finding；
- “任务完成”这类结论由相关外部检查支撑；
- 嵌入式 Workflow 在相关情况下持续使用合适的权威资料和真实 Target Evidence。

分发方面也有一个明确的互操作性标准：PraxFlow 的 first-class packages 应该能够从它自己的扁平 `skills/<name>/SKILL.md` source catalog 被主流且受支持的 Agent Skills 工具发现，而不需要自定义 PraxFlow repository adapter。需要注意，扁平 `skills/` source root 是 PraxFlow 的仓库约定，并不是 Agent Skills Specification 强制规定的通用文件系统布局。

## v0.2 — 真实项目评估

暂时不要增加 Workflow DSL。

至少在以下三类代表性任务中运行 v0.1 packages：

1. 常规 application/backend repository；
2. embedded/RTOS repository；
3. legacy 或文档很差的 repository。

记录失败模式，例如：

- Skill trigger overlap；
- 不必要的 activation；
- Workflow instructions 被忽略，或者以有害顺序执行；
- 过多提问；
- Evidence claim 没有可追踪依据；
- 修改范围过宽；
- 明明有更强 Capability，却使用了过弱验证；
- Domain Pack 规则没有实际影响正在执行的 Workflow。

应该先用这些失败来修改 package，再考虑引入新的抽象。

## v0.3 — Evals 与 Conformance

增加可重复 Eval，覆盖：

- trigger precision；
- question quality；
- assumption visibility；
- evidence provenance；
- diagnosis information gain；
- curated changes 上的 review precision / recall；
- change-scope discipline；
- verification selection。

条件允许时比较：

```text
baseline agent
vs
agent + individual Skill
vs
agent + full Workflow
vs
agent + Workflow + Domain Pack
```

目标是建立因果证据：PraxFlow 的哪些部分实际上带来了质量提升。

## v0.4 — 第二个 Domain Pack

只有 Embedded 已经验证 Domain Pack 机制之后，才增加第二个具有明显差异的领域。

Backend / distributed systems 是一个较强候选，因为它带来 transaction、migration、idempotency、authorization、observability 和 distributed failure 等不同风险。

第二个 Pack 应该用来验证 Domain Pack 这个抽象是否真的可复用，而不是 Embedded-specific 的偶然结构。

## Managed distribution Decision Gate

当 Native client plugin 或 managed bundle 能够实质改善更新、发现或集成体验时，可以增加这些分发层。

它们必须仍然是 canonical `skills/` catalog 之上的派生分发层。不要为了适配某个 client marketplace，再维护第二套手工同步的方法论 source tree。

## Workflow manifest Decision Gate

Machine-readable Workflow manifest 暂时延后。

只有真实 Workflow 持续出现自然语言 Skill Package 难以可靠表达的需求时，才考虑 manifest，例如：

- 显式 branches；
- resumable state；
- durable checkpoints；
- client-independent human approval gates；
- deterministic dependency resolution；
- eval instrumentation；
- static workflow validation。

如果未来引入 manifest，应该从已经验证过的 Workflow 中抽取出来，而不是脱离真实使用独立设计。

## Runtime Decision Gate

除非可移植的 Agent Skills orchestration 被真实用例证明不够，否则不要开发 PraxFlow Runtime。

Runtime 只有在解决客户端 Agent 本身无法合理解决的、已经被观察到的问题时才成立。

## 长期方向

PraxFlow 将来可能扩展到 Research、Product Development、Technical Writing，以及其他对证据敏感的知识工作。

这只是长期方向，不是 v0.1 的当前能力声明。

Core methodology 应该通过成功迁移到不同领域来获得通用性，而不是仅仅依靠更宽泛的文字描述。
