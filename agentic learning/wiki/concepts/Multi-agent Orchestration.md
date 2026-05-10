---
type: concept
topic:
  - agent
  - workflow
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
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

## 概念详解

Multi-agent Orchestration 关注的不是“有几个 Agent”，而是多个能力单元如何在同一任务里分工、通信、交接、验证和收敛。它出现的原因是复杂任务往往有不同认知形态：有人负责理解需求，有人负责搜索证据，有人负责实现，有人负责测试，有人负责审查风险。如果让一个 Agent 串行承担全部角色，可能上下文过长、视角单一、验证不足；如果让多个 Agent 无边界并行，又会冲突、重复和失控。

有效编排至少要有四个结构：任务切分（每个 agent 拥有什么文件或责任）、通信协议（怎样报告进度、阻塞和结果）、集成权威（谁解决冲突并做最终判断）、验证路径（如何证明整体任务完成）。[[Oh My Codex (OMX)]] 的 `$team` 是本地代码 Agent 场景里的具体例子：leader 分配 worker lane，worker 在 worktree 中执行，任务状态和 mailbox 记录协作，最后由 leader 集成和验证。

证据边界上，Multi-agent Orchestration 是工程组织模式，不等于跨组织协议。[[A2A]] 更偏 agent-to-agent 通信协议；本卡更偏一个任务内部如何组织多个 worker/role/handoff/eval。它也不是性能保证：当任务无法清晰切分、共享文件高度重叠或 leader 不做最终验证时，多 Agent 会增加错误面。

一个常见工程陷阱是把“并行”误当成“协作”。真正的 orchestration 需要定义共享事实来源：任务状态在哪里、谁拥有文件、谁能修改计划、谁能宣布完成、验证失败时由谁修。没有这些约束，每个 Agent 都可能局部合理，却在集成时产生互相覆盖、证据不一致或责任空洞。反过来，如果任务可以按文件、模块或评测维度切开，多 Agent 能让探索、实现、测试和审查并行进行，提高吞吐但仍由 leader 收敛。
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

## 边界细节

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

## 现代性状态

- 判定：current-practice / frontier-adjacent
- 当前工程实践：多 Agent 编排已在 coding agent、research agent、customer support 和 workflow automation 中广泛出现，核心稳定结构是角色、任务边界、handoff、共享状态和 verification。
- 前沿 / 易变：具体协议、team runtime、agent-to-agent communication、tool权限和产品形态仍在快速变化，因此本卡保持 `freshness: watch`。
- 稳定部分：没有 ownership、通信、集成权威和验证路径的多 Agent，不是可靠编排，只是并发。
- 复查点：当 A2A/ACP/MCP 等协议或主流框架改变 multi-agent 抽象边界时，再更新本卡；单个本地工具命令变化优先写入对应 source note。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[Oh My Codex Repo]]
- Anchor: [[前沿主源清单#RAG 进化]], [[Oh My Codex Repo#为什么收]]
- Evidence type: frontier/source index note + local orchestration repo source note + engineering synthesis.
- Confidence: medium
- Boundary: OMX `$team` 是本地 coding-agent orchestration 例子；不要把它的 worker/mailbox/worktree 机制直接外推为所有多 Agent 系统的标准。

## 复习触发

- 为什么多 Agent 编排的关键不是 Agent 数量，而是 ownership 和 verification？
- Multi-agent Orchestration 和 A2A 的边界在哪里？
- 如果两个 worker 同时修改同一核心文件，leader 应该怎样判断这是编排问题而不是实现问题？

## 相关链接

- [[Agent]]
- [[Agent Harness]]
- [[Handoff]]
- [[A2A]]
- [[Oh My Codex (OMX)]]
