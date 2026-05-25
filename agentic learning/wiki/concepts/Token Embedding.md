---
type: concept
topic:
  - llm
  - transformer
status: growing
created: 2026-05-25
updated: 2026-05-25
last_checked: 2026-05-25
freshness: stable
conflicts: []
aliases:
  - token embedding
  - input embedding
  - 词嵌入
  - 输入嵌入
  - token 向量
source:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need]]"
  - "[[Attention Is All You Need]]"
  - "[[Token]]"
  - "[[Embedding]]"
evidence:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#输入、Token Embedding 与向量空间]]"
  - "[[Attention Is All You Need#Ingest 摘要]]"
  - "[[Token#概念详解]]"
  - "[[Embedding#边界细节]]"
related:
  - "[[Token]]"
  - "[[Embedding]]"
  - "[[Transformer]]"
  - "[[Positional Encoding]]"
  - "[[Self-Attention]]"
---

# Token Embedding

## 一句话

Token Embedding 是把离散 token ID 查表映射成模型内部向量表示的输入层，让 Transformer 可以对文本片段做矩阵计算。

## 概念详解

自然语言进入 Transformer 前，先会被 tokenizer 切成 [[Token]]，再变成整数 ID。模型不能直接计算“词”或“字”的字符含义；它实际拿到的是一串编号。Token embedding 层就是一个可训练的 embedding table：每个 token ID 对应表里一行向量，模型用 ID 去查到这行向量，然后把这个向量送进后续网络。最小流程是：文本片段 -> token -> token ID -> embedding table 的某一行 -> 连续向量。

这解释了“一个字、一个词是不是一串很长的数学向量”：更准确地说，是 tokenizer 产生的 token 会被映射成一个固定长度向量。视频里用 512 维解释原始 Transformer 的输入表示，这适合作为论文时代的具体例子，但不能当成 Transformer 的固定规则。现代模型可以是几百、几千甚至更高维；维度多，表示容量更大，但计算和显存成本也更高。

Token embedding 是训练出来的参数，不是人工提前写好的语义表。预训练开始时，这张表通常随机初始化；训练过程中，模型通过“预测下一个 token / 预测被遮住的 token”等目标，不断调整 embedding table、attention 层、FFN 层等所有参数。于是语义、语法、格式、代码符号和多语言模式会分布式地进入这些向量表示。

它和 RAG 里的 [[Embedding]] 容易混淆。RAG embedding 通常把 query 或 chunk 编码成一个检索向量，用来做语义搜索；token embedding 是 LLM 内部输入层，把单个 token ID 变成模型 block 能处理的表示。二者都叫 embedding，都是向量表示，但粒度、用途和生命周期不同。

Token embedding 也不是 Q/K/V 本身。Q/K/V 是注意力层对当前 token representation 做线性投影得到的三组向量；token embedding 是更早的输入表示。可以把它理解为“入场证”，Q/K/V 是进入 attention 计算后临时投影出的查询、匹配和内容通道。

## 它解决什么问题

它解决的是“离散 token 如何进入连续神经网络计算”的问题。没有 token embedding，Transformer 只能看到 token ID 这样的编号，无法在向量空间里做加法、点积、投影和 attention。

## 它不是什么

Token Embedding 不是 tokenizer。Tokenizer 决定文本怎么切成 token 和 ID；token embedding 把这些 ID 映射成向量。

它也不是 RAG 的 document embedding。RAG embedding 面向检索；token embedding 面向模型内部序列计算。

它更不是 Q/K/V。Q/K/V 是 attention 层里的投影结果，不是输入表的原始查表向量。

## 最小例子

```text
文本: "Paris"
tokenizer: "Paris" -> token_id = 12345
embedding table: row 12345 -> [0.12, -0.03, ..., 768 个数]
```

这串数字会继续加上位置相关信息，再进入 Transformer block。

如果沿用原始 Transformer 的教学例子，可以把最后一行想成 512 个数；换到现代具体模型时，要查看该模型配置，而不是默认所有模型都是 512 维。

## 常见误解 / 风险

- 把 token embedding 当成可读词典：单个维度通常不能直接命名为“性别”“城市”“语法”。
- 把 token embedding 和 RAG embedding 混成一件事：前者是模型内部参数，后者通常是外部检索系统产物。
- 以为 512 维是 Transformer 固定值：维度是架构超参数，不是 Transformer 规则。
- 以为 embedding 一次训练后永远准确表达事实：它承载的是训练中学到的统计表示，不是可审计知识库。

## 边界细节

和 [[Token]] 的边界：token 是离散单位 / ID；token embedding 是 ID 对应的连续向量。

和 [[Embedding]] 的边界：通用 embedding 卡主要记录 RAG / semantic search 的向量表示；Token Embedding 是 Transformer 输入侧的内部表示层。

和 [[Positional Encoding]] 的边界：token embedding 表示“这个 token 是什么”；position signal 表示“这个 token 在哪里”。原始 Transformer 把二者相加后再进入 attention。

和 [[Self-Attention]] 的边界：self-attention 在 token representation 之间计算关系；token embedding 只是这些 representation 的起点。

## 现代性状态

- 判定：foundation。
- 稳定部分：离散 token ID 需要映射到连续向量，才能进入 Transformer 计算。
- 易变部分：tokenizer、embedding 维度、是否共享输入/输出 embedding、位置表示方式、量化和压缩实现。
- 复查点：学习具体模型时，维度、tokenizer 和 embedding 共享策略要看该模型配置，不要从原始 Transformer 直接外推。

## 现代系统怎么吸收 Token Embedding 的价值

现代 LLM 系统一般不会直接暴露 token embedding 给应用层；应用层更常接触 tokenizer、token 预算、logits、RAG embedding 或向量数据库。理解 token embedding 的价值在于：它把“字/词/编号”与“模型内部向量计算”连接起来，也帮你区分为什么 RAG 的 embedding 模型和 LLM 内部 embedding table 不是同一个工程接口。

## 证据锚点

- Source: [[20分钟读懂AI神级论文 Attention Is All You Need]]
- Anchor: [[20分钟读懂AI神级论文 Attention Is All You Need#输入、Token Embedding 与向量空间]]
- Source: [[Attention Is All You Need]]
- Anchor: [[Attention Is All You Need#Ingest 摘要]]
- Supporting concepts: [[Token#概念详解]], [[Embedding#边界细节]]
- Evidence type: video source note + paper source note + existing concept boundary synthesis.
- Confidence: high for token-ID-to-vector boundary; medium for model-specific dimensions and implementation details.
- Boundary: 本卡只解释 LLM 内部 token ID -> vector lookup 的输入表示层，不把它扩展成 RAG document embedding、tokenizer 或 Q/K/V 投影。

## 复习触发

1. Token、token ID、token embedding 三者是什么关系？
2. Token Embedding 和 RAG 里的 Embedding 为什么不能混用？
3. Q/K/V 为什么不是输入 embedding 本身？

## 相关链接

- [[Token]]
- [[Embedding]]
- [[Transformer]]
- [[Positional Encoding]]
- [[Self-Attention]]
