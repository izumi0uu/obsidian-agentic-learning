---
type: concept
topic:
  - llm
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
  - "[[Agent]]"
  - "[[Transformer]]"
  - "[[LLM Training Pipeline]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
---

# LLM

## 一句话

LLM 是大语言模型，擅长根据上下文生成可能合理的文本。

## 概念详解

LLM 的问题背景是让机器在自然语言、代码和多模态文本环境里生成有用输出。现代 LLM 通常基于大规模预训练和后训练，输入一段上下文后预测接下来合理的 token 序列。[[Attention Is All You Need]] 支撑的是其中一个关键架构地基：Transformer 通过 self-attention 和 multi-head attention 在当前序列里建模关系，使模型能并行训练并捕捉远距离依赖。

但 LLM 不是完整 Agent。它可以生成解释、计划、代码或工具调用意图，却不会自己拥有长期记忆、权限、文件系统、浏览器、API、测试环境或审计日志。Agent 系统把 LLM 接进 harness：给它工具、状态、检索、memory、policy、trace、evaluation 和 human-in-the-loop。这个边界能解释为什么同一个模型在聊天窗口里只是回答问题，在 Codex/OMX/Computer Use 里才会变成可行动系统。

学习 LLM 时不要只背“会生成文字”。更重要的是抓住三层：模型架构层解释它如何处理上下文；训练和对齐层解释它为什么会遵循任务；系统层解释如何把不可靠的生成变成可验证流程。事实性、权限、记忆和执行都不是 LLM 单体天然保证的。

这也是为什么 Agent 学习不能从“模型会推理”直接跳到“系统会完成任务”。LLM 的能力会影响计划质量和语言理解，但可靠交付还依赖外部可验证环节：检索补事实，工具连接真实环境，测试验证代码，policy 限制权限，trace 保存过程，evaluation 形成反馈。把这些外层机制看清楚，才能避免把所有成功或失败都归因到模型本身。


## 它解决什么问题

LLM 可以理解和生成自然语言，帮助人类完成解释、总结、翻译、改写、代码生成、问答和推理辅助。

现代 LLM 的一个重要架构地基是 [[Transformer]]。Transformer 让模型可以用 [[Self-Attention]] 在当前上下文中建模 token 之间的关系，并通过 [[Multi-Head Attention]] 同时关注不同类型的信息。

## 它不是什么

LLM 不是数据库。它可能说出看起来很确定但实际错误的内容。

LLM 不是长期记忆。对话上下文以外的信息需要外部系统保存。

LLM 不是行动系统。它本身不会真正打开网页、读文件、调用 API 或修改代码，除非被接入工具和运行环境。

LLM 也不等于 Transformer。Transformer 是架构地基，LLM 还涉及预训练数据、tokenization、规模化训练、对齐、推理策略、工具接入和产品系统。

LLM 也不等于训练流水线。[[LLM Training Pipeline]] 解释模型怎样通过预训练、后训练、偏好优化、推理强化、工具能力和评测闭环变强。

## 最小例子

我问：“用一句话解释 Agent。”

LLM 可以生成解释。但如果我要它“检查我的仓库并创建笔记”，就需要工具、权限和执行循环。

## 常见误解

- 把 LLM 当数据库：看起来确定的回答仍可能错。
- 把 LLM 当 Agent：没有工具、状态、权限和执行环境时，它只是生成输出。
- 把模型变强等同于系统可靠：事实验证、测试、trace 和人工确认仍然需要外部机制。

## 边界细节

LLM 的边界是生成和上下文建模。它不是数据库、长期记忆、执行器或权限系统。需要可靠行动时，必须把 LLM 放进 Agent Harness，并用检索、工具、测试、trace 和人类确认补足。

## 现代性状态

foundation。LLM 是 Agent 学习的模型地基，不是前沿协议卡。具体模型产品会变化，但“上下文生成 + 外部 harness 才能行动”的边界稳定。

## 证据锚点

- Evidence type: source evidence — [[Attention Is All You Need#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Attention Is All You Need]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- LLM、Transformer、Agent 三者边界怎么切？
- 为什么 LLM 不是长期记忆或执行系统？

## 相关链接

- [[Agent]]
- [[Transformer]]
- [[LLM Training Pipeline]]
- [[Self-Attention]]
- [[Tool Calling]]
- [[RAG]]
- [[Memory]]
