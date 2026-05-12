---
type: review
topic:
  - agent
  - langgraph
  - workflow
  - framework
  - review
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[LangGraph]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Agent Framework 编排范式对比]]"
related:
  - "[[reviews/复习记录索引]]"
  - "[[02 经典智能体范式综合实践]]"
  - "[[LangGraph]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Evaluation]]"
  - "[[Durable Execution]]"
  - "[[Agent Framework 编排范式对比]]"
---

# 02 LangGraph 专项回答

日期：2026-05-12

## 来源

这页承接 LangGraph 章节题，基于一个“三步问答助手”案例：

```text
理解用户需求
-> 使用 Tavily API 搜索信息
-> 基于搜索结果生成回答
```

案例代码的核心结构：

- `SearchState`：保存 `messages`、`user_query`、`search_query`、`search_results`、`final_answer`、`step`。
- `understand_query_node`：理解用户输入，并生成搜索词。
- `tavily_search_node`：调用 Tavily 搜索，写入搜索结果；失败时写入 `search_failed`。
- `generate_answer_node`：根据搜索结果生成回答；搜索失败时 fallback 到模型已有知识。
- `StateGraph(SearchState)`：用 `START -> understand -> search -> answer -> END` 表达线性流程。
- `InMemorySaver`：用于本地内存 checkpoint。

边界：这页是学习回答记录，不是 raw evidence，不直接替代 [[LangGraph]] 或 [[Agent Workflow]] 概念卡。答完后把新的边界、误解或工程模式写回概念卡、对比页、[[05 Query 写回队列]] 或 [[02 问题池]]。

## 使用规则

- 从 `LG-A` 开始，每次回答一个小节。
- 图结构可以用 ASCII 图、Mermaid 或表格表达。
- 如果涉及代码改造，先写状态字段、节点、条件边和停止条件，再写代码。
- 每个小节答完后必须判断写回归宿。

---

## LG-A：三步问答助手的图结构

### A1. 状态机 / 有向图结构

问题：

LangGraph 将智能体流程建模为状态机和有向图。请画出案例中“理解-搜索-回答”流程的图结构，标注节点、边和状态转换条件。

回答区：

我的图结构：

```text

```

节点说明：

| 节点 | 输入状态 | 输出状态 | 关键副作用 / 风险 |
|---|---|---|---|
| `understand` |  |  |  |
| `search` |  |  |  |
| `answer` |  |  |  |

边和转换条件：

| 边 | 条件 | 说明 |
|---|---|---|
| `START -> understand` |  |  |
| `understand -> search` |  |  |
| `search -> answer` |  |  |
| `answer -> END` |  |  |

Codex 反馈：


### 本小节写回候选

- [ ] 如果答清楚 state / node / edge 的边界，写回 [[LangGraph]] 或 [[Agent Workflow]]。
- [ ] 如果发现 `step` 字段与条件边的关系不清，写回 [[Agent State]]。

---

## LG-B：添加反思节点与循环机制

### B1. 反思节点设计

问题：

当前助手是线性流程。请扩展案例，添加一个“反思”节点：如果生成的答案质量低，例如过于简短或缺乏细节，系统应该重新搜索或重新生成答案。请设计这个循环机制的条件边逻辑。

回答区：

新增 state 字段：

```yaml

```

新增节点：

| 节点 | 作用 | 输入 | 输出 |
|---|---|---|---|
| `reflect` |  |  |  |
| 可选：`rewrite_query` |  |  |  |
| 可选：`regenerate_answer` |  |  |  |

条件边设计：

```text

```

停止条件 / 防死循环：

- 

Codex 反馈：


### B2. 条件边伪代码

问题：

请把上面的循环机制写成伪代码，说明什么情况下进入 `END`、什么情况下重新搜索、什么情况下只重新生成答案。

我的伪代码：

```python

```

Codex 反馈：


### 本小节写回候选

- [ ] 如果答清楚 `reflect -> search / answer / END` 的条件边，写回 [[LangGraph]]。
- [ ] 如果答清楚质量评估和终止条件，写回 [[Evaluation]] / [[Agent Workflow]]。
- [ ] 如果答清楚循环预算、重试次数、超时或人工升级，写回 [[Agent Harness]] / [[Durable Execution]]。

---

## LG-C：充分利用循环的复杂应用场景

### C1. 设计一个循环型 LangGraph 应用

问题：

LangGraph 的优势在于对循环的原生支持。请设计一个更复杂的应用场景，充分利用这一特性，例如“代码生成-测试-修复”循环、“论文写作-审阅-修改”循环等。要求画出完整图结构并说明关键节点功能。

回答区：

我选择的场景：

- [ ] 代码生成-测试-修复循环
- [ ] 论文写作-审阅-修改循环
- [ ] 其他：

完整图结构：

```text

```

节点说明：

| 节点 | 功能 | 输入 | 输出 | 失败处理 |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

关键循环条件：

| 条件 | 下一节点 | 为什么 |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Codex 反馈：


### C2. State / Checkpoint / Trace 设计

问题：

这个循环应用中，哪些信息应该放进 state？哪些信息应该进入 checkpoint？哪些信息只适合留在 trace 里？

回答区：

| 信息 | state | checkpoint | trace | 理由 |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

Codex 反馈：


### 本小节写回候选

- [ ] 如果答清楚循环型应用图结构，写回 [[LangGraph]] / [[Agent Workflow]]。
- [ ] 如果答清楚 state、checkpoint、trace 的分层，写回 [[Agent State]] / [[Durable Execution]] / [[Trace]]。
- [ ] 如果形成完整代码生成或论文写作架构，写入 [[05 Query 写回队列]]。

---

## LG-D：框架选型题

### D1. 三个产品的框架选择

问题：

假设你是一家 AI 公司的技术架构师，公司计划开发以下三个智能体产品应用。请为每个应用选择最合适的框架：[[AutoGen]]、[[AgentScope]]、[[CAMEL]]、[[LangGraph]] 或不借助框架从零开发，并详细说明理由。

应用 A：

智能客服系统，需要处理大量并发用户请求，每秒 1000+，要求响应时间低于 2 秒，系统需要 7×24 小时稳定运行，并支持水平扩展。

应用 B：

科研论文辅助写作平台，需要一个“研究员智能体”和一个“写作智能体”深度协作，共同完成文献综述、实验设计、数据分析和论文撰写。要求智能体能够进行多轮深度讨论，自主推进任务。

应用 C：

金融风控审批系统，需要按照严格流程处理贷款申请：资料审核 -> 风险评估 -> 额度计算 -> 合规检查 -> 人工复核 -> 最终决策。每个环节都有明确判断标准和分支逻辑，要求流程可追溯、可审计。

回答区：

| 应用 | 我的框架选择 | 核心理由 | 为什么不选其他框架 | 风险 / 补充工程 |
|---|---|---|---|---|
| A 智能客服 |  |  |  |  |
| B 科研写作 |  |  |  |  |
| C 金融风控 |  |  |  |  |

Codex 反馈：


### D2. 选型背后的抽象中心

问题：

请用一句话说明每个选择背后的抽象中心：它主要依赖消息协作、角色扮演、平台并发、状态图 workflow，还是普通工程服务？

回答区：

- 应用 A：
- 应用 B：
- 应用 C：

Codex 反馈：


### 本小节写回候选

- [ ] 如果答清楚 AutoGen / AgentScope / CAMEL / LangGraph 的抽象中心，写回 [[Agent Framework 编排范式对比]]。
- [ ] 如果答清楚高并发客服不一定适合多 Agent 框架，写回 [[Agent Framework]] 或 [[Agent Framework 全量选型对比 2026-05]]。
- [ ] 如果答清楚金融风控需要可审计 workflow，写回 [[Agent Workflow]] / [[Human-in-the-loop]] / [[Trace]]。

---

## 总收束标准

完成这页后，应能用自己的话说明：

- LangGraph 里的 state、node、edge、condition 分别承担什么。
- 线性 graph 如何升级为带 reflection / evaluator 的循环 graph。
- 为什么循环必须有预算、停止条件和失败升级。
- state、checkpoint、trace 在长任务循环里分别保存什么。
- 框架选型时为什么不能只看“支持多 Agent”，而要看抽象中心、延迟、并发、审计、部署和业务风险。

## 总写回候选

- [ ] [[LangGraph]]：补三步助手、条件边、循环案例和框架边界。
- [ ] [[Agent Workflow]]：补线性流程、条件边、循环、人工复核和停止条件。
- [ ] [[Agent State]]：补 LangGraph state 字段设计、context 投影和 checkpoint 区分。
- [ ] [[Evaluation]]：补反思节点、答案质量判断和再搜索 / 再生成条件。
- [ ] [[Durable Execution]]：补长任务循环的 checkpoint、重试和恢复边界。
- [ ] [[Agent Framework 编排范式对比]]：补三类产品的框架选型判断。
