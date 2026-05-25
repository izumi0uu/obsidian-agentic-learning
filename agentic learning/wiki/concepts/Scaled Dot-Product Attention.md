---
type: concept
topic:
  - llm
  - transformer
  - math
status: growing
created: 2026-05-25
updated: 2026-05-25
last_checked: 2026-05-25
freshness: stable
conflicts: []
aliases:
  - scaled dot-product attention
  - 缩放点积注意力
  - 缩放点乘注意力
  - QK attention
source:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need]]"
  - "[[Attention Is All You Need]]"
evidence:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Linear、Softmax 与 Scaled Dot-Product Attention]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Self-Attention 与 Q / K / V]]"
  - "[[Attention Is All You Need#需要我读的内容]]"
related:
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Vector Similarity Metrics]]"
  - "[[L2 Normalization]]"
---

# Scaled Dot-Product Attention

## 一句话

Scaled Dot-Product Attention 是 Transformer 里用 Q 和 K 的点积计算注意力分数、按维度缩放后 softmax、再加权汇总 V 的基础 attention 公式。

## 概念详解

Self-attention 需要回答一个计算问题：当前 token 应该从哪些 token 吸收多少信息。Transformer 把每个 token representation 投影成 Query、Key、Value。Query 表示“我在找什么”，Key 表示“我能被怎样匹配”，Value 表示“如果被关注，我提供什么内容”。

Scaled Dot-Product Attention 的核心公式可以写成：

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

`QK^T` 的每个元素来自一个 query 向量和一个 key 向量的 dot product。点积越大，通常表示这两个向量在当前投影空间里越匹配。除以 `sqrt(d_k)` 是缩放：当 key/query 维度较大时，未经缩放的点积数值容易变大，softmax 可能进入梯度很小的区域；缩放让分数尺度更稳定。softmax 把这些分数变成权重，再乘以 V，得到当前 token 汇总上下文后的表示。

口头复述时可以把公式链压成一句话：先用 `QK^T` 算“谁和谁匹配”，再除以 `sqrt(d_k)` 稳定分数尺度，然后用 softmax 把分数变成权重，最后乘以 `V` 汇总真正要带回来的内容。也就是 `QK^T / sqrt(d_k) -> softmax -> V`。

这里的 dot product 和 RAG 检索里的 [[Vector Similarity Metrics]] 相邻但不等同。二者都用向量几何比较，但 attention 里的 Q/K 是模型内部临时投影，目标是生成每个 token 的上下文表示；RAG 里的 dot product / cosine 通常比较 query embedding 和 document embedding，目标是排序候选资料。不要把 attention 分数直接当成检索相关性或事实置信度。

它和 [[Multi-Head Attention]] 的关系是“计算核 vs 组合层”。Scaled Dot-Product Attention 是一个 head 里的 attention 计算形式；multi-head attention 是把多组投影后的 attention head 并行运行、拼接并投影回模型维度的层结构。

## 它解决什么问题

它解决的是“如何把 Q/K 的匹配关系变成可归一化的注意力权重，并用这些权重汇总 V”的问题。

## 它不是什么

它不是完整 Transformer。Transformer 还包括 embedding、position signal、multi-head 组合、FFN、残差、归一化和输出层。

它也不是 [[Vector Similarity Metrics]] 这张卡里的 RAG 检索配置。attention 内部的点积不是外部向量库的检索 metric。

它更不是事实解释。注意力权重可以帮助观察模型内部信号，但不能直接证明模型为什么给出某个最终答案。

## 最小例子

```text
query("它") · key("书") = 8.1
query("它") · key("桌子") = 2.4

softmax 后，"书" 获得更高权重。
输出表示 = 高权重 * value("书") + 低权重 * value("桌子") + ...
```

这个例子只说明 attention 的匹配直觉，不表示真实模型中某个 head 一定按这个人类标签工作。

公式复述可以对应到这一步：`QK^T` 产生“它”和候选词的匹配分数，`/ sqrt(d_k)` 防止分数尺度过大，softmax 变成权重，最后对各个候选词的 `V` 做加权求和。

## 常见误解 / 风险

- 把 `QK^T` 理解成普通字符串匹配：它比较的是投影后的向量，不是词面相同。
- 忽略 `/ sqrt(d_k)`：缩放不是装饰，而是为了让 softmax 分数尺度更稳定。
- 把 attention dot product 和 cosine similarity 混用：除非有归一化条件，否则点积会受向量长度影响。
- 把注意力权重当可审计推理理由：它是内部计算信号，不是完整因果解释。

## 边界细节

和 [[Self-Attention]] 的边界：self-attention 是同一序列内部互相关注的机制；scaled dot-product attention 是其中一种具体打分和汇总公式。

和 [[Multi-Head Attention]] 的边界：multi-head attention 并行运行多组 attention head；每个 head 内部通常使用 scaled dot-product attention。

和 [[Vector Similarity Metrics]] 的边界：二者都涉及点积，但一个在模型内部 attention 里，一个在外部检索 / 相似度排序里。

和 [[L2 Normalization]] 的边界：L2 normalization 可以让两个单位向量的 dot product 按 cosine 理解；Transformer attention 的 Q/K 缩放不等于对 Q/K 做 L2 normalize。

## 现代性状态

- 判定：foundation。
- 稳定部分：`QK^T / sqrt(d_k) -> softmax -> V` 是理解 Transformer attention 的核心公式。
- 易变部分：现代 attention 实现可能加入 FlashAttention、GQA/MQA、sliding window、block attention、RoPE 等工程优化或变体。
- 复查点：学习 serving / 长上下文优化时，要区分 attention 数学公式、attention kernel 性能优化和 KV cache 内存管理。

## 现代系统怎么吸收 Scaled Dot-Product Attention 的价值

应用层通常不会手写这个公式，但它解释了为什么 attention 可以并行矩阵化，也解释了 Q/K/V、multi-head、KV cache 和长上下文成本之间的关系。工程上更常接触的是推理框架、attention kernel、KV cache 和上下文预算；概念上先抓住这个公式，才能理解后续优化到底在优化什么。

## 证据锚点

- Source: [[20分钟读懂AI神级论文 Attention Is All You Need]]
- Anchors: [[20分钟读懂AI神级论文 Attention Is All You Need#Linear、Softmax 与 Scaled Dot-Product Attention]], [[20分钟读懂AI神级论文 Attention Is All You Need#Self-Attention 与 Q / K / V]]
- Source: [[Attention Is All You Need]]
- Anchor: [[Attention Is All You Need#需要我读的内容]]
- Evidence type: video source note + Transformer paper source note + mathematical mechanism synthesis.
- Confidence: high for formula boundary; medium for simplified examples.
- Boundary: 本卡只记录 Transformer attention head 内部的 Q/K/V 打分与汇总公式，不把 generic dot product、RAG 相似度 metric 或 attention kernel 优化混成同一概念。

## 复习触发

1. `QK^T`、`sqrt(d_k)`、softmax、`V` 分别承担什么作用？
2. Scaled Dot-Product Attention 和 Multi-Head Attention 的关系是什么？
3. 为什么 attention 里的 dot product 不等同于 RAG 向量检索的相似度配置？

## 相关链接

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Vector Similarity Metrics]]
- [[L2 Normalization]]
