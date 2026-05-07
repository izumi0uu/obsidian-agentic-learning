---
type: concept
topic:
  - agent
  - tools
  - frontier
status: seed
created: 2026-05-05
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
related:
  - "[[Tool Calling]]"
  - "[[Agent Loop]]"
  - "[[Evaluation]]"
  - "[[Browser Agent]]"
  - "[[GUI Grounding]]"
---

# Computer Use

## 一句话

Computer Use 是让模型或 Agent 通过浏览器、桌面、终端、鼠标键盘或屏幕理解来操作计算机。

## 它解决什么问题

很多任务没有稳定 API，只能通过网页、GUI 或已有软件完成。Computer Use 让 Agent 可以像人一样观察界面并执行动作。

## 它不是什么

Computer Use 不是普通函数调用。

函数调用通常是结构化 API；Computer Use 面对的是屏幕、控件、坐标、页面状态和失败恢复。

## 最小例子

Agent 打开网页，搜索资料，点击结果，读取页面，返回总结。

## 常见误解 / 风险 / 边界细节

- 点错按钮。
- 被网页中的 prompt injection 影响。
- 表单提交前没有人工确认。
- 读取到错误页面状态。
- 稳定重复任务可能更适合 API 或脚本，而不是让模型每次看屏幕。
- Computer Use 的能力边界常被环境影响：分辨率、登录态、弹窗、滚动位置都可能改变结果。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[OpenAI Computer Use 文档]]
- Source: [[Anthropic Computer Use 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Tool Calling]]
- [[Agent Loop]]
- [[Evaluation]]
- [[Browser Agent]]
- [[GUI Grounding]]
- [[Approval Gate]]
