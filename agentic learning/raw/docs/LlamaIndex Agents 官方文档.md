---
type: source
source_type: docs
title: LlamaIndex Agent Documentation
url: https://developers.llamaindex.ai/python/framework/understanding/agent/
author: LlamaIndex
site: developers.llamaindex.ai
topic:
  - agent
  - framework
  - rag
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
  - https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/
related:
  - "[[Agent Framework]]"
  - "[[RAG]]"
  - "[[Agentic RAG]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# LlamaIndex Agents 官方文档

## 为什么收

LlamaIndex 从 data / index / retrieval 生态进入 Agent，很适合观察“知识库、RAG、工具调用和 Agent workflow 如何结合”。在 Agent framework 选型里，它常常不是因为多 Agent 聊天最强，而是因为数据连接、索引、retriever、query engine 和 agent workflow 之间的衔接成熟。

## 先读什么

- Building an agent
- Using existing tools
- Maintaining state
- Human in the loop
- Multi-agent patterns
- RAG / Indexing / Querying / Observability / Evaluating

## 一句话

LlamaIndex Agents 是以数据/RAG 生态为底盘的 Agent 框架路线：agent 可选择函数、query engine 等工具，多 Agent 可以通过 AgentWorkflow 等 pattern 组织，尤其适合知识密集型应用。

## 需要我读的内容

### 必读块 1：agent loop 与 tool 选择

- 位置：Building an agent。
- 为什么必读：支撑 LlamaIndex 在本页中的定位：LLM agent 执行多步循环并从工具集中选择下一步。
- 中文概括：官方文档把 agent 描述为拿到任务后多步执行、使用工具、判断是否完成；工具可以是普通函数，也可以是 LlamaIndex query engine。
- 支撑概念：[[Agent Loop]], [[Tool Calling]], [[Agentic RAG]]。
- 证据边界：这支持“agent + tools + loop”定位；不自动支持其在所有流程编排上优于 LangGraph。

### 必读块 2：pre-built workflows 与多 Agent patterns

- 位置：Building an agent / Multi-agent patterns。
- 为什么必读：支撑 LlamaIndex 不只是 RAG 库，也提供 AgentWorkflow、FunctionAgent 等 agentic workflow 抽象。
- 中文概括：官方文档区分自建 agentic workflows 和预置 FunctionAgent / AgentWorkflow，并把多 Agent patterns 单独列为学习路径。
- 支撑概念：[[Agent Workflow]], [[Multi-agent Orchestration]]。
- 证据边界：多 Agent 能力需要结合具体 pattern 和版本复查。

## 可以拆成概念卡

- LlamaIndex AgentWorkflow
- Query engine as tool
- Data/RAG-first agent framework

## 我的疑问

- 什么时候 LlamaIndex agent 应该调用 query engine，什么时候应该先固定成普通 RAG workflow？
- AgentWorkflow 与 LangGraph / Mastra workflow 的状态和恢复边界有什么差异？

## 边界提醒

LlamaIndex 的独特价值在数据和检索生态，不应被误读成“所有 Agent 编排都必须从 RAG 框架开始”。知识密集场景优先考虑；非知识密集、强控制流场景应另看 workflow/runtime。
