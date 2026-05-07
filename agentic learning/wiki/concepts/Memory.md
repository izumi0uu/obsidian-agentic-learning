---
type: concept
topic:
  - agent
  - memory
status: seed
created: 2026-05-05
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
related:
  - "[[Agent]]"
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
---

# Memory

## 一句话

Memory 是 Agent 保存和使用过去信息的机制。

## 它解决什么问题

没有记忆的 Agent 很难完成长期任务，也很难记住用户偏好、历史决策、项目状态和过去失败。

## 常见类型

- 短期记忆：当前上下文窗口里的信息。
- 长期记忆：保存到数据库、文件、向量库或知识图谱里的信息。
- 任务记忆：当前任务的步骤、状态、结果和待办。
- 用户记忆：用户偏好、习惯、约束和长期目标。

前沿 Agent 记忆系统通常还会区分：

- [[Semantic Memory]]：事实、偏好、概念。
- [[Episodic Memory]]：过去事件和任务轨迹。
- [[Long-term Memory]]：跨会话保存和调用记忆的总能力。

## 它不是什么

上下文窗口不是长期记忆。

RAG 也不等于完整记忆。RAG 更偏向检索知识，Memory 还包括状态、偏好和任务过程。

## 最小例子

如果我多次告诉学习 Agent：“我完全零基础，请先解释边界再讲实现”，它以后能自动用这种方式组织回答，这就是用户记忆的一种价值。

## 风险

- 记住错误信息。
- 记住过时偏好。
- 该忘的不忘。
- 隐私和权限不清楚。
- 检索到的记忆和当前任务不相关。

## 证据锚点

- Source: [[LangGraph Memory 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[RAG]]
- [[Evaluation]]
- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]
