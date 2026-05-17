---
type: source
source_type: docs
title: Letta Memory
url: https://docs.letta.com/guides/core-concepts/stateful-agents
author: Letta
site: docs.letta.com
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
  - "[[Memory Reflection]]"
  - "[[Tool Registry]]"
---

# Letta Memory 官方文档

## 为什么收

Letta 继承 MemGPT 的记忆层思想，强调 stateful agent、memory blocks、archival memory 和 agent 自我编辑记忆，适合理解“记忆不是普通 RAG”的边界。

## 一句话

Letta 把 Agent 视为能持久保存状态、维护记忆块、并通过工具编辑自己记忆的系统。

## 先读什么

- Introduction to Stateful Agents。
- Memory blocks。
- Archival memory。
- Context hierarchy。

## 可以拆成概念卡

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Memory Reflection]]

## 我的疑问

- Agent 自主改记忆时，如何避免写入错误事实？
- memory block 适合放用户偏好，还是也适合放项目状态？

## 边界提醒

Letta 的 memory block 更像“始终可见的结构化上下文”，archival memory 更像“按需检索的外部长期存储”。这两者不要混为一谈。
