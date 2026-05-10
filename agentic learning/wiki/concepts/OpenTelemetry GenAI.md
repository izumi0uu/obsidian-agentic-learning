---
type: concept
topic:
  - observability
  - evaluation
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[OpenTelemetry GenAI Semantic Conventions]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[Arize Phoenix Tracing 文档]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[OpenTelemetry GenAI Semantic Conventions#关键事实]]"
  - "[[Langfuse Observability and Evaluation#OpenTelemetry 补充]]"
  - "[[Arize Phoenix Tracing 文档#关键事实]]"
related:
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Replay]]"
  - "[[Evaluation]]"
---

# OpenTelemetry GenAI

## 一句话

OpenTelemetry GenAI 是 OpenTelemetry 为生成式 AI 调用、token、模型、工具和 Agent 事件定义的观测语义约定方向。

## 概念详解

OpenTelemetry GenAI 出现的背景是：LLM 应用和 Agent 平台都在记录 trace，但如果每个平台用自己的字段名和事件结构，跨系统调试、成本分析、评测回流和平台迁移都会变得困难。OpenTelemetry 的价值不是替你判断答案对不对，而是给 span、event、attribute 和 metric 提供一套更统一的语义语言。

在传统服务里，OpenTelemetry 常用来描述 HTTP 请求、数据库调用、队列和错误。到了 GenAI 场景，观测对象变成了模型请求、prompt/response、token 计数、模型名、provider、tool call、retrieval、agent step、错误、延迟和成本。[[OpenTelemetry GenAI]] 可以让这些事件更容易进入 collector、APM、Langfuse、Phoenix 或其他 observability 平台。

它和 [[Eval Harness]] 的关系是间接的：OTel 负责把过程数据标准化传出去；harness 可以消费这些 trace，把失败样本变成 dataset、run、score 或 regression case。没有 evaluator，OTel 只告诉你发生了什么；有 evaluator，trace 才能进入质量闭环。


学习这张卡时要把“标准化”和“产品能力”分开。OpenTelemetry GenAI 关注事件应该叫什么、属性怎么表达、span 如何关联；它本身不决定 UI 怎么展示、失败怎么打分、数据保留多久、哪些字段要脱敏。工程上经常是 SDK 或 hook 先产生本地事件，再由 adapter 转成 OTel 语义，最后进入 collector 或平台。

## 它解决什么问题

不同框架和平台都会记录 trace，但字段不统一就很难跨系统分析。OpenTelemetry GenAI 试图让模型调用、工具调用、token、延迟和错误有统一语义。

相关生态包括 OpenTelemetry semantic conventions、OpenInference、Phoenix、Langfuse OTel integration。

## 它不是什么

OpenTelemetry GenAI 不是一个评测指标。

它也不是可视化平台本身。它更像统一记录格式和语义层。

它也不保证隐私安全。是否记录 prompt、输出、工具返回和用户数据，以及如何脱敏、采样、保留，仍是系统设计问题。

## 最小例子

```text
span: gen_ai.chat
attributes: model, provider, input_tokens, output_tokens, tool_calls, latency
```

或者在 Agent 场景里：

```text
trace: booking_agent_run
  span: gen_ai.request
  span: tool.call search_flights
  span: tool.call reserve_ticket
  event: human_approval_requested
```

OTel 的目标是让这些名字和字段更可迁移，而不是规定你的业务成功标准。

## 常见误解和风险

- trace 记录了发生什么，不代表好不好。
- prompt 和输出日志可能包含敏感信息。
- 不统一 schema 时，后续 eval 和 debug 会很痛苦。
- 以为接入 OTel 就完成 observability；实际还需要采样、可视化、告警、retention、权限和 eval 回流。

## 边界细节

OpenTelemetry GenAI 和相邻概念的边界：

- [[Trace]]：一条具体执行记录；OTel GenAI 规定这类记录的语义字段怎么表达。
- [[Observability]]：围绕 trace/metrics/logs 的平台能力；OTel 是数据标准和传输生态的一部分。
- [[Replay]]：用保存的输入、工具结果或环境快照重放；OTel trace 能提供线索，但未必包含 replay 所需的全部可复现状态。
- [[Evaluation]]：判断质量；OTel 只是提供可供 evaluator 使用的过程证据。

当概念卡或工程设计提到 OTel 时，要问清楚：是在讨论语义约定、传输协议、collector、平台集成，还是评测数据消费？这些层不要混成一个词。

## Hook / JSONL 到 OTLP 的适配边界

本地 harness 可能先把事件写成 JSONL、metrics 或 state 文件，例如 `.omx/logs/turns-*.jsonl`、`.omx/metrics.json`、`.omx/state/session.json`。这些是有价值的本地观测数据，但还不是 OpenTelemetry。

要接入 OpenTelemetry，需要一个 adapter 把本地事件转换成 span、event、attribute 和 metric，再通过 OTLP 发给 collector 或平台。[[Agent Lifecycle Hook]] 可以是这个 adapter 的触发点，但字段语义、脱敏、采样和关联 ID 仍要由工程层设计。

## 现代性状态

- 判定：frontier / volatile。
- 当前工程实践：把 LLM call、tool call、retrieval 和 agent span 统一成 trace，是 Agent observability 的稳定方向。
- 前沿 / 易变：OpenTelemetry GenAI semantic conventions 仍处于发展状态，字段命名、事件结构和平台支持需要持续复查。
- 复查点：当 OTel semantic conventions、OpenInference、Phoenix/Langfuse/OpenAI tracing 兼容方式有稳定变更时，更新本卡。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[OpenTelemetry GenAI Semantic Conventions]]
- Source: [[Langfuse Observability and Evaluation]]
- Source: [[Arize Phoenix Tracing 文档]]
- Anchor: [[Agent 工程基础设施主源#为什么收]] / [[OpenTelemetry GenAI Semantic Conventions#关键事实]] / [[Langfuse Observability and Evaluation#OpenTelemetry 补充]] / [[Arize Phoenix Tracing 文档#关键事实]]
- Evidence type: official/docs source notes + engineering synthesis.
- Confidence: medium
- Boundary: 标准化 trace 语义是稳定方向；具体 attribute 名称、事件结构和平台支持属于 watch/freshness 范围。

## 复习触发

- 为什么 OpenTelemetry GenAI 不是评测指标？
- Hook/JSONL 事件要变成 OTel span，至少需要补哪些设计？
- [[Trace]]、[[Observability]]、[[OpenTelemetry GenAI]] 三者分别处在哪一层？

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Agent Lifecycle Hook]]
- [[Replay]]
- [[Evaluation]]
