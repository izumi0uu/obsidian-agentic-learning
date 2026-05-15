---
type: map
topic:
  - agent
  - langgraph
  - workflow
  - infrastructure
  - rag
  - evaluation
  - governance
status: growing
created: 2026-05-14
updated: 2026-05-14
last_checked: 2026-05-14
freshness: watch
source:
  - "[[LangGraph 官方文档]]"
  - "[[LangGraph GitHub Repo]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[LangGraph Memory 官方文档]]"
evidence:
  - "[[LangGraph 官方文档#一句话]]"
  - "[[LangGraph 官方文档#边界提醒]]"
  - "[[LangGraph GitHub Repo#一句话]]"
  - "[[LangSmith Evaluation and Observability#一句话]]"
  - "[[LangGraph Memory 官方文档#一句话]]"
related:
  - "[[LangGraph]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Durable Execution]]"
  - "[[Human-in-the-loop]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
  - "[[Tool Permissioning]]"
---

# LangGraph 生产项目蓝图

## 一句话

一个真实的 LangGraph 生产项目不是“把 demo 的三步链条换成 graph”，而是把一个长任务 Agent 拆成可恢复、可审计、可审批的 [[Agent Workflow]]：用 [[Agent State]] 保存事实进度，用节点承载检索、推理、工具执行、审批和评估，用条件边控制失败、循环和升级，用 checkpoint / trace / eval / deployment 治理把 toy demo 变成可上线系统。

最小判断：如果系统需要多轮状态、条件路由、人工审批、外部工具副作用、暂停恢复或过程评估，LangGraph 这类 [[State Graph Runtime]] 才开始有价值；如果只是一次问答、一次结构化抽取或低风险调用，普通函数、chain 或 provider SDK 可能更轻。

## 适用场景

本页用一个“企业知识 + 工单处置助手”作为工程蓝图。它接收用户问题或工单，检索内部知识库、产品文档、历史 ticket、CRM / 数据库信息，必要时调用内部工具创建工单、修改状态、发送通知或提交审批。

适合 LangGraph 的条件：

| 条件 | 为什么需要 graph | 例子 |
|---|---|---|
| 任务会跨多个步骤 | 需要显式记录节点输入输出和下一步 | 分类 -> 多源检索 -> 草稿 -> 校验 -> 工具执行 |
| 有分支和循环 | 需要条件边，而不是靠 prompt 临场判断 | 证据不足时重新检索，答案不合格时重写 |
| 有外部副作用 | 工具调用前要权限、幂等、审批和审计 | 创建工单、改订单状态、发邮件 |
| 需要人类介入 | 人要看到 state / evidence / proposed action 后批准 | 高风险退款、合规回答、跨用户数据访问 |
| 需要恢复 | 进程重启、超时、人工等待后不能丢进度 | approval 等一天后从 checkpoint 继续 |
| 需要评估过程 | 最终答案对不够，还要看检索、工具、路由是否安全 | trace + trajectory evaluator + regression dataset |

不优先用 LangGraph 的场景：单轮 FAQ、固定 ETL、纯分类器、没有副作用的低风险文本生成、团队尚未准备好维护 state schema / checkpoint store / trace / eval 的小原型。

## 端到端架构

> 工程综合：以下是基于 LangGraph / LangSmith 官方能力和本 vault 已有 Agent 工程概念整理出的生产蓝图，不是官方唯一推荐架构。

```text
User / API / UI
  -> request_intake_node
  -> policy_precheck_node
  -> classify_or_plan_node
  -> retrieval_plan_node
  -> multi_source_retrieval_node
  -> evidence_rerank_and_filter_node
  -> draft_answer_or_action_node
  -> risk_assessment_node
      -> low_risk: tool_execution_node
      -> high_risk: human_approval_node -> tool_execution_node
      -> evidence_gap: retrieval_plan_node
  -> validation_node
      -> pass: final_response_node
      -> answer_bad: draft_answer_or_action_node
      -> policy_fail: human_review_or_reject_node
  -> final_response_node
  -> END

Side channels:
  checkpoint store / thread state
  trace + spans + audit log
  eval datasets + online evaluators
  deployment config + secrets + policy versions
```

### 分层责任

| 层 | 负责什么 | 不负责什么 |
|---|---|---|
| LangGraph graph | 节点、边、条件路由、循环、interrupt/resume、state 更新 | 自动保证答案正确、自动设计业务策略 |
| Retrieval / RAG | 多源召回、权限过滤、rerank、引用证据 | 决定高风险动作是否允许执行 |
| Tool layer | 结构化工具 schema、幂等键、超时、重试、权限 | 让 LLM 自由调用所有内部 API |
| Human approval | 对高风险动作做有上下文的批准、修改或拒绝 | 把所有低风险步骤都变成人工点击 |
| Checkpoint / persistence | 保存 thread / state / pending writes，用于恢复 | 代替长期记忆或业务数据库 |
| Trace / eval | 看见过程、打分、沉淀失败样本、回归测试 | 只靠漂亮 trace 证明系统有效 |
| Deployment / governance | 环境、版本、密钥、数据保留、监控、发布门禁 | 用一个 demo notebook 承担生产 SLA |

### 生产文件形态（示意）

```text
app/
  graph.py                 # StateGraph 定义、节点注册、条件边
  state.py                 # TypedDict / Pydantic state schema
  nodes/
    intake.py
    retrieval.py
    generation.py
    tools.py
    approval.py
    validation.py
  tools/
    ticketing.py           # 内部 API wrapper，含权限与幂等
    crm.py
  policies/
    risk_policy.py         # 哪些动作需要人工审批
    access_policy.py       # RAG / tool 权限过滤
  evals/
    datasets/*.jsonl
    evaluators.py
  deployment/
    langgraph.json
    env.example
```

文件形态不是重点，重点是责任不能混：节点只做一类动作，state schema 明确，工具层自己有权限和幂等，eval 不是上线后才补。

## State / 节点 / 边

### State schema

生产 state 不应该只塞一串 `messages`。`messages` 适合保存对话上下文，但生产 graph 还需要显式字段保存任务、证据、风险、审批、工具结果、错误和预算。

```python
class SupportAgentState(TypedDict):
    thread_id: str
    user_id: str
    tenant_id: str
    user_query: str
    task_type: Literal["qa", "ticket_action", "refund", "handoff"]

    permissions: list[str]
    retrieval_plan: list[dict]
    evidence: list[dict]          # source_id, snippet, score, acl, freshness
    citations: list[str]

    draft_answer: str
    proposed_action: dict | None  # tool_name, args, risk_level, idempotency_key
    tool_results: list[dict]

    risk_level: Literal["low", "medium", "high"]
    approval_status: Literal["not_required", "pending", "approved", "rejected"]
    validation_errors: list[str]
    retry_count: int
    max_retries: int
    final_answer: str | None
```

边界细节：

- `state` 保存“恢复和路由需要知道的事实”，不是保存所有日志。
- checkpoint 保存 state snapshot / pending writes，用于恢复；长期用户偏好进入 [[Memory]] / long-term store；完整过程进入 [[Trace]]。
- 不要把权限判断只写进 prompt；权限、租户、数据来源和工具参数要作为 state / metadata 可检查。
- 大对象、原始文件、完整检索语料不宜全塞 state；state 保存引用、摘要、哈希或对象 ID。

### 节点设计

| 节点 | 主要输入 | 主要输出 | 生产边界 |
|---|---|---|---|
| `request_intake` | user_query, user_id | normalized request, tenant_id | 做输入规范化，不做业务承诺 |
| `policy_precheck` | user_id, permissions, query | allow / deny / review hint | 权限判断应可测试，不靠模型口头承诺 |
| `classify_or_plan` | query, history summary | task_type, retrieval_plan draft | 复杂计划可用模型，但输出要结构化 |
| `multi_source_retrieval` | retrieval_plan, permissions | evidence candidates | 必须做 ACL / tenant filter，避免越权 RAG |
| `evidence_filter` | evidence candidates | ranked evidence, citations | 处理 freshness、重复、来源冲突 |
| `draft_answer_or_action` | query, evidence | draft_answer / proposed_action | 不直接执行副作用，只提出动作 |
| `risk_assessment` | proposed_action, policy | risk_level, approval requirement | 高风险动作进入 approval gate |
| `human_approval` | state summary, evidence, action | approved / rejected / edited args | 人类必须看到证据、参数、风险和可选修改 |
| `tool_execution` | approved action | tool_results | 工具 wrapper 负责幂等、超时、审计 |
| `validation` | draft, evidence, tool_results | pass / retry / reject | 同时检查格式、引用、权限、任务完成度 |
| `final_response` | final state | final answer, audit summary | 给用户的内容不等于内部 trace 全量暴露 |

### 边和条件路由

```text
risk_assessment -> human_approval
  条件：risk_level == "high" 或 policy 要求人工确认

risk_assessment -> tool_execution
  条件：risk_level in {"low", "medium"} 且工具在 allowlist 内

risk_assessment -> final_response
  条件：只需要回答，不需要外部副作用

validation -> retrieval_plan
  条件：证据不足、来源冲突、citation 不支持答案，且 retry_count < max_retries

validation -> draft_answer_or_action
  条件：证据够，但回答结构差、没有利用证据或工具参数不完整

validation -> human_review_or_reject
  条件：权限失败、高风险被拒绝、达到重试预算、来源冲突无法自动解决

validation -> final_response
  条件：任务完成、引用可追溯、工具结果成功或失败已解释
```

停止条件要显式：成功、用户取消、审批拒绝、重试预算耗尽、权限拒绝、工具不可用、证据不足且不能继续检索。没有停止条件的循环不是 Agent 能力，而是生产事故入口。

## 生产控制点

| 控制点 | 放在哪里 | 为什么 |
|---|---|---|
| 输入准入 | `request_intake` / `policy_precheck` | 拒绝无权限、越界或无法处理的请求 |
| RAG 权限过滤 | retrieval 前后 | 防止检索到用户不该看的文档；详见 [[RAG Access Control]] |
| 多源检索质量 | `retrieval_plan` + `evidence_filter` | 向量召回、关键词、结构化 DB、历史 ticket、知识图谱可能互补 |
| 引用可靠性 | `validation` | 最终回答的 claim 要能回到 evidence；详见 [[RAG Citation Faithfulness]] |
| 工具最小权限 | tool registry / wrapper | 每个工具限定 schema、scope、tenant、rate limit 和 allowlist |
| 副作用审批 | `risk_assessment` -> `human_approval` | 高风险动作先展示 state summary、参数、证据和影响范围 |
| 幂等与补偿 | `tool_execution` | 重试不能重复扣费、重复发邮件或重复创建工单 |
| Checkpoint / resume | graph compile / persistence | 人工等待、失败重启、长任务恢复都依赖 durable state |
| Trace / audit | 每个节点 / 工具 span | 调试、合规、复盘、成本和延迟都需要结构化过程记录 |
| Offline eval | 发布前 | 用固定 dataset / regression suite 比较 graph、prompt、retriever 和 tool 改动 |
| Online eval | 生产中 | 对真实 trace 做质量、安全、格式、trajectory 监控 |
| 部署治理 | CI/CD / LangSmith Deployment 或自托管 | 管理环境、密钥、版本、伸缩、数据保留和回滚 |

### RAG / 多源检索

生产 LangGraph 项目里的 RAG 通常不是一个 `retriever.invoke(query)` 节点，而是一组可被 trace 和 eval 的子流程：query rewrite / planning、权限过滤、向量召回、关键词召回、结构化查询、rerank、冲突处理、citation assembly。LangGraph 的价值在于让这些步骤变成节点和 state，而不是把所有检索逻辑藏进一个 prompt。

### 工具与权限

工具层至少要有四个边界：

1. schema：LLM 只能提交结构化参数。
2. permission：当前用户 / tenant / task 是否允许此工具。
3. idempotency：重试或恢复不会重复执行不可逆动作。
4. audit：谁、何时、基于什么证据、调用了什么工具、结果是什么。

[[Tool Permissioning]] 和 [[Approval Gate]] 是生产蓝图的一部分，不是上线后补丁。

### Human approval

人类审批不是最终“Approve”按钮，而是 graph 中的一个风险节点。审批 UI / 消息至少应展示：用户请求、检索证据、拟执行工具、关键参数、风险级别、可修改字段、拒绝后路径。审批结果要写回 state，并可从 checkpoint resume。

### Checkpoint / resume

根据官方文档，LangGraph 的 persistence / durable execution 围绕 checkpoint、thread、resume、interrupt 等机制展开。学习上要抓住三层：

- thread：一次用户任务或会话的持久执行线索。
- checkpoint：某个 super-step / 节点边界的 state snapshot。
- resume / replay：从已有 checkpoint 恢复或重跑后续步骤。

工程边界：checkpoint 能恢复 graph state，不自动解决外部副作用。工具节点必须自己处理幂等、事务、补偿和外部系统一致性。

### Trace / eval / deployment

[[LangSmith Evaluation and Observability]] 的 source note 把 trace、dataset、evaluator、experiment 和 production monitoring 连接成闭环。本蓝图里至少要有：

- node-level trace：每个节点输入、输出、错误、延迟、token/cost、model/tool version。
- trajectory eval：是否走了正确节点、是否绕过审批、是否陷入循环。
- RAG eval：检索召回、引用支持、权限过滤是否正确。
- tool eval：工具参数是否合规，失败后是否解释或升级。
- regression dataset：从失败 trace 和人工反馈沉淀样例。
- release gate：graph / prompt / retriever / tool policy 改动前后跑离线 eval。

部署可以使用 LangSmith / LangGraph deployment 路线，也可以自托管。无论哪种，生产系统都要显式管理 secrets、checkpoint store、trace retention、tenant isolation、rate limit、rollback、版本兼容和数据脱敏。

## 失败模式

| 失败模式 | 表现 | 控制方式 |
|---|---|---|
| State schema 贫血 | 只有 messages，没有权限、证据、工具结果和失败原因 | 先设计 state，再写节点 |
| 节点职责混杂 | 一个节点既检索、生成、执行工具又决定审批 | 拆成可 trace / 可测试的职责节点 |
| 条件边靠自然语言 | 模型说“我觉得可以继续”，但没有结构化路由 | routing function 输出固定标签和停止条件 |
| 循环无预算 | 反复检索 / 重写，成本失控 | `retry_count`、timeout、token budget、escalation |
| RAG 越权 | 检索到别的租户或无权限文档 | retrieval 前后做 ACL / tenant filter |
| 引用幻觉 | 回答带 citation，但 evidence 不支持 claim | citation faithfulness eval + 人审高风险答案 |
| 工具重复副作用 | resume / retry 后重复创建工单、重复发送通知 | idempotency key、transaction、tool result checkpoint |
| 审批无上下文 | 人只能看一个按钮，看不到风险和证据 | approval state summary + evidence + proposed args |
| checkpoint 误用 | 把 checkpoint 当长期记忆或业务数据库 | checkpoint 只保存执行恢复所需 state；业务事实进 DB/store |
| trace 不可用 | 出事后只知道最终答案错了 | node/span trace、metadata、redaction、retention |
| eval 太晚 | 上线后才发现 graph 改动破坏旧流程 | offline regression + online evaluator + failure-to-dataset |
| 框架迷信 | 认为用了 LangGraph 就是生产级 Agent | 生产级来自 state、policy、tooling、eval、deployment 的组合 |

## 它不是什么

- 不是 LangGraph API 教程：本页不教 `add_node` / `add_edge` 的具体语法，语法以官方文档为准。
- 不是框架选型排行榜：如果任务不需要 state graph / durable workflow，LangGraph 不是默认答案。
- 不是所有 Agent 必须采用的唯一架构：简单任务可用 chain、普通服务或 provider SDK。
- 不是 toy demo 放大版：生产项目的关键不在“多几个节点”，而在权限、恢复、副作用、trace、eval 和治理。
- 不是把所有业务逻辑交给 LLM：模型负责低确定性判断；权限、幂等、审批、schema、发布门禁应该由工程系统承载。

## 证据锚点

- 本 vault source note：[[LangGraph 官方文档#一句话]]、[[LangGraph 官方文档#边界提醒]]。
- Repo source note：[[LangGraph GitHub Repo#一句话]]、[[LangGraph GitHub Repo#边界提醒]]。
- LangSmith source note：[[LangSmith Evaluation and Observability#一句话]]、[[LangSmith Evaluation and Observability#边界提醒]]。
- Memory source note：[[LangGraph Memory 官方文档#一句话]]、[[LangGraph Memory 官方文档#边界提醒]]。
- 相关概念：[[LangGraph#现代系统怎么吸收 LangGraph 的价值 / 局限]]、[[Agent Workflow#现代系统怎么吸收 Agent Workflow 的价值 / 局限]]、[[Trace#现代系统怎么吸收 Trace 的价值 / 局限]]、[[Evaluation#现代系统怎么吸收 Evaluation 的价值 / 局限]]。
- 官方查证（2026-05-14）：LangGraph overview / durable execution / persistence / deployment 文档强调 low-level orchestration、durable execution、human-in-the-loop、persistence、checkpoint / thread / resume、LangSmith tracing/evaluation 和 deployment 路线。
- Evidence type：官方文档 / repo source notes + 2026-05-14 官方网页查证 + 工程综合。
- Confidence：medium-high for architecture/control-point shape；medium for deployment/API details because LangGraph / LangSmith 产品层 `freshness: watch`，需按官方文档复查。

## 复习触发

1. 为什么一个生产 LangGraph 项目的 state 不应该只包含 `messages`？至少列出 6 个需要显式保存的字段。
2. 在“退款审批”场景里，哪些节点可以自动执行，哪些节点必须进入 [[Human-in-the-loop]]？为什么？
3. checkpoint、long-term memory、trace、audit log 四者分别保存什么？哪个不能替代哪个？
4. 如果 validation 发现 citation 不支持答案，应该回到 retrieval、draft、human review 还是 END？写出条件边。
5. 为什么“最终答案正确”仍可能在生产 eval 里失败？举一个工具权限或审批绕过的例子。

## 相关链接

- [[LangGraph]]
- [[Agent Workflow]]
- [[Agent State]]
- [[Durable Execution]]
- [[Human-in-the-loop]]
- [[Trace]]
- [[Evaluation]]
- [[RAG]]
- [[RAG Access Control]]
- [[RAG Citation Faithfulness]]
- [[Tool Permissioning]]
- [[Approval Gate]]
- [[Policy Engine]]
- [[Workflow Guardrails]]
- [[Agent Framework 全量选型对比 2026-05]]
