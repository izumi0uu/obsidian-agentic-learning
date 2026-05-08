---
type: concept
topic:
  - llm
  - reasoning
  - planning
status: seed
created: 2026-05-08
updated: 2026-05-08
source:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
evidence:
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#为什么收]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]"
last_checked: 2026-05-08
freshness: stable
conflicts: []
related:
  - "[[Planning]]"
  - "[[Reasoning Trace]]"
  - "[[ReAct]]"
  - "[[Agent Loop]]"
---

# Plan-and-Solve Prompting

## 一句话

Plan-and-Solve Prompting 是一种提示方法：先让 LLM 写出解题计划，再让它按计划完成推理。

## 它解决什么问题

普通 Zero-shot Chain-of-Thought 常用 “Let's think step by step” 触发逐步推理，但模型可能漏掉关键步骤。

Plan-and-Solve 先要求模型生成 plan，相当于先搭一个任务骨架，再逐步填答案。这样尤其针对 missing-step error：不是算错某一步，而是根本没做某一步。

## 它不是什么

Plan-and-Solve Prompting 不是 [[ReAct]]。

它没有外部 Action，也没有 [[Observation]] 反馈。它解决的是一次推理回答中的“先规划再求解”，不是 Agent 在环境中循环行动。

它也不是完整 [[Agent]] 框架。它不处理工具权限、状态持久化、失败重试、trace、评测或 human-in-the-loop。

## 最小例子

```text
Question: 一道多步数学题

Plan:
1. 找出已知条件。
2. 写出需要计算的中间量。
3. 用中间量得到最终答案。

Solve:
按计划逐步计算，并给出答案。
```

## 常见误解

不要把“模型写了计划”直接等同于“模型真的会执行计划”。

计划文本本身也可能幻觉、漏项或过度抽象。没有工具反馈和评测时，它只是更有结构的 reasoning trace，不是可靠执行保证。

## 边界细节

可以把它放在三层里理解：

- [[Reasoning Trace]] 层：计划和求解都还是模型生成的文本。
- [[Planning]] 层：它让规划出现在回答前，但规划不会随环境反馈动态更新。
- [[Agent Loop]] 层：它还没进入行动循环；一旦加入工具调用、观察反馈、状态保存和重试，才更接近 Agent。

和 [[ReAct]] 的最小区别：

```text
Plan-and-Solve: Plan -> Solve -> Answer
ReAct: Thought -> Action -> Observation -> Thought -> ...
```

用户提供的 Planning Phase / Solving Phase 图里出现了 Task Agent、Exec、Loop 和 Replan。那张图更接近 plan-and-execute workflow：它把计划变成任务清单，并在执行阶段允许重新规划。它可以帮助理解 planning 的工程形态，但不要直接当成 Plan-and-Solve Prompting 论文方法本身。

## 证据锚点

- Source: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]
- Anchor: [[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models#Ingest 摘要]]
- Confidence: medium

## 相关链接

- [[Planning]]
- [[Reasoning Trace]]
- [[ReAct]]
- [[Agent Loop]]
