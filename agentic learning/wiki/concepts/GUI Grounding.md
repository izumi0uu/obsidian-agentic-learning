---
type: concept
topic:
  - agent
  - computer-use
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
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

## 证据锚点

- Source: [[OpenAI Computer Use 文档]]
- Source: [[Anthropic Computer Use 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Computer Use]]
- [[Browser Agent]]
- [[Observation]]
- [[Trace]]
