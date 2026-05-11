---
type: concept
topic:
  - llm
  - rag
  - memory
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
related:
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[Non-Parametric Memory]]"
---

# Parametric Memory

## 一句话

Parametric Memory 是模型参数中隐含保存的知识，也就是模型通过训练把语言模式和事实压缩进权重后的“内部知识”。

## 概念详解

Parametric Memory 这个说法在 RAG 论文里用来描述预训练 seq2seq 模型自身携带的知识。模型参数不是数据库表，也不是显式文档；它们通过训练数据和优化过程吸收大量模式，使模型能在没有现场检索的情况下回答很多常识、语言和事实问题。

它的优势是调用方便：模型生成时天然会使用参数中的统计知识，不需要每个问题都访问外部索引。它的局限也很明显：知识来源难追溯，更新通常需要再训练或微调，过期事实不容易删除，模型还可能把参数知识、上下文线索和生成猜测混在一起。

RAG 引入 [[Non-Parametric Memory]]，正是为了解决参数化知识难更新、难引用、难检查的问题。论文里的对比不是说 parametric memory 没价值，而是说知识密集任务需要外部可检索材料来补足模型内部知识。

在现代 Agent 学习里，要避免把 parametric memory 和 Agent 长期记忆混淆。模型“知道巴黎是法国首都”属于参数知识；Agent “记得用户喜欢先讲边界”通常应该存放在外部 memory store，并带有用户、时间和来源边界。

这个概念也解释了为什么 LLM 看起来像“记得很多东西”却仍会幻觉：参数中保存的是分布式模式，不是带主键、时间戳和来源的事实记录。模型生成时会把参数知识和当前 prompt 混合使用，所以需要外部证据、工具或评测来约束高风险事实。

不过 parametric memory 仍然很重要。没有模型参数中学到的语言、常识和推理模式，检索到的外部资料也难以被理解和组织。现代架构的关键不是二选一，而是让参数知识负责泛化，让外部 memory 负责可更新证据。

## 它解决什么问题

预训练模型通过大量数据学习语言和事实模式，这些知识被压缩进参数里。它让模型不需要每次查询外部数据库也能回答很多问题。

它也让模型具备语言流畅性、常识联想和跨领域迁移能力；没有参数化知识，检索到资料后也难以组织成自然回答。

## 它不是什么

Parametric Memory 不是可直接编辑的数据库。你不能像改一行文档那样删除模型权重里的某个事实。

它也不能稳定提供来源引用。模型说出的事实可能来自训练数据，也可能是上下文推断或生成错误。

它也不是 Agent 的用户记忆。用户偏好、项目状态和任务轨迹如果只靠模型参数保存，就既不可控也不可删除。

## 最小例子

LLM 知道“巴黎是法国首都”可能来自参数中的知识，而不是现场检索。

但如果今天某公司改了退款政策，模型参数里的旧政策不能可靠更新；更好的做法是通过 [[RAG]] 检索最新政策文档，把它作为外部证据放入上下文。

## 常见误解和风险

- 误解：模型能答出来就说明它“记得正确来源”。实际可能没有可验证来源。
- 误解：参数知识越多就不需要 RAG。快速变化、权限敏感和需要引用的知识仍适合外部检索。
- 风险：把模型自信回答当作数据库查询结果，会放大幻觉和过期事实。

## 边界细节

RAG 的核心动机之一，就是参数化知识难更新、难引用、难检查，所以引入 [[Non-Parametric Memory]]。

和 [[LLM]] 的边界：parametric memory 是 LLM 能力的一部分，但 LLM 还包括架构、推理、上下文处理、指令跟随和生成机制。

和 [[Memory]] 的边界：Agent memory 是系统层能力，通常需要外部状态、写入策略、检索和权限；parametric memory 是模型训练后内化在权重里的知识，用户通常不能直接治理。

## 现代性状态

Parametric Memory 是基础地基。

这个概念帮助理解为什么 LLM 可以在没有检索时回答问题，也解释了为什么 RAG、tool use 和 long-term memory 仍然必要。现代系统不是抛弃 parametric memory，而是把它与外部知识、工具和评测结合起来，避免把模型内部知识当成唯一事实来源。

## 现代系统怎么吸收 Parametric Memory 的价值

现代系统通常让模型参数知识负责语言理解、常识推断和生成组织，让 non-parametric memory / RAG 负责最新、可引用、权限受控的资料，让工具负责实时动作或计算。

这种分工能减少“模型什么都靠记忆回答”的风险，也让知识更新从重新训练转移到外部数据管线。

## 证据锚点

- Evidence type: paper source — [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- Boundary: 当前卡采用 RAG 论文里的 parametric memory 术语；它不是神经网络权重机制的完整解释，也不覆盖所有模型编辑研究。
- Engineering synthesis: “参数知识适合语言和常识，外部 memory 适合可更新和可引用知识”是现代 RAG / Agent 架构总结。
- Confidence: medium。

## 复习触发

- 为什么 Parametric Memory 不是数据库？
- RAG 为什么要引入 Non-Parametric Memory？
- 用户偏好应该存在模型参数里，还是外部 Agent memory 里？为什么？

## 相关链接

- [[LLM]]
- [[RAG]]
- [[Non-Parametric Memory]]
