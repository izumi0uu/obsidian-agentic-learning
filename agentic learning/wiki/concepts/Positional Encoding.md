---
type: concept
topic:
  - llm
  - transformer
status: growing
created: 2026-05-05
updated: 2026-05-25
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Attention Is All You Need]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need]]"
evidence:
  - "[[Attention Is All You Need#为什么收]]"
  - "[[20分钟读懂AI神级论文 Attention Is All You Need#Positional Encoding：给并行模型补上顺序]]"
related:
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[LLM]]"
---

# Positional Encoding

## 一句话

Positional Encoding 是给 Transformer 输入注入位置信息的机制。

## 概念详解

Positional Encoding 的问题背景是 Transformer 的 self-attention 本身对集合式 token 关系很强，但没有 recurrence 或 convolution 时，模型需要额外知道 token 的顺序。自然语言里顺序会改变意义：“狗追人”和“人追狗”包含相同词但关系相反。位置编码把位置信息注入 token 表示，让 attention 在计算关系时能区分第一个、后一个、相隔多远和相对顺序。

[[Attention Is All You Need]] 的 source note 要求重点读 3.5 Positional Encoding，理解为什么去掉 recurrence/convolution 后必须注入位置。原始 Transformer 使用正弦/余弦位置编码，但现代 LLM 可能使用不同的位置方案；因此概念卡要保留稳定抽象：位置编码解决“序列顺序如何进入模型”的问题，而不是把某个具体公式当成唯一实现。

它和上下文窗口、长期记忆、RAG 都不同。位置编码帮助模型在当前序列内部理解位置关系；上下文窗口决定一次能放多少 token；长期记忆和 RAG 决定跨会话或外部知识如何保存/检索。对 Agent 来说，位置编码解释底层模型为什么能处理有序文本，但不负责维护任务状态、文件历史或工具执行结果。

在 Agent 笔记里，这个概念的价值是防止把“模型能处理上下文”误解成“模型拥有外部时间线”。位置编码让模型知道当前输入里 token 的相对/绝对顺序，但它不会知道昨天发生了什么，也不会自动记住上次工具结果。跨会话连续性仍然要靠 conversation state、memory store 或日志恢复。


## 它解决什么问题

Transformer 去掉了 recurrence 和 convolution，所以模型本身不会天然知道 token 的顺序。Positional Encoding 把位置相关信息加到输入表示中，让模型能区分“我喜欢你”和“你喜欢我”这种顺序差异。

## 它不是什么

Positional Encoding 不是上下文窗口。

它也不是长期记忆。它只帮助模型在当前序列中感知位置。

## 最小例子

如果一句话有 10 个 token，模型需要知道第 1 个 token 和第 8 个 token 不是同一个位置。Positional Encoding 给每个位置加入可区分的位置信号。

## 常见误解

- 有位置信息不等于能无限处理长文本。
- 原始 Transformer 的正弦/余弦位置编码不是现代所有 LLM 的唯一做法。

## 边界细节

Positional Encoding 解决当前序列的位置注入，不解决长文本全部问题。上下文长度、位置外推、检索、记忆和上下文工程是相邻但不同的系统层问题。

## 现代性状态

foundation / transitional。位置注入是稳定问题，原始正弦位置编码是论文时代实现之一；现代 LLM 可能采用不同方案，所以卡片保留抽象边界。

## 证据锚点

- Evidence type: source evidence — [[Attention Is All You Need#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Attention Is All You Need]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 位置编码解决什么问题，和上下文窗口有什么区别？
- 为什么原始正弦编码不等于现代所有 LLM 的唯一做法？

## 相关链接

- [[Transformer]]
- [[Self-Attention]]
- [[LLM]]
- [[Attention Is All You Need]]
