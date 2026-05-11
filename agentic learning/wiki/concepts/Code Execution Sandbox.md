---
type: concept
topic:
  - coding-agent
  - security
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Sandbox Workspace]]"
  - "[[Coding Agent]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
---

# Code Execution Sandbox

## 一句话

Code Execution Sandbox 是给 Agent 运行代码、命令、浏览器或数据分析任务的隔离执行环境，用来限制文件、网络、进程、资源和凭证的风险边界。

## 概念详解

Coding Agent 的危险不只来自“写错代码”，还来自执行代码时的副作用：删除文件、读取密钥、访问内网、下载恶意依赖、跑高成本任务、泄露数据或污染宿主环境。Code Execution Sandbox 把这些动作放进受控环境，让运行结果可以被收集，副作用可以被限制，必要时环境可以销毁。

Sandbox 可以是容器、microVM、临时远程环境、浏览器隔离层或受限本地进程。它关注的是执行边界：代码在哪里跑、能看到哪些文件、能不能联网、资源上限是多少、凭证怎样注入、运行后哪些 artifact 能带回来。

社区和产品文档经常把 sandbox 描述成“给 AI/Agent 安全运行代码的环境”，但真正需要检查的是隔离强度和默认权限：是否挂载宿主目录、是否允许外网、是否复用登录态、是否把 API key 放入环境变量、是否允许安装依赖或启动子进程。不同产品在这些细节上差异很大，所以概念卡只能说明边界问题，不能替某个产品背书。

对 Agent runtime 来说，sandbox 是工具执行层的一部分；它和 [[Tool Permissioning]]、[[Least Privilege Tools]]、approval gate、audit log 一起构成安全边界，而不是单独解决所有安全问题。好的系统会把“允许调用什么工具”和“工具在哪里执行”分开治理：前者是策略和权限，后者是隔离和资源约束。

一个实用判断是：sandbox 的强弱不看名字，而看默认 deny 的程度。只读文件挂载、临时目录、禁网、短时 token、资源配额和销毁策略越明确，越接近可治理执行；如果 Agent 可以直接访问宿主 home、长期凭证和开放网络，那么即使命令运行在“容器”里，学习上也应把它视为弱隔离。
## 它解决什么问题

Agent 运行代码时可能删除文件、访问网络、泄露密钥、跑高成本任务或破坏系统。Sandbox 把执行限制在可控环境里。

代表生态包括 E2B、Daytona、Modal Sandboxes、Firecracker/microVM 等。这里的重点不是记住产品名，而是理解“代码执行必须有隔离边界”。

## 它不是什么

Code Execution Sandbox 不是绝对安全。隔离层配置错误、宿主目录挂载过宽、网络默认开放、凭证注入不当，都可能让 sandbox 失效。

它也不等于 [[Sandbox Workspace]]。Workspace 更偏工作目录和修改边界；Code Execution Sandbox 更偏进程、网络、系统调用、容器或 VM 隔离。

它也不是权限策略本身。权限策略决定“能不能执行”；sandbox 负责“如果执行，在哪里、带哪些约束执行”。

## 最小例子

```text
Agent 写 Python
-> runtime 把脚本放入临时 sandbox
-> sandbox 限制只读输入目录、禁用默认外网、设置 CPU/内存/时间上限
-> 执行并收集 stdout/stderr/files
-> 返回结果给 Agent
-> 销毁环境
```

如果同一段代码直接在用户主目录运行，风险边界就从 sandbox 扩大到了整个宿主环境。

## 常见误解和风险

- sandbox 仍可能带网络外泄风险。
- 挂载宿主目录时隔离会变弱。
- API key、浏览器登录态和数据库连接要单独隔离。
- 只限制文件系统不够；依赖安装、子进程、网络和资源消耗也需要控制。

## 边界细节

和 [[Tool Permissioning]] 的边界：permissioning 决定工具是否允许被调用、参数是否需要确认；sandbox 决定工具运行时的环境限制。两者应该叠加，而不是互相替代。

和 [[Code Execution Sandbox]] 自身的安全边界：本地 sandbox、远程容器、microVM 的隔离强度不同；学习卡只描述概念，不替具体安全评估背书。

和 [[Agent Harness]] 的关系：harness 负责把模型 tool call 转成真实执行，sandbox 是 harness 可选但重要的执行后端。

## 现代性状态

Code Execution Sandbox 是当前工程实践。

- 基础地基：隔离执行、容器、VM、最小权限是长期存在的安全思想。
- 当前工程实践：coding agent、browser agent、data analysis agent 会把代码运行放进 sandbox 或受控 workspace。
- 前沿 / 易变：具体 sandbox 产品、网络策略、凭证注入方式、浏览器隔离和远程开发环境 API 变化较快。

## 现代系统怎么吸收 Sandbox 的价值

现代 Agent 系统通常把 sandbox 和权限、审计、artifact 收集结合起来：执行前检查工具和参数，执行时限制环境，执行后记录 stdout/stderr、生成文件和退出码，并把结果作为 observation 返回给模型。

这让 Agent 的“能运行代码”从危险能力变成可治理能力：用户可以知道跑了什么、在哪里跑、看到了哪些文件、产生了哪些输出。

## 证据锚点

- Evidence type: engineering source note / infrastructure source — [[Agent 工程基础设施主源]]。
- Boundary: source note 支持 sandbox 作为 Agent 基础设施主题；具体 E2B、Daytona、Modal、Firecracker 的产品能力、默认网络和隔离强度需要查各自官方文档。
- Engineering synthesis: 文件、网络、进程、资源和凭证边界是安全工程总结，不应理解为某个产品的统一保证。
- Confidence: medium。

## 复习触发

- Sandbox Workspace 和 Code Execution Sandbox 的差别是什么？
- 为什么 sandbox 不能替代 tool permissioning？
- 如果给 sandbox 挂载了用户主目录和真实 API key，风险边界发生了什么变化？

## 相关链接

- [[Sandbox Workspace]]
- [[Coding Agent]]
- [[Least Privilege Tools]]
- [[Tool Permissioning]]
