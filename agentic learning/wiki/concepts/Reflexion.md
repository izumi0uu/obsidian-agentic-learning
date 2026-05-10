---
type: concept
topic:
  - agent
  - reflection
  - evaluation
  - memory
status: seed
created: 2026-05-08
updated: 2026-05-10
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
---

# Reflexion

## 一句话

Reflexion 是一种让语言 Agent 在执行后生成反思文本，并把反思作为经验记忆来改进下一轮行动的机制。

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

## 证据锚点

- Source: [[Reflexion - Language Agents with Verbal Reinforcement Learning]]
- Anchor: [[Reflexion - Language Agents with Verbal Reinforcement Learning#Ingest 摘要]]
- Anchor: [[Reflexion - Language Agents with Verbal Reinforcement Learning#图片录入：Reflexion Agent Loop]]
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[Memory Reflection]]
- [[Evaluation]]
- [[Trajectory]]
- [[Trajectory Evaluation]]
- [[Long-term Memory]]
- [[Reasoning Trace]]
