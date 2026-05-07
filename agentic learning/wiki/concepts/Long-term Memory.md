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
  - "[[Letta Memory 官方文档]]"
  - "[[Zep Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Letta Memory 官方文档#为什么收]]"
  - "[[Zep Memory 官方文档#为什么收]]"
related:
  - "[[Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
  - "[[RAG]]"
---

# Long-term Memory

## 一句话

Long-term Memory 是 Agent 跨会话保存和重新使用信息的能力。

## 它解决什么问题

没有长期记忆，Agent 每次对话都像第一次见你。它无法稳定记住用户偏好、项目状态、历史决策、失败经验或长期目标。

长期记忆让 Agent 能把重要信息写入外部存储，在未来任务中检索并使用。

## 它不是什么

长期记忆不是上下文窗口。

它也不只是聊天记录归档。真正有用的长期记忆要解决写入、检索、更新、冲突、过期、删除、权限和来源问题。

## 最小例子

你多次强调：“学习 Agent 时先讲边界，再讲实现。”

Agent 把这条偏好写入用户记忆。之后你问 [[MCP]]，它会先说明 MCP 不是 Agent 框架，再讲工具连接协议。

## 常见误解 / 风险 / 边界细节

- 记住越多不一定越好，旧信息会污染新任务。
- 错误记忆比没记忆更危险。
- 用户记忆、项目记忆、任务记忆需要分开。
- 记忆必须能被删除、审计和解释来源。

## 证据锚点

- Source: [[LangGraph Memory 官方文档]]
- Source: [[Letta Memory 官方文档]]
- Source: [[Zep Memory 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]
- [[Memory Reflection]]
- [[RAG]]
