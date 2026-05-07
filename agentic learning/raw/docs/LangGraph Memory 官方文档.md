---
type: source
source_type: docs
title: "LangGraph Memory"
url: "https://docs.langchain.com/oss/python/concepts/memory"
author: LangChain
site: docs.langchain.com
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
  - "[[Memory]]"
---

# LangGraph Memory 官方文档

## 为什么收

这份文档把 Agent memory 分成 thread-scoped short-term memory 和跨会话 long-term memory，并明确借用 semantic、episodic、procedural memory 的分类，是整理记忆系统概念的稳定来源。

## 一句话

LangGraph memory 关注 Agent 如何在有限上下文之外保存、检索和更新长期信息。

## 先读什么

- Long-term memory：跨会话保存信息。
- Semantic memory：事实、偏好、概念。
- Episodic memory：过去事件、行动轨迹、示例经验。

## 可以拆成概念卡

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]

## 我的疑问

- 记忆更新应该发生在回复前的 hot path，还是后台异步整理？
- 记忆冲突和遗忘策略应该由框架处理，还是由业务系统处理？

## 边界提醒

“长期记忆”不是把聊天记录无限塞回上下文，而是要有写入、检索、更新、冲突处理和权限边界。
