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
updated: 2026-05-07
last_checked: 2026-05-07
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

LangGraph 用图结构组织 Agent 工作流，让状态、节点、边和循环都变成显式工程对象。

## 可以拆成概念卡

- [[Agent Loop]]
- [[Memory]]
- [[Long-term Memory]]
- [[Planning]]
- state graph
- human-in-the-loop
- durable execution

## 我的疑问

- 什么时候需要 LangGraph，而不是简单 chain 或普通 workflow？
- 图结构怎样帮助 Agent 可调试？

## 边界提醒

LangGraph 是 Agent 工程框架，不是模型本身。
