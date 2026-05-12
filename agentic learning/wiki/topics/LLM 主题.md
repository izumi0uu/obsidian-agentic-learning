---
type: map
topic:
  - llm
status: active
created: 2026-05-05
updated: 2026-05-12
related:
  - "[[LLM]]"
  - "[[Token]]"
  - "[[Context Window]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[Transformer]]"
  - "[[LLM 基础结构对比]]"
  - "[[LLM 输入输出基础边界对比]]"
  - "[[Agent 知识地图]]"
---

# LLM 主题

## 一句话总览

LLM 主题先回答“模型一次调用如何读输入、生成输出、受什么边界限制”，再进入 Transformer 架构、训练/后训练、prompt-time reasoning 和 Agent 工程承载。最小入口是 [[LLM]]、[[Token]]、[[Context Window]]、[[Prompt]]、[[Hallucination]] 和 [[LLM 输入输出基础边界对比]]。

## 先看这个

- [[LLM]]：理解语言模型的生成能力和边界。
- [[LLM 输入输出基础边界对比]]：区分 token、context window、prompt 和 hallucination。
- [[LLM 基础结构对比]]：区分 Transformer、self-attention、multi-head attention 和 positional encoding。
- [[Context Engineering]]：理解 prompt 之外，系统如何选择和装配上下文。
- [[RAG 主题]]：理解模型外部知识如何进入上下文，并用 evaluation / citation 降低幻觉风险。

## 学习路线

1. **输入输出边界**：读 [[Token]]、[[Context Window]]、[[Prompt]]、[[Hallucination]]，先知道一次模型调用能看到什么、怎样被指令、哪里会不可靠。
2. **模型结构地基**：读 [[Transformer]]、[[Self-Attention]]、[[Multi-Head Attention]]、[[Positional Encoding]]，理解注意力机制和位置表示只是模型架构，不是 Agent 行动能力。
3. **训练与能力来源**：读 [[LLM Training Pipeline]]、[[Scaling Laws for Neural Language Models]]、[[Training Language Models to Follow Instructions with Human Feedback]]，理解预训练、指令微调、偏好优化和推理强化的证据边界。
4. **prompt-time reasoning**：读 [[Zero-shot CoT]]、[[Plan-and-Solve Prompting]]、[[Reasoning Trace]]，理解 prompt pattern 可以改善任务表现，但不等于可靠执行系统。
5. **接到 Agent / RAG**：读 [[Tool Calling]]、[[RAG]]、[[Memory]]、[[Agent Loop]]，理解 LLM 如何被包进工具、检索、状态和评估闭环。

## 基础边界表

| 层 | 概念 | 学习问题 | 边界提醒 |
|---|---|---|---|
| 输入单位 | [[Token]] | 模型实际读写的片段是什么？ | token 不等于单词；影响成本、长度和截断 |
| 调用容量 | [[Context Window]] | 一次调用最多能放多少输入/输出？ | 长上下文不等于长期记忆，也不保证正确使用证据 |
| 任务组织 | [[Prompt]] | 怎样把目标、证据、约束和格式给模型？ | prompt 不是魔法咒语，不能替代工具、状态和评估 |
| 输出风险 | [[Hallucination]] | 输出何时与事实或证据不一致？ | 有 RAG / citation 也仍需 faithfulness 检查 |
| 上下文装配 | [[Context Engineering]] | 哪些资料、tool result、memory 和规则进入本轮上下文？ | 它比 prompt engineering 更偏系统工程 |

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "llm")
SORT file.name ASC
```

## 已完成概念入口

- [x] [[LLM]]
- [x] [[Token]]
- [x] [[Context Window]]
- [x] [[Prompt]]
- [x] [[Hallucination]]
- [x] [[LLM 输入输出基础边界对比]]
- [x] [[Transformer]]
- [x] [[Self-Attention]]
- [x] [[Multi-Head Attention]]
- [x] [[Positional Encoding]]
- [x] [[LLM 基础结构对比]]
- [x] [[Context Engineering]]
- [x] [[Zero-shot CoT]]
- [x] [[Plan-and-Solve Prompting]]
- [x] [[Reasoning Trace]]

## 下一批概念

- [ ] temperature：采样随机性、稳定输出和 creative variation 的边界是否需要单独成卡？
- [ ] top-p / top-k / decoding：是否作为 generation control 对比页处理？
- [ ] structured output：和 [[Tool Calling]]、schema validation、[[Type-safe Agent SDK]] 的边界需要补吗？

## 推理和提示

- [[Zero-shot CoT]]
- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]
- [[Prompt]]
- [[Context Engineering]]

## Transformer 地基

- [[LLM 基础结构对比]]：先用一张边界页切开 Transformer、self-attention、multi-head attention 和 positional encoding。
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]

## 训练和后训练

- [[LLM Training Pipeline]]
- [[Toolformer]]
- [[Scaling Laws for Neural Language Models]]
- [[Training Compute-Optimal Large Language Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[Constitutional AI - Harmlessness from AI Feedback]]
- [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- [[The Llama 3 Herd of Models]]

## 关键边界

LLM 是生成能力，Agent 是行动系统。学习 LLM 时先抓 [[Token]]、[[Context Window]]、[[Prompt]]、[[Hallucination]] 这类输入输出限制，再看 Agent 如何用 [[Tool Calling]]、[[RAG]]、[[Memory]]、[[Agent State]]、[[Trace]] 和 [[Evaluation]] 补足限制。

Transformer 是 LLM 的架构地基之一，但不是 Agent 能力本身。Prompt 能影响模型行为，但不能替代 retrieval、工具执行、权限控制、评估和 human-in-the-loop。

## 证据锚点

- Concept anchors: [[LLM#证据锚点]], [[Token#证据锚点]], [[Context Window#证据锚点]], [[Prompt#证据锚点]], [[Hallucination#证据锚点]], [[Context Engineering#证据锚点]], [[Transformer#证据锚点]]。
- Topic anchors: [[LLM 输入输出基础边界对比#证据锚点]], [[LLM 基础结构对比#证据锚点]]。
- Source examples: [[Attention Is All You Need]], [[OpenAI - A Practical Guide to Building Agents]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- Evidence type: 本页是主题导航和学习路线；稳定定义回到概念卡，路线/边界判断属于工程综合 / inference。

## 复习触发

1. 为什么 context window 大不等于 memory 强？
2. Prompt 和 Context Engineering 的边界是什么？
3. 一个 RAG 答案带 citation 仍然可能 hallucinate 吗？你会怎么查？
4. Transformer 架构地基和 Agent 行动系统之间隔着哪些工程层？

## 相关链接

- [[Agent 知识地图]]
- [[LLM]]
- [[LLM 输入输出基础边界对比]]
- [[LLM 基础结构对比]]
- [[Token]]
- [[Context Window]]
- [[Prompt]]
- [[Hallucination]]
- [[Context Engineering]]
- [[RAG 主题]]
