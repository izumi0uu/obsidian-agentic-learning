---
type: source
source_type: docs
title: scikit-learn TF-IDF documentation
url: https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
author: scikit-learn developers
site: scikit-learn.org
topic:
  - rag
  - retrieval
  - sparse-retrieval
  - machine-learning
created: 2026-05-15
updated: 2026-05-15
last_checked: 2026-05-15
freshness: stable
conflicts: []
status: seed
source:
  - https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting
  - https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
related:
  - "[[TF-IDF]]"
  - "[[Embedding]]"
  - "[[Hybrid Search]]"
  - "[[Retriever]]"
---

# scikit-learn TF-IDF 文档

## 为什么收

TF-IDF 是理解稀疏检索、关键词检索、BM25 和 [[Hybrid Search]] 的基础概念。它能帮我把“向量化”切成两类：一类是词项权重形成的稀疏向量，另一类是 [[Embedding]] 形成的稠密语义向量。

## 一句话

scikit-learn 文档把 TF-IDF 描述为基于词频和逆文档频率的文本特征表示；`TfidfVectorizer` 把原始文档转换成 TF-IDF 特征矩阵。

## 需要我读的内容

### 必读块 1：TF-IDF 是什么

- 位置：User Guide / `7.2.3.4. Tf-idf term weighting`
- 原文短摘：
  > Tf means term-frequency while tf-idf means term-frequency times inverse document-frequency.
- 中文概括：
  - TF-IDF 的核心不是“语义理解”，而是给词项一个权重：在当前文档里出现得多，权重上升；在整个语料里太常见，权重下降。
- 支撑概念：
  - [[TF-IDF]]
  - [[Hybrid Search]]
- 证据边界：
  - 这是传统文本特征抽取 / sparse retrieval 的基础定义，不证明它在所有 RAG 任务中优于 dense embedding。

### 必读块 2：为什么不用原始词频

- 位置：User Guide / `7.2.3.4. Tf-idf term weighting`
- 原文短摘：
  > scale down the impact of tokens that occur very frequently
- 中文概括：
  - 只看词频会让“的、and、system”这类常见词影响过大；IDF 用全语料里的文档频率压低常见词，让更有区分度的词更突出。
- 支撑概念：
  - [[TF-IDF]]
  - [[Retriever]]
- 证据边界：
  - IDF 是相关性特征，不是事实校验；高权重词匹配不等于答案被证据支持。

### 必读块 3：TfidfVectorizer 的工程角色

- 位置：API Reference / `sklearn.feature_extraction.text.TfidfVectorizer`
- 原文短摘：
  > Convert a collection of raw documents to a matrix of TF-IDF features.
- 中文概括：
  - `TfidfVectorizer` 的输入是原始文档集合，输出是 TF-IDF 特征矩阵；文档被表示成词表维度上的稀疏数值向量。
- 支撑概念：
  - [[TF-IDF]]
  - [[Embedding]]
- 证据边界：
  - 这是 scikit-learn API 语义；不同搜索引擎、BM25 实现或 neural sparse retriever 会有不同权重公式和索引结构。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[TF-IDF]] | 区分稀疏词法向量和 dense embedding，补 [[Hybrid Search]] 的 sparse side | [[scikit-learn TF-IDF 文档#需要我读的内容]] | P1 |

## 边界提醒

- TF-IDF 是基础特征表示，不是现代 embedding 模型。
- 它适合解释关键词检索为什么能补足向量检索，但生产搜索常会使用 BM25、全文索引、稀疏神经检索或 hybrid search。
- 具体公式、归一化和 stop words/tokenization 参数属于实现细节；概念卡只沉淀稳定边界。
