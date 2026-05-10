---
type: concept
topic:
  - rag
  - evaluation
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Self-RAG - Learning to Retrieve Generate and Critique]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Self-RAG - Learning to Retrieve Generate and Critique#为什么收]]"
  - "[[Self-RAG - Learning to Retrieve Generate and Critique#一句话]]"
  - "[[Self-RAG - Learning to Retrieve Generate and Critique#边界提醒]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Agentic Retrieval]]"
  - "[[Corrective RAG]]"
  - "[[Evaluation]]"
---

# Self-RAG

## 一句话

Self-RAG 是让模型自适应判断是否检索、如何生成、证据是否支持答案的一类 RAG 方法。

## 概念详解

Self-RAG 解决的是固定检索策略的局限。普通 RAG 常默认每个问题都检索 top-k 文档，但有些问题不需要外部知识，有些问题需要先查证，有些生成内容需要判断证据是否支持。固定检索可能浪费成本，也可能把无关资料引入上下文，反而让答案变差。

原始 Self-RAG 论文的重点不是简单 prompt “请反思”，而是训练模型使用 reflection tokens 来控制 retrieve、generate 和 critique。也就是说，模型学习在生成过程中判断：是否需要检索、检索到的 passages 是否相关、生成内容是否被证据支持、最终回答是否有用。这个训练式控制信号，是它和普通自我检查 prompt 的关键区别。

在现代工程里，人们可能用 LLM judge、工具节点、图工作流或 prompt 模拟 Self-RAG 的一部分价值，例如“先判断是否需要检索”“回答后检查证据支持度”。但这些近似不应直接等同于论文方法。闭源模型 API 场景下，reflection token 的训练机制不可见，工程系统只能把它拆成外部 evaluator、retrieval policy、critique node 或 human review。

和 [[Corrective RAG]] 的边界：Corrective RAG 更偏检索后质量评估和补救流程；Self-RAG 更强调模型自适应决定检索、生成和批判。和 [[Agentic RAG]] 的边界：Agentic RAG 是系统/工作流层的检索决策；Self-RAG 原始线索更偏模型训练与控制信号。三者都关心证据质量，但机制不同。

现代性上，Self-RAG 是 foundation-for-frontier：作为论文方法，它是理解自适应检索和证据批判的重要地基；作为产品能力或工程实现，它仍然易变。学习时要保留论文边界，不把所有“带反思的 RAG”都叫 Self-RAG。

## 它解决什么问题

固定检索策略会浪费成本，也会在不需要检索时引入噪音。Self-RAG 想让模型根据任务需要选择检索，并批判生成内容是否被证据支持。

## 它不是什么

Self-RAG 不是简单在 prompt 里写“请自我反思”。

原始论文强调通过 reflection tokens 学习 retrieve、generate、critique 的控制信号。工程实现可以近似，但不能把名字泛化到所有自检 RAG。

## 最小例子

问题：“Transformer 论文是哪一年？”

模型可能判断需要检索，找到论文来源后生成答案，并检查证据是否足以支持年份。

问题：“把这句话改得更通顺。”

模型可能判断不需要外部检索。

## 常见误解 / 风险

- 自我判断不等于真实可靠。
- 如果底层模型没训练过类似控制信号，prompt 近似效果有限。
- 对企业知识库，是否检索可能应由 policy 或任务类型决定。
- Self-RAG 和 [[Corrective RAG]] 都关注证据质量，但机制不同。

## 边界细节

和 [[Corrective RAG]] 的边界：Corrective RAG 强调检索质量评估和补救分支；Self-RAG 强调模型自适应检索、生成和批判控制。

和 [[Agentic RAG]] 的边界：Agentic RAG 可以用外部 workflow 做决策；Self-RAG 原始方法把部分决策学习进模型控制信号。

和普通 prompt reflection 的边界：prompt 反思可以是工程近似，但不自动继承 Self-RAG 论文的训练机制和效果。

## 现代性状态

- 判定：transitional / frontier。
- 稳定部分：自适应检索和证据批判是 RAG 可靠性的重要方向。
- 易变部分：reflection-token 训练、闭源模型近似、LLM judge、workflow 节点和产品 API。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：看到框架示例称 self-reflective RAG 时，要检查它是论文式 Self-RAG，还是 prompt/workflow 近似。

## 现代系统怎么吸收 Self-RAG 的价值

现代系统通常把 Self-RAG 的价值拆成外部组件：retrieval policy 判断是否检索，evaluator 判断证据是否相关，faithfulness checker 判断答案是否被支持，workflow 决定重查或拒答。这是工程吸收，不等于论文训练机制。

## 证据锚点

- Source: [[Self-RAG - Learning to Retrieve Generate and Critique]]
- Anchor: [[Self-RAG - Learning to Retrieve Generate and Critique#为什么收]]
- Anchor: [[Self-RAG - Learning to Retrieve Generate and Critique#一句话]]
- Anchor: [[Self-RAG - Learning to Retrieve Generate and Critique#边界提醒]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: paper source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: paper source supports reflection-token training and retrieve/generate/critique control; workflow/prompt approximations are engineering synthesis and should not be treated as identical to the original method.

## 复习触发

- Self-RAG 为什么不是“请模型反思一下”？
- Self-RAG、Corrective RAG、Agentic RAG 分别把证据质量控制放在哪一层？
- 闭源模型 API 场景里，哪些部分只能做工程近似？

## 相关链接

- [[RAG]]
- [[Agentic Retrieval]]
- [[Corrective RAG]]
- [[Evaluation]]
