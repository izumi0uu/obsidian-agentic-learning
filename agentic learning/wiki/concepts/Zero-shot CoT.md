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
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]"
evidence:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]"
  - "[[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？#CoT是什么？]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？#CoT：最简单的激活方式，加一句话就够了]]"
related:
  - "[[Plan-and-Solve Prompting]]"
  - "[[Reasoning Trace]]"
  - "[[ReAct]]"
  - "[[Planning]]"
  - "[[Agent Workflow]]"
---

# Zero-shot CoT

## 一句话

Zero-shot CoT 是不提供示例，只在 prompt 里加一句类似“让我们一步步思考”的提示，让模型先生成中间推理步骤，再给出答案。

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

## 现代系统怎么吸收 Zero-shot CoT 的价值

现代系统不一定会把完整 CoT 暴露给用户，但会吸收它的几个价值：

- 对复杂问题，要求模型先给结构化步骤、约束或检查清单。
- 对高风险任务，把推理结果转成可验证的 plan、test、rubric 或 intermediate artifact。
- 对需要外部事实的任务，把纯 CoT 升级为 [[ReAct]]、RAG 或 tool-using workflow。
- 对生产系统，用 [[Evaluation]]、测试、引用、trace 或 reviewer 检查结果，而不是只相信模型写出来的推理链。

小边界：强模型可能已经更擅长隐式推理，但当你需要教学、审查、调试或复盘时，让它显式写出中间结构仍然有价值。

## 证据锚点

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Source: [[raw/repos/xiaolinnote/questions/012 ai agent 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？]]
- Source: [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]
- Confidence: medium

## 相关链接

- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]
- [[ReAct]]
- [[Planning]]
- [[Agent Workflow]]
