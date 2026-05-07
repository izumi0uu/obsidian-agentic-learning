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
evidence: []
related:
  - "[[LLM]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Memory]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
---

# Agent

## 一句话

Agent 是围绕目标循环行动的系统，通常会观察状态、调用工具、更新记忆并根据反馈调整下一步。

## 它解决什么问题

普通 LLM 更像一次性生成器：给它上下文，它给出回答。Agent 试图解决的是连续任务：任务需要多步执行、读取环境、调用工具、处理失败和持续修正。

## 它不是什么

Agent 不等于聊天机器人。

Agent 不等于“会调用工具的 LLM”。

Agent 不等于完全自主的系统。很多可靠 Agent 反而会在关键步骤要求人类确认。

## 最小例子

目标：整理一个文件夹里的会议记录。

Agent 可能会：

1. 查看文件列表。
2. 读取每个文件。
3. 提取日期、参与人和决议。
4. 写入汇总表。
5. 检查是否有遗漏。

这里的关键不是“它会写总结”，而是它能围绕目标连续行动。

## 常见失败点

- 目标理解错了。
- 计划拆得太粗或太细。
- 调用了错误工具。
- 读到了过期或不完整的信息。
- 没有在高风险动作前请求确认。
- 没有评估最终结果。

## 证据锚点

- Source: 待补
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Memory]]
- [[Planning]]
- [[Evaluation]]
