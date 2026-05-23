---
type: source
source_type: article
title: "AI Engineering From Scratch - Few-Shot, Chain-of-Thought, Tree-of-Thought"
url: https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/02-few-shot-cot
author: Rohit G.
site: aiengineeringfromscratch.com
topic:
  - llm
  - prompting
  - reasoning
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
status: seed
source:
related:
  - "[[Few-shot Prompting]]"
  - "[[Few-shot CoT]]"
  - "[[Zero-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Tree of Thoughts]]"
  - "[[ReAct]]"
  - "[[Prompt Chaining]]"
---

# AI Engineering From Scratch - Few-Shot CoT

## 为什么收

这篇 lesson 的学习价值在于：它把 prompt-time reasoning 技术放进同一条成本 / 准确率 / 复杂度谱系里，而不是把 CoT、few-shot、self-consistency、ToT、ReAct 和 prompt chaining 当成互相替代的神奇短语。

它适合作为 [[LLM 主题]] 里 prompt-time reasoning 路线的课程证据，也适合给 [[Tree of Thoughts]]、[[Zero-shot CoT]] 和 [[ReAct]] 补一条“什么时候升级到更复杂策略”的边界。

## 一句话

Few-shot、CoT、Self-Consistency、ToT、ReAct 和 Prompt Chaining 都是在推理时增加结构或计算；差别在于它们分别增加示例、显式中间步骤、多次采样、树状搜索、外部观察或顺序流水线。

## 关键事实

- 课程把 zero-shot 与 few-shot 的区别定义为：zero-shot 只给任务，few-shot 先给输入 / 输出示例，让模型从示例中匹配任务格式。
- 示例选择不是随便挑；语义相似、标签覆盖和难度匹配会影响 few-shot 效果。
- CoT 的关键机制是让中间推理步骤变成后续生成的上下文；这能帮助多步数学、逻辑或符号任务，但会增加 token 成本。
- Few-shot CoT 相比 Zero-shot CoT 多了带推理步骤的 worked examples，因此更适合要求固定推理格式或高准确率的任务。
- Self-Consistency 对同一问题采样多条 CoT 路径，再对最终答案投票；它需要非零 temperature 产生多样路径，因此代价是 N 倍调用成本和延迟。
- Tree of Thoughts 把单条推理链扩展成多候选 thought 的生成、评估、剪枝和搜索，适合搜索空间大且能阶段性评估的问题。
- ReAct 把 reasoning 与 tool action / observation 交替组织起来，适合知识密集或需要外部事实回填的问题。
- Prompt Chaining 把大任务拆成多个顺序 prompt，让前一步输出成为下一步输入；它的价值在于每步更简单、中间结果可检查、不同步骤可用不同模型。
- 课程给出的工程取舍轴是准确率、延迟、成本和实现复杂度；大多数生产任务不应一开始就上最贵的策略。

## 概念拆分

- [[Few-shot Prompting]]：示例作为推理时任务定义。
- [[Few-shot CoT]]：示例不只给答案，还给推理过程。
- [[Self-Consistency]]：多条推理路径 + 最终答案投票。
- [[Tree of Thoughts]]：中途展开、评估、剪枝和搜索。
- [[ReAct]]：推理与外部 action / observation 交替。
- [[Prompt Chaining]]：多 prompt 顺序流水线。

## 边界提醒

这些技术都属于推理时 / prompt-time / runtime scaffolding，不会更新模型参数。它们能提高某些任务的表现，但不能替代事实来源、工具执行、权限控制、评测集、trace 和成本治理。

简单事实题、低风险分类、格式转换或高吞吐场景通常不需要复杂推理 scaffold。复杂 scaffold 的收益必须用任务成功率、错误类型、成本和延迟一起衡量。

## 外部链接

- Lesson: <https://aiengineeringfromscratch.com/lesson.html?path=phases/11-llm-engineering/02-few-shot-cot>
- Source markdown: <https://raw.githubusercontent.com/rohitg00/ai-engineering-from-scratch/main/phases/11-llm-engineering/02-few-shot-cot/docs/en.md>
