---
type: concept
topic:
  - agent
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Planning]]"
  - "[[Tool Calling]]"
  - "[[Evaluation]]"
  - "[[ReAct]]"
  - "[[Observation]]"
---

# Agent Loop

## 一句话

Agent Loop 是 Agent 的行动循环：观察当前状态，决定下一步，执行动作，再根据反馈继续调整。

## 常见结构

```text
observe -> think/plan -> act -> evaluate/reflect -> observe
```

## 它解决什么问题

很多任务不是一次回答就结束，而是需要根据环境变化不断推进。Agent Loop 让系统能够处理多步任务和中途反馈。

[[ReAct]] 论文给了一个典型形式：reasoning trace、action 和 observation 交替出现。它说明 Agent 的“思考”应该被外部反馈不断校正。

## 它不是什么

Agent Loop 不是固定魔法公式。不同系统可能把 planning、reflection、evaluation 或 memory 放在不同位置。

## 最小例子

任务：帮我修一个测试失败。

- observe：读取错误日志。
- think：判断可能原因。
- act：修改代码。
- evaluate：重新跑测试。
- observe：如果还有错误，继续循环。

## 常见风险

- 循环没有停止条件。
- 每一步都很自信，但整体方向错了。
- 反馈信号太弱，例如只看模型自评。
- 工具结果没有被正确解释。

## ReAct 视角

```text
Thought -> Action -> Observation -> Thought -> Action
```

这个结构提醒我：Agent Loop 的关键不是“多想几步”，而是每次行动后都让 [[Observation]] 回到循环中。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Planning]]
- [[Tool Calling]]
- [[Evaluation]]
- [[ReAct]]
- [[Observation]]
