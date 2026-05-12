---
type: source
source_type: docs
title: "LangGraph Official Documentation"
url: "https://docs.langchain.com/oss/python/langgraph/overview"
author: LangChain
site: docs.langchain.com
topic:
  - agent
  - langgraph
created: 2026-05-05
updated: 2026-05-12
last_checked: 2026-05-12
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Memory]]"
  - "[[Planning]]"
  - "[[Long-term Memory]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# LangGraph 官方文档

## 为什么收

LangGraph 是学习工程化 Agent 的重要框架。它把 Agent 看成有状态的图，适合理解循环、分支、人工确认和长任务执行。

## 先读什么

- Overview
- Agents
- Durable execution
- Human-in-the-loop
- Memory

## 一句话

LangGraph 是 LangChain 生态里的低层 agent orchestration runtime：用状态图组织长任务 Agent，让节点、边、状态、持久化、human-in-the-loop 和 durable execution 变成显式工程对象。

## 可以拆成概念卡

- [[Agent Loop]]
- [[Memory]]
- [[Long-term Memory]]
- [[Planning]]
- state graph
- human-in-the-loop
- durable execution

## 我的疑问

- 什么时候需要 LangGraph，而不是简单 chain、普通 workflow 或更高层 harness？
- 图结构怎样帮助 Agent 可调试？
- LangGraph 作为 runtime，与 LangChain agents、Deep Agents harness、LangSmith observability 的分层边界是什么？

## 边界提醒

LangGraph 是 Agent orchestration runtime / 工程框架，不是模型本身，也不是 Deep Agents harness。当前文档明确把 Deep Agents 放在 LangGraph 之上的 harness 层，把 LangGraph 放在 durable execution、streaming、human-in-the-loop 和 persistence 的 runtime 层。
