---
type: source
source_type: docs
title: "Zep Memory"
url: "https://help.getzep.com/v2/memory"
author: Zep
site: help.getzep.com
topic:
  - agent
  - memory
  - graph
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
  - "[[GraphRAG]]"
---

# Zep Memory 官方文档

## 为什么收

Zep 是 Agent memory store 的代表之一，强调从 chat history 构建用户级知识图谱，并通过 Memory API 或 Graph API 取回上下文。

## 一句话

Zep 把 Agent memory 做成可写入、可检索、可图谱化的外部记忆层。

## 先读什么

- Memory API：如何 add / retrieve memory。
- Graph API：如何处理 JSON、非结构文本和图谱记忆。

## 可以拆成概念卡

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[GraphRAG]]

## 我的疑问

- 什么时候应该用图记忆，而不是向量记忆？
- 记忆图里的事实过期后如何修正？

## 边界提醒

图记忆并不天然正确。它更容易表达实体关系，但仍然需要事实来源、冲突处理和更新策略。
