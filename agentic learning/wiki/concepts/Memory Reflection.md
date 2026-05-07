---
type: concept
topic:
  - memory
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Letta Memory 官方文档]]"
  - "[[LangGraph Memory 官方文档]]"
evidence:
  - "[[Letta Memory 官方文档#为什么收]]"
  - "[[LangGraph Memory 官方文档#为什么收]]"
related:
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
  - "[[Evaluation]]"
---

# Memory Reflection

## 一句话

Memory Reflection 是从历史对话、任务轨迹或事件记忆中总结出更稳定长期记忆的过程。

## 它解决什么问题

Agent 不能把每条历史都直接塞进长期记忆。Reflection 用来压缩、抽象和更新：哪些事实值得保留，哪些偏好反复出现，哪些失败模式需要变成规则。

## 它不是什么

Memory Reflection 不是“让模型想一想”。

它应该是有输入、触发条件、写入位置、审查机制和冲突处理的记忆维护流程。

## 最小例子

连续几次学习任务后，Agent 发现：

- 用户经常问“这不是什么”。
- 用户希望概念有最小例子。
- 用户不想只收资料，还要沉淀成卡片。

Reflection 可以把这些总结成用户学习偏好。

## 常见误解 / 风险 / 边界细节

- 总结错了会长期污染系统。
- 不应该把一次临时情绪写成长期偏好。
- 高敏信息不能因为“有用”就自动记住。
- 最好把 reflection 结果放入待确认区，而不是直接永久化。

## 证据锚点

- Source: [[Letta Memory 官方文档]]
- Source: [[LangGraph Memory 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Long-term Memory]]
- [[Episodic Memory]]
- [[Semantic Memory]]
