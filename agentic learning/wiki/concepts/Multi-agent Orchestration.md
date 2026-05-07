---
type: concept
topic:
  - agent
  - workflow
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[Oh My Codex Repo]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[Oh My Codex Repo#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Agent Harness]]"
  - "[[Handoff]]"
  - "[[Oh My Codex (OMX)]]"
---

# Multi-agent Orchestration

## 一句话

Multi-agent Orchestration 是把多个 Agent 按角色、任务边界、交接规则和验证流程组织起来，让它们协作完成一个单 Agent 难以高效完成的任务。

## 它解决什么问题

复杂任务往往包含不同工作面：需求澄清、架构判断、代码实现、测试验证、安全审查、文档更新。

多 Agent 编排让这些工作可以拆成不同 lane：

- planner 负责计划。
- executor 负责实现。
- verifier 负责验证。
- critic 负责审查风险。
- leader 负责整合结果和最终判断。

[[Oh My Codex (OMX)]] 的 `$team` 就是代码 Agent 场景里的一个具体例子：多个 worker 在不同 worktree 里并行处理任务，再由 leader 整合。

## 它不是什么

Multi-agent Orchestration 不是“Agent 越多越好”。

如果任务边界不清、文件高度重叠、验证标准模糊，多 Agent 只会增加沟通成本、冲突和错误面。

它也不是 [[A2A]]。A2A 偏跨系统 Agent 通信协议；Multi-agent Orchestration 偏一个任务内部如何分工、调度、汇总和验证。

## 最小例子

```text
leader
  -> planner: 制定计划
  -> executor A: 修改 API
  -> executor B: 修改前端
  -> test-engineer: 补测试
  -> verifier: 跑验证并报告
  -> leader: 整合、解决冲突、给最终结论
```

## 常见误解和风险

- 误解：多 Agent 必然比单 Agent 强。
- 误解：角色名字清楚，协作就会清楚。
- 风险：多个 worker 写同一批文件，产生难合并冲突。
- 风险：leader 不做最终验证，只拼接 worker 汇报。
- 风险：每个 Agent 都有上下文缺口，局部正确可能整合后错误。

## 使用边界

适合多 Agent：

- 任务能拆分成相对独立的文件或模块。
- 每个 worker 有清晰 ownership。
- 有明确测试或验收标准。
- leader 有时间做 integration。

不适合多 Agent：

- 只有一个小 bug。
- 需求还没澄清。
- 修改集中在同一个核心文件。
- 没有验证路径。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[Oh My Codex Repo]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Harness]]
- [[Handoff]]
- [[A2A]]
- [[Oh My Codex (OMX)]]
