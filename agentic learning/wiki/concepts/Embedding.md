---
type: concept
topic:
  - rag
  - llm
status: growing
created: 2026-05-06
updated: 2026-05-24
last_checked: 2026-05-10
freshness: stable
conflicts: []
aliases:
  - Embeddings
  - 嵌入
  - 向量表示
  - 嵌入模型
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[TF-IDF]]"
  - "[[AI Engineering From Scratch - Embeddings]]"
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]"
  - "[[TF-IDF#边界细节]]"
  - "[[AI Engineering From Scratch - Embeddings#关键事实]]"
  - "[[AI Engineering From Scratch - Embeddings#边界提醒]]"
related:
  - "[[RAG]]"
  - "[[Vector Database]]"
  - "[[Retriever]]"
  - "[[Chunking]]"
  - "[[TF-IDF]]"
  - "[[Semantic Search]]"
  - "[[Dense Retrieval]]"
  - "[[L2 Normalization]]"
  - "[[Vector Similarity Metrics]]"
  - "[[Matryoshka Embeddings]]"
  - "[[Embedding Quantization]]"
  - "[[MTEB]]"
---

# Embedding

## 一句话

Embedding 是把文本、图片或其他对象转换成向量表示，让系统可以用距离或相似度计算“语义接近”。

## 概念详解

Embedding 把离散的内容映射到连续向量空间。对 RAG 来说，它的价值在于：用户问题和文档原文经常不是同一组词，但它们可能表达相近含义。[[AI Engineering From Scratch - Embeddings]] 把这个问题称为 vocabulary mismatch：query 和文档语义相关，却没有共享足够词面。把问题和 chunk 都变成向量后，系统可以用相似度搜索找到“意思接近”的资料，而不是只依赖关键词完全匹配。

这里的向量通常是 dense vector representation：几百到几千个数字共同表示语义方向，大多数维度都可能携带信息。维度是向量长度，不是 token 数，也不是可以逐个命名的人工语义标签。它和 [[TF-IDF]] / bag-of-words 这类 sparse representation 的区别在于：sparse vector 的维度往往对应词表项，主要表达词面统计；embedding 的维度是模型训练出的连续表示，主要用于语义相似、聚类、分类或检索。

在 RAG pipeline 里，embedding 通常发生两次：入库时，对每个 chunk 生成向量并写入 [[Vector Database]] 或向量索引；查询时，对用户问题或改写后的 query 生成向量，再做 top-k 检索。经典 RAG 论文的 dense vector index 和 top-k retrieval 支持这一类语义检索边界；现代基础设施 source note 则说明向量数据库、搜索引擎和评测工具已经把 embedding 检索作为基础工程层处理。

Embedding 的关键边界是：相似不等于正确。两个文本向量接近，只说明模型在训练空间里认为它们语义相关，不说明 retrieved chunk 一定回答了问题，也不说明资料可信、最新或有权限。领域术语、代码符号、编号、错误码、短实体名和多语言文本都可能让纯向量检索失败，因此生产系统常把 embedding 检索和关键词/全文检索组成 [[Hybrid Search]]，再用 [[Reranking]] 提升排序质量。

Embedding 也不是“理解本身”。它是检索和聚类的表示层，不负责事实验证、权限控制、引用检查或答案生成。一个好的 embedding 模型能提高召回，但如果 [[Chunking]] 破坏上下文、metadata 丢失、索引过期，embedding 仍会把错误或不完整的片段送给模型。

证据边界：source notes 支持 RAG 使用 dense retrieval / vector index 和现代向量检索基础设施；Embeddings lesson 支持 vocabulary mismatch、dense vector、相似度度量、ANN / HNSW、维度截短、量化和 MTEB 的工程边界。不同 embedding 模型的维度、训练数据、跨语言能力、价格、MTEB 排名和 API 性能属于易变实现细节，不写成稳定定义。

## 它解决什么问题

用户的问题和文档原文不一定用同样措辞。Embedding 让系统能找“意思相近”的片段，而不只找关键词完全匹配。

## 它不是什么

Embedding 不是理解本身，也不是事实验证。

两个文本向量相似，只表示模型认为它们语义接近，不表示检索结果一定能回答问题。

## 最小例子

```text
"如何重置密码？" -> [0.12, -0.04, ...]
"忘记密码怎么办？" -> [0.11, -0.05, ...]
```

这两个向量距离近，所以可以被语义检索匹配到。

## 常见误解 / 风险

- 模型、语言、领域不同，embedding 质量会变。
- 长文档直接 embedding 可能稀释重点，所以需要 [[Chunking]]。
- embedding 不处理权限、时效和事实可靠性。
- 纯语义相似会漏掉产品编号、函数名、错误码等精确匹配需求。

## 边界细节

和 [[Vector Database]] 的边界：embedding 是表示；vector database 是存储和搜索这些表示的系统。

和 [[L2 Normalization]] 的边界：embedding 生成语义向量；L2 normalization 只把已有向量缩放到单位长度，让相似度比较更关注方向。

和 [[Vector Similarity Metrics]] 的边界：embedding 生成向量；cosine similarity、dot product 和 Euclidean / L2 distance 决定如何比较向量。

和 [[Hybrid Search]] 的边界：embedding 检索偏语义；hybrid search 把语义检索和关键词/全文检索结合起来。

和 [[TF-IDF]] 的边界：TF-IDF 是词表维度上的稀疏词项权重，擅长精确词面匹配；embedding 是模型学习出的稠密语义表示，擅长语义相似。

和 [[Reranking]] 的边界：embedding 常用于初召回；reranker 在较小候选集上做更精细的相关性排序。

和 [[Matryoshka Embeddings]] / [[Embedding Quantization]] 的边界：后两者是 embedding 向量的成本优化方式。Matryoshka 改“用多少维”；quantization 改“每一维用多少精度 / bit 表示”。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：用向量表示语义相似，并作为 RAG 检索基础。
- 易变部分：具体 embedding 模型、维度、价格、跨语言能力、多模态能力和供应商 API。
- 复查点：更换 embedding 模型时，需要重新跑检索评测，而不是只看模型宣传。

## 现代系统怎么吸收 Embedding 的价值

现代 RAG 通常把 embedding 当作召回层之一，而不是唯一判断层。它会配合 chunk metadata、hybrid search、rerank、权限过滤和评测集。对代码、法律、医疗、产品文档等场景，embedding 的结果必须和关键词、结构化过滤或人工标注样本一起验证。

模型选型时，[[MTEB]] 可以作为通用 benchmark 初筛，但不能替代业务 query / corpus 上的 retrieval evaluation。上线前更重要的是固定测试集、召回指标、长尾 query、专业术语、延迟、成本和索引版本。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]
- Source: [[AI Engineering From Scratch - Embeddings]]
- Anchors: [[AI Engineering From Scratch - Embeddings#关键事实]], [[AI Engineering From Scratch - Embeddings#边界提醒]]
- Evidence type: paper source note + infrastructure source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 dense retrieval / vector index 的 RAG 角色；embedding 模型能力和具体 API 是实现细节，需要按当前模型复查。

## 复习触发

- 为什么 embedding 相似不等于答案正确？
- 什么时候纯向量检索会输给关键词检索？
- embedding、vector database、retriever 三者分别负责什么？
- 为什么 L2 normalized embedding 的 dot product 可以按 cosine similarity 理解？

## 相关链接

- [[RAG]]
- [[Vector Database]]
- [[Retriever]]
- [[Chunking]]
- [[TF-IDF]]
- [[L2 Normalization]]
- [[Vector Similarity Metrics]]
- [[Semantic Search]]
- [[Matryoshka Embeddings]]
- [[Embedding Quantization]]
- [[MTEB]]
