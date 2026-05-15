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
updated: 2026-05-13
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

# 03 LangGraph 专项回答

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

完成状态：已回答。用户用 Excalidraw 画出了线性“理解-搜索-回答”流程；下方整理为可检索文本。

用户图 1：线性理解-搜索-回答流程

![[Drawing 2026-05-11 21.47.57.excalidraw.md]]

我的图结构：

```text
START
  -> understand_query_node
     输入：messages / user_query
     输出：search_query, step = "search"
  -> tavily_search_node
     输入：search_query
     输出：search_results 或 search_failed, step = "answer"
  -> generate_answer_node
     输入：user_query + search_results/search_failed
     输出：final_answer, step = "done"
  -> END

Excalidraw 原图还原：
user_input -- understand --> understand_query
understand_query -- understand and call tool --> tavily_search
tavily_search -- search and return --> generate_answer
generate_answer -- print --> output

共享状态：
SearchState(messages, user_query, search_query, search_results, final_answer, step)
understand_query 更新 search_query + step
tavily_search 更新 search_results/search_failed + step
generate_answer 更新 final_answer + step
```

节点说明：

| 节点           | 输入状态 | 输出状态 | 关键副作用 / 风险 |
| ------------ | ---- | ---- | ---------- |
| `understand` | `messages`, `user_query` | `search_query`, `step="search"` | 误解用户意图会让后续搜索词偏掉；这里不应真正调用 Tavily。 |
| `search`     | `search_query` | `search_results` 或 `search_failed`, `step="answer"` | 外部 Tavily 调用可能失败、超时、返回噪音或过期信息。 |
| `answer`     | `user_query`, `search_results` / `search_failed` | `final_answer`, `step="done"` | 如果搜索失败，会 fallback 到模型已有知识；风险是缺少最新证据或产生幻觉。 |

边和转换条件：

| 边 | 条件 | 说明 |
|---|---|---|
| `START -> understand` | 初始 `SearchState` 已创建 | 进入理解节点，读取用户输入。 |
| `understand -> search` | 无条件边；节点完成后继续 | `search_query` 被写入 state；如果未来要处理空查询，才需要条件边。 |
| `search -> answer` | 无条件边；无论搜索成功或失败都继续 | 成功时带 `search_results`，失败时带 `search_failed`，由回答节点决定 fallback。 |
| `answer -> END` | `final_answer` 已生成 | 线性流程结束。 |

Codex 反馈：

你这张图已经抓住了核心主干：`understand_query -> tavily_search -> generate_answer -> output`，并且画出了每个节点对共享 state 的更新，这是 LangGraph 里最重要的学习点之一。

需要校准的地方有三处：

1. `user_input` 和 `output` 更像外部输入/最终产物，不是案例里的 LangGraph 节点；题目要求的图结构最好显式补上 `START` 和 `END`。
2. 你图里的 `initial_state` 不应该承担所有后续更新的名字；更准确是 `SearchState` 或 `shared state`。`initial_state` 只表示进入图之前的初始值，节点执行后它已经变成运行中的 state。
3. `understand and call tool` 这个边标签容易误导：`understand` 节点负责理解和生成 `search_query`，真正调用 Tavily 的是 `search` 节点。

本题是线性图，所以“状态转换条件”不是复杂判断，而是节点完成后无条件进入下一节点。搜索失败不是 `search -> answer` 的边被切换，而是 `search` 节点把失败信息写进 state，`answer` 节点再根据 `search_failed` 选择 fallback。

写回判断：暂不写回概念卡。[[LangGraph]] 和 [[Agent State]] 已经覆盖 state / node / edge 的边界；如果后面 B 题继续暴露 `step` 字段和条件边的混淆，再把“`step` 是状态字段，不自动等于 LangGraph 条件边”写入 [[Agent State]]。


### 本小节写回候选

- [ ] 如果答清楚 state / node / edge 的边界，写回 [[LangGraph]] 或 [[Agent Workflow]]。
- [ ] 如果发现 `step` 字段与条件边的关系不清，写回 [[Agent State]]。

---

## LG-B：添加反思节点与循环机制

### B1. 反思节点设计

问题：

当前助手是线性流程。请扩展案例，添加一个“反思”节点：如果生成的答案质量低，例如过于简短或缺乏细节，系统应该重新搜索或重新生成答案。请设计这个循环机制的条件边逻辑。

回答区：

完成状态：已回答。用户用 Excalidraw 画出了带 `reflect` 的循环图；下方整理为可检索文本。

用户图 2：反思循环流程

![[Drawing 2026-05-11 21.47.57.excalidraw 1.md]]

新增 state 字段：

```yaml
self_reflexion: ""      # 反思结果 / 失败原因 / 下一步建议
retry_count: 0          # 防止无限循环
max_retries: 2          # 停止预算
```

新增节点：

| 节点                     | 作用                                                           | 输入                                                                            | 输出                                           |
| ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- | -------------------------------------------- |
| `reflect`              | 评估 `final_answer` 是否回答了 `user_query`，判断证据是否足够、答案是否太短、是否需要重试。 | `user_query`, `search_query`, `search_results`, `final_answer`, `retry_count` | `self_reflexion`, `step`, 可选更新 `retry_count` |
| 可选：`rewrite_query`     | 可以不单独建节点；如果保留，它只负责根据 `self_reflexion` 改写 `search_query`。     | `user_query`, `search_query`, `self_reflexion`                                | `search_query`, `step="search"`              |
| 可选：`regenerate_answer` | 可以不单独建节点；如果保留，它只是 `generate_answer` 的再次执行版本。                 | `user_query`, `search_results`, `self_reflexion`                              | `final_answer`, `step="reflect"`             |

条件边设计：

```text
START -> understand_query -> tavily_search -> generate_answer -> reflect

reflect -> END
  条件：答案质量合格，且没有明显缺证据 / 答非所问 / 过短问题。

reflect -> tavily_search
  条件：搜索失败、证据不足、搜索结果和用户问题不匹配，且 retry_count < max_retries。

reflect -> generate_answer
  条件：搜索结果已经够用，但 final_answer 过短、结构差、没有利用证据，且 retry_count < max_retries。

reflect -> END
  条件：retry_count >= max_retries；结束时给出当前最佳答案或失败说明。
```

停止条件 / 防死循环：

- 答案质量通过：进入 `END`。
- 达到 `max_retries`：进入 `END`，不要继续循环。
- 每次从 `reflect` 回到 `search` 或 `answer` 都更新 `retry_count`。
- `self_reflexion` 只保存本轮失败原因和下一步建议，不要把全部历史都塞进去。

Codex 反馈：

你的图已经答到了本题核心：线性三节点后面接一个 `reflect`，再由 `reflect` 决定结束、重新搜索或重新回答。

需要整理的边界是：`rewrite_query` 和 `regenerate_answer` 不是必须新增的 LangGraph 节点。它们分别有点重复 `understand_query` 和 `generate_answer`：

1. 如果要改搜索词，可以让 `reflect -> understand_query` 或 `reflect -> tavily_search`，由已有节点重新生成 / 使用 `search_query`。
2. 如果证据够但答案不好，可以直接让 `reflect -> generate_answer`，不用单独叫 `regenerate_answer`。
3. 真正新增且有独立职责的节点是 `reflect`，因为它负责质量评估和路由判断。

更小、更清楚的版本是：

```text
START
-> understand_query
-> tavily_search
-> generate_answer
-> reflect
   -> pass: END
   -> evidence_bad/search_failed: tavily_search
   -> answer_bad: generate_answer
   -> retry_limit: END
```

写回判断：本节先不写回概念卡。这里暴露出的可复用边界是“节点代表真实执行职责，不代表字段更新动作”；如果后面继续遇到节点拆分过细的问题，再写回 [[LangGraph]] 或 [[Agent Workflow]]。


### B2. 条件边伪代码

问题：

请把上面的循环机制写成伪代码，说明什么情况下进入 `END`、什么情况下重新搜索、什么情况下只重新生成答案。

我的伪代码：我选择画图，见上方嵌入的 Excalidraw。

```python
def reflect_route(state):
    if state["retry_count"] >= state["max_retries"]:
        return "END"

    if answer_is_good(
        user_query=state["user_query"],
        search_results=state["search_results"],
        final_answer=state["final_answer"],
    ):
        return "END"

    state["retry_count"] += 1

    if state.get("search_failed") or evidence_is_weak(state["search_results"]):
        state["self_reflexion"] = "证据不足或搜索失败，需要重新搜索。"
        return "tavily_search"

    if answer_is_too_short_or_off_target(state["final_answer"], state["user_query"]):
        state["self_reflexion"] = "证据可用，但回答质量不够，需要重新生成。"
        return "generate_answer"

    return "END"
```

Codex 反馈：

这段伪代码对应 LangGraph 里的 `add_conditional_edges("reflect", reflect_route, ...)`。重点不是函数名，而是 `reflect` 返回的路由标签必须能落到明确节点：`END`、`tavily_search` 或 `generate_answer`。

小边界：`step` 可以作为 state 里的可读阶段记录，但真正决定下一条边的是 LangGraph 的边配置和 routing function，不是 `step` 字段自己“自动跳转”。


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

- [x] 代码生成-测试-修复循环
- [ ] 论文写作-审阅-修改循环
- [ ] 其他：

完整图结构：

```text

```

节点说明：

| 节点  | 功能  | 输入  | 输出  | 失败处理 |
| --- | --- | --- | --- | ---- |
|     |     |     |     |      |
|     |     |     |     |      |
|     |     |     |     |      |

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

| 应用     | 我的框架选择 | 核心理由 | 为什么不选其他框架 | 风险 / 补充工程 |
| ------ | ------ | ---- | --------- | --------- |
| A 智能客服 |        |      |           |           |
| B 科研写作 | CAMEL  |      |           |           |
| C 金融风控 |        |      |           |           |

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
