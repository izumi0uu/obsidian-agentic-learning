---
type: concept
topic:
  - observability
  - evaluation
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Langfuse Observability and Evaluation#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Trace]]"
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Replay]]"
---

# Observability

## 一句话

Observability 是让 Agent 系统的输入、输出、工具调用、延迟、成本、错误和质量信号可观察、可调试、可追踪。

## 它解决什么问题

Agent 失败通常不是单点错误：可能是检索差、工具参数错、模型选择错、权限被拒、上下文污染、成本暴涨。Observability 让我们看到过程，而不是只看到最终答案。

## 它不是什么

Observability 不是普通日志。

普通日志只记录事件；Agent observability 还要把 LLM call、tool call、retrieval、span、trace、score、用户反馈和实验版本关联起来。

## 最小例子

一次 RAG Agent 回答错误，observability 可以显示：

- query rewrite 生成了错误子问题。
- retriever 返回了旧文档。
- reranker 把相关文档排到后面。
- 模型没有引用来源。

## 常见误解 / 风险 / 边界细节

- 记录越多越好是错的，敏感数据会进入 trace。
- 没有评分的 trace 只是可见，不等于可评估。
- 线上监控和离线 eval 应该互相反馈。
- 采样率、数据保留和脱敏是产品化边界。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Langfuse Observability and Evaluation]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Eval Harness]]
- [[Replay]]
- [[LLM-as-Judge]]
- [[Trajectory Evaluation]]
