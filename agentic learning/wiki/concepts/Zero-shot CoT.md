---
type: concept
topic:
  - llm
  - reasoning
  - prompting
status: seed
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]"
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]"
evidence:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1-Lite-Preview 时间线补充]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1 正式版补充]]"
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？#CoT是什么？]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？#CoT：最简单的激活方式，加一句话就够了]]"
related:
  - "[[Plan-and-Solve Prompting]]"
  - "[[LLM Training Pipeline]]"
  - "[[Reasoning Trace]]"
  - "[[ReAct]]"
  - "[[Planning]]"
  - "[[Agent Workflow]]"
---

# Zero-shot CoT

## 一句话

Zero-shot CoT 是不提供示例，只在 prompt 里加一句类似“让我们一步步思考”的提示，让模型先生成中间推理步骤，再给出答案。

## 概念详解

Zero-shot CoT 的核心是用一个简短提示，让模型在没有示例的情况下显式写出中间推理步骤。它重要不是因为这句话本身神奇，而是因为它揭示了 LLM 的一个可利用特性：生成出的中间文本会进入后续上下文，帮助模型把多步关系、计算过程和条件约束逐步展开。对学习者来说，它是理解 [[Reasoning Trace]]、[[Planning]] 和后续 Agent 推理模式的入口。

证据边界要分清。Plan-and-Solve source note 把 Zero-shot CoT 当作对照：直接“step by step”能改善一些推理题，但容易漏步骤，所以 Plan-and-Solve 才提出先 plan 再 solve。小林笔记把 CoT 作为 Agent 推理模式入门，说明它是最轻量的推理激活方式。DeepSeek-R1 相关 source 则说明显式长推理后来被 reasoning model 和训练方法吸收，但这不是“用户加一句 Zero-shot CoT prompt”的同一层方法。

所以 Zero-shot CoT 是 prompt 层方法，不是环境交互方法。它没有 Action、没有 Observation、没有工具执行、没有 state、没有 evaluator。它适合低风险、可在文本里完成的多步推理；一旦问题依赖实时事实、外部计算、代码执行或长期任务，就要升级到 tool use、RAG、ReAct 或 agent workflow。

还有一个现代边界：许多产品不会向用户展示完整 chain-of-thought，而是给出简短理由、结构化计划或可验证摘要。这不代表 CoT 研究没有价值，而是把“显式中间推理”从用户可见文本转成了内部 reasoning、计划草稿、工具选择依据或评测材料。学习 Zero-shot CoT 时，重点应放在它打开了“中间步骤可影响后续生成”的视角，而不是执着于固定短语或完整推理链展示。
## 它解决什么问题

普通直接回答容易跳步：模型可能直接吐出结论，但中间条件、计算过程或推导关系没有显式展开。

Zero-shot CoT 的想法是让模型把中间过程写出来。因为 LLM 是按 token 顺序生成的，前面写出的推理文本会进入上下文，影响后面继续生成。它有点像做数学题时把草稿写在纸上：不是保证一定对，但比全靠脑内临时记忆更不容易漏步骤。

## 它不是什么

Zero-shot CoT 不是 [[ReAct]]。它没有外部 Action，也没有 [[Observation]] 回填，只是在一次文本生成里展开推理。

它也不是 [[Agent Workflow]]。它不会把计划放进显式 state，不会调用工具，不会自动重试、replan、跑测试或让 evaluator 打分。

它更不是“模型真实思维的窗口”。它只是模型生成出来的推理文本，可能有帮助，也可能自信地写出错误步骤。

## 最小例子

```text
Question: 小明有 3 个苹果，又买了 5 个，吃掉 2 个，还剩几个？

Prompt:
请一步步思考，然后给出答案。

Possible answer:
小明一开始有 3 个苹果。
又买了 5 个，所以一共有 3 + 5 = 8 个。
吃掉 2 个后，还剩 8 - 2 = 6 个。
答案是 6 个。
```

这里的 `zero-shot` 指“不提供示例”；`CoT` 指“让模型写出 chain of thought / 思维链”。

## 常见误解

- 误解：加一句“让我们一步步思考”就等于有规划能力。实际它只是单条文本推理链，不会自动纠错。
- 误解：推理步骤写得长就一定更可靠。实际长推理也可能累积错误。
- 误解：Zero-shot CoT 可以替代工具。实际它拿不到实时数据，也不能执行外部动作。
- 误解：Zero-shot CoT 和 Few-shot CoT 一样稳定。Few-shot CoT 给了示例格式，通常更可控；Zero-shot CoT 更轻，但格式和深度更靠模型自己发挥。
- 误解：2024 年底 DeepSeek-R1-Lite-Preview 这类 thinking / reasoning model 就是 Zero-shot CoT。更精确地说，它们输出形态很像长 CoT，但不是单纯靠用户加一句 prompt 触发，而是模型能力和训练 / 推理时 token 预算共同塑造出来的 reasoning behavior。

## 边界细节

可以把它和附近概念这样分开：

```text
Direct prompting: Prompt -> Answer
Zero-shot CoT: Prompt -> Reasoning steps -> Answer
Plan-and-Solve Prompting: Prompt -> Plan -> Solve -> Answer
ReAct: Thought -> Action -> Observation -> Thought -> ... -> Answer
Agent Workflow: Goal -> Plan/State -> Execute -> Evaluate/Replan -> Done
```

所以 Zero-shot CoT 是 prompt 层的推理激活方法。它的优势是成本低、接入简单；局限是单路径、无外部反馈、无运行时控制。

## 现代性状态

- 判定：foundation / transitional
- 基础地基：显式中间推理有助于教学、调试、复盘和复杂任务拆解，是稳定思想。
- 历史过渡：靠一句 prompt 触发完整 reasoning chain 属于轻量 prompt-era 方法；现代系统通常会隐藏、约束或结构化中间推理。
- 当前工程吸收：把 CoT 价值转成计划、检查清单、rubric、tool-use decision、trace summary 或可验证中间产物。
- 易变部分：具体模型是否暴露 chain-of-thought、是否使用 reasoning tokens、如何训练长推理，会随模型产品变化。

## 现代系统怎么吸收 Zero-shot CoT 的价值

现代系统不一定会把完整 CoT 暴露给用户，但会吸收它的几个价值：

- 对复杂问题，要求模型先给结构化步骤、约束或检查清单。
- 对高风险任务，把推理结果转成可验证的 plan、test、rubric 或 intermediate artifact。
- 对需要外部事实的任务，把纯 CoT 升级为 [[ReAct]]、RAG 或 tool-using workflow。
- 对生产系统，用 [[Evaluation]]、测试、引用、trace 或 reviewer 检查结果，而不是只相信模型写出来的推理链。

小边界：强模型可能已经更擅长隐式推理，但当你需要教学、审查、调试或复盘时，让它显式写出中间结构仍然有价值。

## 和 reasoning model 的关系

2024 年底的 DeepSeek-R1-Lite-Preview 可以说是“用户体验上很像 CoT 的 thinking model”：它会展示较长的推理过程，并且官方发布页强调“更长推理、更好表现”的 inference scaling。

但它不应该被归类为严格的 Zero-shot CoT：

```text
Zero-shot CoT: 普通模型 + prompt 触发“请一步步思考”
Reasoning model: 模型训练 / 后训练阶段已经强化长推理、验证、反思等行为
```

所以你的记忆可以这样校准：R1-Lite-Preview 和后来 R1 把 CoT 这种“显式中间推理”的价值产品化、模型能力化了；它们不是论文里最原始的 Zero-shot CoT prompt 方法本身。

## 和 DeepSeek-R1 的引用关系

如果说“原理参考这篇论文”，要分两层：

- 思想脉络上：是。DeepSeek-R1 这类 reasoning model 继承了 CoT 研究的核心发现：复杂问题里，让模型展开中间推理步骤通常比直接给答案更有效。
- 方法实现上：不是简单照搬。Zero-shot CoT 是 prompt 方法；DeepSeek-R1 的核心是用强化学习、可验证奖励、cold-start 数据和多阶段训练，把长推理、验证、反思等行为变成模型能力。

因此更准确的说法是：DeepSeek-R1 不是“用了 Zero-shot CoT prompt”，而是把 CoT 这一类显式推理行为通过训练和推理时扩展内化到了 reasoning model 里。

## 证据锚点

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Source: [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- Source: [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]
- Source: [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]], [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1-Lite-Preview 时间线补充]], [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1 正式版补充]], [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？#CoT是什么？]], [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？#CoT：最简单的激活方式，加一句话就够了]]
- Evidence type: prompting paper source note + reasoning-model source note + raw tutorial source notes + engineering synthesis.
- Confidence: medium
- Boundary: Zero-shot CoT 是 prompt 方法；DeepSeek-R1 类 reasoning model 继承显式推理价值，但实现层属于训练/推理时扩展，不等于简单 prompt 技巧。

## 复习触发

- Zero-shot CoT、Plan-and-Solve、ReAct 三者分别多了什么结构？
- 为什么长推理文本不是“模型真实思维”的可靠窗口？
- 遇到需要实时事实或工具执行的问题，为什么 Zero-shot CoT 不够？

## 相关链接

- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]
- [[ReAct]]
- [[Planning]]
- [[Agent Workflow]]
