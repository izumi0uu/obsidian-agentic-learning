---
type: concept
topic:
  - coding-agent
  - security
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[AGENTS.md and Codex Agent Loop]]"
  - "[[OpenAI Computer Use 文档]]"
  - "[[Anthropic Computer Use 文档]]"
evidence:
  - "[[AGENTS.md and Codex Agent Loop#为什么收]]"
  - "[[OpenAI Computer Use 文档#为什么收]]"
  - "[[Anthropic Computer Use 文档#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[Agent Harness]]"
  - "[[Computer Use]]"
  - "[[Approval Gate]]"
---

# Sandbox Workspace

## 一句话

Sandbox Workspace 是给 Agent 执行命令、读写文件或操作 GUI 的隔离工作环境。

## 概念详解

Sandbox Workspace 的问题背景是 Agent 会执行命令、读写文件、打开网页、操作 GUI 和调用外部工具。没有隔离时，一次错误推理、prompt injection 或工具投毒就可能影响用户真实环境：删除文件、读取凭据、污染依赖、提交表单或连接生产服务。Sandbox 把 Agent 的行动限制在可观察、可回滚、权限较小的工作区里。

机制上，sandbox 可以是文件系统范围、容器、VM、隔离浏览器、临时 profile、网络 allowlist、只读挂载、受限 shell 或 per-task worktree。AGENTS.md/Codex source note说明 repo-level instructions 会进入 Agent 上下文并约束操作；Computer Use source notes强调 sandbox browser/VM、human-in-the-loop 和安全环境。这些 evidence 说明 sandbox 不是可选美化，而是 Agent Harness 的执行边界。

它和 [[Code Execution Sandbox]] 相关但更宽：code execution sandbox 偏运行代码；sandbox workspace 还包括文件、浏览器、GUI、凭据和团队并行修改隔离。它也不是绝对安全，尤其当网络、MCP 工具、登录态或宿主挂载过宽时。好的 sandbox 要和 least privilege、approval gate、policy engine、trace 和 git diff/rollback 一起工作。

## 它解决什么问题

Agent 会运行命令、修改文件、访问网页、调用工具。没有隔离时，一次误操作就可能删除文件、泄露凭据、污染系统环境或破坏用户工作。

## 它不是什么

Sandbox 不是绝对安全。

它只是把风险限制在较小边界内，还需要权限、审批、网络控制、日志和人工介入。

## 最小例子

代码 Agent 在一个 repo workspace 里：

- 只能写当前项目目录。
- 运行测试前不能访问生产数据库。
- 高风险命令需要用户确认。
- 所有命令输出进入 trace。

## 常见误解 / 风险 / 边界细节

- Shell sandbox 不一定约束 MCP 工具。
- 浏览器 sandbox 也可能带登录态风险。
- 网络访问常常是隐藏风险。
- 沙箱越宽，越需要 [[Least Privilege Tools]]。

## 边界细节

Sandbox 只缩小损害半径，不是绝对安全。文件系统、网络、MCP 工具、浏览器登录态和环境变量都可能穿透边界。判断 sandbox 是否足够，要看最坏动作能影响什么。

## 现代性状态

current-practice / watch。沙箱是现代 coding/computer-use Agent 的必要工程边界；具体隔离技术、权限和网络策略会随工具变化。

## 证据锚点

- Evidence type: source evidence — [[AGENTS.md and Codex Agent Loop#为什么收]]；[[OpenAI Computer Use 文档#为什么收]]；[[Anthropic Computer Use 文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[AGENTS.md and Codex Agent Loop]]；[[OpenAI Computer Use 文档]]；[[Anthropic Computer Use 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Sandbox Workspace 限制的是哪些损害半径？
- 为什么 sandbox 仍要配合网络、凭据和工具权限控制？

## 相关链接

- [[Coding Agent]]
- [[Agent Harness]]
- [[Computer Use]]
- [[Approval Gate]]
- [[Policy Engine]]
