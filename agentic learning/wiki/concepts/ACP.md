---
type: concept
topic:
  - agent
  - protocol
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent Communication Protocol]]"
evidence:
  - "[[Agent Communication Protocol#为什么收]]"
related:
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Agent]]"
---

# ACP

## 一句话

ACP 是 Agent Communication Protocol，关注 Agent、应用和人之间的标准化消息通信。

## 概念详解

ACP 的问题背景和 A2A 相近：Agent 生态里会出现不同框架、不同服务、不同交互界面之间的通信需求。source note 强调 ACP 来自 BeeAI / IBM / Linux Foundation 生态，关注 RESTful API、多模态消息、同步/异步、streaming、发现和长任务。这些关键词说明 ACP 想处理的不是“模型怎么调用一个函数”，而是“一个可长期运行的 Agent 服务怎样被另一个系统、人或应用调用”。

机制上，ACP 可以理解为把 Agent 暴露成网络服务时需要的通信约定：消息结构、任务生命周期、结果返回、流式进度、发现能力和生产级安全/观测边界。它让 Agent 不只存在于本地脚本或聊天窗口里，而能成为可连接的系统组件。但协议只定义连接形状，不能替代授权、沙箱、审计、评测和业务失败处理。

ACP 的学习价值在于暴露“Agent 通信协议需要解决哪些问题”。它和 A2A 的边界还在演化，尤其当生态合并或迁移时，具体字段可能变化。不要把 ACP 当作稳定历史定论；更稳的理解是：Agent 服务化后，需要一层比普通 REST API 更懂任务、消息、状态和人机协作的协议。

从学习角度看，ACP 把“Agent 作为服务”这件事拆开了：服务发现回答“谁能做”；消息结构回答“怎么表达任务和上下文”；同步/异步与 streaming 回答“长任务如何回报进度”；production-grade 边界回答“身份、安全和观测怎么接入”。这些问题比某个字段名更稳定，也更适合作为概念卡的长期价值。


## 它解决什么问题

Agent 需要异步任务、streaming、多模态消息、状态更新、发现和长任务交互。ACP 提供一套协议化的通信方式，让不同实现可以更容易互操作。

## 它不是什么

ACP 不是具体 Agent 产品。

它也不是长期完全稳定的基础概念。它处于协议演化和生态整合中，更适合作为“Agent 互操作问题”的观察入口。

## 最小例子

一个 UI 应用通过 ACP 给研究 Agent 发任务，研究 Agent streaming 返回计划、进度和最终结果，期间还可以请求用户补充文件或确认动作。

## 常见误解 / 风险 / 边界细节

- 看到 ACP 要先问版本和生态归属。
- 协议格式变化快时，不要把字段细节背成概念。
- 通信协议不能替代权限、审计和评测。
- 和 A2A 的边界可能随着生态合流而变化。

## 边界细节

ACP 的稳定价值是“Agent 服务如何通信”的问题框架；具体字段、生态归属和实现方式可能迁移。不要把 ACP 当成本地多 Agent 编排器，也不要把普通 REST API 只因返回文本就叫 ACP。

## 现代性状态

frontier / volatile。ACP 处在 Agent 通信协议快速演化和迁移阶段，适合用来理解 Agent 服务化、长任务和多模态消息边界；具体生态位置需要按 last_checked 复查。

## 证据锚点

- Evidence type: source evidence — [[Agent Communication Protocol#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Agent Communication Protocol]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- ACP 想解决的通信问题，普通 REST API 为什么不一定够？
- 为什么 ACP 的具体实现细节要按 last_checked 复查？

## 相关链接

- [[A2A]]
- [[MCP]]
- [[Agent]]
- [[Observability]]
