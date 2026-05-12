---
type: concept
topic:
  - agent
  - reflection
  - evaluation
  - memory
status: growing
created: 2026-05-08
updated: 2026-05-12
source:
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning]]"
evidence:
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#为什么收]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#Ingest 摘要]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#图片录入：Reflexion Agent Loop]]"
last_checked: 2026-05-10
freshness: stable
conflicts: []
related:
  - "[[Agent Loop]]"
  - "[[Memory Reflection]]"
  - "[[Evaluation]]"
  - "[[Trajectory]]"
  - "[[Trajectory Evaluation]]"
  - "[[Long-term Memory]]"
  - "[[Reasoning Trace]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
---

# Reflexion

## 一句话

Reflexion 是一种让语言 Agent 在执行后生成反思文本，并把反思作为经验记忆来改进下一轮行动的机制。

## 概念详解

Reflexion 的核心不是“让模型想一想”，而是把失败轨迹、评价反馈和下一轮行动连接起来。Agent 完成一次尝试后，系统读取 [[Trajectory]] 或最终结果，由 evaluator 给出成功/失败或更细反馈；然后 self-reflection 把反馈转成自然语言经验，写入后续上下文或记忆。下一轮 Actor 再利用这段经验，避免重复同类错误。

它重要的原因是：很多 Agent 错误不是知识缺失，而是策略错误、约束遗漏、工具顺序不当或观察误读。Reflexion 试图用语言形式的经验做“轻量学习”，不改模型权重，也能在同一任务或同类任务上改善行为。

从 evaluation 角度看，Reflexion 依赖 evaluator 的质量。错误反馈会生成错误经验，污染后续行动；过宽的成功判断会让 Agent 学不到边界。因此 Reflexion 不能替代 [[Trajectory Evaluation]]、外部 checker、工具验证或人工确认，而是把评价结果转成可复用经验的一种机制。


Reflexion 也可以理解为一种“语言层的 credit assignment”。执行失败后，系统要把失败归因到某个可改变的策略：没有先读题、没有验证工具结果、忽略预算、过早提交答案、没有处理异常。Self-reflection 把这种归因写成下一轮可读的经验。经验写得太泛，就无法改变行为；写得太具体，又可能只适用于一个偶然场景。

这也是它和普通 memory 的边界：Reflexion 里的经验应该来自可追溯的 trajectory 和 evaluator feedback，而不是模型随手生成的座右铭。是否写入长期记忆，需要看反馈是否可靠、是否可泛化、是否会与更高优先级规则冲突。

## 它解决什么问题

Agent 失败后，如果只重新运行一次，可能会重复同样错误。Reflexion 让 Agent 把失败轨迹和评价反馈转成自然语言经验，例如“我刚才没有先确认约束，所以后续搜索方向错了”。

这段经验会进入后续上下文或记忆，让下一轮 Actor 能避开同类错误。

## 它不是什么

Reflexion 不是普通的 [[Reasoning Trace]]。

Reasoning Trace 更偏行动前或行动中的推理痕迹；Reflexion 的 reflective text 更偏行动后的经验总结。

Reflexion 也不是 [[Memory Reflection]] 的同义词。Memory Reflection 偏从历史中总结长期记忆；Reflexion 偏一次任务尝试后，根据评价反馈改进下一轮行动。

Reflexion 不是模型权重训练。它主要通过语言形式的经验写入和上下文再利用来学习。

## 最小例子

```text
Task: 在网页环境里完成购买比较。
Actor: 直接搜索商品，忽略预算限制，失败。
Evaluator: 任务失败，因为结果超预算。
Self-reflection: 下次搜索前先提取预算约束，并把预算作为筛选条件。
Next trial: Actor 读取这条经验，再重新行动。
```

## 常见误解

- 不是所有“请检查答案”都是 Reflexion；Reflexion 需要反馈、轨迹、反思文本和后续再利用。
- 反思文本不一定正确，错误 feedback 会生成错误经验。
- 写入长期记忆前需要审查，否则一次失败可能污染之后的任务。
- Reflexion 能改善行为，但不能替代外部评测、工具校验或人工确认。

## 边界细节

可以把 Reflexion 看成一个三步循环：

```text
执行 -> 评价/反馈 -> 反思 -> 再执行
```

论文图里的更细结构是：

```text
Trajectory -> Evaluator -> Self-reflection -> Experience -> Actor
Actor -> Action -> Environment -> Observation -> Trajectory
```

其中：

- [[Trajectory]] 是短期记忆，记录当前尝试的过程。
- Evaluator 把轨迹或结果转成反馈信号。
- Self-reflection 把反馈转成 reflective text。
- Experience 是长期经验记忆，影响下一轮 Actor。

![[reflexion-agent-loop.svg]]

## 现代性状态

- 判定：foundation / transitional。
- 为什么：Reflexion 是理解“轨迹 -> 评价 -> 反思 -> 再行动”的经典 Agent 机制；现代系统常把它的价值吸收到 eval harness、memory、failure summarization 和 retry policy 中。
- 稳定部分：失败反馈可以转成经验，影响下一轮行为。
- 易变部分：现代产品是否显式叫 Reflexion、反思写入哪里、如何防止错误经验污染，会随框架和安全策略变化。

## 证据锚点

- Source: [[Reflexion - Language Agents with Verbal Reinforcement Learning]]
- Anchor: [[Reflexion - Language Agents with Verbal Reinforcement Learning#Ingest 摘要]]
- Anchor: [[Reflexion - Language Agents with Verbal Reinforcement Learning#图片录入：Reflexion Agent Loop]]
- Evidence type: paper source note + concept diagram asset + Agent evaluation synthesis.
- Confidence: medium
- Boundary: 图示是 Reflexion 论文机制的学习锚点；现代系统可能用不同实现吸收其“失败经验回流”价值。

## 复习触发

- Reflexion 和普通 Reasoning Trace 的区别是什么？
- 如果 evaluator 给错反馈，Reflexion 会发生什么风险？
- 用“Trajectory -> Evaluator -> Self-reflection -> Experience -> Actor”复述 Reflexion loop。

## 相关链接

- [[Agent Loop]]
- [[Memory Reflection]]
- [[Evaluation]]
- [[Trajectory]]
- [[Trajectory Evaluation]]
- [[Long-term Memory]]
- [[Reasoning Trace]]
- [[ReAct Plan-and-Solve Reflexion 对比]]
