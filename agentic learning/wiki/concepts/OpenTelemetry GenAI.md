---
type: concept
topic:
  - observability
  - evaluation
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Trace]]"
  - "[[Observability]]"
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

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Replay]]
- [[Evaluation]]
