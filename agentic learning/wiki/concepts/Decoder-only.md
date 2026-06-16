---
type: concept
topic:
  - llm
  - transformer
  - inference
status: growing
created: 2026-06-08
updated: 2026-06-08
last_checked: 2026-06-08
freshness: stable
conflicts: []
aliases:
  - decoder only
  - Decoder Only
  - decoder-only transformer
  - 仅解码器
  - 仅解码器架构
  - 自回归解码器架构
source:
  - "[[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？]]"
  - "[[补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系]]"
evidence:
  - "[[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#Encoder-only、Decoder-only 和 Encoder-Decoder 三种架构]]"
  - "[[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#为什么 Decoder-only 赢了]]"
  - "[[补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系#2.10 Bert模型与现在大语言模型LLM的区别?]]"
related:
  - "[[Transformer]]"
  - "[[Encoder-only]]"
  - "[[Encoder-Decoder]]"
  - "[[Masked Attention]]"
  - "[[KV Cache]]"
  - "[[LLM]]"
  - "[[LLM 基础结构对比]]"
---

# Decoder-only

## 一句话

Decoder-only 是只保留 Transformer decoder 侧、自回归地根据前缀预测下一个 token 的架构变体。

## 概念详解

理解 Decoder-only 的关键，不是“它负责输出”这种字面印象，而是它的信息流方向和训练目标。它在 attention 里使用 causal mask，当前位置只能看见自己和之前的 token，不能提前看到未来答案；训练时则用 next-token prediction，也就是 CLM（causal language modeling）目标，让模型不断学习“给定前缀，下一步最可能是什么”。

这种设计把大量看起来不同的任务压成一个统一接口。问答、写作、代码补全、翻译、推理和对话，都可以重新表述成“继续生成后面的 token”。因此 Decoder-only 特别适合在海量无标注文本上做大规模自监督训练，再通过 instruction tuning、preference optimization、tool use 和 RAG 把续写能力吸收到更复杂的产品行为里。

它和 [[Masked Attention]]、[[KV Cache]] 有紧密关系。Masked Attention 解释它为什么不能偷看未来 token；KV Cache 则解释它为什么能在推理时逐 token 连续生成而不必每一步都重算整段前缀。也正因为它是自回归热路径，现代通用生成式 LLM 才会把 cache、batching、context window 和吞吐优化都围着 Decoder-only 推理栈来设计。

更重要的边界是：Decoder-only 不是“什么都比其他架构强”，而是“对于通用生成式大模型，这个目标最统一、最容易 scale up”。Encoder-only 仍然很适合理解、打分、分类和 embedding；Encoder-Decoder 仍然很适合输入输出明显分离的翻译、摘要和 seq2seq 任务。Decoder-only 赢的是通用生成式预训练时代的主航道，不是对所有 NLP 场景的全面替代。

## 它解决什么问题

它解决的是“怎样用一个统一训练目标，把大规模无标注文本学习和开放式文本生成连起来”。

相比需要区分理解任务和生成任务的多套接口，Decoder-only 让模型始终做同一件事：根据前缀预测下一个 token。这个统一目标降低了任务切换成本，也更适合持续扩大数据、参数和训练规模。

## 容易混淆的概念

Decoder-only 不是“所有带 decoder 的模型”。Encoder-Decoder 型模型同样有 decoder，但它们还有 encoder，并通过 cross-attention 读取 encoder 输出。

它也不是 [[Masked Attention]] 的同义词。Masked Attention 是内部可见性机制；Decoder-only 是整类架构选择。

它还不是“只会生成、不会理解”。它的理解能力来自同一个 next-token prediction 目标在大规模训练下学出的表示和模式，而不是来自双向 encoder。

## 最小例子

```text
输入前缀: 今天天气真
模型任务: 预测下一个 token
可能输出: 好

下一步前缀变成: 今天天气真好
然后继续预测下一个 token
```

这个“前缀 -> 下一个 token -> 追加到前缀”的循环，就是 Decoder-only 的最小工作形态。

## 常见误解 / 风险

- 误解：Decoder-only 只是为了聊天产品设计的壳。更稳的理解是：它先是统一训练目标的架构选择，聊天只是后续产品形态之一。
- 误解：Decoder-only 一定比 Encoder-only 或 Encoder-Decoder 更先进。其实它只是更适合通用生成式大模型；检索、分类、rerank、翻译和摘要仍可能更偏向其他架构。
- 误解：只要是 LLM 就一定是 Decoder-only。很多 embedding、reranking、分类或特殊 seq2seq 模型并不是。
- 风险：把“Decoder-only 赢了”误说成“其他架构没有价值”，会把模型架构选择和任务求解器选择混成一层。

## 边界细节

和 Encoder-only 的边界：Encoder-only 双向看上下文，更像“读完整句子再理解”；Decoder-only 单向看前缀，更像“沿着前文继续写下去”。

和 Encoder-Decoder 的边界：Encoder-Decoder 把“理解输入”和“生成输出”拆成两段，并通过 cross-attention 连接；Decoder-only 则把所有任务尽量压成单段自回归生成。

和 [[KV Cache]] 的边界：KV Cache 是推理优化，不是架构定义。没有 KV Cache，Decoder-only 仍然是 Decoder-only，只是生成会慢很多。

和 [[Constrained Decoding]] 的边界：Constrained Decoding 是输出阶段的结构约束；Decoder-only 是模型架构。一个 Decoder-only 模型完全可以再叠加 constrained decoding。

## 现代性状态

- 判定：foundation + current-practice。
- 稳定部分：自回归前缀可见性、next-token prediction、通用生成式训练接口。
- 当前工程现实：GPT、Claude、Qwen 这类主流通用生成式 LLM 大多采用 Decoder-only。
- 易变部分：具体 attention 变体、位置编码、cache 管理、长上下文优化和后训练路线。

## 现代系统怎么吸收 Decoder-only 的价值 / 局限

现代系统通常把 Decoder-only 当成“通用生成内核”，再把检索、工具调用、状态、权限、评估和结构化输出放到模型外部。也就是说，架构负责连续生成语言，系统层负责把语言能力变成可靠产品行为。

这也解释了一个常见边界：Decoder-only 本身不等于 Agent，也不等于 RAG。Agent 和 RAG 是围绕这个生成内核搭建的运行时和知识访问结构。

## 证据锚点

- Source: [[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？]]
- Anchors: [[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#Encoder-only、Decoder-only 和 Encoder-Decoder 三种架构]], [[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#为什么 Decoder-only 赢了]]
- Source: [[补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系]]
- Anchor: [[补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系#2.10 Bert模型与现在大语言模型LLM的区别?]]
- Evidence type: interview-oriented source notes + local architecture synthesis.
- Confidence: medium-high for architecture/task boundary; medium for “why it won” because that part is engineering synthesis over current practice rather than a single canonical paper definition.
- Boundary: 本卡记录的是 Transformer 架构变体里“仅解码器 + 自回归 next-token prediction”的稳定学习边界，不把 Encoder-only / Encoder-Decoder 当作 aliases，也不把 Decoder-only 直接等同于 Agent、RAG 或所有生成模型。
- Taxonomy note: this card intentionally leaves `up` empty in this pass; the current taxonomy baseline allows no-`up` terminal states when no reviewed strict parent has been write-backed yet.

## 复习触发

1. 为什么 Decoder-only 的核心不是“有 decoder”，而是“next-token prediction + causal visibility”？
2. Decoder-only 和 Encoder-only 的最小差别是什么？
3. 为什么现代通用生成式 LLM 更偏 Decoder-only，而不是说其他架构全都过时？

## 相关链接

- [[Transformer]]
- [[Encoder-only]]
- [[Encoder-Decoder]]
- [[Masked Attention]]
- [[KV Cache]]
- [[LLM]]
- [[LLM 基础结构对比]]
