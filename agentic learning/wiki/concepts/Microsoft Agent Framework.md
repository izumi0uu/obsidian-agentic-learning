---
type: concept
topic:
  - agent
  - framework
  - workflow
  - microsoft
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts:
  - "Microsoft Learn 当前页面仍标注 public preview；官方 blog 同时将其描述为 Semantic Kernel 与 AutoGen 的 direct successor。"
source:
  - "[[Microsoft Agent Framework 官方文档]]"
  - "[[AutoGen 官方文档]]"
evidence:
  - "[[Microsoft Agent Framework 官方文档#必读块 1：Agent vs workflow 边界]]"
  - "[[Microsoft Agent Framework 官方文档#必读块 2：AutoGen + Semantic Kernel successor]]"
related:
  - "[[Agent Framework]]"
  - "[[AutoGen]]"
  - "[[Agent Workflow]]"
  - "[[Handoff]]"
  - "[[Agent Framework 编排范式对比]]"
---

# Microsoft Agent Framework

## 一句话

Microsoft Agent Framework 是微软把 AutoGen 的多 Agent patterns 和 Semantic Kernel 的企业工程经验合并后的新 Agent SDK 路线：它把 agents 与 workflows 都作为一等对象，并强调状态、middleware、telemetry、human-in-the-loop 和企业集成。

## 概念详解

Microsoft Agent Framework 重要，是因为它改变了“微软多 Agent 框架 = AutoGen”这个旧心智。官方资料把 Agent Framework 描述为 AutoGen 与 Semantic Kernel 的下一代 / direct successor：AutoGen 提供简单 agent 抽象和多 Agent patterns，Semantic Kernel 提供企业级 SDK、类型、工具、telemetry、middleware 等工程经验，Agent Framework 尝试把二者整合成统一框架。这意味着学习微软生态时，不应该只看 AutoGen 的 group chat；还要看 Microsoft Agent Framework 如何重新定义 agent、workflow 和生产治理。

它的关键边界是 agent vs workflow。Microsoft Learn 当前 docs 明确区分：开放式、对话式、需要自主判断的任务适合 agent；步骤明确、路径稳定、需要确定性控制的任务适合 workflow；如果普通函数就能处理，就不要硬上 AI agent。这一点和 Anthropic / OpenAI 的 agentic system 实践提醒相互呼应：框架的目标不是最大化自主性，而是给开发者选择控制粒度。

和 LangGraph 相比，Microsoft Agent Framework 同样强调 workflow，但它的定位更偏微软统一 SDK 与企业生态：C# / Python、Azure AI Foundry、OpenTelemetry、middleware、人机协作、migration from AutoGen / Semantic Kernel 等。LangGraph 的学习入口是 state graph runtime；Microsoft Agent Framework 的学习入口是“微软如何把 agent + workflow + enterprise SDK 收敛成新产品线”。

## 它解决什么问题

它解决微软生态里 agent framework 分裂的问题：AutoGen 偏多 Agent / conversation patterns，Semantic Kernel 偏 enterprise SDK 和模型/工具集成。Microsoft Agent Framework 试图把 agent 抽象、workflow、状态、工具、中间件、telemetry、A2A、MCP 和 Azure 集成收敛到统一入口。

对学习者来说，它解决的是“微软框架该看哪条主线”的问题：当前应把 Microsoft Agent Framework 纳入对比，而不是只比较 AutoGen。

## 它不是什么

它不是 AutoGen 的简单改名，也不是说 AutoGen / Semantic Kernel 的历史概念都失效。更准确地说，MAF 是微软当前整合路线，AutoGen 的 conversation-first 思想和 Semantic Kernel 的企业 SDK 思想仍是理解它的来源。

它也不是所有 Agent 框架的通用标准；它是 Microsoft ecosystem 的 product/framework。离开微软生态时，LangGraph、AgentScope、CAMEL、OpenAI Agents SDK 等仍有不同抽象中心。

## 最小例子

```text
If task is open-ended:
  define agent with tools, memory, middleware, telemetry
If task has stable steps:
  define workflow with explicit stages and state
If task is plain deterministic function:
  do not use AI agent
```

这个例子的重点是 agent / workflow / function 三层选择，而不是“所有问题都交给多 Agent”。

## 常见误解 / 风险

- 误解：微软框架只等于 AutoGen。风险是忽略 Agent Framework 的继任路线。
- 误解：新框架等于生产可直接用。风险是 preview/GA、API 稳定性、迁移成本和 Azure 集成边界仍需复查。
- 误解：workflow 不如 agent 智能。风险是把确定性流程错误地交给开放 agent，增加不可控性。
- 风险：把 Semantic Kernel、AutoGen、MAF 的概念层级混在一起。

## 边界细节

和 [[AutoGen]]：AutoGen 是来源之一，更偏 conversation/team/multi-agent patterns；MAF 是微软当前统一框架路线。

和 [[LangGraph]]：两者都处理 workflow/state；LangGraph 更像低层 state graph runtime，MAF 更像 Microsoft SDK + enterprise integration + agent/workflow 统一入口。

和 [[AgentScope]]：AgentScope 更偏多 Agent 应用平台和分布式运行；MAF 更偏微软生态与 AutoGen/Semantic Kernel 继任整合。

## 现代性状态

- 判定：frontier/volatile product ecosystem。
- 稳定部分：agent vs workflow 边界；AutoGen + Semantic Kernel 整合路线；企业 SDK 中 telemetry/middleware/HITL 的重要性。
- 易变部分：public preview / GA 状态、API 名称、迁移指南、Azure AI Foundry 集成和多语言支持。

## 现代系统怎么吸收 Microsoft Agent Framework 的价值 / 局限

现代系统可以吸收它的一个判断习惯：先判断任务应是 function、workflow 还是 agent，再选框架对象。这个判断比“看到 Agent 就多加几个角色”更重要。

局限是 MAF 强烈绑定微软生态和版本路线。学习上应把它当框架范式与产品路线观察点；生产选型还要结合团队语言栈、云平台、现有 Semantic Kernel / AutoGen 代码、Azure 集成、安全合规和版本稳定性。

## 证据锚点

- Source: [[Microsoft Agent Framework 官方文档]]
- Anchor: [[Microsoft Agent Framework 官方文档#必读块 1：Agent vs workflow 边界]], [[Microsoft Agent Framework 官方文档#必读块 2：AutoGen + Semantic Kernel successor]]
- Source: [[AutoGen 官方文档]]
- Anchor: [[AutoGen 官方文档#必读块 1：Teams / group chat 抽象]]
- Evidence type: official docs/source notes + Microsoft blog note + engineering synthesis.
- Confidence: medium；官方继任路线清楚，但 preview/GA 与 API 稳定性需要持续复查。
- Boundary: 本卡不宣称 MAF 已替代所有 AutoGen/Semantic Kernel 使用场景，只记录微软官方当前整合方向和学习边界。

## 复习触发

1. 为什么 Microsoft Agent Framework 不是 AutoGen 的简单重命名？
2. agent、workflow、function 三者如何决定？
3. MAF 和 LangGraph 都有 workflow，为什么抽象中心仍不同？
4. 当一个项目已经用了 AutoGen，迁移到 MAF 前至少要确认哪些边界？

## 相关链接

- [[Agent Framework]]
- [[Agent Framework 编排范式对比]]
- [[AutoGen]]
- [[LangGraph]]
- [[AgentScope]]
- [[CAMEL]]
- [[Agent Workflow]]
- [[Handoff]]
