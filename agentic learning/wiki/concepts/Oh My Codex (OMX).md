---
type: concept
topic:
  - agent
  - coding-agent
  - workflow
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Oh My Codex Repo]]"
  - "[[oh-my-codex 使用教程]]"
evidence:
  - "[[Oh My Codex Repo#为什么收]]"
  - "[[oh-my-codex 使用教程#0. 先建立心智模型]]"
related:
  - "[[OMX $ 指令]]"
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Sandbox Workspace]]"
  - "[[Trace]]"
  - "[[AGENTS.md]]"
---

# Oh My Codex (OMX)

## 一句话

Oh My Codex, 简称 OMX, 是 OpenAI Codex CLI 的多 Agent 编排和运行时增强层，让 Codex 更容易按“澄清、计划、执行、验证、恢复”的工程流程工作。

## 它解决什么问题

单独用 Codex 时，复杂任务容易遇到几个问题：

- 需求没问清就开始改。
- 大任务没有稳定计划。
- 多个子任务无法安全并行。
- 运行状态、计划、日志和记忆散在对话里。
- 中断后难恢复。
- 团队 worker 互相改同一份文件容易冲突。

OMX 给 Codex 加了一层 [[Agent Harness]]：

- 用 `$deep-interview` 做需求澄清。
- 用 `$ralplan` 做计划和权衡。
- 用 `$ralph` 做持续执行和验证。
- 用 `$team` 启动 tmux worker 并行处理任务。
- 用 `.omx/` 保存 plans、logs、state、memory。
- 用 git worktree 隔离并行 worker 的修改。
- 用 hooks 和 HUD 观察会话生命周期。

具体 `$` 入口见 [[OMX $ 指令]]。小边界：这些 `$` 指令是 Codex 会话里的 skill / workflow 触发入口，不等于普通 shell 命令；有些 workflow 会配合 `omx ...` CLI 和 `.omx/` artifact，但两者不是同一层。

## 它不是什么

OMX 不是新模型，也不是 Codex 的替代品。

它不能保证任务一定正确完成，也不能替代测试、代码审查、权限控制和人工判断。

它也不是一开始学 Agent 就必须安装的工具。对零基础学习来说，先理解 [[Agent]]、[[Agent Loop]]、[[Tool Calling]]、[[Agent Harness]]，再看 OMX 会更顺。

## 最小例子

你有一个中等复杂 bug：

```text
omx --madmax --high
$deep-interview "这个登录 bug 边界不清，先问我 5 个关键问题"
$ralplan "基于澄清结果给出修复计划和风险"
$ralph "按计划修复，跑测试，直到验证通过"
```

如果任务可以拆成多个独立模块：

```text
$team 3:executor "并行修复 API、前端表单和测试用例"
```

每个 worker 会在独立 worktree 中工作，降低互相覆盖文件的风险。

## 常见误解和风险

- 误解：OMX 会让模型更聪明。实际它提升的是流程、状态、并行和恢复能力。
- 误解：`$team` 越多越好。实际只有任务能拆分、边界清晰、验证明确时，并行才有价值。
- 风险：`--madmax` / `--yolo` 会减少审批摩擦，也会扩大误操作风险。
- 风险：git worktree 只隔离文件修改，不隔离真实数据库、生产服务、API key 或外部账户。
- 风险：`omx doctor` 通过不代表真实模型调用一定成功，还要跑 `omx exec` smoke test。

## `$ralplan` 底层机制

`$ralplan` 不是另一个模型，也不是自动执行器。它是 OMX 的 planning workflow。

底层可以拆成四层：

- Prompt routing：识别 `$ralplan`，把当前会话切到 planning 模式。
- State：在 `.omx/state/.../ralplan-state.json` 记录当前 phase、artifact 和是否完成。
- Plan artifact：把需求、取舍、非目标和验证方式沉淀到 `.omx/plans/`，常见产物是 `prd-*.md` 和 `test-spec-*.md`。
- Stop hook：如果计划还没形成明确状态，阻止会话静默结束，要求继续、等待输入或给出 approved handoff。

所以 `$ralplan` 的价值不是让模型突然更聪明，而是把“先计划再执行”做成可追踪、可暂停、可交接的 [[Agent Harness]] 机制。

## 证据锚点

- Source: [[Oh My Codex Repo]]
- Source: [[oh-my-codex 使用教程]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[oh-my-codex 使用教程]]
- [[OMX $ 指令]]
- [[Oh My Codex Repo]]
- [[Agent Harness]]
- [[Coding Agent]]
- [[Sandbox Workspace]]
- [[Trace]]
