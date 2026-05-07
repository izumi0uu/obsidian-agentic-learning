---
type: concept
topic:
  - coding-agent
  - security
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Sandbox Workspace]]"
  - "[[Coding Agent]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
---

# Code Execution Sandbox

## 一句话

Code Execution Sandbox 是给 Agent 运行代码、命令、浏览器或数据分析任务的隔离执行环境。

## 它解决什么问题

Agent 运行代码时可能删除文件、访问网络、泄露密钥、跑高成本任务或破坏系统。Sandbox 把执行限制在可控环境里。

代表生态包括 E2B、Daytona、Modal Sandboxes、Firecracker/microVM 等。

## 它不是什么

Code Execution Sandbox 不是绝对安全。

它也不等于 [[Sandbox Workspace]]。Workspace 更偏工作目录和修改边界；Code Execution Sandbox 更偏进程、网络、系统调用、容器或 VM 隔离。

## 最小例子

```text
Agent 写 Python -> sandbox 运行 -> 收集 stdout/stderr/files -> 返回结果 -> 销毁环境
```

## 常见误解和风险

- sandbox 仍可能带网络外泄风险。
- 挂载宿主目录时隔离会变弱。
- API key、浏览器登录态和数据库连接要单独隔离。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Sandbox Workspace]]
- [[Coding Agent]]
- [[Least Privilege Tools]]
- [[Tool Permissioning]]
