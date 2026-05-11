---
type: concept
topic:
  - agent
  - tools
  - frontier
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
evidence:
  - "[[前沿主源清单#计算机使用]]"
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

## 概念详解

Computer Use 的问题背景是：模型如果只能输出文字，就不能直接完成“在界面上操作”的任务；而很多软件没有稳定 API，或者用户只愿意开放一个隔离浏览器/桌面。Computer Use 把屏幕状态变成模型可观察的信息，再把模型输出的动作交给宿主环境执行，形成观察、动作、反馈的闭环。

机制上，OpenAI source note 描述 screenshot/action loop：模型看截图，返回 click、type、scroll 等动作，宿主执行后把新截图反馈给模型。Anthropic source note 强调预定义工具、reference implementation、agent loop、token 成本和安全提醒。这些 source evidence 共同说明 Computer Use 不是一个单一工具名，而是一类 GUI 操作运行时：视觉或结构化观察、动作空间、执行器、状态反馈、失败恢复和安全策略。

它和 [[Tool Calling]] 的边界是确定性和语义层级。tool calling 通常调用结构化 API，参数和结果比较明确；computer use 操作 UI，页面状态和坐标更脆弱。它和 [[Browser Agent]] 的关系是包含：浏览器可以是 computer use 的主要场景之一。现代系统吸收它的方式通常不是让模型裸奔操作真实电脑，而是在 sandbox、allowlist、approval gate、trace 和 eval harness 里限制风险。

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

## 边界细节

Computer Use 的边界在于 GUI 脆弱性和真实世界副作用。它不是优先方案：有稳定 API 时优先 API，有确定流程时优先脚本；只有 UI 是主要入口或任务结构未知时，才需要 computer-use loop。

## 现代性状态

frontier / volatile。Computer Use 是快速演进的产品/API 能力，但底层模式较稳定：截图或结构化观察、动作输出、宿主执行、反馈循环、sandbox 和 approval。

## 证据锚点

- Evidence type: source evidence — [[前沿主源清单#计算机使用]]；[[OpenAI Computer Use 文档#为什么收]]；[[Anthropic Computer Use 文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[前沿主源清单]]；[[OpenAI Computer Use 文档]]；[[Anthropic Computer Use 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Computer Use 的观察-动作-反馈 loop 是什么？
- 为什么有稳定 API 时不应该优先用 GUI 操作？

## 相关链接

- [[Tool Calling]]
- [[Agent Loop]]
- [[Evaluation]]
- [[Browser Agent]]
- [[GUI Grounding]]
- [[Approval Gate]]
