---
type: concept
topic:
  - rag
  - retrieval
  - reranking
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - Cross-encoder
  - cross-encoder
  - 交叉编码器
source:
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第四层：Rerank 精排]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
up:
  - "[[Reranking]]"
relations:
  - type: contrasts_with
    target: "[[Dense Retrieval]]"
    note: "Dense Retrieval 常用双塔/bi-encoder 思路快速召回；Cross-Encoder 把 query 和 chunk 放在一起深度判断，适合小候选集精排。"
related:
  - "[[Reranking]]"
  - "[[Dense Retrieval]]"
  - "[[Retriever]]"
  - "[[RAG Evaluation]]"
---

# Cross-Encoder

## 一句话

Cross-Encoder 是一种把 query 和 candidate chunk 拼在一起输入模型、直接判断二者相关性的结构，常用于 RAG 的 rerank 精排阶段。

## 概念详解

在初召回阶段，系统通常需要在大量文档里快速找到候选，因此常用 [[Dense Retrieval]] 或 [[BM25]] 这类可索引、可并行的方式。Dense retrieval 常把 query 和 chunk 分开编码成向量，再用相似度比较；这很快，但模型在编码时没有同时看到 query 和 chunk 的逐词交互。

Cross-Encoder 反过来牺牲速度换精度：把 `query + chunk` 作为一对输入，让模型直接看这两个文本之间的关系，输出相关性分数。因为每个候选 chunk 都要单独跑一次模型，它不适合全库召回；但在 top-20、top-50 这类小候选集上做 [[Reranking]] 很合适。

source note 里用 Bi-encoder 与 Cross-encoder 对比解释 rerank：Bi-encoder 像先分别看两份简历再估计匹配度；Cross-encoder 像把两个人放在一起观察互动。这个类比的边界是：Cross-Encoder 更擅长细粒度相关性判断，但成本和延迟更高，不能替代初召回。

## 它解决什么问题

它解决“初召回候选已找到，但排序不够精细”的问题。向量相似度可能把表面相似但不能回答问题的 chunk 排前；Cross-Encoder 可以更细地判断 query 和 chunk 是否真正相关。

## 它不是什么

Cross-Encoder 不是 [[Retriever]] 的全部，也不是大规模向量召回的替代品。

它不是 [[Reranking]] 本身；Reranking 是流程位置，Cross-Encoder 是常见 reranker 模型结构之一。

它也不是答案生成器。它只给候选相关性打分，不负责生成最终回答。

## 最小例子

```text
候选集：retrieve top 50
for each chunk:
  score = cross_encoder("query [SEP] chunk")
按 score 排序 -> 取 top 5 放入上下文
```

## 常见误解 / 风险

- 用 Cross-Encoder 直接扫全库，成本不可控。
- 初召回没有正确证据时，Cross-Encoder 只能在错误候选里排序。
- reranker 分数提升不等于最终答案忠实；还要看 citation 和 RAG evaluation。
- 多语言、代码、表格场景需要单独评估模型适配性。

## 边界细节

和 [[Dense Retrieval]] 的边界：dense retrieval 优先速度和可索引；Cross-Encoder 优先相关性判断。

和 [[Reranking]] 的边界：Reranking 可以用 Cross-Encoder、LLM judge、规则或业务权重；Cross-Encoder 是其中一种常见实现。

和 [[Reciprocal Rank Fusion]] 的边界：RRF 先合并多路排序；Cross-Encoder 常在融合后的小候选集上精排。

## 现代性状态

- 判定：current-practice。
- 稳定部分：cross-encoder reranker 是 RAG 精排常见结构。
- 易变部分：具体模型、batching、延迟、量化和多语言能力变化快。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第四层：Rerank 精排]]
- [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]
- [[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]

## 复习触发

1. 为什么 Cross-Encoder 常用于 rerank 而不是全库召回？
2. Cross-Encoder 和 Dense Retrieval 的速度/精度交换是什么？
3. 初召回漏证据时，Cross-Encoder 为什么救不了？

## 相关链接

- [[Reranking]]
- [[Dense Retrieval]]
- [[Retriever]]
- [[Reciprocal Rank Fusion]]

