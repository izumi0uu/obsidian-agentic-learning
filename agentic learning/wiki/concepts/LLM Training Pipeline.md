---
type: concept
topic:
  - llm
  - training
  - evaluation
status: seed
created: 2026-05-09
updated: 2026-05-09
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
last_checked: 2026-05-09
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

## 证据锚点

- Source: [[Scaling Laws for Neural Language Models]]
- Source: [[Training Compute-Optimal Large Language Models]]
- Source: [[Training Language Models to Follow Instructions with Human Feedback]]
- Source: [[Constitutional AI - Harmlessness from AI Feedback]]
- Source: [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- Source: [[The Llama 3 Herd of Models]]
- Source: [[Toolformer]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[Transformer]]
- [[Evaluation]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Agent Framework]]
