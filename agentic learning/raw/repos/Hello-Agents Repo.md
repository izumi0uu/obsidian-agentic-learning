---
type: source
source_type: repo
title: "Hello-Agents: 从零开始构建智能体"
url: https://github.com/datawhalechina/hello-agents
author: Datawhale China
site: github.com
topic:
  - agent
  - learning-path
  - practice
created: 2026-05-06
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Memory]]"
  - "[[RAG]]"
  - "[[MCP]]"
  - "[[A2A]]"
  - "[[Evaluation]]"
  - "[[Context Engineering]]"
  - "[[GSSC Pipeline]]"
---

# Hello-Agents Repo

## 为什么收

Hello-Agents 是 Datawhale 的中文系统化 Agent 教程，定位是“从零开始构建智能体”。它适合作为当前 vault 的入门课程骨架，帮助把 [[Agent]]、[[Agent Loop]]、[[Tool Calling]]、[[Memory]]、[[RAG]]、[[MCP]]、[[A2A]] 和 [[Evaluation]] 串成连续学习路径。

截至 2026-05-06，它仍然活跃：GitHub API 显示最近 push 是 2026-05-02，最新 release 是 `V1.0.2`，发布日期为 2026-02-10；仓库约 42.7k stars、5.1k forks。

## 一句话

Hello-Agents 适合作为中文 Agent 系统入门和动手实践教材，但不应该替代论文、官方文档和协议规范。

## 先读什么

- 第 1 章：初识智能体，对应 [[Agent]]。
- 第 3 章：大语言模型基础，对应 [[LLM]]。
- 第 4 章：智能体经典范式构建，对应 [[ReAct]]、[[Agent Loop]]。
- 第 8 章：记忆与检索，对应 [[Memory]]、[[RAG]]。
- 第 9 章：上下文工程，对应 [[Context Engineering]] 和 [[GSSC Pipeline]]。
- 第 10 章：智能体通信协议，对应 [[MCP]]、[[A2A]]。
- 第 12 章：智能体性能评估，对应 [[Evaluation]]。

## 可以拆成概念卡

这份资料暂时不急着拆新卡，优先作为既有概念卡的补充例子：

- [[Agent]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Memory]]
- [[RAG]]
- [[Context Engineering]]
- [[GSSC Pipeline]]
- [[MCP]]
- [[A2A]]
- [[Evaluation]]

## 怎么用于复习

它更适合放进 [[资料收集索引]] 和 [[Agent 知识地图]] 之间，当作中文课程骨架来触发问题：

- 读第 1、3、4 章，补 [[Agent]]、[[Agent Loop]]、[[Tool Calling]] 的基础边界。
- 读第 8、12 章，补 [[Memory]]、[[RAG]] 和 [[Evaluation]]。
- 读第 9 章，补 [[Context Engineering]]、[[GSSC Pipeline]] 和长时程任务里的 context builder / note tool / terminal tool 组合。
- 读第 10 章，补 [[MCP]]、[[A2A]] 等协议线。
- 从综合案例中选一个最小项目，用费曼复述说明它为什么是 Agent，而不是普通 chatbot。

## 我的疑问

- 它的章节讲法和主源文档有哪些不一致？
- 它的代码案例适合我直接跑，还是更适合先当作结构参考？
- 第 10 章里的协议内容在 2026 是否需要用最新 MCP/A2A 官方文档校准？

## 边界提醒

它是“中文系统入门 + 实践教材”，不是“前沿事实主源”。

遇到 [[MCP]]、[[A2A]]、[[Self-RAG]]、[[Agentic Retrieval]]、[[Tool Poisoning]] 等快速变化概念时，要回到官方文档、论文和 OWASP/主项目仓库校准。

## 第九章上下文工程 / GSSC

- Chapter 9 raw page: <https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md>
- Chapter 9 English page: <https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter9/Chapter9-Context-Engineering.md>
- 关键事实：第九章把 `ContextBuilder` 写成实现 [[GSSC Pipeline|GSSC]] 的上下文构建器，并把 GSSC 展开为 Gather、Select、Structure、Compress 四个阶段。
- 学习价值：这给 [[Context Engineering]] 提供了一个可执行的工程骨架，能把“上下文工程”拆成候选信息汇集、信息选择、结构化组织和超预算压缩。
- 边界：GSSC 是 Hello-Agents / 教学实现中的 context builder pipeline，不应直接当成行业统一标准；写稳定概念卡时要保留“实践模式”而不是“协议/标准”的边界。
