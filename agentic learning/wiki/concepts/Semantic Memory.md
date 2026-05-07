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
  - "[[LangGraph Memory 官方文档]]"
  - "[[Zep Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Zep Memory 官方文档#为什么收]]"
  - "[[Mem0 Memory 官方文档#为什么收]]"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Episodic Memory]]"
  - "[[RAG]]"
---

# Semantic Memory

## 一句话

Semantic Memory 保存相对稳定的事实、偏好、概念和关系。

## 它解决什么问题

Agent 需要知道“用户是谁、项目是什么、术语如何定义、某个偏好是否长期成立”。这些不是一次任务里的临时步骤，而是可在多个任务中复用的知识。

## 它不是什么

Semantic Memory 不是事件流水账。

“昨天我打开网页失败三次”更像 [[Episodic Memory]]；“用户偏好中文解释，并希望先讲边界”更像 semantic memory。

## 最小例子

在你的 vault 里：

- “[[Agent]] 是围绕目标行动的系统。”
- “用户对 Agent 和 Obsidian 从零开始。”
- “当前学习系统采用 raw/wiki/maps 三层。”

这些都适合成为 semantic memory。

## 常见误解 / 风险 / 边界细节

- 稳定事实也会过期。
- 用户偏好可能依场景变化。
- 语义记忆需要冲突解决，例如“用户现在想要详细解释”可能覆盖旧偏好。
- 语义记忆的来源应该可追溯。

## 证据锚点

- Source: [[LangGraph Memory 官方文档]]
- Source: [[Zep Memory 官方文档]]
- Source: [[Mem0 Memory 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Long-term Memory]]
- [[Episodic Memory]]
- [[Memory]]
- [[Obsidian + LLM Wiki]]
