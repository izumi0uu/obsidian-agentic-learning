---
type: map
topic:
  - llm
  - reasoning
  - prompting
  - comparison
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
source:
  - "[[Zero-shot CoT]]"
  - "[[Few-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Tree of Thoughts]]"
  - "[[Prompt Engineering]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]"
  - "https://platform.openai.com/docs/guides/reasoning"
  - "https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them"
  - "https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking"
  - "https://ai.google.dev/gemini-api/docs/thinking"
evidence:
  - "[[Zero-shot CoT#概念详解]]"
  - "[[Few-shot CoT#边界细节]]"
  - "[[Self-Consistency#边界细节]]"
  - "[[Zero-shot CoT#现代系统怎么吸收 Zero-shot CoT 的价值]]"
  - "[[Zero-shot CoT#和 reasoning model 的关系]]"
  - "[[Prompt Engineering#概念详解]]"
  - "[[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1-Lite-Preview 时间线补充]]"
related:
  - "[[LLM 主题]]"
  - "[[Zero-shot CoT]]"
  - "[[Few-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Tree of Thoughts]]"
  - "[[Prompt Engineering]]"
  - "[[Reasoning Trace]]"
  - "[[Token]]"
  - "[[Context Window]]"
  - "[[LLM Training Pipeline]]"
---

# CoT 与 Reasoning Tokens 边界

## 一句话总览

[[Zero-shot CoT]] 是 prompt 层的显式推理触发方法；reasoning tokens 是 reasoning model 在输出最终答案前消耗的内部推理预算；“一步步思考”对复杂推理有用，但对“法国首都是什么”这类单跳事实题通常只是改变输出形式，收益很小。

## 为什么这组值得总结

这组概念容易被一句话混掉：“现在模型是不是已经内置 CoT 了？”更稳的回答是：现代模型吸收了 CoT 的价值，但吸收位置发生了变化。

- prompt-era：用户在 prompt 里显式要求“step by step”，模型把中间推理写进可见输出。
- reasoning-model era：模型在训练、后训练或推理时计算预算里学会更长的分解、验证和反思，用户未必看到完整思维链。
- product/API era：供应商把这类内部推理暴露为 reasoning effort、thinking budget、extended thinking 等控制面或摘要，而不是直接返回完整 chain-of-thought。

边界：这页是学习综合，不把各家产品参数写成同一个标准字段。具体模型是否暴露 reasoning summary、如何计费、是否允许调 thinking budget，需要回到当日官方文档。

## 核心区别表

| 问题 | 应看概念 | 最小判断 | 常见误解 |
|---|---|---|---|
| “Zero-shot CoT 现在内置了吗？” | [[Zero-shot CoT]] / reasoning model | CoT 的价值被很多模型训练化、产品化，但经典 Zero-shot CoT 仍是 prompt 方法 | 把“模型会推理”直接等同于“内置了那句 prompt” |
| “简单事实题加一步步思考会怎样？” | [[Prompt Engineering]] / [[Token]] | 可能触发解释型输出，但通常没有推理收益，还会增加 token 和延迟 | 任何问题都应该 CoT |
| “internal reasoning tokens 是什么？” | reasoning model / [[Token]] | 模型内部推理预算，通常不可见，但会影响输出预算、成本和延迟 | 把隐藏 reasoning tokens 当成可见思维链 |
| “完整 CoT 是否应该展示给用户？” | [[Reasoning Trace]] / safety boundary | 多数生产场景更适合展示简要依据、检查项或可验证中间产物 | 可见推理越长越可信 |

## 三层边界

### 1. 显式 CoT 输出

经典 Zero-shot CoT 的结构是：

```text
Prompt + "let's think step by step" -> visible reasoning steps -> answer
```

它的价值在于让中间文本进入后续上下文，帮助模型展开多步关系。局限也明显：它是单路径文本推理，没有工具、没有外部 observation、没有 evaluator，也不保证中间步骤真实或正确。

如果问题的关键不是“把一条链写完整”，而是“在多个候选方向之间搜索和回溯”，边界就进入 [[Tree of Thoughts]]：它仍然属于 prompt-time / inference-time reasoning scaffold，但已经从单链 CoT 升级为多分支候选生成、评估和剪枝。

在这两者之间还有两个常见增强：[[Few-shot CoT]] 用带推理步骤的 worked examples 让模型模仿推理格式，[[Self-Consistency]] 则对同一问题采样多条推理链并聚合最终答案。它们仍是 prompt-time / inference-time 策略，不改变模型参数，也不等于 tool-using agent；差别在于一个用示例约束格式，另一个用更多采样成本换鲁棒性。

### 2. 内部 reasoning tokens

reasoning tokens 更像 hidden scratchpad / internal reasoning budget：

```text
input tokens -> hidden/internal reasoning tokens -> visible output tokens
```

这些 token 通常不会作为完整原始思维链返回给用户，但会影响模型在回答前能做多少内部拆解、比较和检查。工程上要记住两个小边界：

- 看不见不等于免费；内部推理仍会占预算、成本和延迟。
- 有内部推理不等于答案可靠；事实题仍需要事实来源，工具题仍需要工具执行，高风险任务仍需要验证。

### 3. Reasoning model / thinking mode

DeepSeek-R1、OpenAI reasoning models、Claude extended thinking、Gemini thinking budget 这类产品或模型路线，把“先展开推理再回答”的价值从 prompt 字符串提升到模型行为或 API 控制面。

更精确的记法：

```text
Zero-shot CoT: 普通模型 + prompt 触发显式推理文本
Reasoning model: 训练/后训练/推理预算塑造内部或半透明推理行为
```

所以可以说现代 reasoning model 继承了 CoT 研究脉络，但不能说它们只是“自动帮你加了 step by step”。

## 简单事实题的判断

“法国的首都是什么？”这类问题属于单跳事实题。模型如果知道答案，直接输出“巴黎”就够了。

加上“一步步思考”后，模型可能生成：

```text
法国是一个国家。
法国的首都是巴黎。
所以答案是巴黎。
```

这不是有价值的多步推理，只是把输出风格改成了解释型。对这类问题，CoT 的主要副作用是增加 token、延迟和无意义解释；极端情况下还可能因为过度解释引入错误分支。

## 什么时候该显式要求推理

更适合要求结构化推理的场景：

- 多步数学、逻辑推导、代码调试。
- 需求分析、方案比较、架构取舍。
- 需要先列约束、失败模式、检查清单的任务。
- 需要把推理产物变成 plan、rubric、test case 或可验证中间件的任务。

不太适合显式 CoT 的场景：

- 简单事实问答、短分类、格式转换。
- 纯检索型问题，除非要求解释证据选择。
- 高风险事实结论；这里更需要来源、工具、引用和验证，而不是更长推理链。

## Prompt 写法边界

现代 reasoning model 上，不必机械添加“请一步步思考”。更稳的 prompt 是给清楚目标、约束和输出形态：

```text
请直接给结论；如果问题需要多步推理，先在内部检查约束，
最后只输出简要依据和可验证结论。
```

如果你需要复盘或教学，可以要求：

```text
请给出简要推理摘要、关键假设、检查点和最终答案。
```

小边界：要求“简要依据 / 检查点 / 可验证步骤”比要求“完整思维链”更适合生产系统，因为它保留审查价值，同时减少泄露、不稳定解释和冗长 token 成本。

## 现代性状态

判定：foundation + current-practice + watch。

- foundation：显式中间推理能帮助复杂任务拆解，是稳定学习地基。
- current-practice：现代系统会把 CoT 价值吸收到 internal reasoning、plan artifact、rubric、tool decision、trace summary 和 evaluator 中。
- watch：各供应商对 reasoning tokens / thinking budget / extended thinking 的命名、可见性、计费和 API 控制方式会变化，需要按官方文档复查。

## 证据锚点

- [[Zero-shot CoT#概念详解]]：支持 Zero-shot CoT 是 prompt 层显式推理触发方法。
- [[Zero-shot CoT#现代系统怎么吸收 Zero-shot CoT 的价值]]：支持现代系统不一定展示完整 CoT，而是转成计划、检查清单、rubric 或可验证中间产物。
- [[Zero-shot CoT#和 reasoning model 的关系]] / [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning#R1-Lite-Preview 时间线补充]]：支持 reasoning model 和经典 Zero-shot CoT prompt 的层级区别。
- OpenAI reasoning docs / tokens help：支持 reasoning model、reasoning effort、reasoning token 与输出预算的官方边界。
- Anthropic extended thinking docs / Gemini thinking docs：支持不同供应商把内部推理能力暴露为不同 API 控制面的事实。
- Evidence type: existing concept cards + raw paper source note + official provider docs + learning synthesis.
- Confidence: high for Zero-shot CoT / reasoning model boundary; medium for provider-specific API details，因为它们会随产品更新。
- Boundary: 本页不记录价格、具体模型可用性或完整参数表；这些属于 volatile 产品细节。

## 复习触发

1. 为什么“现代模型会推理”不等于“Zero-shot CoT 内置”？
2. 对“法国首都是什么”加“一步步思考”，到底改变的是任务能力还是输出分布？
3. internal reasoning tokens 和可见 chain-of-thought 的最小区别是什么？
4. 什么场景应该要求简要依据，而不是完整思维链？

## 相关链接

- [[LLM 主题]]
- [[Zero-shot CoT]]
- [[Few-shot CoT]]
- [[Self-Consistency]]
- [[Tree of Thoughts]]
- [[Prompt Engineering]]
- [[Reasoning Trace]]
- [[Token]]
- [[Context Window]]
- [[LLM Training Pipeline]]
