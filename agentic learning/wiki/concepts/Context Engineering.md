---
type: concept
topic:
  - llm
  - agent
  - rag
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Agent Harness]]"
---

# Context Engineering

## 一句话

Context Engineering 是设计进入模型上下文的信息结构、顺序、预算、来源和更新方式。

## 它解决什么问题

Agent 的表现不只取决于 prompt，还取决于它看到什么：系统指令、工具说明、用户目标、历史状态、检索材料、记忆、trace 摘要和安全约束。

## 它不是什么

Context Engineering 不只是 prompt engineering。

Prompt 更像写指令；context engineering 更像管理模型运行时能看到的整个信息环境。

## 最小例子

```text
system rules
-> task brief
-> current plan
-> selected memories
-> retrieved evidence
-> tool schemas
-> recent trace summary
```

## 常见误解和风险

- 上下文越多不一定越好。
- 无关资料会稀释注意力。
- 外部资料可能包含 prompt injection。
- 长上下文仍然需要结构和优先级。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[RAG]]
- [[Memory]]
- [[Agent Harness]]
