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
  - masked attention
  - masked multi-head attention
  - causal mask
  - causal masking
  - 因果掩码
  - 遮罩注意力
  - 掩码注意力
source:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need]]"
  - "[[Attention Is All You Need]]"
evidence:
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Masked Attention：防止模型提前看到答案]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Decoder：从理解输入到逐词生成]]"
  - "[[Attention Is All You Need#需要我读的内容]]"
related:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Token]]"
  - "[[Constrained Decoding]]"
---

# Masked Attention

## 一句话

Masked Attention 是在 attention 计算里遮住不允许看的位置，让生成模型只能基于当前位置之前的 token 预测后续 token。

## 概念详解

Transformer decoder 训练时有一个看似矛盾的问题：训练数据里完整答案已经存在，但模型的任务是学会“根据前文预测下一个 token”。如果 decoder 在预测第 i 个位置时能直接看到第 i 之后的标准答案，它就会通过答案泄漏完成训练，而不是学到自回归生成。

Masked attention 的做法是在 attention score matrix 上加一个 mask。对当前位置来说，未来 token 的注意力分数会在 softmax 前被置为不可选的极小值或等价形式；softmax 后这些位置的权重接近 0。这样第 i 个位置只能关注自己和之前的位置，不能关注未来答案。原始 Transformer 把它用于 decoder self-attention；现代 decoder-only LLM 也依赖类似 causal mask 来维持 next-token prediction。

它解释了“为什么不让 LLM 先看到答案”：训练时如果让模型看到未来 token，损失会变得虚假地低，推理时却没有未来答案可看，训练目标和真实生成条件不一致。mask 让训练条件模拟推理条件：永远只能用已知前缀预测下一步。

可以把训练和推理的差别理解成一个学习类比：训练像做练习题，每预测一步后可以拿标准答案检查和更新参数；推理像考试，未来答案不存在，只能根据已经写出的前缀继续生成。这个类比只帮助理解训练条件一致性，不是 masked attention 的严格定义。

Masked attention 不是把 prompt 里的敏感词盖住，也不是安全过滤。它是模型内部 attention 的可见性约束。它也不等同于 [[Constrained Decoding]]：constrained decoding 是在输出 token 选择时按 schema / grammar mask 非法 token；masked attention 是在上下文 token 之间的 attention 里 mask 不该看的位置。

## 它解决什么问题

它解决自回归训练里的“未来答案泄漏”问题，让模型在训练和推理时都只能依赖已知前缀。

## 它不是什么

Masked Attention 不是内容审查、敏感词遮挡或权限控制。

它也不是 structured output 的 token-level schema mask；那个边界更接近 [[Constrained Decoding]]。

它还不等于所有 attention mask。Padding mask 用来忽略补齐位置；causal / future mask 用来防止看到未来 token。二者都叫 mask，但语义不同。

## 最小例子

```text
目标序列: I love you

预测 love 时，模型可见:
I

不可见:
you
```

在 attention matrix 里，`love` 这个位置不能给未来的 `you` 分配注意力权重。

学习类比：训练阶段可以在“预测后”对照标准答案；但在“预测时”，attention mask 仍然让当前位置看不到未来 token。推理阶段没有标准答案可对照，所以模型天然只能沿着已生成前缀一步步继续。

## 常见误解 / 风险

- 误以为 mask 是为了让模型“更诚实”：它只是防止训练时偷看未来答案，不直接保证事实正确。
- 把 masked attention 和 safety guardrail 混在一起：安全策略发生在系统层，attention mask 发生在模型计算图里。
- 以为推理时也有完整答案可 mask：推理时未来 token 尚未生成，causal 约束天然存在；KV cache 等 serving 优化只是复用已生成前缀。

## 边界细节

和 [[Self-Attention]] 的边界：self-attention 定义 token 之间如何互相关注；masked attention 是给 self-attention 加可见性限制。

和 [[Multi-Head Attention]] 的边界：masked multi-head attention 只是多个 head 都遵守同一类未来遮罩；多头本身解决多子空间并行关系建模。

和 [[Constrained Decoding]] 的边界：masked attention mask 的是上下文位置；constrained decoding mask 的是下一步输出 token 候选。

和 [[KV Cache]] 的边界：KV cache 缓存已生成前缀的 K/V；它不会让模型看到未来 token，也不会改变 causal mask 的学习边界。

## 现代性状态

- 判定：foundation。
- 稳定部分：自回归生成需要因果可见性约束，不能训练时偷看未来 token。
- 易变部分：不同框架如何表示 attention mask、padding mask、block mask、sliding window mask 和长上下文 mask。
- 复查点：具体模型的 attention pattern 可能加入局部窗口、稀疏 attention 或 block attention，但“防未来泄漏”的 causal 边界仍是自回归模型地基。

## 现代系统怎么吸收 Masked Attention 的价值

应用层通常不直接操作 masked attention；它由模型架构和推理框架处理。工程价值在于理解训练/推理条件一致性：模型不是一次性看到完整未来答案后再生成，而是在 causal 约束下逐 token 预测。这个边界也解释了为什么长上下文、KV cache、streaming output 和 next-token prediction 会绑在一起。

## 证据锚点

- Source: [[20分钟读懂AI神级论文 Attention Is All You Need]]
- Anchors: [[20分钟读懂AI神级论文 Attention Is All You Need#Masked Attention：防止模型提前看到答案]], [[20分钟读懂AI神级论文 Attention Is All You Need#Decoder：从理解输入到逐词生成]]
- Source: [[Attention Is All You Need]]
- Anchor: [[Attention Is All You Need#需要我读的内容]]
- Evidence type: video source note + Transformer paper source note + engineering synthesis.
- Confidence: high for causal-mask training boundary; medium for implementation-specific mask forms.
- Boundary: 本卡只记录 attention 可见性约束，不把它等同于安全过滤、padding mask、schema-constrained decoding 或权限控制。

## 复习触发

1. 为什么训练时不能让 decoder 看到未来 token？
2. Masked Attention 和 Constrained Decoding 都叫 mask，它们分别 mask 什么？
3. Causal mask 和 padding mask 有什么不同？

## 相关链接

- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[KV Cache]]
- [[Constrained Decoding]]
