---
type: map
topic:
  - agent
  - workflow
  - security
  - durable-execution
  - comparison
status: active
created: 2026-05-14
updated: 2026-05-14
source:
  - "[[Workflow Guardrails]]"
  - "[[Workflow Guardrails 主源]]"
  - "[[Prefect Workflow Control Points]]"
  - "[[Agent Workflow Static Verification]]"
evidence:
  - "[[Workflow Guardrails#证据锚点]]"
  - "[[Workflow Guardrails 主源#值得先读的主源]]"
  - "[[Prefect Workflow Control Points#需要我读的内容]]"
related:
  - "[[Agent 知识地图]]"
  - "[[Guardrails]]"
  - "[[Workflow Guardrails]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
---

# Workflow Guardrails 与 Prefect 控制点映射

## 一句话总览

Workflow guardrails 回答“LLM / Agent workflow 的哪些边界需要检查”；Prefect control points 回答“这些检查结果如何落到 flow/task/state/transaction/automation 上”。

## 为什么这组值得对比

- 混淆风险高：容易把 guardrail 理解成最终输出过滤，也容易把 Prefect hook 误当成内容安全能力。
- 共同问题域明确：LLM workflow 里有模型输出、工具调用、检索片段、DB 写入、外部 API 和失败恢复。
- 工程价值高：业务项目 / Prefect 语境下，真正危险的不是“模型说错一句话”，而是错误结果被写库、触发副作用或悄悄进入下游流程。
- 证据密度足够：OpenAI / LangChain / NeMo / Bedrock / Guardrails AI 等主源支撑 guardrail placement；Prefect docs 支撑 state hook、transaction、automation。

边界：本页是工程映射，不是 Prefect 官方 guardrails 文档，也不是任何具体项目的实现说明。

## 共同问题域

共同问题是：一个 LLM workflow 的中间结果会变成后续步骤的输入，甚至变成真实系统副作用。控制点要尽量靠近风险发生位置：

```text
input -> retrieval / observation -> model -> validator -> tool/internal API -> transaction/DB -> state hook/automation
```

如果只在最后一步过滤，人已经看不到的中间副作用可能早就发生了。

## 核心映射表

| Guardrail 类型 | 放在 workflow 哪里 | Prefect 可承载点 | 业务项目 / Prefect 语境例子 | 边界 |
|---|---|---|---|---|
| input guardrail | flow entry / request intake | flow 开始 task；early fail state；policy task | 检查请求来源、用户权限、PHI/PII、任务是否允许自动处理 | 只保护入口，不保护后续检索和工具结果 |
| output guardrail | LLM 输出后、给用户或下游前 | validation task；FAILED / review state | 检查总结、字段、claim、citation 是否可展示 | 不等于可以写 DB |
| tool guardrail / execution rail | tool call / internal API call 前后 | tool task wrapper；approval task；state hook | 调用 internal API、发送消息、写入 billing/session 记录前检查参数和权限 | 真正副作用前还要 transaction / idempotency |
| retrieval / observation rail | retrieval、转写、tool result 后 | retrieval task 后的 validation task | 转写结果、检索片段、外部系统返回值是否可信、是否含注入或越权数据 | 不替代索引层 access control |
| validator / schema guard | LLM raw output -> typed output | Pydantic/schema validation task；Guardrails AI style validator | LLM 抽取结构化字段后，先生成 validated output，再进入业务规则 | schema 通过不等于事实正确 |
| policy engine | allow / deny / approval 决策 | policy task；branch / conditional flow | 高风险写库、跨用户数据读取、外部通知是否需要人工复核 | policy 规则需要版本化和测试 |
| on_fail action | validation failure 后的处置 | retry、reask task、manual review branch、FAILED state | retry LLM、清空无效字段、阻断写库、标记 FAILED、人工复核 | 不要让失败被静默吞掉 |
| state change hook | task/flow 状态变化 | `on_failure`、`on_completion`、`on_crashed`、`on_running` | 失败回写、审计、Slack/告警、补偿任务入口 | hook 承载处置，不产生安全判断 |
| transaction / side-effect guard | commit / rollback / idempotency 边界 | Prefect transactions；business idempotency key | 通过 validator + policy 后才写 DB；失败时 rollback 或补偿 | 不可逆外部 API 仍需业务补偿 |
| automation / observability guard | 运行时事件响应 | Prefect automations / events | 超时告警、暂停 work pool、创建复核 flow run、恢复 schedule | 主要是运行治理，不是内容过滤 |
| static workflow check | 部署前 / CI | Prefect flow lint + 外部 graph checker / CI | 检查敏感路径是否绕过 approval，失败路径是否无 exit | Prefect docs 不直接提供 Agentproof 式验证 |

## 执行时序 / 机制差异

```text
1. Intake: request guardrail decides whether the flow should start.
2. Evidence: retrieval / transcription / observation guardrail decides whether evidence can enter model context.
3. Generation: output validator converts raw LLM output into typed / validated output.
4. Decision: policy engine decides allow / deny / approval / review.
5. Side effect: transaction boundary commits or rolls back DB / file / external API work.
6. Runtime governance: state hook and automation record, alert, pause, resume, or create follow-up work.
7. Static check: graph / workflow lint checks whether sensitive paths bypass required control points.
```

关键边界是：validator 负责“这个结果像不像可用数据”，policy 负责“这次能不能执行”，transaction 负责“副作用怎么提交或回滚”，state hook / automation 负责“运行结果怎么被看见和处置”。

## 业务项目 / Prefect 工程映射（工程综合）

> 这一节是基于用户提供的项目 / Prefect 语境做的工程综合，不是外部文档对任何具体项目的直接描述。

对“LLM 结果不能直接写 DB”的最小落地可以是：

```text
transcript / retrieval
  -> observation guardrail
  -> LLM extraction
  -> schema validator
  -> business validator
  -> policy decision
  -> human review if needed
  -> transaction commit DB write
  -> state hook audit / notification
```

失败策略可以映射为：

| 失败类型 | 可能动作 | Prefect 表达 |
|---|---|---|
| JSON / schema 失败 | reask 或 deterministic fix | retry / reask task |
| 字段不可信 | filter / clear field | validation task 输出 partial result |
| 高风险或证据不足 | refrain / manual review | review branch / paused flow |
| 业务规则违反 | exception / FAILED | task failure + audit hook |
| 写库前失败 | rollback / no commit | transaction rollback |
| 外部 API 已调用失败 | compensation | follow-up compensation flow |

## 最容易混淆的边界

- [[Guardrails]] vs [[Workflow Guardrails]]：前者是防护层总称；后者强调防护层放在 workflow 哪些边界上。
- Prefect hook vs guardrail：hook 是状态变化后的执行入口；guardrail 是判断、拦截或修正逻辑。hook 可以承载 guardrail 结果，但不是判断本身。
- transaction vs validator：validator 判断数据是否合格；transaction 控制副作用是否提交或回滚。
- automation vs approval gate：automation 处理事件响应；approval gate 是高风险动作前的准入点。
- runtime guardrail vs static verification：runtime guardrail 检查当前执行；static verification 检查 graph 是否存在坏路径。

## 现代系统如何吸收或限制

来源支持的稳定部分：

- [[Workflow Guardrails 主源]] 支持 guardrails 已经被多个框架放到 input/output/tool/retrieval/execution/middleware/callback/filter 等控制点。
- [[Prefect Workflow Control Points]] 支持 Prefect 具备 state hooks、transactions、automations 这些 workflow 承载点。
- [[Agent Workflow Static Verification]] 支持 runtime guardrails 与 workflow graph 静态检查互补。

工程综合 / inference：

- Prefect 适合承载 workflow guardrails 的 orchestration 结果，但不替代模型内容安全、schema validation、business policy 和 human approval。
- 具体系统应把 guardrail 定义、policy 规则、failure policy 和 state transition 都写成可测试、可追踪的对象，否则 guardrails 会变成散落的业务代码。

## 它们共同不是什么

- 都不是“加一个安全库就完成治理”。
- 都不是最终回答过滤器。
- 都不是事实正确性的证明。
- 都不是只靠 prompt 能实现的行为约束。
- 都不是一次性配置；随着工具、数据、模型、业务规则和外部 API 变化，需要复查。

## 证据锚点

- Guardrail placement: [[Workflow Guardrails 主源#值得先读的主源]]
- Prefect control points: [[Prefect Workflow Control Points#需要我读的内容]]
- Durable concept: [[Workflow Guardrails#证据锚点]]
- Static complement: [[Agent Workflow Static Verification#证据锚点]]
- Evidence type: official docs/source notes + engineering synthesis.
- Boundary: 业务项目 / Prefect 段落是工程映射；没有声称 Prefect 官方把这些能力命名为 guardrails。
- Confidence: medium-high for mapping shape; medium for exact project implementation because真实代码、数据模型和业务 SLA 未在本页验证。

## 复习触发

1. Prefect `on_failure` hook 为什么不是 guardrail 本身？
2. 如果 LLM 输出要写 DB，validator、policy、transaction 三者分别做什么？
3. 哪些风险必须在 tool/internal API 调用前检查，而不是等最终 output guardrail？
4. Agentproof 这类 static verification 能发现什么，不能发现什么？

## 相关链接

- [[Workflow Guardrails]]
- [[Guardrails]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Policy Engine]]
- [[Approval Gate]]
- [[Agent Lifecycle Hook]]
- [[Agent Workflow Static Verification]]
