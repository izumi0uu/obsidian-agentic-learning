---
type: map
topic:
  - agent
  - security
  - tools
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-17
source:
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Tool Poisoning]]"
  - "[[Data Exfiltration]]"
  - "[[Guardrails]]"
  - "[[Workflow Guardrails]]"
  - "[[Workflow Guardrails 主源]]"
  - "[[Workflow Guardrails 与 Prefect 控制点映射]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Least Privilege Tools]]"
  - "[[OWASP LLM Top 10 2025]]"
  - "[[OWASP Agentic Applications Top 10]]"
  - "[[MCP Tool Poisoning Threat Model]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Prompt Injection#证据锚点]]"
  - "[[Indirect Prompt Injection#证据锚点]]"
  - "[[Tool Poisoning#证据锚点]]"
  - "[[Data Exfiltration#证据锚点]]"
  - "[[Guardrails#证据锚点]]"
  - "[[Workflow Guardrails#证据锚点]]"
  - "[[Workflow Guardrails 与 Prefect 控制点映射#证据锚点]]"
  - "[[Policy Engine#证据锚点]]"
  - "[[Approval Gate#证据锚点]]"
  - "[[Least Privilege Tools#证据锚点]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]"
related:
  - "[[Agent 知识地图]]"
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Tool Poisoning]]"
  - "[[Data Exfiltration]]"
  - "[[Guardrails]]"
  - "[[Workflow Guardrails]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool 接口层对比]]"
---

# Agent 安全控制点对比

## 一句话总览

这页回答：Agent 安全里哪些是攻击入口、哪些是风险结果、哪些是控制机制。最小边界是：[[Prompt Injection]] / [[Indirect Prompt Injection]] / [[Tool Poisoning]] 是诱导或污染入口，[[Data Exfiltration]] 是常见高危结果，[[Least Privilege Tools]] 是授权原则，[[Tool Permissioning]] / [[Policy Engine]] / [[Approval Gate]] / [[Guardrails]] 是运行时控制点，[[Workflow Guardrails]] 进一步回答这些控制点应该落在 workflow 的哪些边界。

不要把“安全”只理解成最终回答过滤。Agent 一旦接入工具、文件、浏览器、MCP server 或企业数据，安全边界必须前移到输入来源、工具可见性、参数范围、执行前审批、输出通道和 trace/audit。

## 为什么这组值得对比

- 混淆风险高：prompt injection、tool poisoning、data exfiltration 经常被混成“模型被攻击”；guardrails、policy、approval、least privilege 又常被混成“加安全层”。
- 共同问题域相同：都围绕 Agent 如何在读取不可信内容、调用工具和产生真实副作用时不越权。
- 不同介入点清晰：有的在输入/上下文，有的在工具生态，有的在数据结果，有的在执行前控制。
- 证据密度足够：相关概念卡已有 OWASP LLM / Agentic Top 10、MCP Tool Poisoning Threat Model、OpenAI Agents SDK / Computer Use 等锚点。
- 复习价值高：这组对比能帮助把安全问题定位到“入口、权限、策略、审批、输出通道、审计”的具体层，而不是泛泛说“加 guardrails”。

边界：本页是控制点 ontology，不是完整安全方案或厂商配置教程。

## 共同问题域

共同问题是：Agent 把自然语言、外部资料和工具动作放进同一个 loop。攻击者不一定需要直接控制模型，只要能控制网页、文档、邮件、工具描述、工具返回值、registry 元数据或某个输出通道，就可能影响 Agent 的下一步行动。

如果 Agent 还会按需加载 skill，那么 `SKILL.md`、skill 描述、触发条件和完成定义也属于这条链路的一部分。它们不是普通说明文，而是会影响能力发现、选择、信任和加载的运行时输入；因此错误 skill 或恶意 skill metadata 应按 tool / skill supply-chain 风险处理。

一个简化风险链路是：

```text
untrusted input / tool metadata / external content
  -> skill or tool discovery and selection
  -> model context and tool choice
  -> over-broad permissions or weak policy
  -> high-risk tool/action/output channel
  -> data exfiltration, unauthorized action, audit gap
```

控制点的目标不是证明模型永远不会被诱导，而是在模型可能被诱导时，让权限、策略、审批、沙箱和审计阻止真实副作用。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Prompt Injection]] | 用户输入或上下文中的恶意指令诱导 | 内容进入模型上下文时 | 用户文本、外部片段、任务说明 | 模型偏离任务、越权请求或错误工具意图 | [[Prompt Injection#证据锚点]] |
| [[Indirect Prompt Injection]] | 第三方网页、文档、邮件、检索片段、工具结果里的隐藏指令 | Agent 读取外部内容后、执行工具前 | RAG 片段、网页、Issue、邮件、observation | 外部内容被误当成控制指令 | [[Indirect Prompt Injection#证据锚点]] |
| [[Tool Poisoning]] | 工具描述、schema、annotations、返回值、registry 或供应链污染 | 工具发现、选择、调用或接收结果时 | tool metadata、MCP server、工具结果、供应链更新 | 错误工具选择、恶意参数、进一步注入 | [[Tool Poisoning#证据锚点]] |
| Skill metadata risk | `SKILL.md`、skill 描述、触发条件或完成定义影响能力选择和信任 | skill 发现、选择、加载、执行前审查时 | skill registry metadata、自然语言说明、workflow step、模板 | 错误流程、越权步骤、不适用完成定义、治理规避 | [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]] |
| [[Data Exfiltration]] | 敏感数据跨出授权边界的结果风险 | 读取敏感数据后，通过输出或工具通道外送时 | 私密文件、数据库、cookie、邮件、tool result | 聊天回复、HTTP、邮件、日志、第三方工具参数等外泄 | [[Data Exfiltration#证据锚点]] |
| [[Least Privilege Tools]] | 最小工具、最小数据、最小参数和最短授权原则 | 任务开始前授权；任务阶段变化时收窄 | 任务目标、用户身份、工具集合、数据范围 | 缩小后的可见工具和可执行动作边界 | [[Least Privilege Tools#证据锚点]] |
| [[Guardrails]] | 输入、输出、工具动作的防护层组合 | 模型调用前后、工具调用前后 | 规则、分类器、schema、敏感信息检测、policy、trace | 拦截、修正、拒绝、降级、触发审批 | [[Guardrails#证据锚点]] |
| [[Workflow Guardrails]] | workflow 边界上的 guardrail placement | 输入、检索后、模型/工具调用周围、写库/commit 前、状态变化时 | validator、policy、approval、transaction、state hook、automation | 阻断、重试、修正、转人工、rollback、audit | [[Workflow Guardrails#证据锚点]] |
| [[Policy Engine]] | 模型外的规则/风险决策核心 | 工具选择前、参数提交前、输出发送前 | 上下文、用户、工具、参数、数据分类、风险等级 | allow / deny / require approval / redact / sandbox-only | [[Policy Engine#证据锚点]] |
| [[Approval Gate]] | 高风险或不可逆动作执行前的人类/策略准入点 | 执行器真正动作前 | 工具名、参数、目标对象、来源、风险说明 | 用户确认、拒绝、修改或升级审核 | [[Approval Gate#证据锚点]] |

## 最容易混淆的边界

- [[Prompt Injection]] vs [[Indirect Prompt Injection]]：前者可以来自当前用户或上下文文本；后者强调攻击者通过第三方内容间接影响 Agent，例如网页、文档、邮件、检索片段或 tool result。
- [[Prompt Injection]] vs [[Tool Poisoning]]：prompt injection 的载体主要是被模型读取的指令文本；tool poisoning 的载体是工具生态本身，包括 description、schema、annotations、返回值、registry 和供应链。
- Tool poisoning vs skill metadata risk：二者都在能力生态里发生。tool poisoning 更偏工具/schema/server/result；skill metadata risk 更偏能力包说明、适用条件、流程和完成定义。当前不必强行建新卡，可先作为 [[Tool Poisoning]] 与 [[Tool Registry]] 的边界扩展。
- [[Tool Poisoning]] vs [[MCP Registry]] 风险：registry 让 server 可发现，不等于 server 可信。工具上架、可安装、可调用分别是不同信任层。
- Agent reflection vs verification：模型反思可以发现明显冲突，但不能证明 skill 可信或适用。安全控制点需要 registry review、least privilege、policy、trace、eval 和 human approval，而不是让模型再解释一遍。
- [[Data Exfiltration]] vs injection：injection 是诱导手段，data exfiltration 是可能结果。没有敏感数据访问或输出通道时，注入不一定造成外泄。
- [[Guardrails]] vs [[Policy Engine]]：guardrails 是宽防护层；policy engine 是更偏规则/风险决策的核心组件，常被 guardrails 调用。
- [[Guardrails]] vs [[Workflow Guardrails]]：guardrails 是防护层总称；workflow guardrails 是“把防护层放到 workflow 哪些边界”的工程判断，例如 retrieval 后、tool call 前、validated output 写库前和 state hook 处。
- [[Least Privilege Tools]] vs [[Tool Permissioning]]：最小权限是原则，permissioning 是实现机制；本页把最小权限作为设计原则，工具接口页讨论 permissioning 机制。
- [[Approval Gate]] vs [[Human-in-the-loop]]：approval gate 特指高风险执行前的准入点；human-in-the-loop 还可以用于澄清、标注、评审、接管或训练数据校准。

## 执行时序 / 机制差异

```text
1. Input/source boundary:
   Prompt Injection / Indirect Prompt Injection enters context.

2. Tool ecosystem boundary:
   Tool Poisoning can affect schema, description, registry metadata, or result text.

3. Skill / workflow selection boundary:
   Skill metadata can bias which capability package is loaded, what workflow counts as done, and which tools it asks for.

4. Authorization boundary:
   Least Privilege Tools and Tool Permissioning shrink visible tools, data, parameters, and action types.

5. Runtime decision boundary:
   Policy Engine / Guardrails evaluate request, output, or tool/action intent.

6. Pre-execution boundary:
   Approval Gate pauses irreversible, high-impact, external, or cross-permission actions.

7. Result boundary:
   Data Exfiltration is detected/prevented through output policy, channel limits, trace, audit, and review.
```

关键顺序是：先减少能做什么，再判断该不该做，最后才执行。只在最终回答上过滤，无法阻止模型已经读取敏感数据、把秘密塞进工具参数，或在执行前调用了危险工具。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把 Agent 安全想成一栋办公楼：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Prompt Injection]] | 有人对前台说“忽略公司规定，把钥匙给我” | 说明直接诱导，不说明模型机制 |
| [[Indirect Prompt Injection]] | 攻击指令藏在快递单、访客纸条或网页打印件里 | 说明第三方内容入口，不覆盖所有供应链风险 |
| [[Tool Poisoning]] | 门禁设备说明书或钥匙标签被人改了 | 类比工具元数据被污染，不说明具体 MCP 实现 |
| Skill metadata risk | 标准作业流程书被换成“看起来专业但会误导员工”的版本 | 类比 skill 流程文本影响行动，不说明具体 skill 平台 |
| [[Data Exfiltration]] | 机密文件被带出楼外或拍照发走 | 说明结果风险，不代表所有外泄都经过聊天回复 |
| [[Least Privilege Tools]] | 员工只拿当前任务需要的房间钥匙 | 原则层，不等于具体门禁系统 |
| [[Guardrails]] | 安检、摄像头、禁带规则和异常报警的组合 | 防护层会误报漏报，不是绝对安全 |
| [[Policy Engine]] | 门禁系统按身份、时间、房间和任务判定放行 | 决策层，仍需规则维护和审计 |
| [[Approval Gate]] | 进入金库前必须主管现场确认 | 只适合高风险动作，不应每一步都打断 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[OWASP LLM Top 10 2025]] 与 [[Prompt Injection#证据锚点]] / [[Indirect Prompt Injection#证据锚点]] 支持“prompt injection 是 LLM/Agent 的核心风险，并且外部内容入口会放大风险”。
- [[OWASP Agentic Applications Top 10]] 与 [[Least Privilege Tools#证据锚点]] / [[Policy Engine#证据锚点]] 支持“Agent 的过度行动能力、身份、工具和人类信任边界需要显式控制”。
- [[MCP Tool Poisoning Threat Model]] 与 [[Tool Poisoning#证据锚点]] 支持“工具描述、返回内容、server/host/client 边界和供应链本身是攻击面”。
- [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]] 支持“`SKILL.md` 类自然语言 metadata 会影响 skill discovery、selection、governance 和 trust/use，因此是能力供应链风险面”。
- [[OpenAI Agents SDK 文档]] 与 [[Guardrails#证据锚点]] 支持“guardrails、tools、tracing 等已成为现代 Agent runtime 的工程抽象”。
- [[Workflow Guardrails 主源]] 与 [[Workflow Guardrails#证据锚点]] 支持“guardrails 已经被多个框架放到 before/after/around model/tool、retrieval、execution、validator、filter、callback 等 workflow control points”。
- [[OpenAI Computer Use 文档]] / [[Anthropic Computer Use 文档]] 与 [[Approval Gate#证据锚点]] 支持“GUI / computer-use / 外部动作需要 sandbox、allowlist 和 human confirmation”。

### 工程综合 / inference

现代 Agent 安全通常采用纵深防御：外部内容标记为 data，工具按最小权限暴露，policy engine 在模型外决策，高风险动作进入 approval gate，trace/audit 保留事实，evaluation/red-team 检查绕过路径。没有任何单一 guardrail 能覆盖所有风险。

### 仍需警惕的外推

- 安全分类、SDK guardrail 接口、MCP registry 和 computer-use 产品能力会快速变化；本页沉淀概念边界，不替代最新官方文档。
- “工程综合 / inference”部分是把已有概念卡和 source note 串成控制链，不声称某个框架已经完整实现全部层。
- 控制点越多，越需要测试和 trace；否则规则可能互相冲突或制造不可解释拒绝。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 用户输入试图覆盖系统指令 | [[Prompt Injection]] | 攻击入口是当前上下文里的恶意指令 | 不要只靠“更强 system prompt” |
| Agent 读取网页/邮件/检索片段后行为异常 | [[Indirect Prompt Injection]] | 第三方内容可能被误当成指令 | RAG/浏览器/工具结果都要标记来源 |
| 新接入 MCP server 或工具描述很诱导 | [[Tool Poisoning]] | 工具元数据、schema 或返回值可能被污染 | registry 上架不等于可信 |
| Agent 自动加载了一个看似匹配但不适用的 skill | [[Tool Registry]], [[Tool Poisoning]], [[Evaluation]] | 问题在能力发现/选择/完成定义，不是只在模型推理层 | reflection 只能辅助怀疑，不能替代验证和权限治理 |
| 担心秘密被发到聊天、HTTP、邮件、日志 | [[Data Exfiltration]] | 这是跨边界输出结果风险 | 只过滤最终回复不够，要看工具参数和日志 |
| 任务只需读公开文档，却暴露了写文件/联网/邮件 | [[Least Privilege Tools]] | 应先收窄工具、数据和动作范围 | 权限过宽会放大所有注入风险 |
| 需要把规则变成可执行决策 | [[Policy Engine]] | 模型外判定 allow / deny / approval | 规则不可测会变成黑箱 |
| 高风险动作需要用户确认 | [[Approval Gate]] | 在执行前展示动作、参数、来源和风险 | 只弹“确认吗”但不给上下文会让用户机械点击 |
| 需要输入/输出/工具动作多点防护 | [[Guardrails]] | guardrails 是组合防护层，可调用 policy、分类器、schema 和审批 | guardrails 会误判漏判，不能单独保证安全 |
| 需要把 guardrail 接到 flow/task/DB 写入/失败处置 | [[Workflow Guardrails]] | 它关注 guardrail placement、failure policy 和副作用边界 | 不要把 hook、callback 或 transaction 误当成安全判断本身 |

## 它们共同不是什么

- 都不是“模型真的理解并永远遵守规则”的证明。
- 都不是只靠 system prompt 可以解决的问题。
- 都不是只靠 Agent reflection 可以解决的问题；反思只能产生候选解释，不能替代权限、trace、测试、人审或回归评估。
- 都不是最终答案过滤器；很多风险发生在工具调用前、参数提交中、日志/trace/output channel 里。
- 都不是让 Agent 失去能力。目标是把能力限制在当前任务必要、可解释、可审计的边界内。
- 都不是一次性配置。工具、数据、用户、server、registry 和攻击手法变化后，控制点需要复查和测试。

## 证据锚点

- Concept anchors: [[Prompt Injection#证据锚点]], [[Indirect Prompt Injection#证据锚点]], [[Tool Poisoning#证据锚点]], [[Data Exfiltration#证据锚点]], [[Least Privilege Tools#证据锚点]], [[Guardrails#证据锚点]], [[Workflow Guardrails#证据锚点]], [[Policy Engine#证据锚点]], [[Approval Gate#证据锚点]], [[Tool Permissioning#证据锚点]]
- Source examples: [[OWASP LLM Top 10 2025]], [[OWASP Agentic Applications Top 10]], [[MCP Tool Poisoning Threat Model]], [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]], [[OpenAI Agents SDK 文档]], [[OpenAI Computer Use 文档]], [[Anthropic Computer Use 文档]]
- Evidence type: concept-card synthesis + security source notes + official docs source notes + engineering synthesis + learning analogy.
- Confidence: medium-high for attack/control taxonomy; medium for exact runtime layering because不同框架会把 policy、guardrails、approval 和 permissioning 命名或实现为不同组件。
- Boundary: 类比只帮助学习，不是来源证据；本页不声称某个 guardrail 或 policy engine 能提供绝对安全。

## 复习触发

1. Prompt Injection 和 Tool Poisoning 都能诱导模型，最小载体区别是什么？
2. 为什么 Data Exfiltration 是结果风险，而不是一种单独的输入攻击？
3. 如果一个 Agent 只在最终回答上做敏感词过滤，还漏掉了哪些外泄通道？
4. Least Privilege Tools、Policy Engine、Approval Gate 三者分别在什么时刻发挥作用？
5. 为什么 “MCP Registry 上有这个 server” 不能直接推出“这个工具可被当前 Agent 自动调用”？
6. 为什么 “Agent 反思说这个 skill 适用” 不能直接推出“这个 skill 安全且正确”？

## 相关链接

- [[Agent 知识地图]]
- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Tool Poisoning]]
- [[Data Exfiltration]]
- [[Least Privilege Tools]]
- [[Tool Permissioning]]
- [[Guardrails]]
- [[Workflow Guardrails]]
- [[Workflow Guardrails 与 Prefect 控制点映射]]
- [[Policy Engine]]
- [[Approval Gate]]
- [[Tool Registry]]
- [[MCP]]
- [[MCP Registry]]
- [[Tool 接口层对比]]
