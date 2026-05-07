---
type: concept
topic:
  - evaluation
  - observability
  - frontier
status: seed
created: 2026-05-05
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Reasoning Trace]]"
  - "[[Observability]]"
  - "[[Replay]]"
---

# Trace

## 一句话

Trace 是记录 Agent 执行过程的轨迹，包括输入、模型输出、工具调用、工具结果、状态变化和最终结果。

## 它解决什么问题

Agent 失败时，单看最终答案很难知道哪里错了。Trace 让我们能看到每一步，定位是计划错、工具错、检索错、权限错还是模型解释错。

## 它不是什么

Trace 不是日志的简单堆积。

好的 trace 应该能支持调试、重放、评测和成本/延迟分析。

[[Reasoning Trace]] 是 trace 的一种子类型。它关注模型显式写出的推理过程；完整 trace 还应该包括工具调用、工具结果、状态变化和最终结果。

## 最小例子

一个 RAG Agent 的 trace 可能包括：

1. 用户问题。
2. query rewrite。
3. 检索请求。
4. 返回的文档片段。
5. rerank 结果。
6. 生成答案。
7. 引用来源。

## 边界细节

Trace 是 observability 的基础，也是 eval harness 复现失败的重要材料。

一个实用边界：trace 记录“发生了什么”，score/eval 才判断“好不好”。不要把完整 trace 等同于质量评估。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Source: [[LangSmith Evaluation and Observability]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Evaluation]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Observability]]
- [[Replay]]
