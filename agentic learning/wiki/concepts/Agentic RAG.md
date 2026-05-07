---
type: concept
topic:
  - rag
  - agent
  - frontier
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
related:
  - "[[RAG]]"
  - "[[Agent]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
---

# Agentic RAG

## 一句话

Agentic RAG 是让 Agent 主动决定何时检索、检索什么、是否改写问题、是否重试和如何使用证据的 RAG 模式。

## 它解决什么问题

普通 RAG 往往是固定流程：问题进来，检索一次，生成答案。

复杂任务可能需要拆问题、多次检索、比较来源、判断证据是否足够、发现检索失败后重查。Agentic RAG 把这些决策交给 Agent 或图工作流。

## 它不是什么

Agentic RAG 不是“加一个 Agent”就自动变强。

如果没有评估、停止条件和证据引用，它可能只是更复杂、更不稳定的 RAG。

## 最小例子

用户问：“LangGraph 和 OpenAI Agents SDK 在 human-in-the-loop 上有什么区别？”

Agentic RAG 可能会：

1. 拆成两个子问题。
2. 分别检索 LangGraph 和 OpenAI 文档。
3. 判断证据是否足够。
4. 追加检索 guardrails 或 handoff。
5. 汇总对比。

## 边界细节

Agentic RAG 的核心不是检索，而是检索决策。

## 证据锚点

- Source: [[前沿主源清单]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Agent]]
- [[Planning]]
- [[Evaluation]]
