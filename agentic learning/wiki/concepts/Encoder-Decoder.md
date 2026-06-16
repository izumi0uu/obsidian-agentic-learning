---
type: concept
topic:
  - llm
  - transformer
  - seq2seq
status: growing
created: 2026-06-08
updated: 2026-06-08
last_checked: 2026-06-08
freshness: stable
conflicts: []
aliases:
  - encoder decoder
  - Encoder Decoder
  - 编码器-解码器
  - 编码器解码器
  - seq2seq transformer
source:
  - "[[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？]]"
  - "[[Attention Is All You Need]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need]]"
evidence:
  - "[[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#Encoder-only、Decoder-only 和 Encoder-Decoder 三种架构]]"
  - "[[Attention Is All You Need#需要我读的内容]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Decoder：从理解输入到逐词生成]]"
related:
  - "[[Transformer]]"
  - "[[Encoder-only]]"
  - "[[Decoder-only]]"
  - "[[Masked Attention]]"
  - "[[LLM 基础结构对比]]"
---

# Encoder-Decoder

## 一句话

Encoder-Decoder 是先用 encoder 双向理解输入、再用 decoder 在 cross-attention 条件下逐步生成输出的 Transformer 架构变体。

## 概念详解

理解 Encoder-Decoder 的关键，是它把“读懂输入”和“生成输出”明确拆成两段。encoder 先把输入序列编码成一组上下文化表示；decoder 再一边看自己已经生成的前缀，一边通过 cross-attention 读取 encoder 侧表示，逐 token 生成目标输出。这种结构天然适合输入和输出明显分离的任务，比如翻译、摘要、问答式重写和其他典型 seq2seq 场景。

原始 [[Transformer]] 论文讲的其实就是这一类结构，而不是今天最常见的纯 [[Decoder-only]] 大语言模型。它的教学价值很高，因为它让“理解输入”和“生成输出”这两种职责在架构图上显式分开。看翻译例子时，这种分工非常直观：左边把“我爱你”读懂，右边把 `I love you` 逐步写出来。

它和 [[Decoder-only]] 的差别，不只是多了一个 encoder，而是任务组织方式不同。Decoder-only 倾向把一切都压成“给定前缀继续生成”；Encoder-Decoder 则保留一个更显式的条件生成接口：先有输入，再基于输入生成另一段输出。也因此，它在很多经典 seq2seq 任务里更自然，但在“海量无标注文本统一做 next-token prediction”这条大模型主航道上，不如 [[Decoder-only]] 简洁。

更稳的边界是：Encoder-Decoder 不是“过渡技术”或者“只用于翻译的旧架构”。它只是没有成为通用开放式生成的统一底座，但在输入输出边界明确、希望保留强条件生成结构的任务上，依然是有力选择。T5、BART 这一类模型就是理解这条路线的常见入口。

## 它解决什么问题

它解决的是“如何在明确读取一个输入之后，再有条件地生成另一段输出”。

当任务天然是输入文本到输出文本的映射，而不是开放式续写时，Encoder-Decoder 能更清楚地表达这种结构。

## 容易混淆的概念

Encoder-Decoder 不是所有有 encoder 和 decoder 名字的系统。这里讨论的是 Transformer 架构变体，不是任意软件系统里的编解码流程。

它也不是 [[Decoder-only]] 加了一层 prompt engineering。前者是模型内部结构分工，后者是给模型的外部输入组织方式。

它还不是所有生成任务的默认最优解。很多现代开放式生成产品更偏向 [[Decoder-only]]，因为统一训练目标更容易 scale。

## 最小例子

```text
输入：我爱你
encoder：先把输入序列表示成可读取的上下文
decoder：基于 encoder 输出 + 已生成前缀
输出：I love you
```

或者：

```text
source text -> encoder representations
target prefix + cross-attention -> next target token
```

## 常见误解 / 风险

- 误解：Encoder-Decoder 就是“有两个模型拼起来”。更准确地说，它是一个架构内部分工，encoder 和 decoder 共享同一任务目标但职责不同。
- 误解：它和 [[Encoder-only]] 很接近，因为两者都有 encoder。其实前者还要承担条件生成路径，后者通常停在表示/判别层。
- 误解：只要任务要输出文本，就应该优先选 Encoder-Decoder。现代很多生成产品已经用 [[Decoder-only]] 统一承接这类任务。
- 风险：把它的“适合 seq2seq”误读成“适合所有需要输入输出的系统”，会忽略训练目标统一性、规模化预训练和 serving 生态的现实差异。

## 边界细节

和 [[Encoder-only]] 的边界：Encoder-only 往往在理解/表示/判别处结束；Encoder-Decoder 会在此基础上继续条件生成输出。

和 [[Decoder-only]] 的边界：Encoder-Decoder 显式拆分输入理解与输出生成；Decoder-only 尽量把任务压成单段自回归续写。

和 [[Masked Attention]] 的边界：[[Masked Attention]] 是 decoder 侧防未来泄漏的内部机制；Encoder-Decoder 是更高一层的整体架构组织。

和 [[Transformer]] 的边界：[[Transformer]] 是架构家族；Encoder-Decoder 是其中一种经典变体，而且正是原始论文的默认教学入口。

## 现代性状态

- 判定：foundation + current-practice。
- 稳定部分：encoder 负责编码输入、decoder 负责编码前缀并结合 cross-attention 生成输出，这个结构边界稳定。
- 当前工程现实：它仍然适合翻译、摘要、重写、条件生成等输入输出分离明确的任务。
- 易变部分：具体训练目标、模型规模、位置编码、长上下文支持、蒸馏路线和产品化 serving 形态。

## 现代系统怎么吸收 Encoder-Decoder 的价值 / 局限

现代系统吸收它价值的方式，往往不是把它当成“万能聊天内核”，而是把它放在条件生成特别明确的场景里。它保留了很清晰的输入/输出分工，因此在翻译、摘要、改写和某些结构化文本转换任务中仍然自然。

它的局限也很清楚：如果目标是把几乎所有任务统一成一个开放式生成接口，并直接吃海量无标注文本做统一预训练，那么 [[Decoder-only]] 通常更顺手。这解释了为什么今天主流通用生成式 LLM 不以 Encoder-Decoder 为主干，但并不否认它在经典 seq2seq 问题上的价值。

## 证据锚点

- Source: [[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？]]
- Anchor: [[2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？#Encoder-only、Decoder-only 和 Encoder-Decoder 三种架构]]
- Source: [[20分钟读懂AI神级论文 Attention Is All You Need]]
- Anchor: [[20分钟读懂AI神级论文 Attention Is All You Need#Decoder：从理解输入到逐词生成]]
- Source: [[Attention Is All You Need]]
- Anchor: [[Attention Is All You Need#需要我读的内容]]
- Evidence type: Transformer paper/video source notes + interview-oriented source note + local architecture synthesis.
- Confidence: medium-high for structure/task-fit boundary; medium for broader modern engineering role because that part is synthesis over current practice.
- Boundary: 本卡记录的是 Transformer 架构变体里“encoder 先理解输入、decoder 再条件生成输出”的稳定学习边界，不把翻译、摘要、T5、BART 或 cross-attention 都当作 aliases，也不把 Encoder-Decoder 直接等同于所有生成模型。
- Taxonomy note: this card intentionally leaves `up` empty in this pass; the current taxonomy baseline allows no-`up` terminal states when no reviewed strict parent has been write-backed yet.

## 复习触发

1. 为什么 Encoder-Decoder 的核心不是“有两部分”，而是“先理解输入、再条件生成输出”？
2. Encoder-Decoder 和 [[Decoder-only]] 在任务组织方式上的最小差别是什么？
3. 为什么原始 [[Transformer]] 论文是 Encoder-Decoder 入口，但现代通用生成式 LLM 却大多走向 [[Decoder-only]]？

## 相关链接

- [[Transformer]]
- [[Encoder-only]]
- [[Decoder-only]]
- [[Masked Attention]]
- [[LLM 基础结构对比]]
