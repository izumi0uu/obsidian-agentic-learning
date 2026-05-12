---
type: map
topic:
  - agent
  - browser
  - computer-use
  - security
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Browser Agent]]"
  - "[[Computer Use]]"
  - "[[GUI Grounding]]"
  - "[[Observation]]"
  - "[[Sandbox Workspace]]"
  - "[[Code Execution Sandbox]]"
  - "[[Tool Permissioning]]"
evidence:
  - "[[Browser Agent#证据锚点]]"
  - "[[Computer Use#证据锚点]]"
  - "[[GUI Grounding#证据锚点]]"
  - "[[Observation#证据锚点]]"
  - "[[Sandbox Workspace#证据锚点]]"
  - "[[Code Execution Sandbox#证据锚点]]"
  - "[[Tool Permissioning#证据锚点]]"
related:
  - "[[Agent Loop]]"
  - "[[Trace]]"
  - "[[Guardrails]]"
  - "[[Environment Observation 类型对比]]"
---

# Browser Computer Use 执行栈对比

## 一句话总览

[[Browser Agent]] 是浏览器任务形态；[[Computer Use]] 是更宽的 GUI / desktop / browser 操作运行时；[[GUI Grounding]] 是把截图、控件、坐标、DOM 或可访问性树落到动作目标的能力；[[Observation]] 是动作后的反馈；[[Sandbox Workspace]]、[[Code Execution Sandbox]] 和 [[Tool Permissioning]] 分别限制工作区、执行环境和工具权限风险。

最小边界：Browser Agent 不是简单爬虫，Computer Use 不是函数调用，GUI Grounding 不是任务策略，Observation 不是 Action，sandbox 不是权限策略，permissioning 也不是执行隔离。

## 为什么这组值得对比

- 混淆风险：浏览器自动化、computer use、GUI grounding、observation、sandbox、tool permissioning 都会出现在“会操作界面的 Agent”讨论里。
- 共同问题域：它们共同回答“Agent 如何在 UI 世界里安全地看、点、输入、等待、恢复和受控执行”。
- 不同介入点：有的是任务对象，有的是操作运行时，有的是视觉/结构化定位能力，有的是反馈信号，有的是风险边界。
- 证据密度：相关卡已有 OpenAI / Anthropic Computer Use、browser-use、Playwright MCP、ReAct、AGENTS.md/Codex source、Agent 基础设施等 anchors。
- 复习价值：这组对比能防止把“模型能点屏幕”误解为“端到端网页任务可靠且安全”。

边界：这页不追踪具体 Computer Use API 的最新字段；具体产品能力属于 volatile/watch 信息。

## 共同问题域

共同问题是：许多真实任务没有稳定 API，只能通过网页或 GUI 完成。Agent 必须从环境中观察状态，决定动作，执行后读取反馈，同时限制错误点击、数据泄露、表单提交、登录态污染和不可逆副作用。

```text
Goal
  -> Browser Agent / Computer Use task
  -> Observe screen / DOM / accessibility / tool result
  -> GUI Grounding chooses actionable target
  -> Action executed by browser/desktop/runtime
  -> Observation returned
  -> Sandbox + Tool Permissioning + Trace constrain and record risk
```

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Browser Agent]] | 浏览器任务形态和环境 | 多步网页观察/动作/恢复 | 网页、任务目标、登录态、工具 | 完成网页任务或结构化结果 | [[Browser Agent#证据锚点]] |
| [[Computer Use]] | GUI / desktop / browser 操作运行时 | screenshot/action 或结构化 GUI loop | 截图、控件状态、动作空间 | click/type/scroll 等动作结果 | [[Computer Use#证据锚点]] |
| [[GUI Grounding]] | 把观察落到可操作元素 | 每次动作前定位目标 | 截图、坐标、DOM、OCR、accessibility tree | 目标元素、坐标或 selector | [[GUI Grounding#证据锚点]] |
| [[Observation]] | 动作后的外部反馈 | action 后写回 context/state/trace | 工具结果、页面状态、错误、截图 | 下一轮决策依据 | [[Observation#证据锚点]] |
| [[Sandbox Workspace]] | 工作区和资料/登录态隔离 | 整个任务执行期间 | 文件、浏览器 profile、GUI、凭据边界 | 限制损害半径的 workspace | [[Sandbox Workspace#证据锚点]] |
| [[Code Execution Sandbox]] | 代码/命令/进程/网络执行隔离 | 工具执行时 | 命令、代码、网络、资源、凭证 | 受限执行结果和 artifacts | [[Code Execution Sandbox#证据锚点]] |
| [[Tool Permissioning]] | 工具和动作的权限/审批策略 | tool call 前、中、后 | 工具名、参数、风险等级、用户/策略 | allow/deny/confirm/scope | [[Tool Permissioning#证据锚点]] |

## 最容易混淆的边界

### Browser Agent vs Computer Use

[[Browser Agent]] 专注浏览器环境：网页状态、表单、DOM、登录态、弹窗、下载和跨页面任务。[[Computer Use]] 更宽，可以包括桌面、浏览器、终端、鼠标键盘和屏幕理解。浏览器是 computer use 的重要场景之一，但不是全部。

### Computer Use vs Tool Calling

Computer Use 面对 UI、坐标、控件、截图、页面变化和失败恢复；传统 tool calling 更偏结构化 API，参数和结果更明确。如果有稳定 API 或确定流程，通常优先 API / 脚本，而不是让模型裸操作 GUI。

### GUI Grounding vs Observation

[[GUI Grounding]] 是动作前把“我要点保存按钮”落到具体元素、坐标或 selector；[[Observation]] 是动作后环境返回“点击后发生了什么”。一个负责定位，一个负责反馈；两者都可能出错。

### Sandbox Workspace vs Code Execution Sandbox

[[Sandbox Workspace]] 更宽：工作目录、浏览器 profile、GUI、凭据、团队并行修改隔离。[[Code Execution Sandbox]] 更偏命令、进程、网络、资源和系统隔离。Browser / computer-use 任务经常两者都需要。

### Tool Permissioning vs Sandbox

[[Tool Permissioning]] 决定“能不能调用这个工具、这个参数是否需要确认”；sandbox 决定“如果调用，它在哪里执行、能访问什么资源”。允许/拒绝和隔离/资源约束应叠加，而不是互相替代。

## 执行时序 / 机制差异

```text
1. User goal enters Browser Agent / Computer Use runtime
2. Runtime captures Observation: screenshot / DOM / accessibility tree / tool result
3. Model chooses high-level action or target
4. GUI Grounding maps target to coordinate / selector / control
5. Tool Permissioning checks action risk and may require approval
6. Sandbox Workspace / Code Execution Sandbox constrains execution environment
7. Runtime executes click/type/scroll/download/command
8. New Observation + Trace records feed next loop
```

关键点：模型通常不应直接拥有真实电脑；真实执行、权限、sandbox、trace 和审批由 runtime / harness 负责。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文、官方文档或 source note 证据。

像让实习生在隔离浏览器里帮你订票：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Browser Agent]] | 负责在订票网站完成任务的人 | 不代表所有桌面软件 |
| [[Computer Use]] | 允许他看屏幕、点按钮、输入文字的工作方式 | UI 操作比 API 脆弱 |
| [[GUI Grounding]] | 他能分清哪个按钮是“确认” | 点对按钮不等于策略正确 |
| [[Observation]] | 点击后页面显示“支付成功/失败” | 页面文字可能误导或被注入 |
| [[Sandbox Workspace]] | 给他一个临时浏览器 profile | 不等于绝对安全 |
| [[Tool Permissioning]] | 支付前必须让你确认 | 审批也要记录和执行 |

## 现代系统如何吸收或限制

- 来源支持：[[Browser Agent]]、[[Computer Use]] 和 [[GUI Grounding]] 的证据锚点支持 screenshot/action loop、浏览器自动化工具、GUI 状态和失败恢复；[[Observation]] 支持 action 后反馈进入 loop；sandbox/permissioning 卡支持执行边界和权限策略。
- 工程综合 / inference：现代系统通常用 browser profile、container/VM、tool allowlist、approval gate、trace、retry 和 eval harness 把 GUI 操作限制成可观察、可回滚、可审批的动作。
- 仍需警惕的外推：具体 API action 名称、模型 computer-use 能力、browser automation 项目状态和安全默认值会变化；本页只写稳定边界。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 任务主要发生在网页里，需要跨页面操作 | [[Browser Agent]] | 它描述浏览器作为环境的任务形态 | 稳定流程可能更适合脚本，不必用 Agent |
| 软件没有 API，只能看屏幕和操作 GUI | [[Computer Use]] | 它描述 screenshot/action 或 GUI loop | UI 脆弱、成本高、真实副作用强 |
| Agent 经常点错控件或输入错位置 | [[GUI Grounding]] | 根因可能是观察到动作目标的映射错误 | grounding 正确也不保证任务策略正确 |
| 需要判断行动后环境发生了什么 | [[Observation]] | action 后反馈决定下一轮 | observation 可能被注入、截断或过期 |
| 要限制浏览器 profile、文件和凭据影响范围 | [[Sandbox Workspace]] | 它缩小任务 workspace 的损害半径 | 登录态/网络/挂载过宽会穿透边界 |
| 要限制命令、代码、网络和资源 | [[Code Execution Sandbox]] | 它控制执行环境 | sandbox 配置错误会造成假安全感 |
| 要控制提交表单、下载、发送、删除等高风险动作 | [[Tool Permissioning]] | 它设置 allow/deny/confirm/scope | 只看工具名不够，参数和上下文也要审查 |

## 它们共同不是什么

- 都不是完整生产级 Agent framework。
- 都不能保证任务成功；还需要 planning、state、trace、eval、retry 和 human-in-the-loop。
- 都不能把网页或 GUI 内容默认当可信事实；网页内容也是 prompt injection 和数据泄露攻击面。
- 都不是越自动越好；高风险提交、支付、外发和登录态操作需要审批、审计和最小权限。

## 证据锚点

- Concept anchors: [[Browser Agent#证据锚点]], [[Computer Use#证据锚点]], [[GUI Grounding#证据锚点]], [[Observation#证据锚点]], [[Sandbox Workspace#证据锚点]], [[Code Execution Sandbox#证据锚点]], [[Tool Permissioning#证据锚点]]
- Source examples: [[OpenAI Computer Use 文档#为什么收]], [[Anthropic Computer Use 文档#为什么收]], [[browser-use GitHub Repo#为什么收]], [[Playwright MCP Repo]], [[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]], [[AGENTS.md and Codex Agent Loop#为什么收]], [[Agent 工程基础设施主源#为什么收]]
- Evidence type: existing concept-card synthesis + docs/repo/source notes + engineering synthesis + learning analogy.
- Confidence: medium for GUI stack boundaries; medium-low for product-specific behavior because Computer Use/API/tooling details are volatile.
- Boundary: “Browser Agent -> Computer Use -> GUI Grounding -> Observation -> sandbox/permissioning”是本页学习框架，不是某个官方统一架构。

## 复习触发

1. 为什么 Browser Agent 不是普通爬虫？
2. GUI Grounding 成功但任务失败，可能是哪一层出了问题？
3. Observation 为什么既是证据又是攻击面？
4. Sandbox Workspace 和 Tool Permissioning 为什么必须叠加？
5. 有稳定 API 时，为什么通常不该优先使用 Computer Use？

## 相关链接

- [[Browser Agent]]
- [[Computer Use]]
- [[GUI Grounding]]
- [[Observation]]
- [[Sandbox Workspace]]
- [[Code Execution Sandbox]]
- [[Tool Permissioning]]
- [[Agent Loop]]
- [[Trace]]
- [[Guardrails]]
- [[Environment Observation 类型对比]]
- [[LLM Wiki 工作流]]
