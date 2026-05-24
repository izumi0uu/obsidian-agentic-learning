---
type: map
topic:
  - llm
status: active
created: 2026-05-05
updated: 2026-05-23
related:
  - "[[NLP]]"
  - "[[LLM]]"
  - "[[Token]]"
  - "[[Context Window]]"
  - "[[Context Rot]]"
  - "[[KV Cache]]"
  - "[[Constrained Decoding]]"
  - "[[Structured Outputs]]"
  - "[[Prompt]]"
  - "[[Prompt Engineering]]"
  - "[[Few-shot Prompting]]"
  - "[[Hallucination]]"
  - "[[Transformer]]"
  - "[[Few-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Tree of Thoughts]]"
  - "[[Prompt Chaining]]"
  - "[[LLM 基础结构对比]]"
  - "[[LLM 输入输出基础边界对比]]"
  - "[[CoT 与 Reasoning Tokens 边界]]"
  - "[[LLM 上下文限制与突破条件]]"
  - "[[PBRFT 到 Agentic RL 的训练范式转变对比]]"
  - "[[Agent Skills 按需加载与上下文边界]]"
  - "[[Agent 知识地图]]"
---

# LLM 主题

## 一句话总览

LLM 主题先回答“自然语言任务是什么、模型一次调用如何读输入、生成输出、受什么边界限制”，再进入 Transformer 架构、推理缓存、结构化输出、训练/后训练、prompt-time reasoning 和 Agent 工程承载。最小入口是 [[NLP]]、[[LLM]]、[[Token]]、[[Context Window]]、[[Context Rot]]、[[KV Cache]]、[[Structured Outputs]] / [[Constrained Decoding]]、[[Prompt]]、[[Prompt Engineering]]、[[Hallucination]] 和 [[LLM 输入输出基础边界对比]]。

## 先看这个

- [[LLM]]：理解语言模型的生成能力和边界。
- [[NLP]]：理解自然语言任务域，避免把任务、模型、架构和工程方法混成一层。
- [[LLM 输入输出基础边界对比]]：区分 token、context window、prompt 和 hallucination。
- [[LLM 上下文限制与突破条件]]：把 context window 的容量、计算、结构和治理限制拆开看。
- [[Context Rot]]：理解长窗口里“看得见”和“用得稳”不是一回事。
- [[KV Cache]]：理解自回归解码为什么要缓存历史 K/V，以及长上下文为什么会变成显存和带宽问题。
- [[LLM 基础结构对比]]：区分 Transformer、self-attention、multi-head attention 和 positional encoding。
- [[Prompt Engineering]]：理解 prompt 如何从一次性文本变成可测试、可版本化、可回滚的工程资产。
- [[Few-shot Prompting]]：理解示例如何在推理时临时定义任务格式、标签边界和输出风格。
- [[Context Engineering]]：理解 prompt 之外，系统如何选择和装配上下文。
- [[Agent Skills 按需加载与上下文边界]]：理解 skill 为什么不是超长 prompt，而是由 runtime 按需读取、装配和验证的外部能力包。
- [[RAG 主题]]：理解模型外部知识如何进入上下文，并用 evaluation / citation 降低幻觉风险。

## 学习路线

1. **任务和输入输出边界**：读 [[NLP]]、[[Token]]、[[Context Window]]、[[Prompt]]、[[Prompt Engineering]]、[[Few-shot Prompting]]、[[Hallucination]]，先知道自然语言任务是什么、一次模型调用能看到什么、怎样被指令、哪里会不可靠，以及 prompt / 示例如何被工程化维护。
2. **模型结构地基**：读 [[Transformer]]、[[Self-Attention]]、[[Multi-Head Attention]]、[[Positional Encoding]]，理解注意力机制和位置表示只是模型架构，不是 Agent 行动能力。
3. **推理运行成本**：读 [[KV Cache]] 和 [[LLM 上下文限制与突破条件]]，理解长上下文为什么会放大显存、带宽、延迟和并发吞吐问题。
4. **结构化输出控制**：读 [[Structured Outputs]] 和 [[Constrained Decoding]]，理解 structured output 是应用层 typed boundary，constrained decoding 是可能的 token-level 机制；再和 [[Tool Calling]]、schema validation、[[Type-safe Agent SDK]] 区分。
5. **训练与能力来源**：读 [[LLM Training Pipeline]]、[[Scaling Laws for Neural Language Models]]、[[Training Language Models to Follow Instructions with Human Feedback]] 和 [[PBRFT 到 Agentic RL 的训练范式转变对比]]，理解预训练、指令微调、偏好优化、推理强化和轨迹级 Agentic RL 的证据边界。
6. **prompt-time reasoning**：读 [[Zero-shot CoT]]、[[Few-shot CoT]]、[[Self-Consistency]]、[[Plan-and-Solve Prompting]]、[[Tree of Thoughts]]、[[Prompt Chaining]]、[[Reasoning Trace]] 和 [[CoT 与 Reasoning Tokens 边界]]，理解 prompt pattern 可以改善任务表现，但不等于可靠执行系统；现代 reasoning model 会吸收 CoT 价值，但不等于经典 prompt 技巧本身。
7. **接到 Agent / RAG**：读 [[Tool Calling]]、[[RAG]]、[[Memory]]、[[Agent Loop]]，理解 LLM 如何被包进工具、检索、状态和评估闭环。

## 基础边界表

| 层 | 概念 | 学习问题 | 边界提醒 |
|---|---|---|---|
| 输入单位 | [[Token]] | 模型实际读写的片段是什么？ | token 不等于单词；影响成本、长度和截断 |
| 任务域 | [[NLP]] | 自然语言任务到底是什么？ | NLP 不是 LLM、Transformer 或 Prompt Engineering |
| 调用容量 | [[Context Window]] | 一次调用最多能放多少输入/输出？ | 长上下文不等于长期记忆，也不保证正确使用证据 |
| 长输入可靠性 | [[Context Rot]] | 为什么输入更长后反而可能更不稳？ | 信息在窗口里不等于模型会正确、稳定地使用 |
| 任务组织 | [[Prompt]] | 怎样把目标、证据、约束和格式给模型？ | prompt 不是魔法咒语，不能替代工具、状态和评估 |
| 输入工程 | [[Prompt Engineering]] | 怎样设计、测试、版本化和优化 prompt？ | 不是 prompt 本身，也不是完整 context engineering |
| 示例条件化 | [[Few-shot Prompting]] | 示例怎样临时定义任务边界？ | 不是微调，也不是事实证据来源 |
| 输出风险 | [[Hallucination]] | 输出何时与事实或证据不一致？ | 有 RAG / citation 也仍需 faithfulness 检查 |
| 上下文装配 | [[Context Engineering]] | 哪些资料、tool result、memory 和规则进入本轮上下文？ | 它比 Prompt Engineering 更偏系统工程 |

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "llm")
SORT file.name ASC
```

## 已完成概念入口

- [x] [[LLM]]
- [x] [[NLP]]
- [x] [[Token]]
- [x] [[Context Window]]
- [x] [[Context Rot]]
- [x] [[KV Cache]]
- [x] [[Constrained Decoding]]
- [x] [[Structured Outputs]]
- [x] [[Prompt]]
- [x] [[Prompt Engineering]]
- [x] [[Few-shot Prompting]]
- [x] [[Hallucination]]
- [x] [[LLM 输入输出基础边界对比]]
- [x] [[LLM 上下文限制与突破条件]]
- [x] [[Transformer]]
- [x] [[Self-Attention]]
- [x] [[Multi-Head Attention]]
- [x] [[Positional Encoding]]
- [x] [[LLM 基础结构对比]]
- [x] [[Context Engineering]]
- [x] [[Zero-shot CoT]]
- [x] [[Few-shot CoT]]
- [x] [[Self-Consistency]]
- [x] [[Plan-and-Solve Prompting]]
- [x] [[Tree of Thoughts]]
- [x] [[Prompt Chaining]]
- [x] [[Reasoning Trace]]

## 下一批概念

- [ ] temperature：采样随机性、稳定输出和 creative variation 的边界是否需要单独成卡？
- [ ] top-p / decoding：[[Top-K]] 已补 retrieval / decoding 混淆边界；是否还需要 generation control 对比页？
- [x] structured output：已用 [[Structured Outputs]] 补齐应用层结构契约，用 [[Constrained Decoding]] 补齐解码层机制，并和 [[Tool Calling]]、schema validation、[[Type-safe Agent SDK]] 做边界。

## 推理和提示

- [[Zero-shot CoT]]
- [[Few-shot CoT]]
- [[Self-Consistency]]
- [[CoT 与 Reasoning Tokens 边界]]
- [[Plan-and-Solve Prompting]]
- [[Tree of Thoughts]]
- [[Prompt Chaining]]
- [[Reasoning Trace]]
- [[Prompt]]
- [[Prompt Engineering]]
- [[Few-shot Prompting]]
- [[Context Engineering]]

## 生成与输出控制

- [[Structured Outputs]]
- [[Constrained Decoding]]
- [[Top-K]]

## Transformer 地基

- [[LLM 基础结构对比]]：先用一张边界页切开 Transformer、self-attention、multi-head attention 和 positional encoding。
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[KV Cache]]：推理时复用历史 K/V 的运行机制，连接 attention 结构、长上下文和 serving 显存管理。

## 训练和后训练

- [[LLM Training Pipeline]]
- [[PBRFT 到 Agentic RL 的训练范式转变对比]]
- [[Toolformer]]
- [[Scaling Laws for Neural Language Models]]
- [[Training Compute-Optimal Large Language Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[Constitutional AI - Harmlessness from AI Feedback]]
- [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- [[The Llama 3 Herd of Models]]

## 关键边界

[[NLP]] 是自然语言任务域，LLM 是现代主要求解器之一。学习 LLM 时先抓 [[NLP]]、[[Token]]、[[Context Window]]、[[Prompt]]、[[Hallucination]] 这类任务和输入输出限制，再看 Agent 如何用 [[Tool Calling]]、[[RAG]]、[[Memory]]、[[Agent State]]、[[Trace]] 和 [[Evaluation]] 补足限制。

Transformer 是 LLM 的架构地基之一，但不是 Agent 能力本身。Prompt 能影响模型行为，[[Prompt Engineering]] 能把 prompt 改动纳入测试和版本治理，但它们仍不能替代 retrieval、工具执行、权限控制、评估和 human-in-the-loop。

## 证据锚点

- Concept anchors: [[LLM#证据锚点]], [[Token#证据锚点]], [[Context Window#证据锚点]], [[KV Cache#证据锚点]], [[Prompt#证据锚点]], [[Prompt Engineering#证据锚点]], [[Few-shot Prompting#证据锚点]], [[Few-shot CoT#证据锚点]], [[Self-Consistency#证据锚点]], [[Structured Outputs#证据锚点]], [[Hallucination#证据锚点]], [[Context Engineering#证据锚点]], [[Transformer#证据锚点]]。
- Topic anchors: [[LLM 输入输出基础边界对比#证据锚点]], [[LLM 基础结构对比#证据锚点]]。
- Source examples: [[Attention Is All You Need]], [[OpenAI - A Practical Guide to Building Agents]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- Evidence type: 本页是主题导航和学习路线；稳定定义回到概念卡，路线/边界判断属于工程综合 / inference。

## 复习触发

1. 为什么 context window 大不等于 memory 强？
2. Prompt、Prompt Engineering 和 Context Engineering 的边界是什么？
3. 一个 RAG 答案带 citation 仍然可能 hallucinate 吗？你会怎么查？
4. Transformer 架构地基和 Agent 行动系统之间隔着哪些工程层？

## 相关链接

- [[Agent 知识地图]]
- [[NLP]]
- [[LLM]]
- [[LLM 输入输出基础边界对比]]
- [[LLM 上下文限制与突破条件]]
- [[LLM 基础结构对比]]
- [[Token]]
- [[Context Window]]
- [[Context Rot]]
- [[KV Cache]]
- [[Prompt]]
- [[Prompt Engineering]]
- [[Few-shot Prompting]]
- [[Hallucination]]
- [[Context Engineering]]
- [[Agent Skills 按需加载与上下文边界]]
- [[Structured Outputs]]
- [[Few-shot CoT]]
- [[Self-Consistency]]
- [[Tree of Thoughts]]
- [[Prompt Chaining]]
- [[RAG 主题]]
