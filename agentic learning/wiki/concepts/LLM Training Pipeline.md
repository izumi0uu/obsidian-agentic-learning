---
type: concept
topic:
  - llm
  - training
  - evaluation
status: growing
created: 2026-05-09
updated: 2026-05-10
source:
  - "[[Scaling Laws for Neural Language Models]]"
  - "[[Training Compute-Optimal Large Language Models]]"
  - "[[Training Language Models to Follow Instructions with Human Feedback]]"
  - "[[Constitutional AI - Harmlessness from AI Feedback]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]"
  - "[[The Llama 3 Herd of Models]]"
  - "[[Toolformer]]"
evidence:
  - "[[Scaling Laws for Neural Language Models#为什么收]]"
  - "[[Training Compute-Optimal Large Language Models#为什么收]]"
  - "[[Training Language Models to Follow Instructions with Human Feedback#为什么收]]"
  - "[[Constitutional AI - Harmlessness from AI Feedback#为什么收]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#为什么收]]"
  - "[[The Llama 3 Herd of Models#为什么收]]"
  - "[[Toolformer#为什么收]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
related:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Evaluation]]"
  - "[[Tool Calling]]"
  - "[[Reasoning Trace]]"
  - "[[Agent Framework]]"
---

# LLM Training Pipeline

## 一句话

LLM Training Pipeline 是把数据、算力、预训练、后训练、偏好优化、推理强化、工具能力和评测闭环组合起来，让模型持续变强的训练流程。

## 概念详解

LLM Training Pipeline 解释的是“模型能力从哪里来”。[[Transformer]] 只是架构；真正的助手能力来自一整套训练流程：大规模预训练让模型学语言、知识和代码分布；SFT 让模型学会按指令格式回答；偏好优化和安全训练让模型更符合人类偏好；推理和工具任务训练让模型更会规划、检查、写代码或生成 tool call；评测闭环再把失败样本反馈到数据、训练或产品策略。

对 Agent 学习来说，这张卡的边界很重要：训练可以让模型更擅长推理和工具接口，但不会自动提供 runtime。真正执行工具、保存 [[Agent State]]、管理权限、记录 [[Trace]]、运行 [[Eval Harness]]、做 [[Patch Validation]] 或恢复长任务，仍属于 Agent framework/harness 的工程责任。

现代训练流水线越来越重视 evaluation：benchmark、红队、人工偏好、可验证任务、代码测试、数学答案、工具调用成功率和真实用户反馈都会影响模型迭代。但训练阶段的 evaluation 和部署后的 observability/eval harness 不是一回事；前者改进模型本体，后者约束具体系统行为。


这条流水线也不是严格线性的一次性过程。现实里，部署后的失败会回流到数据清洗、SFT 示例、偏好数据、工具调用数据、红队样本或 eval set；新模型上线前又会经过离线 benchmark、安全评测、灰度和线上观测。也就是说，training pipeline 和 deployment evaluation 形成闭环，但二者职责不同：训练改变模型，harness 约束系统。

## 它解决什么问题

基础 [[Transformer]] 架构只说明模型如何建模 token 关系，不说明模型为什么会变成好用的助手。

训练流水线回答的是另一件事：模型怎样从大规模文本中获得底子，再通过指令、偏好、反馈、工具任务和评测，变得更会遵循指令、推理、写代码、调用工具和适配 Agent 框架。

## 它不是什么

LLM Training Pipeline 不是 [[Agent Framework]]。

训练可以让模型更会规划、反思和调用工具，但真正执行工具、保存 [[Agent State]]、管理权限、记录 [[Trace]]、恢复任务，仍然属于 Agent runtime / harness。

它也不等于单纯“把模型做大”。规模很重要，但数据质量、数据配比、后训练、评测和推理时计算同样重要。

## 最小例子

```text
pre-training
-> supervised fine-tuning
-> preference optimization / RLHF / RLAIF
-> reasoning and tool-use training
-> safety and domain evaluations
-> failure data back into training or prompts
```

## 关键阶段

- 预训练 scaling：用大量 token、参数和计算量学习语言、知识、代码和模式。
- 数据治理：去重、过滤低质数据、提高代码、数学、多语言、专业数据和安全数据质量。
- 指令微调 SFT：用人类或合成示范教模型按任务格式回答。
- 偏好优化：用人类或 AI 偏好，让模型更有用、更无害、更符合指令。
- 推理强化：用数学、代码、可验证任务和 reward 信号，强化长链推理、检查和修正。
- 工具 / Agent 兼容训练：让模型更稳定地产生 tool call、读 observation、遵守 schema、处理失败。
- 多模态训练：把文本、图像、音频、视频、屏幕和动作对齐到同一任务空间。
- 评测闭环：用 benchmark、红队、真实失败样例和回归测试反过来改数据、prompt、后训练和产品策略。

## Agent 兼容性

现代模型变强的一部分，是更适合被 [[Agent Framework]] 调度：

- 能稳定遵循 system prompt 和 tool rules。
- 能输出结构化 JSON 或 tool call。
- 能理解工具返回的 observation。
- 能把任务拆成可执行步骤。
- 能在工具失败、测试失败或权限拒绝后换路径。
- 能根据 evaluator 或 trace 生成可用修正。

这不是纯模型能力，也不是纯框架能力，而是模型和 runtime 的接口配合能力。

## 常见误解

- 预训练越大不一定产品越好；助手能力很依赖后训练和评测。
- RLHF 不等于事实正确；它更多优化偏好和行为。
- 推理模型不等于 Agent；推理强还需要工具、状态、权限和环境。
- 合成数据不是自动变好；错误合成数据会放大偏差。
- Eval 分数提升不等于真实任务可靠，仍要看部署场景和失败模式。

## 边界细节

可以把现代 LLM 变强分成两条线：

```text
模型本体变强：知识、推理、代码、指令遵循、工具格式
系统接管变强：工具执行、状态、权限、trace、评测、产品 UX
```

这也是理解 “Codex CLI / Claude Code / Hermes Agent / OMX” 的关键：强模型提供决策质量，Agent runtime 提供真实行动和边界。

评测边界也要切开：训练 pipeline 里的 evaluation 用来选择数据、奖励和模型版本；部署后的 [[Evaluation]] / [[Observability]] 用来判断某个 Agent 系统在真实工具、权限和用户任务里是否可靠。

## 现代性状态

- 判定：frontier / volatile。
- 为什么：预训练、SFT、偏好优化和评测闭环是稳定框架，但推理强化、合成数据、多模态、工具使用训练和具体后训练 recipe 仍在快速演进。
- 稳定部分：训练流水线不是单一步骤；数据、后训练和评测共同塑造模型能力。
- 易变部分：最佳数据配比、RL 方法、推理模型训练、tool-use 数据和安全评测做法会持续变化。

## 证据锚点

- Source: [[Scaling Laws for Neural Language Models]]
- Source: [[Training Compute-Optimal Large Language Models]]
- Source: [[Training Language Models to Follow Instructions with Human Feedback]]
- Source: [[Constitutional AI - Harmlessness from AI Feedback]]
- Source: [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- Source: [[The Llama 3 Herd of Models]]
- Source: [[Toolformer]]
- Anchor: [[Scaling Laws for Neural Language Models#为什么收]] / [[Training Compute-Optimal Large Language Models#为什么收]] / [[Training Language Models to Follow Instructions with Human Feedback#为什么收]] / [[Constitutional AI - Harmlessness from AI Feedback#为什么收]] / [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#为什么收]] / [[The Llama 3 Herd of Models#为什么收]] / [[Toolformer#为什么收]]
- Evidence type: paper/source notes + training/evaluation synthesis.
- Confidence: medium
- Boundary: 本卡解释训练流水线的结构；具体前沿训练 recipe 和最新模型能力需要按 source freshness 复查。

## 复习触发

- 为什么 LLM Training Pipeline 不是 Agent Framework？
- 训练阶段 evaluation 和部署后 eval harness 的区别是什么？
- “模型本体变强”和“系统接管变强”分别包括哪些能力？

## 相关链接

- [[LLM]]
- [[Transformer]]
- [[Evaluation]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Agent Framework]]
