---
type: concept
topic:
  - llm
  - agent
  - tool-use
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Toolformer]]"
evidence:
  - "[[Toolformer#为什么收]]"
related:
  - "[[Tool Calling]]"
  - "[[Agent]]"
  - "[[LLM]]"
---

# Tool Use

## 一句话

Tool Use 是模型或 Agent 使用外部工具来补足自身能力的行为。

## 它解决什么问题

LLM 不能天然访问实时信息、精确计算、调用 API 或操作环境。工具使用让系统可以把这些任务交给外部能力完成。

## 它不是什么

Tool Use 不等于 Agent。

会使用工具只是能力之一。Agent 还需要目标、状态、规划、反馈循环、权限和评估。

## 最小例子

模型遇到数学计算时调用 calculator，遇到事实问题时调用 search，遇到日期问题时调用 calendar。

## 边界细节

[[Tool Calling]] 更偏接口和结构化调用；Tool Use 更偏能力和行为。

## 证据锚点

- Source: [[Toolformer]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Tool Calling]]
- [[Agent]]
- [[LLM]]
