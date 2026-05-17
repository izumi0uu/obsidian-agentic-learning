---
type: source
source_type: docs
title: LangChain Deep Agents Documentation
url: https://docs.langchain.com/oss/python/deepagents/overview
author: LangChain
site: docs.langchain.com
topic:
  - agent
  - langchain
  - langgraph
  - frontier
created: 2026-05-11
updated: 2026-05-11
last_checked: 2026-05-11
freshness: volatile
conflicts:
  - Deep Agent 也可指 RUC-NLPIR 的 DeepAgent 论文/项目名；本 note 只记录 LangChain deepagents SDK / Deep Agents SDK。
status: seed
source:
related:
  - "[[Agent Harness]]"
  - "[[Agent Framework]]"
  - "[[Durable Execution]]"
  - "[[Long-term Memory]]"
  - "[[Multi-agent Orchestration]]"
---

# LangChain Deep Agents 官方文档

## 为什么收

LangChain 的 Deep Agents SDK / `deepagents` 是一个具体的长任务 Agent harness，适合观察现代框架如何把 planning、subagents、filesystem、memory、permissions 和 LangGraph runtime 包在一起。

它值得单独收，是因为用户常会把三层混在一起：通用 deep agent 形态、LangChain 的 `deepagents` SDK，以及其他论文或项目名 DeepAgent。

## 先读什么

- Deep Agents overview：确认 SDK 的定位、核心能力和与 LangGraph 的关系。
- Deep Agents quickstart / package README：看 `create_deep_agent` 如何把 tools、instructions、subagents 等装配成可运行 agent。
- LangChain products / concepts：确认 LangChain、LangGraph、Deep Agents SDK 在 framework、runtime、harness 三层中的分工。

## 一句话

LangChain Deep Agents SDK 是建立在 LangGraph 上的 agent harness：LangGraph 负责有状态编排和运行时，`deepagents` 提供长任务 Agent 常用的 planning、filesystem、subagents、memory 和权限脚手架。

## 关键事实

- 官方文档把 Deep Agents SDK 放在 harness 层，而不是底层 runtime 层；底层运行时是 LangGraph。
- 官方文档描述它适合构建会规划、使用子 Agent、持久化上下文并能随时间学习的 agent。
- `deepagents` 的价值不在于定义一种全新模型，而在于把长任务 Agent 的常见工程部件预封装。
- 典型组成包括：详细系统指令、planning / todo、虚拟或持久化文件系统、subagents、memory、interrupt / permissions，以及 LangGraph 生态的 streaming、durable execution 和 human-in-the-loop 能力。

## 可以拆成概念卡

- [[LangChain DeepAgents]]
- [[Agent Harness]]
- [[Agent Framework]]
- [[Agent State]]
- [[Durable Execution]]
- [[Multi-agent Orchestration]]
- [[Long-term Memory]]
- [[Tool Permissioning]]

## 我的疑问

- `deepagents` 的默认 filesystem / memory 在生产系统中应该如何做数据隔离和权限治理？
- subagents 是不是会诱发过度拆分任务，导致 trace 更长、成本更高？
- 它和手写 LangGraph graph 的边界在哪里：什么时候用 harness，什么时候直接建 graph？

## 边界提醒

本 note 只支撑 LangChain / LangGraph 生态里的 Deep Agents SDK。它不能证明“所有 deep agent 都必须使用 LangGraph”，也不能把 RUC-NLPIR 的 DeepAgent 论文/项目名并入 LangChain `deepagents`。

具体 API、包名、默认工具和推荐写法会随 LangChain / LangGraph 版本变化，因此保持 `freshness: volatile`。

## 外部链接

- Docs: <https://docs.langchain.com/oss/python/deepagents/overview>
- Products / layer concepts: <https://docs.langchain.com/oss/python/concepts/products>
- Repo: <https://github.com/langchain-ai/deepagents>
- Distinct project boundary: RUC-NLPIR DeepAgent <https://github.com/RUC-NLPIR/DeepAgent>
