---
type: concept
topic:
  - evaluation
  - observability
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Langfuse Observability and Evaluation#为什么收]]"
related:
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Eval Harness]]"
---

# Replay

## 一句话

Replay 是用保存的输入、工具结果、检索结果或环境快照重放 Agent 执行过程，让失败可以复现、比较和回归测试。

## 概念详解

Replay 解决的是 Agent 调试里最痛的事：失败发生过，但下一次运行不一定复现。模型采样、外部网页、API 返回、检索索引、时间、权限和用户状态都可能变化。没有 replay，团队只能猜“刚才为什么失败”；有 replay，失败 trace 可以变成可重复实验。

Replay 通常依赖 [[Trace]]，但比 trace 要求更高。Trace 记录发生了什么；Replay 还需要足够的输入、工具返回、环境快照、随机种子或 mock，使系统能在可控条件下再次走过相同或相似路径。对 eval harness 来说，replay 是把线上失败转成 regression case 的桥：先保存失败样本，再固定变量，最后用新策略重跑，看是否真的修复。

它也有层级：轻量 replay 只重放模型输入输出；中等 replay 固定检索结果和工具返回；强 replay 还保存浏览器 DOM、文件系统、数据库快照或 sandbox 状态。层级越强，可复现性越好，成本和隐私风险也越高。


Replay 的关键不是“完全重复过去”，而是明确复现实验的控制变量。对于 RAG，可以固定 query、检索结果、rerank 输入和生成 prompt；对于 coding agent，可以固定 repo commit、依赖、测试命令和失败日志；对于 browser agent，可以固定截图、DOM、accessibility tree 和动作序列。固定得越清楚，修复前后比较才越有意义。

它也能帮助评估 prompt 或 workflow 变更：把过去失败的 trace 转成 replay dataset，用新版本重跑。如果新版本只在随机重试中偶然成功，而不是在固定条件下稳定改善，就不能轻易声称问题已修复。

## 它解决什么问题

Agent 失败后，如果不能复现，就很难知道修复是否有效。Replay 让一次失败可以变成可调试、可比较、可回归测试的样本。

它还帮助区分“模型这次随机答错”与“工作流/工具/检索设计稳定有缺陷”。

## 它不是什么

Replay 不是重新问模型同一个问题。

真正的 replay 要尽量控制变量：相同输入、相同工具返回、相同检索材料、相同环境状态，或者明确标注哪些部分被重新采样了。

Replay 也不是完整 [[Evaluation]]。它提供可重复样本；是否成功仍需要 checker、rubric、judge、测试或人工 review。

## 最小例子

一次 Browser Agent 点错按钮：

- 保存截图序列。
- 保存每次 action。
- 保存 DOM 或 accessibility snapshot。
- 修复策略后重放，检查它是否还会点错。

如果外部网站已经变化，就要明确这是 partial replay：只能验证策略在旧 snapshot 上是否改善，不能证明真实网站上一定成功。

## 常见误解 / 风险 / 边界细节

- 外部网站变化会破坏 replay。
- 工具结果如果没有固定，会让结果不可比较。
- replay 数据可能包含敏感内容。
- replay 更适合调试失败，不等于完整可靠性评估。
- 重放旧环境可能让系统“修好过去”，但没有覆盖新的真实分布。

## 边界细节

Replay 和相邻概念的边界：

- [[Trace]]：保存执行记录；Replay 使用记录和快照重建执行条件。
- [[Observability]]：帮助发现值得 replay 的失败；Replay 把失败转成可重复样本。
- [[Eval Harness]]：批量运行 replay case、比较版本、记录结果。
- [[Benchmark]]：固定公共任务集；Replay 更常来自线上或开发过程中的具体失败样本。

设计 replay 时要标注“固定了什么，重新采样了什么”。如果模型输出重新采样、工具结果实时获取、环境没有快照，那么结果只能说明“再次运行表现”，不能称为严格 replay。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 为什么：trace-driven debugging、dataset replay、failure regression 已经是 Agent eval/observability 平台的重要方向；但浏览器、电脑使用、多工具环境的强 replay 仍然实现复杂。
- 稳定部分：失败样本应该能回放或转成 regression eval。
- 易变部分：平台 replay API、环境快照格式、浏览器/桌面状态保存和隐私策略。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Langfuse Observability and Evaluation]]
- Anchor: [[LangSmith Evaluation and Observability#为什么收]] / [[Langfuse Observability and Evaluation#为什么收]]
- Evidence type: observability/evaluation platform source notes + engineering synthesis.
- Confidence: medium
- Boundary: “失败样本可重复”是稳定价值；完整环境 replay 的实现能力和成本随平台变化。

## 复习触发

- 为什么 Replay 不是“再问一次模型”？
- 一个 RAG Agent 的 replay 至少要固定哪些输入或工具结果？
- Replay、[[Trace]]、[[Eval Harness]] 如何形成失败回归闭环？

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Eval Harness]]
- [[Sandbox Workspace]]
