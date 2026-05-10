---
type: concept
topic:
  - llm
  - transformer
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Attention Is All You Need]]"
evidence:
  - "[[Attention Is All You Need#为什么收]]"
related:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[LLM]]"
---

# Multi-Head Attention

## 一句话

Multi-Head Attention 是并行运行多个 attention head，让模型从不同表示子空间关注不同关系的机制。

## 概念详解

Multi-Head Attention 的问题背景是单一 attention 视角容易把不同关系压在同一个表示空间里。语言序列同时包含词法、句法、指代、位置、主题和格式关系；如果只用一个注意力分布，模型很难在同一层里分别捕捉这些关系。Transformer 用多个 head 并行计算 attention，让每个 head 在不同投影子空间里学习不同类型的 token 交互，再把结果拼接和投影回模型表示。

在 [[Attention Is All You Need]] 的学习目标里，Multi-Head Attention 要和 Scaled Dot-Product Attention 区分：后者是一种 attention 计算形式，前者是把多个 attention head 组合起来的层结构。它帮助模型同时关注不同位置和不同表示关系，但不意味着每个 head 都有清晰的人类语义，也不意味着可视化某个 head 就等于解释模型推理。

对 Agent 学习来说，它的边界尤其重要：Multi-Head Attention 是 LLM 内部序列建模机制，不是多个 Agent、不是多模型协作，也不是 tool routing。它说明 LLM 为什么能成为强文本底座，却不解释工具权限、状态恢复、计划执行或安全评估。现代系统通常不直接操作 head，而是在模型外层用工具、RAG、trace 和 evaluation 约束输出。

从机制上看，每个 head 都会把输入表示投影成自己的 query/key/value 空间，计算一组注意力结果。多个 head 的意义不是“让模型开会”，而是让同一层能并行提取不同关系，再交给后续层继续组合。学习时只需要把这个抽象抓住，不必把每个 head 都解释成固定语法功能。


## 它解决什么问题

单个 attention 可能把不同关系平均在一起。多个 head 可以让模型在不同子空间里同时关注不同类型的信息，例如语法关系、指代关系或位置关系。

## 它不是什么

Multi-Head Attention 不是多个 Agent。

它也不是多模型协作。它是单个 Transformer 层内部的计算结构。

## 最小例子

一个 head 可能更关注主语和动词的关系，另一个 head 可能更关注代词和指代对象的关系。最终这些 head 的结果会被拼接和投影。

## 常见误解

- head 数越多不一定越好。
- attention head 的可视化不能直接等同于模型解释。

## 边界细节

Multi-Head Attention 是单个模型层内部的并行表示机制，不是多个 Agent 或多个模型。head 的可视化最多是分析线索，不能直接当成模型真实原因或可靠解释。

## 现代性状态

foundation。Multi-Head Attention 是 Transformer 论文中的稳定架构概念。现代实现会变体化，但它在本 vault 中主要用来建立 LLM 内部机制边界。

## 证据锚点

- Evidence type: source evidence — [[Attention Is All You Need#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Attention Is All You Need]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Multi-Head Attention 为什么不是多个 Agent？
- 为什么 attention head 可视化不能直接当解释？

## 相关链接

- [[Transformer]]
- [[Self-Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
