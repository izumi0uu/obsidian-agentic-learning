---
type: concept
topic:
  - llm
  - nlp
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: stable
conflicts: []
aliases:
  - Natural Language Processing
  - 自然语言处理
source:
  - "[[161 01_AI 05_模型调优与微调 11 NLP是什么]]"
  - "[[164 01_AI 05_模型调优与微调 补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系]]"
  - "[[142 ai llm 1. 什么是大语言模型？和传统 NLP 模型有什么区别？]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[161 01_AI 05_模型调优与微调 11 NLP是什么#题目正文]]"
  - "[[164 01_AI 05_模型调优与微调 补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系#题目正文]]"
  - "[[142 ai llm 1. 什么是大语言模型？和传统 NLP 模型有什么区别？#页面正文]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
related:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Prompt Engineering]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
---

# NLP

## 一句话

NLP 是让机器处理自然语言任务的问题域和能力集合，不是某一个模型、架构或提示词技巧。

## 概念详解

NLP 的核心问题是：怎样让机器处理人类语言。这里的“处理”很宽，既包括理解，也包括生成、检索、排序、质量检查和安全识别。面试资料里的直接定义很适合作为边界起点：NLP 不是单一模型，而是一组“让机器处理文本”的能力集合。

传统 NLP 更像一条 pipeline。一个任务会拆成分词、词性标注、命名实体识别、意图分类、语义匹配、问答或摘要等多个子任务，每一步可能有自己的模型、标注数据和错误传播问题。这个范式的优点是可控、任务边界明确；缺点是任务迁移成本高，换领域时常常要重做数据、特征和模型适配。

BERT 时代把 NLP 推进到“预训练表示 + 下游微调”。它让很多理解类任务共享同一个预训练底座，但不同任务往往仍需要不同的任务头、数据集或微调副本。它证明了大规模无标注语料和预训练很重要，却还没有把所有任务统一到一个交互接口下。

现代 [[LLM]] 改变的是求解路径：很多 NLP 任务可以通过 prompt、上下文、工具、检索和结构化输出表达给同一个生成式模型。但这不意味着 NLP 消失了。NLP 仍然是任务域，LLM 只是当前很强的一类求解器。一个系统是在做摘要、问答、分类、实体抽取、重排还是安全检测，仍要用 NLP 的任务边界来拆需求、设计评估和检查失败。

从工程视角看，NLP 还是需求拆解语言。用户说“让模型读懂这段内容”，实际可能是分类、抽取、聚类、匹配、总结、翻译、问答或安全审查；这些任务的输入、输出、ground truth、指标和失败后果都不一样。把它们都叫“让 LLM 处理文本”会让系统设计变钝：分类要看标签一致性，抽取要看字段完整性，摘要要看事实保真，检索排序要看召回和相关性，安全检测要看误杀和漏检。

这也是 NLP 对 Agent 学习有价值的原因。Agent 常常把自然语言任务藏在 workflow 的节点里：先理解用户意图，再检索证据，再生成计划，再调用工具，再解释结果。每个节点都可能是一个小 NLP 任务，也都可能需要独立 guardrail 或 evaluation。如果不先识别这些任务，就很容易把失败归因到“模型不够聪明”，而忽略了任务定义、证据质量、输出格式、权限边界或评估指标的问题。

## 它解决什么问题

- 文本理解：分词、实体识别、意图识别、语义匹配、情感分析、分类。
- 文本生成：标题生成、摘要、改写、翻译、问答、对话。
- 检索与排序：query 和文档的相关性判断、召回、[[Reranking|重排]]。
- 质量与安全：去重、错别字检测、违禁内容识别、低质内容过滤。
- 任务接口：把自然语言输入输出变成可训练、可评估、可上线的系统任务。

## 它不是什么

NLP 不是 [[LLM]]。LLM 可以处理很多 NLP 任务，但 NLP 是更宽的任务域，历史上也包括规则系统、统计模型、BERT 类模型、检索排序模型和专用分类器。

NLP 不是 [[Transformer]]。Transformer 是模型架构，NLP 是任务域。Transformer 可以用于 NLP，也可以用于视觉、多模态或代码建模。

NLP 不是 [[Prompt Engineering]]。Prompt Engineering 是使用 LLM 解决任务时的输入设计和工程治理方法；NLP 任务可以用 prompt 表达，但也可以用传统模型、检索器或规则系统解决。

NLP 也不是 [[RAG]]。RAG 是把检索和生成结合起来的架构路线，常用于知识密集型 NLP 任务；它不是所有 NLP 任务的总称。

## 最小例子

同一句用户输入“我想退货”可以落到多个 NLP 任务：

- 意图识别：判断这是退货请求。
- 实体抽取：找出商品、订单号或时间。
- 检索：从知识库找退货政策。
- 生成：把政策组织成用户能读懂的回复。

现代 LLM 可以把这些步骤包进一个对话式接口里，但系统设计时仍需要知道每一步到底在解决哪个 NLP 子问题。

## 常见误解

- 把 NLP 等同于 LLM：LLM 很强，但不是 NLP 的全部历史和全部工程形态。
- 把 NLP 等同于 Transformer：架构和任务域不是同一层。
- 以为 LLM 出现后传统 NLP 完全没价值：高精度分类、检索排序、合规过滤、低延迟线上判断，仍可能需要专用模型、规则或混合方案。
- 只看生成效果，不看任务评估：摘要、问答、分类、抽取和重排的错误形态不同，不能只用一个“看起来像人话”的标准评估。

## 边界细节

最稳的切法是四层：

- 任务域：[[NLP]]，回答“自然语言任务是什么”。
- 模型/求解器：[[LLM]]、BERT 类模型、分类器、检索模型，回答“用什么能力来解”。
- 架构：[[Transformer]]、encoder-only、decoder-only，回答“模型内部怎么建模序列”。
- 工程方法：[[Prompt Engineering]]、[[RAG]]、tool use、structured output，回答“怎样把能力接到产品和工作流里”。

这样切开以后，很多混淆会消失：LLM 可以成为 NLP 的主力求解器，但它不替代任务定义；RAG 可以服务知识密集型 NLP，但不是所有 NLP；prompt 可以表达任务，但不等于任务本身。

## 现代性状态

foundation。NLP 是稳定的基础任务域语言，不是短期前沿词。变化的是主要求解器和工程入口：从规则与传统机器学习，到预训练表示，再到 LLM、RAG、Agent 和工具化工作流。对当前 Agent 学习来说，NLP 的价值是提供“任务是什么”的地基，避免把所有语言任务都粗暴归为“让 LLM 回答一下”。

## 现代系统怎么吸收 NLP 的价值

现代系统通常把 NLP 任务吸收到更大的 LLM application 或 Agent workflow 里：

- 用 prompt 和 schema 表达分类、抽取、摘要、改写等任务。
- 用 [[RAG]] 和 [[Retriever]] 给问答、摘要和解释提供外部证据。
- 用 [[Reranking]]、过滤器和评估器控制检索质量。
- 用结构化输出、guardrails 和 human review 把自然语言输出接到业务副作用前。

所以工程上不是“还要不要学 NLP”，而是要知道 NLP 任务被现代 LLM 系统藏到了哪些接口、评估和失败边界里。

## 证据锚点

- Evidence type: raw definition — [[161 01_AI 05_模型调优与微调 11 NLP是什么#题目正文]] 和 [[164 01_AI 05_模型调优与微调 补充原文：BERT、NLP、TFRecord 与 TensorFlow Transformer 关系#题目正文]] 直接支持“能力集合，不是单一模型”的边界。
- Evidence type: paradigm comparison — [[142 ai llm 1. 什么是大语言模型？和传统 NLP 模型有什么区别？#页面正文]] 支持传统 NLP pipeline、BERT 过渡和 LLM 统一任务接口的对比。
- Evidence type: paper title / task-domain signal — [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]] 把 RAG 放在 knowledge-intensive NLP tasks 的任务域语境中。
- Boundary: 本卡是基础概念卡，只沉淀任务域边界；不把每个 NLP 子任务展开成独立卡。
- Confidence: medium

## 复习触发

1. NLP、LLM、Transformer、Prompt Engineering 四者分别在哪一层？
2. 为什么“LLM 能做 NLP 任务”不等于“NLP 就是 LLM”？
3. 一个客服问答系统里，哪些部分是 NLP 任务，哪些部分是 RAG 或 Agent 工程？

## 相关链接

- [[LLM]]
- [[Transformer]]
- [[Prompt Engineering]]
- [[RAG]]
- [[Retriever]]
- [[Reranking]]
