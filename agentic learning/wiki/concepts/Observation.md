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
  - "[[Agent Loop]]"
  - "[[ReAct]]"
  - "[[Tool Calling]]"
---

# Observation

## 一句话

Observation 是 Agent 执行动作后从环境或工具得到的反馈。

## 它解决什么问题

Agent 需要知道自己的动作产生了什么结果，才能决定下一步。Observation 把外部世界的状态带回循环中。

## 它不是什么

Observation 不是模型自己的想法。

它也不一定可信。网页、工具返回值或环境状态可能错误、过期或被恶意污染。

## 最小例子

Agent 调用搜索工具，搜索结果摘要就是 observation；代码 Agent 运行测试，测试失败日志也是 observation。

## 边界细节

没有 observation，Agent Loop 容易退化成一次性计划生成。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[ReAct]]
- [[Tool Calling]]
