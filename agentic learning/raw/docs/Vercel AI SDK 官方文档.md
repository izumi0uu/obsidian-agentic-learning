---
type: source
source_type: docs
title: Vercel AI SDK Agents Documentation
url: https://ai-sdk.dev/docs/agents/overview
author: Vercel
site: ai-sdk.dev
topic:
  - agent
  - framework
  - frontend
  - typescript
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
  - https://ai-sdk.dev/docs/introduction
related:
  - "[[Agent Framework]]"
  - "[[Tool Calling]]"
  - "[[Context Engineering]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Vercel AI SDK 官方文档

## 为什么收

Vercel AI SDK 是前端/Next.js/TypeScript 生态里非常常见的 AI 应用工具包。它不是传统意义上“全套多 Agent 平台”，但官方已经提供 agents、ToolLoopAgent、memory、subagents、telemetry、UI streams 等模块，适合在全量对比中明确边界：什么时候它是足够轻的 agent toolkit，什么时候需要 Mastra / LangGraph / ADK 这类更完整 runtime。

## 先读什么

- Agents overview
- Building Agents
- Workflow Patterns
- Loop Control
- Memory
- Subagents
- Tool Calling
- Telemetry
- AI SDK UI / Generative UI

## 一句话

Vercel AI SDK 更像 TypeScript / frontend-first 的 AI app toolkit：用 ToolLoopAgent 管理 LLM + tools + loop + context + stopping conditions，并把流式 UI、provider/model、telemetry 和 workflow patterns 接到应用层。

## 需要我读的内容

### 必读块 1：ToolLoopAgent

- 位置：Agents overview / ToolLoopAgent Class。
- 为什么必读：支撑它在本对比中的定位：不是底层 state graph，而是轻量 tool loop abstraction。
- 中文概括：官方文档把 agent 拆成 LLM、tools 和 loop；ToolLoopAgent 负责循环、上下文管理和停止条件，适合多数工具循环任务。
- 支撑概念：[[Agent Loop]], [[Tool Calling]], [[Context Engineering]]。
- 证据边界：适合 agent loop / app integration，不等同于完整企业 Agent 平台。

### 必读块 2：structured workflows 边界

- 位置：Agents overview / Structured Workflows。
- 为什么必读：支撑“不确定性 agent vs 显式 workflow”的判断。
- 中文概括：官方提醒 agent 灵活但非确定；需要可靠、可重复、显式控制流时，应使用 core functions 和 workflow patterns。
- 支撑概念：[[Agent Workflow]], [[Agent Framework]]。
- 证据边界：这与 Microsoft / Mastra 的 agent-vs-workflow 边界相互印证，但具体 API 不同。

## 可以拆成概念卡

- ToolLoopAgent
- Generative UI agent boundary
- Frontend-first AI app toolkit

## 我的疑问

- ToolLoopAgent 与 OpenAI Agents SDK 的 agent loop 在 state、handoff、guardrail 和 tracing 上如何取舍？
- Vercel AI SDK 与 Mastra 组合时，谁负责 agent runtime，谁负责 UI streaming？

## 边界提醒

Vercel AI SDK 不应被等同于 LangGraph 这类 orchestration runtime；它的强项是 TypeScript 应用、streaming UI、provider/tool calling 和轻量 loop control。
