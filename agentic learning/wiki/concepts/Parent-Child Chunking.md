---
type: concept
topic:
  - rag
  - ingestion
  - retrieval
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - 父子切割
  - 父子 Chunking
  - Parent Child Chunking
  - Parent-Child 索引
  - 父子索引
source:
  - "[[raw/repos/xiaolinnote/questions/037 ai rag 4. RAG 中的文档是怎么存的？粒度是多大？详细说说文档切割（Chunking）策略？]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/037 ai rag 4. RAG 中的文档是怎么存的？粒度是多大？详细说说文档切割（Chunking）策略？#策略四：父子切割（Parent-Child Chunking）]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第一层：索引优化]]"
up:
  - "[[Chunking]]"
relations:
  - type: uses
    target: "[[Retriever]]"
    note: "检索时用子 chunk 精准定位，命中后回取父 chunk 给 LLM 阅读。"
  - type: mitigates
    target: "[[Context Precision]]"
    note: "子 chunk 帮助精确检索，父 chunk 帮助保留上下文；但是否改善 precision/recall 仍需评估。"
related:
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[Retriever]]"
  - "[[Dense Retrieval]]"
  - "[[Context Recall]]"
  - "[[Context Precision]]"
---

# Parent-Child Chunking

## 一句话

Parent-Child Chunking（父子切割）是在 RAG 中用小 chunk 做检索、命中后返回对应大 chunk 给 LLM 阅读的切分策略。

## 概念详解

RAG 的 chunk 粒度有一个经典矛盾：chunk 太大，检索不精准；chunk 太小，语义和上下文不完整。Parent-Child Chunking 试图同时保留两者优点：把同一份文档切成细粒度 child chunks 和较大 parent chunks。入库时通常给 child chunks 建向量索引；查询时先用 child chunk 精准匹配；命中后根据 `parent_id` 找回对应 parent chunk，把更完整上下文送给 LLM。

xiaolinnote source note 用“检索时用放大镜，返回时用全景图”解释这个策略。child chunk 聚焦某个小话题，便于向量检索定位；parent chunk 包含前后文、标题和限定条件，便于模型理解答案边界。这对长文档、章节结构明显或答案依赖上下文的资料尤其有价值。

它的代价也很明确：需要维护 parent-child 映射、存储可能增加、索引构建更复杂、去重和上下文预算更难。如果 parent chunk 过大，仍然可能把噪音带入上下文；如果 child chunk 切得不好，检索仍然找不到正确入口。因此它是 chunking 策略，不是 RAG 质量保险。

## 它解决什么问题

它解决检索精度和上下文完整性之间的张力：小 chunk 适合匹配，大片段适合阅读。

## 它不是什么

Parent-Child Chunking 不是普通 fixed-size chunking，也不是简单增大 chunk size。

它不是 [[Retriever]]，而是 retriever 使用的索引/切分组织方式。

它也不是 reranking；它改变候选 chunk 的组织和回取方式，reranking 改变候选排序。

## 最小例子

```text
parent chunk: 退款政策整节（1000 tokens）
child chunks:
  child A: 退款条件（200 tokens, parent_id=policy_1）
  child B: 到账时间（200 tokens, parent_id=policy_1）
  child C: 异常处理（200 tokens, parent_id=policy_1）

query 命中 child B -> 回取 parent policy_1 -> 放入上下文
```

## 常见误解 / 风险

- 只建 parent，不建 child，检索仍然粗。
- child 命中后返回过大的 parent，带来噪音和 token 成本。
- parent-child 映射或版本更新不同步，导致引用和上下文错位。
- 没有评估 Context Recall / Precision 就假设一定提升。

## 边界细节

和 [[Chunking]] 的边界：Parent-Child Chunking 是 chunking 的一种层级策略。

和 [[Dense Retrieval]] 的边界：child chunks 常用于向量检索，但也可以配合 sparse / hybrid route。

和 [[Context Recall]] / [[Context Precision]] 的边界：父子切割可能提升覆盖和上下文完整性，也可能引入噪音，必须用评估确认。

## 现代性状态

- 判定：current-practice。
- 稳定部分：小块检索、大块返回是 RAG 索引优化常见模式。
- 易变部分：chunk 大小、overlap、parent 选择、引用粒度和框架实现需要按资料类型调整。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/037 ai rag 4. RAG 中的文档是怎么存的？粒度是多大？详细说说文档切割（Chunking）策略？#策略四：父子切割（Parent-Child Chunking）]]
- [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第一层：索引优化]]

## 复习触发

1. 为什么 child chunk 适合检索，parent chunk 适合阅读？
2. Parent-Child Chunking 可能怎样引入噪音？
3. 它和简单调大 chunk size 的区别是什么？

## 相关链接

- [[Chunking]]
- [[Document Ingestion]]
- [[Retriever]]
- [[Dense Retrieval]]
- [[Context Recall]]
- [[Context Precision]]

