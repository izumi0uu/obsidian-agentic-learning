---
type: source
source_type: docs
title: OpenTelemetry Semantic Conventions for Generative AI
url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
author: OpenTelemetry
site: opentelemetry.io
topic:
  - observability
  - infrastructure
  - agent
  - evaluation
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[OpenTelemetry GenAI]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Agent Lifecycle Hook]]"
---

# OpenTelemetry GenAI Semantic Conventions

## 为什么收

这是 OpenTelemetry 对生成式 AI 观测语义约定的官方页面。它适合用来校准 [[OpenTelemetry GenAI]]：哪些 trace、span、event、metric 字段属于标准化方向，哪些仍处于快速演进状态。

## 关键事实

- OpenTelemetry GenAI semantic conventions 当前标记为 Development。
- 它覆盖 GenAI inputs/outputs events、exceptions、metrics、model spans、agent spans 等信号。
- 它还包含 Anthropic、OpenAI、MCP 等技术特定语义约定方向。

## 可以拆成概念卡

- [[OpenTelemetry GenAI]]
- [[Trace]]
- [[Observability]]

## 边界提醒

OpenTelemetry GenAI 是互操作语义层，不是 dashboard，也不是 eval 指标。它回答“观测数据怎么统一命名和传输”，不直接回答“这条 agent trajectory 好不好”。

