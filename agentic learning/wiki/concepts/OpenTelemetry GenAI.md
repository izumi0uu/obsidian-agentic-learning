---
type: concept
topic:
  - observability
  - evaluation
  - infrastructure
status: seed
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

## 它解决什么问题

不同框架和平台都会记录 trace，但字段不统一就很难跨系统分析。OpenTelemetry GenAI 试图让模型调用、工具调用、token、延迟和错误有统一语义。

相关生态包括 OpenTelemetry semantic conventions、OpenInference、Phoenix、Langfuse OTel integration。

## 它不是什么

OpenTelemetry GenAI 不是一个评测指标。

它也不是可视化平台本身。它更像统一记录格式和语义层。

## 最小例子

```text
span: gen_ai.chat
attributes: model, provider, input_tokens, output_tokens, tool_calls, latency
```

## 常见误解和风险

- trace 记录了发生什么，不代表好不好。
- prompt 和输出日志可能包含敏感信息。
- 不统一 schema 时，后续 eval 和 debug 会很痛苦。

## Hook / JSONL 到 OTLP 的适配边界

本地 harness 可能先把事件写成 JSONL、metrics 或 state 文件，例如 `.omx/logs/turns-*.jsonl`、`.omx/metrics.json`、`.omx/state/session.json`。这些是有价值的本地观测数据，但还不是 OpenTelemetry。

要接入 OpenTelemetry，需要一个 adapter 把本地事件转换成 span、event、attribute 和 metric，再通过 OTLP 发给 collector 或平台。[[Agent Lifecycle Hook]] 可以是这个 adapter 的触发点，但字段语义、脱敏、采样和关联 ID 仍要由工程层设计。

## 现代性状态

- 当前工程实践：把 LLM call、tool call、retrieval 和 agent span 统一成 trace，是 Agent observability 的稳定方向。
- 前沿 / 易变：OpenTelemetry GenAI semantic conventions 仍处于发展状态，字段命名、事件结构和平台支持需要持续复查。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[OpenTelemetry GenAI Semantic Conventions]]
- Source: [[Langfuse Observability and Evaluation]]
- Source: [[Arize Phoenix Tracing 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Agent Lifecycle Hook]]
- [[Replay]]
- [[Evaluation]]
