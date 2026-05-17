---
type: source
source_type: docs
title: Arize Phoenix Tracing
url: https://arize.com/docs/phoenix/tracing/llm-traces
author: Arize AI
site: arize.com
topic:
  - observability
  - evaluation
  - agent
  - infrastructure
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Observability]]"
  - "[[Trace]]"
  - "[[OpenTelemetry GenAI]]"
  - "[[Agent Lifecycle Hook]]"
---

# Arize Phoenix Tracing 文档

## 为什么收

Phoenix 是开源 LLM observability / tracing 工具的代表之一，适合回答“这些本地 hook / trace / tool call 数据能接到什么应用里实时观察”。

## 关键事实

- Phoenix 用 OpenTelemetry 跟踪 LLM 应用执行路径，能记录 retrieval、embedding、LLM invocation、response generation 等多步骤时间线。
- Phoenix 支持 OTLP，并提供 OpenAI、LangChain、LlamaIndex、DSPy 等框架和 SDK 的 instrumentation。
- 它能观察 latency、token usage、runtime exceptions、retrieved documents、embedding、LLM parameters、prompt templates、tool descriptions 和 function calls。

## 可以拆成概念卡

- [[Observability]]
- [[Trace]]
- [[OpenTelemetry GenAI]]

## 边界提醒

Phoenix 是观测平台，不是 Agent runtime 本身。它能帮助看见轨迹、调试性能和质量问题，但是否阻断动作、如何审批、如何恢复，仍要由 [[Agent Harness]]、[[Guardrails]]、[[Tool Permissioning]] 或业务系统负责。

