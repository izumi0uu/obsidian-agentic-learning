---
type: source
source_type: docs
title: OpenAI Agents SDK Documentation
url: https://openai.github.io/openai-agents-python/
author: OpenAI
site: openai.github.io
topic:
  - agent
  - openai
  - tools
created: 2026-05-05
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent]]"
  - "[[Tool Calling]]"
  - "[[Evaluation]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Approval Gate]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# OpenAI Agents SDK 文档

## 为什么收

这是学习 OpenAI Agent 工程接口的主文档。适合理解 agent、tools、handoffs、guardrails、tracing 这些生产系统概念。

## 先读什么

- Quickstart
- Agents
- Tools
- Handoffs
- Guardrails
- Tracing

## 一句话

OpenAI Agents SDK 提供构建 agentic app 的工程抽象，包括 Agent、工具、交接、护栏和追踪。

## 可以拆成概念卡

- [[Agent]]
- [[Tool Calling]]
- guardrails
- handoff
- [[Trace]]
- [[Observability]]
- [[Evaluation]]

## 我的疑问

- SDK 里的 Agent 和我概念卡中的 Agent 定义有什么差别？
- guardrails 应该算 Agent 的一部分，还是系统外层保护？

## 边界提醒

SDK 文档会随版本变化，读的时候要注意日期和当前安装版本。

## Tracing 补充

OpenAI Agents SDK 文档把 tracing 作为 SDK 内建能力之一，用于记录、调试和可视化 agent workflow。它适合作为 [[Trace]]、[[Observability]] 和 [[Agent Lifecycle Hook]] 的现代工程证据：模型调用、工具调用、handoff、guardrail 等运行时事件可以被 SDK 组织成 trace，而不是只留在 prompt 文本里。

边界：tracing 是观测和调试能力，不自动等于质量评估；真正判断输出好不好，还需要 [[Evaluation]]、人工反馈或任务指标。


## 2026-05-12 full framework comparison 补充

OpenAI Agents SDK 在本次全量对比中定位为 OpenAI-first 的轻量 agentic app SDK：核心抽象包括 Agent、tool、handoff、guardrail、session、tracing 和 MCP。它适合快速构建围绕 OpenAI 模型和 Responses/Agents 平台能力的应用，但不应被误认为通用 state graph runtime 或企业 agent platform。

证据边界：本补充依据官方 SDK 文档当前导航和 quickstart/agents/tools/handoffs/guardrails/tracing/session 页面；具体 API、默认模型、托管能力和平台集成属于 volatile，需要随官方文档复查。
