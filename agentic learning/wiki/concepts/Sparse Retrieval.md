---
type: concept
topic:
  - rag
  - retrieval
  - search
status: growing
created: 2026-05-15
updated: 2026-05-15
last_checked: 2026-05-15
freshness: stable
conflicts: []
source:
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]"
  - "[[scikit-learn TF-IDF 文档]]"
  - "[[Hybrid Search]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#关键词检索：字面匹配，靠统计]]"
  - "[[scikit-learn TF-IDF 文档#为什么收]]"
  - "[[Hybrid Search#概念详解]]"
related:
  - "[[BM25]]"
  - "[[TF-IDF]]"
  - "[[Hybrid Search]]"
  - "[[Embedding]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
---

# Sparse Retrieval

## 一句话

Sparse Retrieval 是用稀疏词项表示或倒排索引来做检索的家族：它看重词面命中、词频、稀缺度和精确匹配，常见代表包括 [[BM25]]、[[TF-IDF]] 风格特征、全文检索和部分稀疏神经检索。

## 概念详解

Sparse Retrieval 的核心是：文本被表示成“很多维但大多数为 0”的词项空间。每个维度通常对应词、token、ngram 或搜索系统中的 term；一篇文档只在自己出现过的词项上有非零权重，所以叫 sparse。查询进入系统后，也会被切成词项，再用倒排索引或稀疏向量打分，找到词面上最相关的文档或 chunk。

它出现得比现代 dense [[Embedding]] 检索早，但在 RAG 里没有消失。原因很朴素：很多用户问题靠精确词面就能定位证据，例如产品型号、错误码、函数名、表字段、法规条款、人名、版本号和缩写。Dense retrieval 擅长语义相似，却可能把精确词看得不够重；sparse retrieval 正好能把这些字面信号抬起来。

[[BM25]] 是现代搜索引擎和 RAG 工程中最常见的 sparse retrieval 代表。[[TF-IDF]] 则更适合作为学习入口：它帮助理解词频、逆文档频率和稀疏词项权重，但不等于整个 sparse retrieval 家族。生产系统常把 sparse retrieval 和 dense retrieval 组合成 [[Hybrid Search]]，再用 RRF、权重融合、去重和 [[Reranking]] 控制最终上下文质量。

证据边界：xiaolinnote 的多路召回 source note 直接把“BM25 关键词检索”标为 Sparse Retrieval，并把它放在向量检索之外的第二路召回；scikit-learn TF-IDF source note 支持 TF-IDF 作为稀疏词项表示的基础定义；本卡把这些合并成 RAG 工程里的家族边界。

## 它解决什么问题

Sparse Retrieval 解决的是“只靠语义向量时，精确词面信号容易被稀释”的问题。

没有 sparse side 时，用户问 `ERR_CONNECTION_RESET`、`M4 Pro`、`LSTM`、`invoice_id` 或某个法规条款编号，dense retrieval 可能召回语义接近但没有精确证据的 chunk。Sparse retrieval 能优先命中包含这些词项的文档，让检索系统保住“字面上必须出现”的信号。

## 它不是什么

Sparse Retrieval 不是 [[TF-IDF]] 的别名。TF-IDF 是一种基础词项权重方法；sparse retrieval 是更大的检索家族。

Sparse Retrieval 也不是 [[BM25]] 的别名。BM25 是常见代表，但全文检索、倒排索引、传统关键词检索和稀疏神经检索也可以属于这个方向。

Sparse Retrieval 不是语义理解系统。它通常不理解同义词、改写、跨语言含义或隐含关系；这些盲区需要 [[Embedding]]、query rewrite、知识图谱或多路召回来补。

## 最小例子

```text
query: "M4 Pro 芯片参数"

sparse retrieval:
  tokenize -> ["M4", "Pro", "芯片", "参数"]
  inverted index / sparse scoring
  -> documents containing "M4 Pro" rank high

dense retrieval:
  query embedding -> semantic nearest chunks
  -> may find "Apple processor specs", but may miss exact "M4 Pro"
```

RAG 里常见组合：

```text
query
  -> dense retrieval top-k
  -> sparse retrieval / BM25 top-k
  -> merge with RRF
  -> rerank
  -> context
```

## 常见误解 / 风险

- 把 sparse retrieval 当成“旧技术”：它不是最会理解语义的检索方式，但在精确词、编号、代码和专有名词上仍然很实用。
- 把 sparse retrieval 等同于 TF-IDF：这样会错过 BM25、全文索引和现代搜索引擎的工程角色。
- 以为 sparse retrieval 不需要分词：中文、代码符号、大小写、停用词、ngram 和 tokenizer 都会直接影响召回。
- 只看词面命中：词重叠不代表文档真的能回答问题，后面仍然需要 rerank、引用和评估。
- 在 Hybrid Search 中直接相加分数：BM25 分数和向量相似度量纲不同，通常要用 RRF、归一化或二阶段排序。

## 边界细节

和 [[Embedding]] / dense retrieval 的边界：sparse retrieval 看词面和稀疏权重，dense retrieval 看语义空间距离。前者保精确匹配，后者补同义表达和语义相似。

和 [[BM25]] 的边界：BM25 是 sparse retrieval 的常见打分函数和工程代表；sparse retrieval 是家族名。

和 [[TF-IDF]] 的边界：TF-IDF 是理解 sparse vector 的基础表示；BM25 在其直觉上加入词频饱和和文档长度等修正，更常见于搜索引擎。

和 [[Hybrid Search]] 的边界：sparse retrieval 是一路检索信号；Hybrid Search 是把 sparse 与 dense 等多路信号合并的策略。

和 [[Reranking]] 的边界：sparse retrieval 负责召回或初排；reranking 在候选集合上重新判断相关性。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：稀疏词项、倒排索引、精确词面匹配和 dense retrieval 的互补关系很稳定。
- 现代吸收方式：生产 RAG 常通过 BM25 / full-text / search engine + vector retrieval 形成 hybrid search。
- 易变部分：具体 tokenizer、搜索引擎默认公式、稀疏神经检索模型、产品是否支持 hybrid search 会变化。

## 现代系统怎么吸收 Sparse Retrieval 的价值

现代 RAG 系统通常不会只靠 sparse retrieval，也不会只靠 dense retrieval。更常见的工程形态是：用 sparse retrieval 保住精确词、实体、编号和代码符号，用 dense retrieval 覆盖同义表达和语义近邻，再通过 RRF、去重、metadata / permission filter、rerank 和 evaluation 控制质量。

排错时也要把它单独看：如果失败样本集中在产品型号、错误码、字段名、人名或法规条款上，优先检查 sparse side 是否存在、分词是否正确、索引是否更新、BM25 候选是否被融合阶段压掉。

## 证据锚点

- Source: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]]
- Source: [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]
- Anchor: [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#关键词检索：字面匹配，靠统计]]
- Source: [[scikit-learn TF-IDF 文档]]
- Anchor: [[scikit-learn TF-IDF 文档#为什么收]]
- Related concept anchors: [[TF-IDF#概念详解]], [[BM25#概念详解]], [[Hybrid Search#概念详解]]
- Evidence type: raw RAG source notes + official-library TF-IDF source note + existing concept-card synthesis.
- Confidence: medium-high
- Boundary: 本卡记录 stable retrieval family boundary；不判断某个具体搜索产品、tokenizer 或 sparse neural retriever 的当前最优能力。

## 复习触发

1. 为什么 `M4 Pro`、错误码、函数名这类查询常需要 sparse retrieval？
2. Sparse Retrieval、[[BM25]]、[[TF-IDF]] 三者为什么不是同义词？
3. Sparse retrieval 和 dense retrieval 的盲区为什么适合放进 [[Hybrid Search]]？

## 相关链接

- [[BM25]]
- [[TF-IDF]]
- [[Embedding]]
- [[Hybrid Search]]
- [[Retriever]]
- [[Reranking]]
- [[RAG]]
