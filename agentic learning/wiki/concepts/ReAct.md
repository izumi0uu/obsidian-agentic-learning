---
type: concept
topic:
  - agent
  - reasoning
  - tool-use
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
  - "[[Tool Calling]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
---

# ReAct

## 一句话

ReAct 是让语言模型交替生成 reasoning traces 和 actions 的 Agent 模式。

## 它解决什么问题

纯推理容易脱离外部事实并产生幻觉；纯行动又缺少可解释的计划和状态跟踪。ReAct 把“想”和“做”交替起来，让工具或环境反馈修正后续推理。

## 它不是什么

ReAct 不是完整的生产级 Agent 平台。

它也不是所有 Agent 都必须采用的固定格式。真实系统可能隐藏推理、改用结构化 planner，或把行动循环封装在框架里。

## 最小例子

```text
Thought: 我需要查资料。
Action: Search[问题]
Observation: 搜索结果
Thought: 结果不够，换关键词。
Action: Search[新关键词]
```

## 边界细节

ReAct 的价值在于揭示 [[Agent Loop]] 的核心：行动不是一次性输出，而是和观察反馈绑定在一起。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Observation]]
