---
type: concept
topic:
  - agent
  - workflow
  - security
  - evaluation
status: growing
created: 2026-05-14
updated: 2026-05-23
last_checked: 2026-05-23
freshness: watch
conflicts: []
source:
  - "[[Workflow Guardrails 主源]]"
  - "[[Prefect Workflow Control Points]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs]]"
  - "[[OpenAI Structured Outputs 文档]]"
evidence:
  - "[[Workflow Guardrails 主源#值得先读的主源]]"
  - "[[Workflow Guardrails 主源#边界提醒]]"
  - "[[Prefect Workflow Control Points#需要我读的内容]]"
  - "[[Agentproof - Static Verification of Agent Workflow Graphs#论文主张]]"
  - "[[OpenAI Structured Outputs 文档#Constrained decoding 锚点]]"
related:
  - "[[Guardrails]]"
  - "[[Agent Workflow]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Constrained Decoding]]"
  - "[[Agent Workflow Static Verification]]"
---

# Workflow Guardrails

## 一句话

Workflow Guardrails 是把 guardrails 放到 workflow 的输入、模型调用、工具调用、检索、输出、状态变化和副作用提交边界上，而不是只在最终回答上过滤。

## 概念详解

这个概念出现的原因是：Agentic workflow 不再是一次 prompt -> answer。它会读取外部资料、检索、调用工具、handoff 给 specialist、写数据库、触发外部 API、进入人工审批或在失败后重试。只在最外层用户输入和最终回答做 guardrail，会漏掉中间节点：模型可能已经看过不该看的 retrieval chunk，工具参数可能已经包含敏感数据，内部 API 可能已经被调用，或者某个 delegated agent 的输出绕过了最终输出检查。

多个主源支持同一个方向。OpenAI Agents SDK 把 guardrails 的 workflow boundaries 区分为 input、output 和 tool guardrails，并提醒它们并不在 workflow 的同一点运行；LangChain 把 guardrails 做成 middleware，放在 before agent、after agent、around model/tool calls；NeMo Guardrails 把 rails 分成 input、output、dialog、retrieval、execution；AWS Bedrock 的 `ApplyGuardrail` 支持在应用流程中独立评估 input 或 output；Guardrails AI 把 raw LLM output 变成 validated output；Semantic Kernel filters 和 Google ADK callbacks 则展示了 prompt render、function invocation、model/tool/agent 前后这些可拦截点。

因此，Workflow Guardrails 的稳定内核不是某个库的类名，而是一个工程判断：把风险检查放到风险发生之前或刚发生之后的最近边界上。输入风险在 request intake 附近检查，检索污染在 retrieval 后检查，工具越权在 tool call / internal API call 前检查，结构化输出在写库前检查，副作用在 commit 前检查，失败和异常在 workflow state change 时记录、告警或补偿。

它还和 [[Agent Workflow Static Verification]] 互补。runtime workflow guardrails 处理内容、参数、策略和副作用；static verification 更偏部署前检查 workflow graph 的 dead end、不可达 exit、绕过 human gate、敏感工具路径等结构缺陷。一个管“这次具体执行是否安全/合格”，一个管“这张流程图是否天然有坏路径”。

## 它解决什么问题

- 防止只过滤最终回答，却已经发生敏感数据读取、工具误调用或内部副作用。
- 把 guardrails 从散落的业务 if 判断，提升为 workflow 的明确控制点。
- 让失败策略可被审计：retry、reask、fix、filter、refuse、exception、human review、rollback 或 FAILED 状态都有归宿。
- 帮助把 LLM validation、policy engine、human-in-the-loop、trace、Prefect state hook / transaction / automation 连接起来。

## 它不是什么

- 不是 [[Guardrails]] 的替代概念；它是 guardrails 在 workflow 层的放置方式。
- 不是某个厂商 SDK 功能。OpenAI、LangChain、NeMo、Bedrock、Guardrails AI、Semantic Kernel、ADK 的 API 都是证据和实现样本，不是稳定定义本身。
- 不是 [[Policy Engine]]。policy engine 做 allow/deny/approval 等决策，workflow guardrails 决定这些决策应该嵌在哪些流程边界。
- 不是 [[Agent Workflow Static Verification]]。静态验证看 graph topology 和路径策略，workflow guardrails 看运行时内容、参数、输出和副作用。
- 不是“安全已解决”。guardrails 会误判、漏判、延迟过高、规则冲突，仍需最小权限、沙箱、审计、测试和人工复核。

## 最小例子

```text
flow starts
  -> input guardrail: request 是否越权 / 是否含攻击
  -> retrieval
  -> retrieval guardrail: chunk 是否可用 / 是否含注入 / 是否越权
  -> model call
  -> output validator: JSON schema、字段范围、引用支持
  -> tool guardrail: tool + params 是否允许，是否需要 approval
  -> transaction boundary: 通过验证才 commit DB / external API side effect
  -> state hook / automation: failure、crash、timeout、manual review、audit
```

如果 LLM 生成了一个 `billing_claim_status = "approved"`，workflow guardrail 的问题不是“回答好不好听”，而是：这个字段能不能通过 schema 和业务规则？是否有证据支持？是否允许直接写 DB？失败时是 reask、清空字段、标记 FAILED，还是转人工复核？

## 常见误解和风险

- 误解：final output guardrail 足够。风险：tool call、retrieval、日志、DB 写入都可能在最终回答之前发生。
- 误解：把所有 guardrail 都做成 model-based classifier。风险：成本高、延迟高、不可解释，并且对简单 schema/权限问题不如确定性规则。
- 误解：callback / hook 越多越安全。风险：规则散落、顺序不明、失败策略冲突，最后无法审计。
- 误解：Prefect hook 就是 guardrail。风险：hook 只是状态边界；真正的判断仍需要 validator、policy、model guardrail 或业务规则。
- 误解：static verification 能替代 runtime guardrails。风险：graph 检查不理解具体 LLM 输出语义和业务参数正确性。

## 边界细节

| 放置点 | 典型检查 | 更接近的来源证据 | 边界 |
|---|---|---|---|
| workflow input | 用户请求、权限、PII、攻击意图 | OpenAI input guardrails、LangChain before agent、NeMo input rails、Bedrock input evaluation | 不能证明后续检索和工具都安全 |
| retrieval / observation | 检索片段、网页、转写、工具结果是否可信 | NeMo retrieval rails、RAG / indirect prompt injection 相关边界 | 不替代索引层 access control |
| model call around | prompt render、model input/output、中间消息 | LangChain around model calls、Semantic Kernel prompt render filter、ADK model callbacks | 不应把所有业务规则塞进 prompt |
| tool / execution | tool choice、参数、内部 API、外部副作用 | OpenAI tool guardrails、NeMo execution rails、LangChain around tool calls、ADK tool callbacks | 越靠近真实副作用，越需要 policy、approval、sandbox |
| structured output | schema、字段范围、引用、事实支持 | Guardrails AI Guard / Validators / OnFail actions | schema 合格不等于事实正确 |
| constrained decoding | 解码时按 schema / grammar mask 非法 token | OpenAI Structured Outputs、Guidance / Outlines 相关机制 | 只约束单次输出结构，不覆盖 workflow 路径、工具权限或事实正确性 |
| state transition | failure、crash、completion、running | Prefect state change hooks | state hook 承载结果，不生成判断 |
| transaction / commit | DB 写入、文件生成、外部 API 的 commit / rollback / idempotency | Prefect transactions | 不可逆外部动作仍要业务幂等和补偿 |
| automation / observability | 事件触发通知、暂停、恢复、创建 flow run | Prefect automations、IBM orchestration production concerns | 告警不等于预防 |

## 现代性状态

current-practice / watch。把 guardrails 放在 workflow 的多个边界，已经是多个现代 Agent / LLM workflow 框架共同采用的工程方向；但具体 SDK 名称、API 参数、内置检测器、模型分类器和云服务能力仍快速变化，需要按 source note 的 `last_checked` 定期复查。

稳定部分：控制点位置、失败策略、运行时与静态验证互补。

易变部分：OpenAI / LangChain / NeMo / Bedrock / ADK / Semantic Kernel / Guardrails AI / Prefect 的具体 API、版本和产品能力。

## 现代系统怎么吸收这个概念的价值

现代系统通常把 Workflow Guardrails 吸收到四层：

1. **agent/runtime 层**：before/after/around model/tool/agent 的 middleware、callback、filter、guardrail。
2. **validator/policy 层**：schema、PII、business rule、allow/deny/approval、on_fail action。
3. **orchestration 层**：workflow state、retry、failure handling、transaction、rollback、automation。
4. **verification/observability 层**：trace、audit、eval、red-team、static workflow graph check。

工程上最容易被忽略的是第二层到第三层的交界：LLM 输出通过了格式校验，不代表可以写库；policy 允许某个 tool，也不代表这次参数和上下文可以免审批。

## 证据锚点

- Source evidence: [[Workflow Guardrails 主源#值得先读的主源]]
- Prefect source evidence: [[Prefect Workflow Control Points#需要我读的内容]]
- Static verification boundary: [[Agentproof - Static Verification of Agent Workflow Graphs#论文主张]]；[[Agent Workflow Static Verification#概念详解]]
- Existing concept anchors: [[Guardrails#概念详解]]；[[Policy Engine#概念详解]]；[[Approval Gate#概念详解]]；[[Agent Lifecycle Hook#概念详解]]
- Evidence type: official docs + source aggregation + engineering synthesis.
- Boundary: 具体项目 / Prefect 映射是工程综合，不是上述文档对某个业务系统的直接建议。
- Confidence: medium-high for guardrail placement trend; medium for exact implementation mapping because不同框架会改变 API 和命名。

## 复习触发

1. 为什么 output guardrail 不能替代 tool guardrail？
2. 一个 LLM workflow 在“写数据库前”至少应该检查哪三类东西？
3. Prefect state hook、transaction、automation 分别更像哪一种 workflow guardrail 承载点？
4. Workflow Guardrails 和 Agent Workflow Static Verification 的最小区别是什么？

## 相关链接

- [[Guardrails]]
- [[Agent Workflow]]
- [[Agent Lifecycle Hook]]
- [[Policy Engine]]
- [[Approval Gate]]
- [[Constrained Decoding]]
- [[Human-in-the-loop]]
- [[Agent Workflow Static Verification]]
- [[Workflow Guardrails 与 Prefect 控制点映射]]
