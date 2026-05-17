---
type: source
source_type: docs
title: Mem0 Documentation
url: https://docs.mem0.ai/
author: Mem0
site: docs.mem0.ai
topic:
  - agent
  - memory
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
---

# Mem0 Memory 官方文档

## 为什么收

Mem0 是“memory layer for AI agents”的典型产品/开源项目线，适合观察生产化记忆层怎样处理用户、会话和 Agent 级记忆。

## 一句话

Mem0 提供面向 AI 应用和 Agent 的持久化、可检索记忆层。

## 先读什么

- Overview：理解 memory layer 的定位。
- Memory types：区分 user、agent、session memory。
- Integrations：看它如何接入 LangChain、CrewAI、Vercel AI SDK 等。

## 可以拆成概念卡

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]

## 我的疑问

- 记忆层如何判断哪些信息值得保存？
- 记忆层对隐私、删除、审计的支持是否足够产品化？

## 边界提醒

Mem0 是项目/产品，不等于“Agent memory”这个总概念。学习时要抽象出 memory write / search / update / delete 的通用能力。
