---
type: map
topic:
  - observability
  - evaluation
  - security
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Observability]]"
  - "[[Trace]]"
  - "[[Audit Log]]"
  - "[[Replay]]"
  - "[[OpenTelemetry GenAI]]"
evidence:
  - "[[Observability#证据锚点]]"
  - "[[Trace#证据锚点]]"
  - "[[Audit Log#证据锚点]]"
  - "[[Replay#证据锚点]]"
  - "[[OpenTelemetry GenAI#证据锚点]]"
related:
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trajectory Trace 类型对比]]"
---

# Observability Audit 对比

## 一句话总览

[[Observability]] 回答“系统内部发生了什么、如何分析”；[[Trace]] 是一次执行的结构化过程记录；[[Audit Log]] 是关键行动的可追责账本；[[Replay]] 用保存记录和快照复现失败；[[OpenTelemetry GenAI]] 则尝试给 GenAI / Agent 观测数据提供跨平台语义约定。

最小边界：trace 是材料，observability 是分析能力，audit log 是责任链，replay 是复现实验，OpenTelemetry GenAI 是标准化语义层。

## 为什么这组值得对比

- 混淆风险：trace、log、audit、observability、replay、OTel 都像“记录系统”，但目的和字段设计完全不同。
- 共同问题域：它们都围绕 Agent 执行过程的可见性、复盘、合规和回归验证。
- 不同介入点：有的在运行时记录，有的在平台里分析，有的长期留痕，有的重放失败，有的规范字段语义。
- 证据密度：相关卡已有 LangSmith、Langfuse、OpenAI Agents SDK、Arize Phoenix、OpenTelemetry GenAI、Agent 工程基础设施等 source anchors。
- 复习价值：它能防止把“我有日志”误认为“我能调试、评测、审计和复现”。

边界：已有 [[Trajectory Trace 类型对比]] 更偏 ontology：trajectory / trace / reasoning trace / evaluation / replay；本页更偏 observability stack 与 governance 边界。

## 共同问题域

共同问题是：Agent 不是一次性文本生成，而是跨模型调用、工具、检索、状态、权限和环境的过程。要让系统可维护，必须知道发生了什么、能否解释失败、关键动作能否追责、修复能否复现验证、数据能否跨平台传输。

```text
runtime execution
  -> trace spans/events
  -> observability platform search/dashboard/monitoring
  -> audit log for critical actions and approvals
  -> replay cases for regression
  -> OTel GenAI semantic layer / collector / platform integration
```

这几层可以互相依赖，但不能互相替代。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Trace]] | 单次执行的结构化记录 | 运行时同步记录，事后分析 | span、event、LLM call、tool call、observation、metadata | 可调试过程证据 | [[Trace#证据锚点]] |
| [[Observability]] | 搜索、聚合、可视化、告警和失败分析 | 运行中和运行后持续观察 | traces、metrics、logs、scores、feedback | dashboard、alerts、failure clusters、monitoring | [[Observability#证据锚点]] |
| [[Audit Log]] | 关键行动与授权责任链 | 高风险动作发生时和事后审计 | 用户、agent、工具、权限、审批、结果 | 可追责、可合规读取的行动记录 | [[Audit Log#证据锚点]] |
| [[Replay]] | 失败复现和回归验证 | 事后把失败转成可重复实验 | trace、输入、工具结果、环境快照、版本 | replay case、regression comparison | [[Replay#证据锚点]] |
| [[OpenTelemetry GenAI]] | 观测数据语义标准化 | instrumentation 产生数据后导出/汇聚 | span/event/attribute/metric | 跨系统可解释的 GenAI observability 数据 | [[OpenTelemetry GenAI#证据锚点]] |

## 最容易混淆的边界

### Trace vs Observability

[[Trace]] 是一次或一组执行留下的结构化证据；[[Observability]] 是围绕这些证据建立搜索、过滤、聚合、可视化、告警、失败样本收集和 eval 回流的能力。只有 trace 文件，不等于有 observability；只有 dashboard，也不等于 trace 足够细。

### Trace vs Audit Log

[[Trace]] 偏开发调试、性能、成本和 evaluation，可能保存 prompt、工具返回、中间状态和错误细节。[[Audit Log]] 偏长期责任链：谁、何时、基于什么权限、做了什么关键动作、是否审批、结果如何。Audit log 不需要保存每个 token，但关键动作必须可追责。

### Observability vs Evaluation

Observability 帮你看见和定位；[[Evaluation]] 判断好不好。一个 trace 可以告诉你工具调用失败了，但“这是否算失败、是否阻断上线、是否违反安全策略”需要 evaluator、rubric、规则或人工判断。

### Replay vs Retry

[[Replay]] 不是简单再跑一次；它要说明固定了什么变量：输入、工具返回、检索结果、repo commit、浏览器状态、环境快照或随机性。重新采样模型、实时访问网页和重新拉取索引，只能叫再次运行，不能叫严格 replay。

### OpenTelemetry GenAI vs Observability Platform

[[OpenTelemetry GenAI]] 更像数据语义和传输生态：span/event/attribute 应该怎么表达。它不是 UI、不是打分器、也不自动保护隐私。Observability 平台可以消费 OTel 数据，但平台能力、保留策略和脱敏仍要单独设计。

## 执行时序 / 机制差异

```text
Agent runtime
  -> emits Trace spans/events: model call, tool call, observation, error, score
  -> Observability indexes and visualizes traces, metrics, logs
  -> Audit Log extracts critical actions: approval, external side effect, sensitive access
  -> Replay freezes selected trace + environment variables as regression cases
  -> OpenTelemetry GenAI standardizes fields before/while data flows across collectors and platforms
```

一个故障从发现到修复可以这样流动：

```text
alert/dashboard -> inspect trace -> check audit log if action risky -> build replay case -> run eval harness -> compare fixed version
```

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

把 Agent 系统想成一架飞机：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Trace]] | 黑匣子里记录的飞行过程数据 | trace 可能因采样或脱敏不完整 |
| [[Observability]] | 地面控制台和监控系统 | 看见异常不等于已经判定责任 |
| [[Audit Log]] | 关键指令和授权记录 | 它关注责任链，不保存所有传感器细节 |
| [[Replay]] | 用飞行数据在模拟器复现事故 | 需要固定足够环境变量 |
| [[OpenTelemetry GenAI]] | 统一仪表数据格式 | 标准化字段不等于事故分析结论 |

## 现代系统如何吸收或限制

- 来源支持：[[Observability]]、[[Trace]]、[[Replay]] 和 [[OpenTelemetry GenAI]] 的证据锚点支持 LangSmith / Langfuse / OpenAI Agents SDK / Arize Phoenix / OTel 等现代 observability 和 tracing 工作流；[[Audit Log]] 的证据锚点支持安全、合规和责任链角度。
- 工程综合 / inference：现代系统通常把 trace 当作可观测事实层，把 evaluation 当作判断层，把 audit log 当作合规责任层，把 replay 当作回归实验层，把 OTel 当作跨系统语义层。
- 仍需警惕的外推：具体平台字段、OTel attribute 名称、默认采样、隐私策略和 replay 能力会变化；本页只沉淀稳定边界，不替产品能力背书。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 调试一次 Agent 为什么失败 | [[Trace]] | 需要看到模型调用、工具参数、observation、错误和 metadata | trace 采样或脱敏可能丢根因 |
| 线上持续监控慢、贵、错、失败模式 | [[Observability]] | 需要 dashboard、搜索、聚合、告警和失败样本收集 | 可见不等于会评分；仍需 evaluation |
| 复盘高风险外部动作或权限争议 | [[Audit Log]] | 要回答谁授权、做了什么、影响什么资源 | 记录太细会泄露隐私，太粗又无法追责 |
| 验证一个修复是否真的解决旧失败 | [[Replay]] | 需要固定输入/工具/环境并比较新旧结果 | 环境不可复现时只能降级为近似重跑 |
| 要把 traces 接入多个平台或标准管线 | [[OpenTelemetry GenAI]] | 需要统一 span/event/attribute 语义 | 标准化不自动解决质量和隐私 |

## 它们共同不是什么

- 都不是模型真实内心的证明。
- 都不是单独的质量保证；质量判断还需要 [[Evaluation]]、rubric、checker、人工或业务指标。
- 都不是越详细越好；prompt、工具返回、用户数据和敏感字段需要采样、脱敏、访问控制和保留周期。
- 都不是固定产品名；它们是可被不同平台实现的观测、审计和复现层概念。

## 证据锚点

- Concept anchors: [[Observability#证据锚点]], [[Trace#证据锚点]], [[Audit Log#证据锚点]], [[Replay#证据锚点]], [[OpenTelemetry GenAI#证据锚点]]
- Source examples: [[LangSmith Evaluation and Observability#为什么收]], [[Langfuse Observability and Evaluation#OpenTelemetry 补充]], [[OpenAI Agents SDK 文档#Tracing 补充]], [[Arize Phoenix Tracing 文档#关键事实]], [[OpenTelemetry GenAI Semantic Conventions#关键事实]], [[Agent 工程基础设施主源#为什么收]]
- Evidence type: existing concept-card synthesis + docs/source notes + security/observability engineering synthesis + learning analogy.
- Confidence: high for Trace / Audit / Replay / Observability purpose boundaries; medium for OTel/platform details because标准和产品支持仍会变化。
- Boundary: 本页的 stack layering 是工程综合；具体字段、UI、采样和合规策略需回到实际平台文档。

## 复习触发

1. 为什么“有 trace”不等于“有 observability”？
2. 如果 Agent 发送了一封外部邮件，trace 和 audit log 分别至少要保存什么？
3. Replay 和 retry 的最小区别是什么？
4. OpenTelemetry GenAI 解决的是字段语义问题，为什么它不能替代 evaluation？
5. 在隐私严格场景下，哪些 trace 字段应该只保存摘要或脱敏版本？

## 相关链接

- [[Observability]]
- [[Trace]]
- [[Audit Log]]
- [[Replay]]
- [[OpenTelemetry GenAI]]
- [[Evaluation]]
- [[Eval Harness]]
- [[Trajectory Evaluation]]
- [[Trajectory Trace 类型对比]]
- [[LLM Wiki 工作流]]
