---
type: concept
topic:
  - agent
  - frontier
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[SWE-bench]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Claude Code Hooks 文档]]"
  - "[[Oh My Codex Repo]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[SWE-bench#为什么收]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Claude Code Hooks 文档#关键事实]]"
  - "[[Oh My Codex Repo#本地 hook / 可观测性补充]]"
related:
  - "[[Agent]]"
  - "[[Evaluation]]"
  - "[[Agent Loop]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Patch Validation]]"
  - "[[Repo Context]]"
  - "[[Eval Harness]]"
---

# Agent Harness

## 一句话

Agent Harness 是包住模型、工具、状态、权限、运行环境、trace 和评测逻辑的执行外壳。

## 它解决什么问题

单个 Agent 定义通常只描述“谁在决策”。但真实系统还需要回答：在哪里运行、能调用哪些工具、如何保存状态、如何复现失败、如何评分、如何限制权限。

Harness 负责把这些东西组织成一个可运行、可调试、可评估的系统。

## 它不是什么

Agent Harness 不是模型。

Agent Harness 也不是 Agent 本身。它更像 Agent 的实验台或运行壳。

## 最小例子

代码 Agent 的 harness 可能包括：

- checkout 一个 GitHub repo。
- 给 Agent issue 描述。
- 允许它读写文件和运行测试。
- 收集 patch、日志和测试结果。
- 判断任务是否完成。

[[SWE-bench]] 是一个很好的例子：它提供 issue、repo snapshot、patch 应用和测试运行机制，因此不只是 benchmark，也是代码 Agent 评测 harness 的典型形态。

## 边界细节

Agent Harness 偏运行系统；Eval Harness 偏评测系统。两者经常重叠。

更细一点：如果它回答“Agent 怎么跑起来”，偏 [[Agent Harness]]；如果它回答“怎么重复测试并判断好坏”，偏 [[Eval Harness]]。

## 生命周期 hook 如何增强 Harness

[[Agent Lifecycle Hook]] 是 harness 的一个典型控制点。它把“模型想调用工具”和“工具真的执行”之间插入可观察、可阻断、可记录的边界：

- 工具执行前：做权限判断、参数校验、预算检查、人工确认或拒绝。
- 工具执行后：记录结果、补充上下文、触发 trace/span、更新状态或进入恢复流程。
- 会话边界：在 session start、user prompt submit、compact、stop 时保存状态、计划和日志。

这就是为什么 `PreToolUse` / `PostToolUse` 更应该理解为产品/runtime/harness 能力，而不是 LLM 自身能力。

## 现代性状态

- 基础地基：harness 来自软件工程里的运行壳、测试壳和评测壳思想。
- 当前工程实践：Agent 产品和框架普遍需要 harness 管住 tools、state、permissions、trace、retry、approval 和 evaluation。
- 前沿 / 易变：Codex、Claude Code、OpenAI Agents SDK、LangGraph 等具体 hook、trace、session API 会快速变化，应该靠 source note 的 `freshness: watch/volatile` 跟踪。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[SWE-bench]]
- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Claude Code Hooks 文档]]
- Source: [[Oh My Codex Repo]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Evaluation]]
- [[Agent Loop]]
- [[Agent Lifecycle Hook]]
- [[SWE-bench]]
- [[Patch Validation]]
- [[Repo Context]]
- [[Eval Harness]]
