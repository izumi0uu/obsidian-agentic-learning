---
type: concept
topic:
  - rag
  - retrieval
  - evaluation
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[RAG Evaluation]]"
---

# Reranking

## 一句话

Reranking 是在初步检索后，用更精细的模型或规则重新排序候选上下文。

## 概念详解

Reranking 解决的是“召回到了，但顺序不够好”的问题。初步检索通常为了速度，会用向量相似度、关键词匹配或 hybrid search 找回一批候选；这批候选里可能包含真正有用的证据，也可能混入相似但不能回答问题的片段。Reranker 在较小候选集上重新判断 query 和 document 的相关性，把最可能回答问题的片段排到上下文预算前面。

在 RAG pipeline 中，reranking 位于 [[Retriever]] 之后、生成之前。典型流程是 retrieve top 50，再 rerank top 5 或 top 8。它可以使用 cross-encoder、LLM judge、规则、业务权重或混合策略。它的价值不是找更多资料，而是把“已经找回来的资料”排得更适合生成模型阅读。

Reranking 的边界很关键：如果初检没有召回正确证据，reranker 没法凭空创造证据；如果 chunk 太碎或 metadata 错误，reranker 也可能误判；如果评估只看最终答案，不看 rerank 前后的候选变化，就很难知道质量提升来自召回还是排序。

证据边界：[[RAG 类型对比]] 明确把 reranked RAG 和 hybrid RAG、GraphRAG 等区分开，强调它不是扩大召回；[[Agent 工程基础设施主源]] 支持 RAG 检索基础设施和评估工具是现代工程层。具体 reranker 模型和指标会快速变化，这里只沉淀流程位置和责任边界。


因此 reranking 是质量门的一部分，而不是召回层的替代品。

学习时可以把它看成“昂贵但更细的第二次排序”：先用便宜方法广撒网，再用更强判断把上下文预算留给最可能支撑答案的证据。
## 它解决什么问题

向量库返回的 top-k 不一定是最能回答问题的片段。Reranker 可以在较小候选集上做更精细的 query-document 相关性判断。

## 它不是什么

Reranking 不是扩大召回。

如果初检没有找回正确材料，reranker 只能在错误候选里重新排序。

## 最小例子

```text
retrieve top 50 -> rerank top 8 -> LLM answer
```

## 常见误解 / 风险

- reranker 会增加延迟和成本。
- reranker 指标好，不等于最终答案忠实。
- 多语言、代码、表格场景要单独评估。
- 如果初召回质量太差，reranking 很难救回来。

## 边界细节

和 [[Retriever]] 的边界：retriever 负责找候选；reranker 负责重排候选。工程系统可能把两者都叫 retrieval pipeline，但排错时必须拆开。

和 [[Hybrid Search]] 的边界：hybrid search 增加召回信号；reranking 提升候选排序。

和 [[RAG Evaluation]] 的边界：评估时要分别看 recall、rerank hit rate、answer faithfulness 和 citation accuracy。

## 现代性状态

- 判定：current-practice。
- 稳定部分：在初召回后精排候选，是生产 RAG 常见质量层。
- 易变部分：reranker 模型、LLM-as-reranker、评分指标、延迟成本权衡会变化。
- 复查点：上线前必须用目标语料评估，不要只看通用 benchmark。

## 现代系统怎么吸收 Reranking 的价值

现代 RAG 会把 rerank 前后的候选都写入 trace：哪些文档被召回、哪些被重排到前面、哪些进入最终上下文。这样当答案错误时，可以判断是初召回没命中、reranker 排错，还是 generator 忽略了正确证据。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: infrastructure source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 reranking 作为 RAG 检索质量层；具体 reranker 模型、阈值和指标是实现细节。

## 复习触发

- Reranking 为什么救不了“没有召回正确证据”的失败？
- rerank top 8 和 retrieve top 8 的区别是什么？
- 评估 reranker 时为什么还要看最终答案忠实性？

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Hybrid Search]]
- [[RAG Evaluation]]
