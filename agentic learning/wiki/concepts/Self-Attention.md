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
  - "[[Multi-Head Attention]]"
  - "[[LLM]]"
---

# Self-Attention

## 一句话

Self-Attention 是让同一个序列中的不同位置互相“看见”并计算关系的机制。

## 概念详解

Self-Attention 的问题背景是语言里很多依赖不是相邻的。一个代词可能指向很远的名词，一个结论可能依赖前文条件，代码里的变量使用也可能跨越多行。传统 RNN 按顺序传递状态，远距离依赖和并行训练都会受限制；self-attention 让同一序列中的每个位置直接参考其他位置，用 query、key、value 的关系计算加权表示。

[[Attention Is All You Need]] 的学习目标把 3.2 Attention 和 4 Why Self-Attention 列为重点，原因是它解释了 Transformer 为什么能替代 recurrence/convolution 来建模序列。Self-attention 的价值不是“像人一样注意”，而是提供一种可并行、路径更短的 token 交互机制。它能帮助模型在当前上下文中整合信息，但不等于模型真正理解世界，也不等于输出具有事实保证。

对 Agent 学习来说，Self-Attention 和 [[Memory]] 的边界最容易混淆。attention 处理当前上下文窗口内的关系；memory 处理跨轮、跨任务或外部存储的保存和检索。Agent harness 需要 memory、trace、tools 和 evaluation，是因为 self-attention 本身不会替系统保存长期状态或验证行动结果。

机制上，每个位置会根据自己生成 query，并和其他位置的 key 比较，得到权重后汇总 value。这个过程让 token 表示能吸收上下文信息，所以模型可以处理指代、条件和跨句依赖。它仍然是一次前向计算中的关系建模，不会在计算结束后自动形成可查询、可审计的长期状态。


## 它解决什么问题

语言里很多依赖不是相邻的。一个词可能需要参考前面很远的词。Self-Attention 让每个位置可以关注同一序列中的其他位置，从而建模长距离依赖。

## 它不是什么

Self-Attention 不是人类注意力。

它也不是模型的长期记忆。它只在当前输入序列和当前计算中建立位置之间的关系。

## 最小例子

在句子“那个学生交了作业，因为他很认真”中，“他”需要和“那个学生”建立关系。Self-Attention 提供了一种让这些位置直接交互的方式。

## 常见误解

- attention 权重看起来像解释，但不一定等于真实因果解释。
- Self-Attention 能处理序列内部关系，但不能替代外部知识库。

## 边界细节

Self-Attention 只在当前输入/上下文内建立 token 关系，不保存跨任务记忆。它能支持语言理解能力，但不替代外部知识库、工具执行、状态恢复或事实验证。

## 现代性状态

foundation。Self-Attention 是 Transformer/LLM 的地基概念。它不是前沿产品能力，而是帮助理解上下文建模和 memory 边界的稳定概念。

## 证据锚点

- Evidence type: source evidence — [[Attention Is All You Need#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Attention Is All You Need]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Self-Attention 和 Memory 的边界是什么？
- 为什么它能支持上下文关系但不能替代事实验证？

## 相关链接

- [[Transformer]]
- [[Multi-Head Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
