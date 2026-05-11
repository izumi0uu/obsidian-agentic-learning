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
  - "[[前沿主源清单#代码 Agent]]"
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

## 概念详解

Agent Harness 可以理解为“让 Agent 真的跑起来并留下证据的壳”。如果 [[Agent]] 是围绕目标做决策和行动的系统，那么 harness 负责把这个系统放进可控环境：准备输入、装配上下文、暴露工具、执行工具、隔离文件系统或网络、保存状态、记录 trace、处理失败、运行评测、决定是否停止。它不是智能来源，而是智能被使用时的边界和证据层。

这个概念在代码 Agent 场景里特别清楚。[[SWE-bench]] 不只是一个分数榜，它还提供 repo snapshot、issue、patch 应用和测试运行这类评测壳；没有这些，模型说“我修好了”无法被复现。[[LangSmith Evaluation and Observability]] 说明 trace、dataset、evaluation 对 agent 行为复盘很关键；[[Claude Code Hooks 文档]] 和 [[Oh My Codex Repo]] 这类来源展示了 hook / lifecycle / tool boundary 如何把一次模型动作变成可记录、可阻断、可恢复的运行事件。

因此 harness 的核心价值不是让模型更聪明，而是降低“聪明但不可控”的风险。它把自然语言目标翻译成有权限、有工作区、有日志、有测试、有回滚或人工接管的工程过程。现代 Agent 的很多可靠性问题——权限越界、工具失败、循环不止、上下文丢失、评估不可复现——都不是 prompt 单独能解决的，而是 harness 的责任边界。

可以把 harness 看成三条线的交叉：执行线负责把模型意图变成真实 action，安全线负责决定 action 是否允许、是否需要人类确认，证据线负责保存每一步为什么发生以及结果是什么。缺执行线，Agent 只能说不能做；缺安全线，Agent 可能把错误计划变成真实副作用；缺证据线，失败无法复盘，成功也无法作为可复用经验。这个三线结构解释了为什么 harness 常和 sandbox、tool permissioning、trace、eval harness、patch validation 同时出现。
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

## 常见误解 / 风险

- 误解：Harness 越厚，Agent 就越聪明。实际上 harness 提供控制和证据，不直接提供推理能力。
- 误解：有一个测试集就等于有 harness。测试集只是数据；harness 还要定义环境准备、执行协议、日志、失败处理和评分方式。
- 风险：如果 harness 只记录最终答案，不记录工具调用、输入、输出和权限判断，就很难复现失败。
- 风险：如果 harness 没有 sandbox / approval gate，高能力 Agent 会把错误计划快速变成真实副作用。
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
- Anchor: [[SWE-bench#为什么收]], [[LangSmith Evaluation and Observability#为什么收]], [[Claude Code Hooks 文档#关键事实]], [[Oh My Codex Repo#本地 hook / 可观测性补充]]
- Evidence type: benchmark/source notes + observability docs + hook/runtime repo evidence + engineering synthesis.
- Confidence: medium
- Boundary: “harness 负责状态、权限、trace、sandbox、评测”的拆分是工程综合理解；具体 hook 名称、API 和产品能力会随平台变化。

## 复习触发

- 如果一个模型能改代码但不能运行测试、记录 patch 或隔离工作区，它缺的是 Agent 还是 Harness？
- 为什么 [[SWE-bench]] 既是 benchmark，也能帮助理解 coding agent harness？
- 试着把一次工具调用拆成：模型决策、harness 执行、observation 回填、trace 记录、evaluation 判断。

## 相关链接

- [[Agent]]
- [[Evaluation]]
- [[Agent Loop]]
- [[Agent Lifecycle Hook]]
- [[SWE-bench]]
- [[Patch Validation]]
- [[Repo Context]]
- [[Eval Harness]]
