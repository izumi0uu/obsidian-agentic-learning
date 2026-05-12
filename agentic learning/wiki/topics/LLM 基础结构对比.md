---
type: map
topic:
  - llm
  - transformer
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Positional Encoding]]"
  - "[[LLM Training Pipeline]]"
evidence:
  - "[[LLM#证据锚点]]"
  - "[[Transformer#证据锚点]]"
  - "[[Self-Attention#证据锚点]]"
  - "[[Multi-Head Attention#证据锚点]]"
  - "[[Positional Encoding#证据锚点]]"
  - "[[LLM Training Pipeline#证据锚点]]"
related:
  - "[[Attention Is All You Need]]"
  - "[[Agent]]"
  - "[[LLM 主题]]"
---

# LLM 基础结构对比

## 一句话总览

这页把 LLM 的基础结构拆开：[[LLM]] 是会基于大规模训练生成和理解文本的模型类别；[[Transformer]] 是现代 LLM 的核心架构家族；[[Self-Attention]] 是让 token 彼此建立关系的机制；[[Multi-Head Attention]] 是并行从多个子空间看关系；[[Positional Encoding]] 给无循环的 attention 补位置信息；[[LLM Training Pipeline]] 解释这些结构如何通过预训练、对齐和评估变成可用模型。

最小边界：架构不是能力全部来源；attention 不是 memory；multi-head 不是多个 Agent；positional encoding 不是上下文窗口；training pipeline 不是推理时 Agent loop。

## 为什么这组值得对比

- 混淆风险：学习 Agent 时很容易把 LLM、Transformer、attention、训练流程和 Agent 能力混在一起。
- 共同问题域：它们都回答“模型为什么能处理上下文并生成语言”，但层级不同。
- 不同介入点：有的是模型类别，有的是架构，有的是内部机制，有的是位置信号，有的是训练/对齐流程。
- 证据密度：相关概念卡都已有 [[Attention Is All You Need]] 或训练论文/source note 证据锚点。
- 复习价值：这组对比能帮助把“模型基础能力”和“Agent runtime 能力”切开。

边界：这页只做基础结构学习对比，不追踪最新模型架构细节、上下文扩展技术或产品能力。

## 共同问题域

共同问题是：LLM 如何把一串 token 变成可计算表示，并在训练后生成下一段文本。Transformer 系列用 attention 机制处理 token 之间的关系，用 positional information 表示顺序，再通过大规模训练学习语言、知识、模式和指令跟随倾向。

```text
tokens
  -> embeddings + positional information
  -> self-attention / multi-head attention blocks
  -> transformer layers
  -> pretraining / alignment / evaluation pipeline
  -> LLM behavior at inference time
```

这条链路帮助理解模型基础，但它还不是 Agent：Agent 还需要目标、工具、状态、环境、权限、trace 和 evaluation harness。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[LLM]] | 模型类别和能力承载体 | 训练后在推理时生成 token | prompt/context/token 序列 | 概率分布、文本、结构化输出 | [[LLM#证据锚点]] |
| [[Transformer]] | 架构家族 | 每层处理 token 表示 | token embeddings、位置表示 | contextual representations | [[Transformer#证据锚点]] |
| [[Self-Attention]] | token 关系建模机制 | 每层内部计算 token 间依赖 | query/key/value 表示 | 加权聚合后的上下文表示 | [[Self-Attention#证据锚点]] |
| [[Multi-Head Attention]] | 多个 attention 子空间并行 | attention block 内部并行计算 | 多组投影后的 Q/K/V | 拼接/投影后的多视角表示 | [[Multi-Head Attention#证据锚点]] |
| [[Positional Encoding]] | 顺序/位置信息注入 | attention 前或层内参与表示 | token 位置、序列顺序 | 带位置感的 token 表示 | [[Positional Encoding#证据锚点]] |
| [[LLM Training Pipeline]] | 从架构到可用模型的训练/对齐流程 | 预训练 -> 指令/对齐 -> 评估/部署 | 数据、算力、目标函数、反馈 | 具备语言和指令能力的模型 | [[LLM Training Pipeline#证据锚点]] |

## 最容易混淆的边界

### LLM vs Transformer

[[LLM]] 是模型类别和能力层；[[Transformer]] 是支撑许多现代 LLM 的架构。不能说所有 Transformer 都是 LLM，也不能把某个 LLM 的产品行为全部归因于 Transformer 架构。

### Self-Attention vs Memory

[[Self-Attention]] 在当前上下文窗口内计算 token 关系；它不是长期记忆系统，也不会自动保存任务经验。Agent 的 [[Memory]]、state 或 RAG 需要外部 runtime 和存储机制。

### Multi-Head Attention vs 多 Agent

[[Multi-Head Attention]] 的 head 是同一模型层里的并行表示子空间，不是多个独立 Agent，也没有各自目标、工具或通信协议。

### Positional Encoding vs Context Window

[[Positional Encoding]] 解决 token 顺序/位置信息如何进入模型；context window 是推理时能放入多少 token 的运行约束。二者相关但不等价。

### Training Pipeline vs Agent Loop

[[LLM Training Pipeline]] 解释模型如何从数据和反馈中获得能力；Agent loop 是推理时 runtime 如何围绕目标、工具、观察和状态行动。训练能塑造模型倾向，但不能替代工具执行、权限和 trace。

## 执行时序 / 机制差异

```text
Model architecture side:
Token -> Embedding + Positional Encoding -> Transformer block
      -> Self-Attention / Multi-Head Attention -> Feed-forward layers -> next token logits

Model capability side:
Pretraining data + objective -> base model
Instruction / preference / RL-style alignment -> assistant-like behavior
Evaluation / deployment constraints -> usable model behavior

Agent runtime side:
LLM output -> tool/runtime/action -> observation/state/trace -> next LLM call
```

最后一段 runtime side 是边界对照：它说明 LLM 基础结构和 Agent 执行系统不是同一层。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

像建一座语言工厂：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Transformer]] | 工厂的生产线结构 | 结构本身不等于产品质量 |
| [[Self-Attention]] | 每个工位查看其他工位信息 | 不是长期记忆或外部数据库 |
| [[Multi-Head Attention]] | 多组质检员从不同角度看同一批材料 | 不是多个独立员工/Agent |
| [[Positional Encoding]] | 给材料贴上顺序标签 | 不等于仓库容量 |
| [[LLM Training Pipeline]] | 大规模训练和校准生产线 | 训练后仍需运行时约束 |
| [[LLM]] | 最终能生成语言的成品机器 | 不是完整 Agent 系统 |

## 现代系统如何吸收或限制

- 来源支持：[[LLM]]、[[Transformer]]、[[Self-Attention]]、[[Multi-Head Attention]]、[[Positional Encoding]] 的证据锚点主要回到 [[Attention Is All You Need]]；[[LLM Training Pipeline]] 还连接 scaling、Chinchilla、RLHF、Constitutional AI、DeepSeek-R1、Llama 3、Toolformer 等训练/能力来源 source notes。
- 工程综合 / inference：现代 Agent 系统把 LLM 当成推理和语言接口，但把工具执行、状态、记忆、权限、sandbox、trace 和 evaluation 放到外部 harness，而不是要求 Transformer 内部直接完成。
- 仍需警惕的外推：具体 attention 变体、位置编码实现、长上下文技术和训练配方变化很快；本页只沉淀学习层级，不写最新产品能力结论。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 想解释模型为何能基于上下文生成语言 | [[LLM]] | 它是能力承载层 | 不要把它等同于 Agent |
| 想解释现代 LLM 常见架构底座 | [[Transformer]] | 它定义主要计算结构 | 架构不能单独解释产品能力 |
| 想解释 token 间关系如何被建模 | [[Self-Attention]] | 它计算上下文内依赖 | 不要把 attention 当长期记忆 |
| 想解释为什么有多个 attention head | [[Multi-Head Attention]] | 它从多子空间并行建模关系 | 不要类比成多 Agent 协作 |
| 想解释无 RNN 架构如何知道顺序 | [[Positional Encoding]] | 它给 token 表示补顺序信号 | 不等于上下文窗口长度 |
| 想解释能力从哪里训练出来 | [[LLM Training Pipeline]] | 它连接数据、目标、反馈和评估 | 训练能力不等于运行时安全可靠 |

## 它们共同不是什么

- 都不是完整 [[Agent]] 或 [[Agent Framework]]。
- 都不是工具调用、RAG、长期记忆或 sandbox 本身。
- 都不能保证事实正确、任务完成或安全合规；这些需要 retrieval、tooling、evaluation、guardrails 和 human-in-the-loop。
- 都不是最新产品能力说明；模型 API、上下文长度和推理能力需要查最新官方文档。

## 证据锚点

- Concept anchors: [[LLM#证据锚点]], [[Transformer#证据锚点]], [[Self-Attention#证据锚点]], [[Multi-Head Attention#证据锚点]], [[Positional Encoding#证据锚点]], [[LLM Training Pipeline#证据锚点]]
- Source examples: [[Attention Is All You Need#为什么收]], [[Scaling Laws for Neural Language Models#为什么收]], [[Training Compute-Optimal Large Language Models#为什么收]], [[Training Language Models to Follow Instructions with Human Feedback#为什么收]], [[Constitutional AI - Harmlessness from AI Feedback#为什么收]], [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#为什么收]], [[The Llama 3 Herd of Models#为什么收]], [[Toolformer#为什么收]]
- Evidence type: existing concept-card synthesis + paper/source notes + engineering boundary synthesis + learning analogy.
- Confidence: medium-high for basic architecture boundaries; medium for capability-source synthesis because modern model training recipes and product behavior evolve quickly.
- Boundary: 本页没有精读每篇训练论文的机制细节；只把已有概念卡的证据锚点组织成对比学习页。

## 复习触发

1. 为什么 Self-Attention 不是长期 Memory？
2. Multi-Head Attention 和 multi-agent orchestration 的边界在哪里？
3. Positional Encoding 和 context window 有什么不同？
4. 为什么 LLM Training Pipeline 能塑造模型能力，但不能替代 Agent runtime 的 tool permissioning 和 trace？
5. 用一句话说明 LLM、Transformer、Agent 三者的层级关系。

## 相关链接

- [[LLM]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[LLM Training Pipeline]]
- [[Attention Is All You Need]]
- [[Agent]]
- [[LLM 主题]]
- [[LLM Wiki 工作流]]
