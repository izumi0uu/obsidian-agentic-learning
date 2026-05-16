---
type: concept
topic:
  - rag
  - retrieval
  - sparse-retrieval
  - machine-learning
status: growing
created: 2026-05-15
updated: 2026-05-16
last_checked: 2026-05-15
freshness: stable
conflicts: []
source:
  - "[[scikit-learn TF-IDF 文档]]"
  - "[[Hybrid Search]]"
  - "[[Embedding]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
evidence:
  - "[[scikit-learn TF-IDF 文档#必读块 1：TF-IDF 是什么]]"
  - "[[scikit-learn TF-IDF 文档#必读块 2：为什么不用原始词频]]"
  - "[[scikit-learn TF-IDF 文档#必读块 3：TfidfVectorizer 的工程角色]]"
  - "[[Hybrid Search#概念详解]]"
  - "[[Embedding#概念详解]]"
  - "[[Sparse Retrieval#边界细节]]"
  - "[[BM25#边界细节]]"
relations:
  - type: foundational_for
    target: "[[Sparse Retrieval]]"
    note: "TF-IDF 提供稀疏词项权重的基础直觉；Sparse Retrieval 是更大的检索家族。"
  - type: related_to
    target: "[[Multi-Route Retrieval]]"
    note: "多路召回可能通过 sparse retrieval / BM25 路线间接受益于 TF-IDF-style 词项权重；TF-IDF 本身不是召回路线或多路召回策略。"
related:
  - "[[Embedding]]"
  - "[[Hybrid Search]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Retriever]]"
  - "[[Top-K]]"
  - "[[Reranking]]"
  - "[[Vector Database]]"
---

# TF-IDF

## 一句话

TF-IDF 向量化是把文档表示成“词项权重”的稀疏向量：一个词在当前文档中越重要、在整个语料中越少见，它的权重通常越高。

## 概念详解

TF-IDF 的全名是 term frequency-inverse document frequency。它解决的是传统关键词检索里的一个基础问题：如果只按词出现次数打分，很多常见词会显得很重要，但它们对区分文档没什么帮助。TF-IDF 把两个信号相乘：TF 看一个词在当前文档里出现得多不多，IDF 看这个词在整个文档集合里常不常见。越能区分文档的词，权重越高；到处都出现的词，权重会被压低。

这也是为什么它叫“向量化”。系统先建立一个词表，每个维度对应一个词项；一篇文档会变成一个很长的向量，只有文档里出现过的词项维度有非零权重，所以它是 sparse vector。scikit-learn 的 `TfidfVectorizer` 就是把原始文档集合转换成 TF-IDF 特征矩阵。这个矩阵可以用于相似度搜索、分类、聚类或传统机器学习模型。

在 RAG 语境里，TF-IDF 的学习价值不是取代 [[Embedding]]，而是让你看懂 [[Sparse Retrieval]] 的底层直觉：关键词、实体名、错误码、函数名、法规条款编号这类词面信号，有时比语义相似更可靠。现代 [[Hybrid Search]] 会把 sparse side 和 dense side 组合起来：TF-IDF / [[BM25]] / 全文检索负责精确词面匹配，embedding 负责语义相近匹配，再用合并、去重、[[Reranking]] 和 [[RAG Evaluation]] 检查质量。

证据边界：scikit-learn 文档支持 TF-IDF 的定义和 `TfidfVectorizer` 的工程角色；本卡把它放进 RAG / hybrid search 是工程综合，用来解释稀疏检索和 dense embedding 的边界。

## 它解决什么问题

TF-IDF 解决“哪些词更能区分这篇文档”的问题。

没有 IDF 时，一个文档里高频出现的通用词可能主导相似度；有了 IDF，系统会降低全语料常见词的影响，把更稀有、更能定位主题的词抬高。对检索来说，这让“错误码 502”“OAuth callback”“Number One Observatory Circle”这类关键词更容易成为强信号。

## 它不是什么

TF-IDF 不是 dense [[Embedding]]。它不把语义压进一个连续语义空间，也不理解同义词、上下文关系或跨语言含义。

TF-IDF 也不是 [[Vector Database]]。它是一种文本特征表示或打分特征；向量库是存储和搜索向量的基础设施。一个搜索系统可以用 TF-IDF / BM25 的倒排索引，也可以用 embedding 的近似最近邻索引，还可以把两者组合成 [[Hybrid Search]]。

TF-IDF 不是 [[BM25]] 的同义词。BM25 可以看作从 TF-IDF 直觉发展出的更工程化相关性函数，额外考虑词频饱和、文档长度归一化等因素。学习时可以先用 TF-IDF 建直觉，再把 BM25 放到现代搜索实现层。

## 最小例子

假设有三篇文档：

```text
D1: password reset email
D2: password reset token
D3: system design interview
```

词 `password` 在 D1 和 D2 出现，说明它有检索价值；词 `reset` 也能区分 D1/D2；如果 `system` 在大量文档都出现，IDF 会降低它的权重。每篇文档最终会变成类似这样的稀疏向量：

```text
vocabulary = [password, reset, email, token, system, design, interview]
D1 = [w1, w2, w3, 0, 0, 0, 0]
D2 = [w1, w2, 0, w4, 0, 0, 0]
D3 = [0, 0, 0, 0, w5, w6, w7]
```

这里的 `w` 就是词项权重，不是神经网络 embedding 坐标。

## 常见误解 / 风险

- 把 TF-IDF 向量误认为 embedding：二者都叫向量，但一个是词表维度上的稀疏权重，一个是模型学习出来的稠密语义表示。
- 以为 TF-IDF 已经过时：它不是最强现代检索方法，但它的词面匹配直觉仍然支撑关键词检索、BM25 和 hybrid search 的学习边界。
- 只看高 TF 不看 IDF：出现次数多不等于有区分度；常见词需要降权。
- 以为 sparse retrieval 能理解语义：同义词、改写、跨语言和隐含关系通常需要 embedding、query rewrite 或知识结构补充。
- 忽略 tokenization：中文分词、大小写、停用词、词干化、符号处理会直接影响 TF-IDF 特征。

## 边界细节

和 [[Embedding]] 的边界：TF-IDF 是词法/统计表示，embedding 是神经语义表示。TF-IDF 擅长精确词面匹配，embedding 擅长语义相似。

和 [[Hybrid Search]] 的边界：TF-IDF 是 hybrid search 可能使用的一类 sparse signal；Hybrid Search 是把 sparse 和 dense 检索信号融合的整体策略。

和 [[Top-K]] 的边界：TF-IDF 给文档或 chunk 打相关性分数；Top-K 决定只保留分数最高的 K 个候选。

和 [[Reranking]] 的边界：TF-IDF 常用于初召回或传统排序；reranker 在候选集上做更精细的二阶段排序。

和 [[Sparse Retrieval]] 的边界：Sparse Retrieval 是词法/稀疏检索家族，TF-IDF 是其中的基础表示直觉，不等于整个家族。

和 [[BM25]] 的边界：BM25 延续 TF-IDF 的词频/逆文档频率直觉，但加入词频饱和和长度归一化，更常见于搜索引擎。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：TF、IDF、稀疏词项向量和关键词检索直觉是基础概念。
- 现代吸收方式：生产 RAG 更常直接说 [[BM25]]、全文检索、[[Sparse Retrieval]] 或 hybrid search，但这些说法背后的学习入口仍然是 TF-IDF。
- 易变部分：具体分词器、公式平滑、归一化、搜索引擎实现和稀疏神经模型会变。

## 现代系统怎么吸收 TF-IDF 的价值

现代 RAG 系统通常不把 TF-IDF 当成唯一检索方式，而是吸收它的词面匹配价值：当 query 里有实体名、编号、错误码、字段名、函数名、法规条款、产品型号时，稀疏检索能给出 dense embedding 容易漏掉的强信号。

工程上更常见的形态是：全文/BM25 召回 + 向量召回并行，合并去重后再 rerank。TF-IDF 在这里的价值是帮助你理解为什么“纯向量检索”不是万能，也理解为什么 hybrid search 的 sparse side 对生产 RAG 很重要。

## 证据锚点

- Source: [[scikit-learn TF-IDF 文档]]
- Anchor: [[scikit-learn TF-IDF 文档#必读块 1：TF-IDF 是什么]]
- Anchor: [[scikit-learn TF-IDF 文档#必读块 2：为什么不用原始词频]]
- Anchor: [[scikit-learn TF-IDF 文档#必读块 3：TfidfVectorizer 的工程角色]]
- Related concept anchors: [[Embedding#概念详解]], [[Hybrid Search#概念详解]], [[Reranking#概念详解]], [[Top-K#概念详解]]
- Related sparse retrieval anchors: [[Sparse Retrieval#概念详解]], [[BM25#概念详解]]
- Evidence type: official scikit-learn docs + existing RAG concept cards + engineering synthesis.
- Confidence: high for TF-IDF definition; medium-high for RAG / hybrid search placement.
- Boundary: 本卡不声称 TF-IDF 是现代 RAG 的默认最优检索算法；它是理解 sparse retrieval 和 hybrid search 的基础表示。

## 复习触发

1. TF、IDF 分别在压制什么错误信号？
2. 为什么 TF-IDF 向量是 sparse vector，而 embedding 通常是 dense vector？
3. 用户问题包含错误码、函数名或合同条款编号时，为什么 pure embedding retrieval 可能不如 sparse retrieval 稳？
4. TF-IDF、BM25、Hybrid Search、Reranking 分别在 retrieval 链路的哪一层？

## 相关链接

- [[Embedding]]
- [[Hybrid Search]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Retriever]]
- [[Top-K]]
- [[Reranking]]
- [[Vector Database]]
- [[RAG]]
