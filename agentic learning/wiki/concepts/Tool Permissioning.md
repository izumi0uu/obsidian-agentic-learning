---
type: concept
topic:
  - tool
  - security
  - agent
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[MCP Tool Poisoning Threat Model]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[MCP Tool Poisoning Threat Model#为什么收]]"
related:
  - "[[Least Privilege Tools]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Tool Calling]]"
---

# Tool Permissioning

## 一句话

Tool Permissioning 是给 Agent 工具和工具动作设置权限、范围、审批和风险等级的机制。

## 概念详解

Tool Permissioning 的问题背景是 Agent 的工具不是同一种风险：读公开文档、写本地草稿、发送邮件、删除文件、支付、访问生产数据库、读取浏览器 cookie，风险完全不同。模型能看到一个工具，不代表它应该能在任何上下文调用它。permissioning 把工具、参数、数据范围、动作类型和审批规则变成显式授权模型。

机制上，permissioning 至少包含四层：工具可见性（能不能看到/选择）、调用授权（能不能调用）、参数约束（哪些路径、域名、金额、收件人可用）、执行门槛（自动、审批、拒绝、审计）。Agent 工程基础设施 source note把权限和模型路由、沙箱、观测放在生产基础设施里；MCP Tool Poisoning source note提醒工具描述/结果可能诱导模型非预期调用。这说明权限不能只相信工具描述，也不能只看工具名。

它和 [[Least Privilege Tools]] 的边界：最小权限是原则，tool permissioning 是落地机制。它和 [[Approval Gate]] 的边界：permissioning 决定哪些动作需要 gate，gate 负责把决策前置到执行前。对 MCP/registry 生态来说，permissioning 还要处理远程 server 来源、版本、annotations 信任和供应链更新。

在 MCP 或插件生态中，permissioning 还要处理工具来源和动态变化。一个工具今天是只读，明天版本更新后可能新增写操作；一个 server 的 annotations 声称无副作用，也可能来自不可信来源。因此 permissioning 应由 host/policy 层独立维护，不应完全继承工具自述。


## 它解决什么问题

工具可调用不等于应该随便调用。读文件、发邮件、转账、删库、联网、访问私密数据的风险完全不同，需要分级授权。

## 它不是什么

Tool Permissioning 不是工具列表。

它也不等于 [[Least Privilege Tools]]。最小权限是原则，permissioning 是具体执行机制。

## 最小例子

```text
read_docs: auto allow
send_email: require approval
delete_file: deny outside workspace
charge_card: human approval + audit log
```

## 常见误解和风险

- 工具描述可信，不代表工具行为安全。
- 权限只看工具名不够，还要看参数和上下文。
- 审批应该保留理由和记录。

## 边界细节

Permissioning 要覆盖工具名、参数、数据范围、身份和动作副作用。只隐藏工具列表不够；工具可见、可调用、可传哪些参数、何时需要审批，都是不同层次的权限。

## 现代性状态

current-practice / watch。工具权限已经是 Agent runtime 的核心实践，MCP/Computer Use/SDK 的授权接口会变化，但分层授权和审计边界稳定。

## 证据锚点

- Evidence type: source evidence — [[Agent 工程基础设施主源#为什么收]]；[[MCP Tool Poisoning Threat Model#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Agent 工程基础设施主源]]；[[MCP Tool Poisoning Threat Model]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Tool Permissioning 的四层控制是什么？
- 为什么只看工具名不够？

## 相关链接

- [[Least Privilege Tools]]
- [[Policy Engine]]
- [[Approval Gate]]
- [[Tool Calling]]
