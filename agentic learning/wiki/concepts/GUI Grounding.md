---
type: concept
topic:
  - agent
  - computer-use
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
evidence:
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
related:
  - "[[Computer Use]]"
  - "[[Browser Agent]]"
  - "[[Observation]]"
---

# GUI Grounding

## 一句话

GUI Grounding 是模型把屏幕图像、控件、坐标和页面状态对应到可执行动作的能力。

## 概念详解

GUI Grounding 的问题背景是模型要操作界面时，必须把“用户想点哪里”和“屏幕上哪个元素能被操作”对齐。语言模型可以描述意图，但 UI 是像素、坐标、DOM、可访问性节点、窗口状态和时间变化的组合。没有 grounding，模型可能点错按钮、在错误输入框输入、忽略弹窗，或把视觉上相似的元素混淆。

机制上，GUI grounding 通常把观察表示转成可操作目标：截图中的坐标、可访问性树中的节点、DOM selector、OCR 文本或浏览器工具返回的元素句柄。Computer Use 文档把截图/action loop 作为主线；Anthropic source note 提醒失败可能来自 UI 状态、坐标、登录态、弹窗、权限或页面变化。这说明 GUI grounding 既是模型感知问题，也是运行时反馈和错误恢复问题。

它和 [[Observation]] 有包含关系：observation 是 Agent 读取环境反馈的总称，GUI grounding 是 GUI 场景里把观察落到可执行元素的能力。它和 [[Browser Agent]] 也不同：Browser Agent 是任务形态，GUI grounding 是其中的关键子能力。稳定业务流程如果能用 API 或 selector，就不要只依赖视觉 grounding；视觉路径适合未知或难以结构化的界面，但更需要 sandbox、重试和审批。

GUI grounding 的难点还在于 UI 不是静态图片。加载延迟、响应式布局、滚动位置、hover 状态、modal、验证码、浏览器缩放和语言区域都会改变“同一个按钮”在观察中的表示。工程系统通常会把视觉观察、可访问性树、DOM 查询、动作后截图和错误重试结合起来，让模型不必只凭一次截图做不可逆判断。


## 它解决什么问题

Computer Use 不只是“看截图”。模型必须知道按钮在哪里、文本框是否聚焦、点击哪个坐标、动作后页面是否变化。

## 它不是什么

GUI Grounding 不是理解网页文字。

理解“这个页面讲什么”是一回事；准确点击“右上角保存按钮”是另一回事。

## 最小例子

模型看到截图后判断：

- 搜索框在页面上方。
- 需要点击输入框坐标。
- 输入 `agentic retrieval`。
- 按 Enter。

这就是从视觉观察到 UI 动作的 grounding。

## 常见误解 / 风险 / 边界细节

- 截图分辨率会影响点击精度。
- 弹窗、滚动位置、缩放比例会改变坐标。
- DOM/accessibility tree 和截图各有优缺点。
- 失败可能来自界面状态，不一定来自推理能力。

## 边界细节

GUI Grounding 只解决“把观察落到可操作元素”这一层，不保证任务策略正确。坐标、DOM、可访问性树和截图各有误差；生产场景要结合确认、重试、截图记录和可回滚执行。

## 现代性状态

frontier / volatile。GUI grounding 随多模态模型、可访问性树、浏览器工具和 computer-use API 快速变化。稳定的是“观察必须落到可执行目标”的问题。

## 证据锚点

- Evidence type: source evidence — [[OpenAI Computer Use 文档#为什么收]]；[[Anthropic Computer Use 文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OpenAI Computer Use 文档]]；[[Anthropic Computer Use 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- GUI grounding 要把哪些观察表示落到可操作目标？
- 它为什么不等于任务策略正确？

## 相关链接

- [[Computer Use]]
- [[Browser Agent]]
- [[Observation]]
- [[Trace]]
