---
type: concept
topic:
  - evaluation
  - agent
status: growing
created: 2026-05-05
updated: 2026-05-18
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[GAIA Benchmark]]"
  - "[[SWE-bench]]"
evidence:
  - "[[GAIA Benchmark#为什么收]]"
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Agent Harness]]"
  - "[[Agent Robustness]]"
---

# Task Success Rate

## 一句话

Task Success Rate 是一组任务中端到端成功完成的比例，通常用成功任务数除以总任务数表示。

## 概念详解

Task Success Rate 是 Agent 评测里最直观的指标：任务到底有没有完成。它比“回答看起来不错”更接近真实目标，因为 Agent 往往要修改文件、订票、检索资料、调用 API 或完成多步操作。最终输出漂亮但目标没达成，success rate 仍然应该算失败。

它通常依赖 [[Eval Harness]]：harness 负责批量运行任务、提供工具或环境、收集 trace、执行 checker、判定成功/失败并汇总比例。在 [[SWE-bench]] 里，patch 通过相关测试才算 resolved；在 [[GAIA Benchmark]] 这类任务中，则需要按任务答案或标准判断完成情况。

但 success rate 是入口指标，不是完整解释。它告诉你“多少任务成功”，不告诉你失败为什么发生、过程是否安全、成本是否过高、是否绕过权限、是否污染数据。要理解这些，需要 [[Trace]]、[[Trajectory Evaluation]]、错误分类、人工 review 或更细指标。

和 [[Agent Robustness]] 的关系要看曲线而不是单点：正常集 success rate 相同的两个 Agent，在工具 timeout、噪声 observation、prompt injection 或用户不配合时，成功率下降幅度可能完全不同。Task Success Rate 是被观察的结果指标；Agent Robustness 看这个指标和过程指标在扰动下是否稳定、可恢复、可控。

Task Success Rate 的难点在于“成功”必须先被操作化。问答任务可能有标准答案；代码任务可能用测试；RAG 任务可能用引用一致性和人工评分；浏览器任务可能需要检查最终页面状态。成功定义越模糊，指标越容易被模型话术、人工宽容或 checker 漏洞污染。

在 Agent 系统里，success rate 最适合作为仪表盘第一层，而不是最后结论。它告诉你版本 A 到版本 B 是否更常完成任务；接下来还要用失败分类、trace、trajectory evaluation、cost/latency 和安全指标解释为什么变化，以及这种变化是否值得上线。

## 它解决什么问题

Agent 的输出可能看起来合理，但任务没有完成。Task Success Rate 直接问：目标有没有达成？

它适合用来比较版本：新 prompt、新模型、新工具流程是否让端到端完成率提高。

## 它不是什么

Task Success Rate 不解释失败原因。

它也不保证过程安全。一个 Agent 可能完成任务但用了高风险路径。

它也不是用户满意度、成本效率或合规性的替代指标。真实系统经常需要 success rate + safety rate + latency/cost + human escalation rate 一起看。

## 最小例子

在 SWE-bench 中，如果生成 patch 后测试通过，就算该任务成功；成功任务数除以总任务数就是 success rate。

```text
100 tasks, 37 passed checker
Task Success Rate = 37 / 100 = 37%
```

如果其中 5 个成功任务使用了未经允许的高风险工具，success rate 仍是 37%，但 trajectory/safety evaluation 应该暴露问题。

## 常见误解 / 风险

- 把 success rate 当作唯一指标：它无法说明安全、成本、鲁棒性和失败原因。
- 忽略任务难度分布：简单任务多会抬高整体比例。
- 不区分 partial success：多步任务中“做了一半”是否算成功，需要事先定义。
- checker 太弱：如果判定规则宽松，success rate 会虚高。

## 边界细节

Task Success Rate 常需要 harness 支持，因为必须自动运行任务、检查结果和复现失败。

它和相邻概念的边界：

- [[Benchmark]]：提供任务集和报告协议。
- [[Eval Harness]]：执行任务并计算 success rate。
- [[Patch Validation]]：在代码任务里常作为成功 checker。
- [[Trajectory Evaluation]]：检查成功路径是否安全、合规、经济。
- [[Agent Robustness]]：观察扰动条件下 success rate、恢复动作和安全边界是否稳定。
- [[Observability]]：解释 success rate 变化背后的过程原因。

复习时要问：这个 success 的 checker 是什么？是否允许重试？是否固定工具？是否把人工帮助算进去？这些都会改变指标含义。

## 现代性状态

- 判定：foundation / current-practice。
- 为什么：成功率是评测中的基础指标；在 Agent 场景中，它仍是核心，但必须和过程、安全、成本指标组合。
- 稳定部分：端到端任务是否完成需要被量化。
- 易变部分：不同 benchmark、平台和业务场景对“成功”的 checker 定义会变化。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: [[GAIA Benchmark#为什么收]] / [[SWE-bench#为什么收]]
- Evidence type: benchmark source notes + evaluation synthesis.
- Confidence: medium
- Boundary: 本卡解释 success rate 指标；具体 benchmark 的成功判定和最新分数需要回到对应 source。

## 复习触发

- 为什么 Task Success Rate 不能单独代表安全性？
- 在 SWE-bench 里，success rate 和 [[Patch Validation]] 怎么连接？
- 如果一个 Agent 完成任务但泄露数据，success rate 和 trajectory evaluation 会如何给出不同信号？

## 相关链接

- [[Evaluation]]
- [[Benchmark]]
- [[Agent Harness]]
- [[Agent Robustness]]
