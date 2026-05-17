---
type: source
source_type: docs
title: Pydantic AI Documentation
url: https://pydantic.dev/docs/ai/overview/
author: Pydantic
site: pydantic.dev
topic:
  - agent
  - framework
  - python
  - evaluation
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Framework]]"
  - "[[Evaluation]]"
  - "[[Tool Calling]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Pydantic AI 官方文档

## 为什么收

Pydantic AI 是 Python 类型系统和 Pydantic 生态进入 Agent framework 的代表。它适合用来学习“类型安全、依赖注入、结构化输出、eval、observability、MCP/A2A、durable execution”如何进入 Agent SDK。

## 先读什么

- Overview
- Agents
- Dependencies
- Output
- Tools & Toolsets
- Testing / Pydantic Evals
- Durable Execution
- Pydantic Graph
- MCP / A2A / UI event streams

## 一句话

Pydantic AI 是 Python-first、type-safe 的 GenAI / Agent framework：用 Pydantic 的验证、依赖注入和结构化输出降低 runtime 错误，同时补 eval、Logfire observability、MCP/A2A、durable execution 和 graph 支持。

## 需要我读的内容

### 必读块 1：type-safe agent framework 定位

- 位置：Pydantic AI Overview / Why use Pydantic AI。
- 为什么必读：支撑它和 OpenAI Agents SDK / Vercel AI SDK 的边界：Pydantic AI 的核心卖点是 Python 类型和验证生态。
- 中文概括：官方文档强调 Python agent framework、model-agnostic、type-safe、Pydantic Logfire observability、evals、MCP/A2A/UI、human-in-the-loop 和 durable execution。
- 支撑概念：[[Agent Framework]], [[Tool Calling]], [[Evaluation]], [[Trace]]。
- 证据边界：功能列表代表官方路线；具体 API 和集成成熟度属于 volatile。

### 必读块 2：依赖注入与结构化输出

- 位置：Tools & Dependency Injection Example。
- 为什么必读：支撑“Pydantic AI 更像 typed application SDK，而不是 conversation team 框架”的判断。
- 中文概括：示例把 deps_type、output_type、RunContext、tool schema 和 Pydantic 校验放在 Agent 类型里，让数据依赖和输出结果进入类型检查/验证链路。
- 支撑概念：[[Tool Calling]], [[Eval Harness]], [[Agent State]]。
- 证据边界：类型安全降低某些工程错误，但不能保证业务答案正确。

## 可以拆成概念卡

- Type-safe agent SDK
- Structured output validation
- Pydantic Evals

## 我的疑问

- Pydantic Graph 和 LangGraph 的状态图边界如何区分？
- Durable execution 集成 Temporal / DBOS / Prefect / Restate 时，框架责任和外部 runtime 责任如何分割？

## 边界提醒

Pydantic AI 不只是“把 Pydantic 用在 prompt 里”，而是把类型、依赖、输出、eval 和 observability 放进 Agent SDK；但类型通过不等于事实正确，仍需要测试集、trace 和业务指标。
