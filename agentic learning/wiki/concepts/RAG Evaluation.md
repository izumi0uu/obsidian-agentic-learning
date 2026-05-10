---
type: concept
topic:
  - rag
  - evaluation
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[LLM-as-Judge]]"
---

# RAG Evaluation

## 一句话

RAG Evaluation 是评估检索、上下文、引用和最终回答质量的一组方法。

## 它解决什么问题

RAG 系统失败可能发生在很多层：没检到、检错了、排序错了、上下文太脏、模型误读、引用不支持答案。只看最终回答很难定位问题。

代表工具包括 Ragas、DeepEval、Phoenix、Promptfoo 等。

## 它不是什么

RAG Evaluation 不是只问“答案对不对”。

它也不是只靠 LLM-as-Judge。关键任务需要人工样本、规则、引用校验和回归集。

## 现代性状态

RAG Evaluation 属于 current-practice。

现代系统通常把它拆成可独立评估的层：retrieval、context quality、answer faithfulness、citation accuracy、latency 和 cost。概念稳定，但平台、指标实现和 judge 组合会持续变化。

## 最小例子

```text
问题集 -> retrieve -> 检查 recall / context precision -> answer -> faithfulness / citation check
```

## 常见误解和风险

- judge 模型可能偏向流畅答案。
- 没有标准答案时，指标会更不稳定。
- 只评生成不评检索，会错过根因。

## 边界细节

- RAG Evaluation 评的是整条链路，不只是最终回答。
- 对检索问题，recall / precision / rerank 命中率常比 answer 分数更早暴露根因。
- 对引用问题，必须区分“答案像对了”与“证据真的支持”。
- 没有回归集的评测通常更像一次性诊断，不像稳定评测系统。

## 现代系统怎么吸收它的价值

- 把 retrieval 指标和 answer 指标分开看。
- 对失败样本做 dataset 化和回归测试。
- 用规则 + judge + 人审组合，避免只靠流畅度打分。
- 把引用校验、权限和上下文质量纳入同一评测闭环。

## 复习触发

- 为什么 RAG 评测不能只看最终答案？
- retrieval 指标和 answer faithfulness 各自暴露什么问题？
- 什么时候一个 RAG 系统需要人工样本和回归集，而不是只跑 judge？

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Evaluation]]
- [[Retriever]]
- [[Reranking]]
- [[LLM-as-Judge]]
