---
type: concept
topic:
  - agent
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
related:
  - "[[ReAct]]"
  - "[[Agent Loop]]"
  - "[[Trajectory Trace 类型对比]]"
  - "[[Trace]]"
  - "[[Trajectory]]"
---

# Reasoning Trace

## 一句话

Reasoning Trace 是模型在解决任务过程中显式留下的推理轨迹。

## 它解决什么问题

推理轨迹能帮助跟踪计划、解释中间决策、发现错误传播，也能让人更容易理解 Agent 为什么采取某个动作。

## 它不是什么

Reasoning Trace 不一定等于模型真实内部原因。

它也不一定应该暴露给用户。生产系统可能只保留结构化 trace 或摘要，而不展示完整推理文本。

Reasoning Trace 也不等于 [[Trajectory]]。Trajectory 是一次任务的完整行动路径；Reasoning Trace 只是这条路径里模型显式推理文字的部分。

## 最小例子

ReAct 里的 `Thought` 字段就是一种 reasoning trace。

## 边界细节

Reasoning Trace 偏“推理文字”；[[Trace]] 更广，包括输入、输出、工具调用、工具结果、状态变化和成本延迟等执行记录；[[Trajectory]] 则偏任务实际走过的路径本身。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[ReAct]]
- [[Trajectory Trace 类型对比]]
- [[Trace]]
- [[Trajectory]]
- [[Agent Loop]]
