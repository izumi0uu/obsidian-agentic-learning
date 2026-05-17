---
type: source
source_type: docs
title: Mastra Agent Documentation
url: https://mastra.ai/docs/agents/overview
author: Mastra
site: mastra.ai
topic:
  - agent
  - framework
  - typescript
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Tool Calling]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Mastra 官方文档

## 为什么收

Mastra 是 TypeScript/JavaScript 生态里热门的 Agent framework。它把 agents、tools、memory、structured output、guardrails、approval、workflows、MCP、observability、evals、deployment 和 platform 放进一个前端/全栈开发者熟悉的栈里，适合和 Vercel AI SDK、Pydantic AI、LangGraph 比较。

## 先读什么

- Agents overview
- Tools
- Memory
- Structured Output
- Agent Approval
- Supervisor Agents / Background Tasks
- Workflows
- MCP
- Observability / Evals / Deployment

## 一句话

Mastra 是 TypeScript-first 的 Agent + workflow 框架：agent 处理开放式任务，workflow 处理明确控制流，并提供 memory、tools、structured output、guardrails、approval、observability、evals 和 deployment 入口。

## 需要我读的内容

### 必读块 1：agent vs workflow 边界

- 位置：Agents overview / When to use agents。
- 为什么必读：支撑 Mastra 的现代工程判断：开放式任务用 agent，确定性多步流程用 workflow。
- 中文概括：官方文档把 agent 描述为根据目标自行决定工具和循环次数；当流程需要明确控制流时，应使用 workflows。
- 支撑概念：[[Agent Workflow]], [[Agent Loop]], [[Agent Framework]]。
- 证据边界：这是官方设计建议，不是所有业务场景的固定答案。

### 必读块 2：Agent 能力扩展表

- 位置：Agents overview / Expand your agent。
- 为什么必读：支撑 Mastra 的全栈 Agent framework 定位。
- 中文概括：官方把 tools、memory、structured output、approval、supervisor agents、processors、guardrails、dynamic configuration、channels 等列为 agent 扩展路径。
- 支撑概念：[[Tool Calling]], [[Memory]], [[Guardrails]], [[Approval Gate]]。
- 证据边界：文档包含 new/deprecated 标签，API 和推荐路径需要跟随版本复查。

## 可以拆成概念卡

- TypeScript agent framework
- Agent approval
- Supervisor agents

## 我的疑问

- Mastra workflows 与 Vercel AI SDK workflow patterns 的分层边界是什么？
- Supervisor agents 和传统 orchestrator-workers pattern 的差异有多少来自 framework API，有多少只是命名？

## 边界提醒

Mastra 比 Vercel AI SDK 更像完整 Agent framework；Vercel AI SDK 更像 UI/streaming/tool-loop toolkit。Mastra 的 product/platform 变化快，必须保持 volatile。
