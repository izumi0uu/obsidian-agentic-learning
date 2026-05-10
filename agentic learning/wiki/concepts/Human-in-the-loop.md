---
type: concept
topic:
  - agent
  - safety
  - workflow
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Approval Gate]]"
  - "[[Policy Engine]]"
  - "[[Handoff]]"
  - "[[Agent Loop]]"
---

# Human-in-the-loop

## 一句话

Human-in-the-loop 是在 Agent 工作流中让人类参与确认、修正、接管或提供判断的机制。

## 概念详解

Human-in-the-loop 不是“Agent 不够聪明时问一下人”，而是把人类判断设计成 workflow 的一部分。Agent 系统会遇到模型不确定、需求模糊、权限不足、事实冲突、高风险副作用、伦理或合规判断等场景；这些场景不适合完全交给模型自动推进。把人放进 loop，可以让系统在关键点澄清目标、批准动作、修正结果或直接接管。

它和 [[Approval Gate]] 有包含关系：approval gate 常是某个高风险动作前的“是否允许执行”；Human-in-the-loop 更宽，包含需求澄清、示例提供、偏好选择、结果编辑、失败接管、最终验收和持续反馈。它也和 [[Handoff]] 有交叉：handoff 可能发生在 agent 之间，也可能把任务交给人类。

工程边界是：人类介入必须有足够上下文和明确责任。只弹一个“是否继续”的按钮，如果没有说明风险、diff、成本、回滚方式和替代方案，人类也很难做有效判断。现代系统通常把 Human-in-the-loop 和 trace、policy engine、approval gate、权限层、audit log 绑定，让“什么时候问人、问什么、记录什么、拒绝后怎么办”变成可设计的控制面。

更精确地说，人类介入有三种角色：提供缺失信息、承担价值判断、批准或拒绝副作用。第一种常发生在需求不清时，例如让用户选择目标格式；第二种发生在偏好、合规或伦理判断中；第三种发生在删除、付款、发布、发信、改权限等不可逆动作前。把这些角色分开，能避免把所有问题都做成一个“是否继续”的确认框，也能让系统知道拒绝后应该重问、改计划、降级执行还是停止。
## 它解决什么问题

Agent 会遇到高风险动作、需求不清、权限不足、事实不确定和伦理/合规判断。人类介入可以降低不可逆错误。

## 它不是什么

Human-in-the-loop 不是每一步都问人。

它也不等于 [[Approval Gate]]。Approval Gate 更像某个动作前的确认点；Human-in-the-loop 更广，包括澄清、反馈、编辑、接管和最终审核。

## 最小例子

```text
Agent 生成删除数据库迁移计划
-> policy 判断为高风险
-> 人类审批或修改
-> Agent 才能执行
```

## 常见误解和风险

- 过多确认会让系统不可用。
- 人类审批如果没有足够上下文，也只是橡皮图章。
- 审批点应该由风险和权限决定，而不是模型心情决定。

## 边界细节

Human-in-the-loop 适合高风险、低确定性、价值判断强或权限敏感的节点；不适合把所有低风险步骤都变成人工确认。过多人工确认会让系统不可用，过少确认会让模型错误直接进入现实环境。

和相邻概念的区别：[[Approval Gate]] 是动作前的许可点；[[Policy Engine]] 决定何时必须许可；[[Handoff]] 描述控制权转移；Human-in-the-loop 描述人类作为反馈、判断、审批或接管者进入系统。

## 现代性状态

- 判定：current-practice
- 稳定部分：高风险动作、模糊需求和价值判断需要人类介入，是 Agent 工程的稳定边界。
- 当前工程实践：常和 approval gate、policy engine、trace、audit log、handoff 和 final review 结合。
- 易变部分：具体产品怎样呈现审批 UI、怎样记录审批证据、哪些动作默认需要确认，会随平台和组织策略变化。
- 小边界：Human-in-the-loop 不是降低所有风险的万能保险；人类必须看到足够上下文，审批才有意义。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#为什么收]]
- Evidence type: infrastructure source note + engineering synthesis.
- Confidence: medium
- Boundary: 本卡的人类澄清、审批、接管、最终审核分类是工程综合框架；具体平台实现应回到相应 product/source note 查证。

## 复习触发

- Human-in-the-loop 和 Approval Gate 的最小区别是什么？
- 什么情况下“多问用户”反而会降低系统质量？
- 设计一个删除生产数据前的人类介入点：人需要看到哪些证据？

## 相关链接

- [[Approval Gate]]
- [[Policy Engine]]
- [[Handoff]]
- [[Agent Loop]]
