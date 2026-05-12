---
type: map
topic:
  - coding-agent
  - evaluation
  - security
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Coding Agent]]"
  - "[[Repo Context]]"
  - "[[Patch Validation]]"
  - "[[Sandbox Workspace]]"
  - "[[Code Execution Sandbox]]"
  - "[[AGENTS.md]]"
  - "[[Tool Permissioning]]"
evidence:
  - "[[Coding Agent#证据锚点]]"
  - "[[Repo Context#证据锚点]]"
  - "[[Patch Validation#证据锚点]]"
  - "[[Sandbox Workspace#证据锚点]]"
  - "[[Code Execution Sandbox#证据锚点]]"
  - "[[AGENTS.md#证据锚点]]"
  - "[[Tool Permissioning#证据锚点]]"
related:
  - "[[SWE-bench]]"
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Trace]]"
  - "[[Agent Harness]]"
---

# Coding Agent 执行边界对比

## 一句话总览

[[Coding Agent]] 是能在代码库里理解任务、修改文件并验证结果的 Agent；[[Repo Context]] 是它理解仓库的证据材料；[[Patch Validation]] 是判断改动是否成立的验证纪律；[[AGENTS.md]] 是 repo-local guidance；[[Sandbox Workspace]] 和 [[Code Execution Sandbox]] 限制文件/进程/网络/凭据副作用；[[Tool Permissioning]] 决定哪些工具和动作能被调用。

最小边界：会生成 patch 不等于会修好问题；读到 repo context 不等于理解全仓；测试通过也不代表安全边界完整；AGENTS.md 是指导而不是执行隔离；sandbox 是隔离而不是审批策略。

## 为什么这组值得对比

- 混淆风险：coding agent 任务里常把“读仓库”“改代码”“跑测试”“遵守 AGENTS.md”“sandbox 安全”“工具权限”混成一条模糊流程。
- 共同问题域：它们都围绕“Agent 如何在真实 repo 中安全、可验证地完成代码修改”。
- 不同介入点：有的是主体能力，有的是证据输入，有的是验证输出，有的是指导约束，有的是执行边界，有的是权限控制。
- 证据密度：相关卡已经连接 SWE-bench、Oh My Codex Repo、AGENTS.md/Codex Agent Loop、Agent 工程基础设施等 anchors。
- 复习价值：这组对比能训练“一个 coding agent 失败时，应该归因到上下文、patch、验证、指令还是执行边界”。

边界：这页不是某个 coding-agent 产品手册，也不替代具体仓库的 AGENTS.md 指令。

## 共同问题域

共同问题是：代码修改不是自然语言答案。Agent 要先理解 issue、仓库结构、约束和现有测试，再生成最小 patch，运行验证，报告证据，同时避免破坏用户环境、泄露凭据或越权修改共享文件。

```text
Issue / user task
  -> read AGENTS.md + repo context
  -> inspect code/tests
  -> produce patch
  -> patch validation: tests/lint/typecheck/build/smoke
  -> sandbox + tool permissioning constrain execution
  -> trace/report records evidence and gaps
```

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Coding Agent]] | 执行代码任务的 Agent 形态 | 端到端 issue -> patch -> verify | 用户任务、repo、tools、tests | patch、验证报告、交付说明 | [[Coding Agent#证据锚点]] |
| [[Repo Context]] | 仓库事实和约束证据 | 规划/编辑前持续检索 | 文件、symbols、tests、docs、history、AGENTS.md | scoped understanding / evidence map | [[Repo Context#证据锚点]] |
| [[AGENTS.md]] | repo-local 指令和边界 | 读取后约束所有后续操作 | 人类 guidance、目录规则、构建/测试要求 | 执行约束和风格/安全规则 | [[AGENTS.md#证据锚点]] |
| [[Patch Validation]] | 改动是否真的成立 | patch 后运行验证 | diff、tests、lint、typecheck、build、logs | PASS/FAIL 证据和缺口 | [[Patch Validation#证据锚点]] |
| [[Sandbox Workspace]] | 文件/工作区/登录态隔离 | 整个任务期间 | worktree、filesystem、browser/profile、env | 可回滚、可隔离的修改边界 | [[Sandbox Workspace#证据锚点]] |
| [[Code Execution Sandbox]] | 命令/代码/网络/资源隔离 | 执行 tests/build/scripts 时 | shell command、deps、network、process、credentials | 受限运行结果 | [[Code Execution Sandbox#证据锚点]] |
| [[Tool Permissioning]] | 工具调用权限和审批 | tool call 前、中、后 | 工具名、参数、风险等级、policy | allow/deny/confirm/scope | [[Tool Permissioning#证据锚点]] |

## 最容易混淆的边界

### Coding Agent vs Repo Context

[[Coding Agent]] 是执行主体和工作流；[[Repo Context]] 是它理解仓库的证据输入。把更多文件塞进上下文不等于更懂 repo；真正有用的是能定位相关代码、测试、约束、历史和失败日志。

### Repo Context vs AGENTS.md

[[Repo Context]] 包含代码、测试、文档、目录结构、错误输出等事实；[[AGENTS.md]] 是人类写给 Agent 的 durable guidance。AGENTS.md 可以规定不要改哪些文件、怎么测试、怎么写 PR，但它不等于代码事实，也不替代实际 inspection。

### Patch Validation vs Evaluation

[[Patch Validation]] 是 coding task 的具体验证纪律：diff 是否应用、测试是否通过、类型/lint/build 是否干净、行为是否覆盖。[[Evaluation]] 更大，可以包括 benchmark、trajectory、成本、安全和长期回归。Patch validation 是 coding-agent evaluation 的核心子层。

### Sandbox Workspace vs Code Execution Sandbox

[[Sandbox Workspace]] 管的是修改边界：worktree、文件、profile、凭据、团队并行隔离。[[Code Execution Sandbox]] 管的是执行边界：命令在哪里跑、能否联网、能看哪些文件、资源限制如何。Coding agent 通常需要两者：一个防止乱改，一个防止乱跑。

### Tool Permissioning vs AGENTS.md

[[AGENTS.md]] 是 guidance；[[Tool Permissioning]] 是 runtime policy。AGENTS.md 可以说“不要改 raw”，但 permissioning / sandbox / review 才能在工具层限制或确认高风险动作。只靠文字指令不能替代执行控制。

## 执行时序 / 机制差异

```text
1. Read AGENTS.md and task instructions
2. Build Repo Context: relevant files, symbols, tests, constraints, errors
3. Plan minimal patch within scope
4. Edit files inside Sandbox Workspace
5. Run commands inside Code Execution Sandbox / local constraints
6. Tool Permissioning gates high-risk operations and external side effects
7. Patch Validation collects tests/lint/typecheck/build/smoke evidence
8. Report changed files, verification, gaps, and residual risk
```

这个时序是工程综合，来自本 vault 的 coding-agent 概念卡和 SWE-bench / Codex / OMX 学习材料，不是某个单一产品的统一协议。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

像让维修工修一台复杂机器：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Coding Agent]] | 负责维修的技师 | 技师能力不等于一定修好 |
| [[Repo Context]] | 机器图纸、故障日志、零件位置 | 资料多不等于读懂关键故障 |
| [[AGENTS.md]] | 车间规则：哪些不能碰、怎么交付 | 规则不是实际工具锁 |
| [[Patch Validation]] | 修完后的试车和检测 | 通过一项测试不等于覆盖全部风险 |
| [[Sandbox Workspace]] | 临时维修台，不碰客户正在运行的机器 | 隔离边界配置错误会失效 |
| [[Tool Permissioning]] | 动火/断电/外发零件前审批 | 审批要结合具体动作和参数 |

## 现代系统如何吸收或限制

- 来源支持：[[Coding Agent]]、[[Repo Context]]、[[Patch Validation]] 的证据锚点支持 SWE-bench 式真实 issue、repo context、patch 和测试验证边界；[[AGENTS.md]]、sandbox 和 permissioning 卡支持 repo guidance、工作区隔离、执行隔离和权限策略。
- 工程综合 / inference：现代 coding-agent harness 通常会把 repo retrieval、planning、patch application、command execution、test logs、diff review、trace 和 PR/report 串成闭环。
- 仍需警惕的外推：不同产品对 sandbox、工具权限、AGENTS.md 优先级和测试命令的实现不同；本页只沉淀学习边界，不替实际仓库规则背书。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 判断一个系统是不是在做代码任务而非普通问答 | [[Coding Agent]] | 它强调 repo、patch、验证和交付 | 只生成代码片段不等于完成任务 |
| 失败原因像是没读到相关文件或约束 | [[Repo Context]] | 需要定位缺失的代码/测试/文档/AGENTS 证据 | 上下文过多会噪声化 |
| 需要知道这次修改能不能交付 | [[Patch Validation]] | 它提供 tests/lint/typecheck/build/smoke 证据 | 测试缺口必须明确报告 |
| 需要遵守 repo 人类规则 | [[AGENTS.md]] | 它定义目录级指导和协作边界 | 不能替代代码 inspection 或工具控制 |
| 需要隔离并行工作和文件副作用 | [[Sandbox Workspace]] | worktree / workspace 控制修改范围 | 共享文件冲突仍要上报 |
| 需要运行不可信代码或依赖 | [[Code Execution Sandbox]] | 限制进程、网络、资源和凭据 | 本地宽权限运行会扩大损害半径 |
| 需要限制删除、外发、生产访问等高风险动作 | [[Tool Permissioning]] | 通过策略/审批控制工具和参数 | 只看工具名不看参数会漏风险 |

## 它们共同不是什么

- 都不是“模型会写代码”的同义词；真正交付需要 repo 证据和验证。
- 都不能保证 patch 正确；验证覆盖范围和测试可信度必须显式说明。
- 都不应绕过人类/仓库规则；AGENTS.md、scope、raw immutability、shared file ownership 都是执行边界。
- 都不是安全银弹；sandbox、permissioning、audit、trace 和 review 需要组合。

## 证据锚点

- Concept anchors: [[Coding Agent#证据锚点]], [[Repo Context#证据锚点]], [[Patch Validation#证据锚点]], [[Sandbox Workspace#证据锚点]], [[Code Execution Sandbox#证据锚点]], [[AGENTS.md#证据锚点]], [[Tool Permissioning#证据锚点]]
- Source examples: [[SWE-bench#为什么收]], [[Oh My Codex Repo#为什么收]], [[OpenAI - A Practical Guide to Building Agents#一句话]], [[AGENTS.md and Codex Agent Loop#为什么收]], [[Agent 工程基础设施主源#为什么收]]
- Evidence type: existing concept-card synthesis + benchmark/repo/docs/source notes + engineering synthesis + learning analogy.
- Confidence: medium-high for repo/patch/sandbox boundaries; medium for product-specific runtime behavior because coding-agent implementations vary.
- Boundary: 本页不替代具体仓库的 AGENTS.md、测试说明或安全策略；它只帮助学习 coding-agent 执行边界。

## 复习触发

1. 为什么 Coding Agent 的交付物不是“答案”，而是 patch + validation evidence？
2. Repo Context 缺失和 Patch Validation 失败分别会造成什么不同问题？
3. AGENTS.md 是指导，为什么仍需要 sandbox 和 tool permissioning？
4. 如果测试无法运行，Patch Validation 应该怎样报告缺口？
5. Sandbox Workspace 和 Code Execution Sandbox 在 coding task 中分别限制哪类损害半径？

## 相关链接

- [[Coding Agent]]
- [[Repo Context]]
- [[Patch Validation]]
- [[AGENTS.md]]
- [[Sandbox Workspace]]
- [[Code Execution Sandbox]]
- [[Tool Permissioning]]
- [[SWE-bench]]
- [[Evaluation]]
- [[Eval Harness]]
- [[Trace]]
- [[Agent Harness]]
- [[LLM Wiki 工作流]]
