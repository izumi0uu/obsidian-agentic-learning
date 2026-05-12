---
type: concept
topic:
  - agent
  - platform
  - infrastructure
  - observability
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
source:
  - "[[Agno 官方文档]]"
  - "[[AgentScope 官方文档]]"
  - "[[Google ADK 官方文档]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
evidence:
  - "[[Agno 官方文档#必读块 1：三层架构]]"
  - "[[Agno 官方文档#必读块 2：生产平台能力]]"
  - "[[AgentScope 官方文档#必读块 1：AgentScope 的平台定位]]"
  - "[[Google ADK 官方文档#必读块 2：scale / evaluation / deployment / context]]"
related:
  - "[[Agent Harness]]"
  - "[[Observability]]"
  - "[[Audit Log]]"
  - "[[Approval Gate]]"
  - "[[Tool Permissioning]]"
---

# Agent Control Plane

## 一句话

Agent Control Plane 是管理 Agent 平台运行的控制层：它负责会话、部署、权限、RBAC、观测、审计、调度、human approval 和运行接口，而不是单个 Agent 的推理逻辑本身。

## 概念详解

当 Agent 从 demo 进入团队或生产环境，问题会从“怎么调用模型”变成“谁能运行哪个 Agent、用了哪些工具、成本和延迟多少、哪个动作被批准、失败怎么恢复、日志和审计在哪里”。Agent Control Plane 就是处理这些跨 Agent、跨团队、跨部署生命周期问题的控制面。

[[Agno 官方文档]] 的 source note 把 Agno 分成 SDK、Runtime、Control Plane 三层：SDK 构建 agents/teams/workflows，Runtime 服务化运行，Control Plane 管理平台；并列出 API、storage、context providers、human approval、OpenTelemetry tracing、audit logs、RBAC、interfaces、scheduling、deploy anywhere 等能力。[[AgentScope 官方文档]] 和 [[Google ADK 官方文档]] 也分别把 observability、deployment、distributed / Cloud deployment、evaluation 等放进框架路线，说明 Agent 平台化已经不只是在代码里定义一个 Agent 类。

工程综合：Control Plane 的核心价值是把“运行治理”从应用代码里抽出来；局限是平台功能越强，供应商绑定、权限设计和组织流程成本越高。

## 它解决什么问题

- 多个 Agent / workflow 缺少统一部署、观测和权限管理。
- 高风险工具调用没有审批、审计和责任记录。
- 线上运行缺少成本、延迟、失败、用户会话和 trace 管理。
- 团队协作中无法管理谁能访问哪些 Agent、工具和数据。

## 它不是什么

- 不是 Agent SDK。SDK 让开发者写 Agent；Control Plane 管理 Agent 如何运行和被治理。
- 不是 observability 本身。它可能包含 trace/audit，但还包括权限、部署、调度和接口。
- 不是自动安全保证。Control Plane 需要正确配置 RBAC、工具权限、数据边界和审批策略。

## 最小例子

```text
SDK defines RefundAgent
Runtime serves RefundAgent as API
Control Plane:
  - grants support team access
  - requires approval for refunds > $100
  - records trace and audit log
  - schedules nightly eval run
```

## 常见误解 / 风险

- 误解：有 control plane 就不用设计业务权限。实际平台只提供机制，策略仍要业务定义。
- 误解：console 里的 trace 就等于可审计。审计还需要不可抵赖、责任主体和保留策略。
- 风险：平台化带来供应商绑定和运维复杂度，小项目可能不需要。

## 边界细节

Agent Control Plane 和 [[Agent Harness]] 相邻：harness 更偏单个 Agent 运行外壳与安全边界，control plane 更偏多个 Agent / workflow 的平台治理。和 [[Observability]] 的关系是：observability 是控制面的一类能力，但 control plane 还包括权限、部署、调度和 UI/API 管理。

## 现代性状态

- 判定：frontier / volatile，且部分能力正在变成 current-practice。
- 稳定部分：生产 Agent 需要权限、观测、审批、审计和部署治理。
- 易变部分：Agno AgentOS、Google ADK/Cloud 运行路径、AgentScope deployment/distributed、商业控制台功能和 API。

## 现代系统怎么吸收 Agent Control Plane 的价值 / 局限

现代系统会把 Control Plane 用作组织治理层：统一管理 Agent 服务、工具权限、审批和 trace；底层 workflow/runtime 负责执行，上层产品 UI 负责交互。局限是 control plane 不能自动定义正确权限策略，也不能替代业务负责人对高风险动作的审计责任。

## 证据锚点

- [[Agno 官方文档#必读块 1：三层架构]]：SDK / Runtime / Control Plane 三层。
- [[Agno 官方文档#必读块 2：生产平台能力]]：human approval、OTel tracing、audit logs、RBAC、scheduling、deploy。
- [[AgentScope 官方文档#必读块 1：AgentScope 的平台定位]]：tools、memory、observability、MCP、A2A、deployment 等平台能力。
- [[Google ADK 官方文档#必读块 2：scale / evaluation / deployment / context]]：deployment、observability、evaluation、context management。

## 复习触发

1. Agent SDK、Runtime、Control Plane 三者分别负责什么？
2. 为什么 control plane 不是安全保证本身？
3. 一个企业客服 Agent 上线时，哪些能力应该放在 control plane，而不是业务代码里？

## 相关链接

- [[Agent Harness]]
- [[Observability]]
- [[Audit Log]]
- [[Approval Gate]]
- [[Tool Permissioning]]
- [[Agent Framework 全量选型对比 2026-05]]
