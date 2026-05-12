---
type: map
topic:
  - agent
  - memory
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Long-term Memory]]"
  - "[[Episodic Memory]]"
  - "[[Semantic Memory]]"
  - "[[Memory Reflection]]"
  - "[[Parametric Memory]]"
  - "[[Non-Parametric Memory]]"
  - "[[LangGraph Memory 官方文档]]"
  - "[[Letta Memory 官方文档]]"
  - "[[Zep Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Memory#证据锚点]]"
  - "[[Agent State#证据锚点]]"
  - "[[Long-term Memory#证据锚点]]"
  - "[[Episodic Memory#证据锚点]]"
  - "[[Semantic Memory#证据锚点]]"
  - "[[Memory Reflection#证据锚点]]"
  - "[[Parametric Memory#证据锚点]]"
  - "[[Non-Parametric Memory#证据锚点]]"
related:
  - "[[Agent 主题]]"
  - "[[Context RAG Memory 对比]]"
  - "[[Trajectory Trace 类型对比]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
---

# Agent Memory 类型对比

## 一句话总览

这页回答：Agent 里常见的 memory、state、长期记忆、语义记忆、情景记忆、reflection，以及 RAG 论文里的 parametric / non-parametric memory 到底是不是一回事。

最小边界：[[Agent State]] 让当前任务继续运行；[[Memory]] 让跨时间信息被保存、检索和治理；[[Long-term Memory]] 是跨会话能力层；[[Semantic Memory]] 保存稳定事实/偏好；[[Episodic Memory]] 保存经历和轨迹；[[Memory Reflection]] 从历史中提炼候选长期记忆；[[Parametric Memory]] 在模型权重里；[[Non-Parametric Memory]] 在模型外部可检索存储里。

## 为什么这组值得对比

- 混淆风险：memory 常被泛化成“聊天历史”“上下文窗口”“RAG 文档库”或“模型已经知道的知识”。
- 共同问题域：它们都在处理信息如何跨时间、跨调用或跨任务影响 Agent 行为。
- 不同介入点：有的在当前 run 内保存进度，有的跨会话保存可复用信息，有的是内容分类，有的是写入/提炼流程，有的是模型内部知识来源。
- 证据密度：相关概念卡已有 LangGraph / Letta / Zep / Mem0 memory source note，以及 RAG 论文中的 parametric / non-parametric memory 证据锚点。
- 复习价值：分清这些边界后，才能判断一个系统缺的是 checkpoint、用户偏好记忆、外部文档检索、失败经验回流，还是上下文组织。

边界：这页是学习用的 ontology 对比，不替代具体框架 memory API。具体产品的字段、自动写入策略、删除机制和隐私控制仍需回到对应官方文档复查。

## 共同问题域

共同问题是：Agent 不能只靠一次模型调用里的 prompt 维持所有信息。一个长期任务可能需要记住当前步骤、工具返回、用户偏好、项目事实、失败经验、外部知识库和模型训练中已经内化的常识。

可以把信息生命周期粗略拆成：

```text
current run state -> episode / trace -> reflection -> long-term memory -> selected context
model parameters  -> parametric knowledge
external stores   -> non-parametric knowledge / RAG / memory store
```

这条线说明：memory 不是一个单点数据库，而是一组围绕“写入、保存、检索、更新、过期、权限和证据边界”的工程能力。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Memory]] | 跨时间信息能力总称 | 写入、存储、检索、更新、治理贯穿多轮任务 | 用户偏好、项目事实、历史经验、外部知识 | 可被未来任务选择性使用的信息 | [[Memory#证据锚点]] |
| [[Agent State]] | 当前 run 的工作状态 | 每步执行前后读写 | 目标、阶段、工具结果、错误、审批状态 | 下一步执行依据、可恢复状态 | [[Agent State#证据锚点]] |
| [[Long-term Memory]] | 跨会话保存和复用 | 当前任务结束后仍保留，未来任务检索 | 稳定偏好、事实、经验、项目状态 | 可审计、可更新的长期 store | [[Long-term Memory#证据锚点]] |
| [[Episodic Memory]] | 经历 / 轨迹记录 | 事件发生后保存 | 任务输入、步骤、工具调用、失败原因、反馈 | “那一次发生了什么”的 episode | [[Episodic Memory#证据锚点]] |
| [[Semantic Memory]] | 稳定事实 / 概念 / 偏好 | 从确认事实或 reflection 中写入 | 用户偏好、项目属性、实体关系、长期约束 | 可跨场景复用的背景知识 | [[Semantic Memory#证据锚点]] |
| [[Memory Reflection]] | 记忆维护和提炼流程 | episode / trace 之后，写入长期记忆之前 | 历史对话、episode、trace、评价反馈 | 候选 semantic memory、合并/冲突/不写入决定 | [[Memory Reflection#证据锚点]] |
| [[Parametric Memory]] | 模型权重中的知识 | 训练后隐含存在，生成时被调用 | 训练数据压缩进参数 | 不可直接引用或编辑的内部知识 | [[Parametric Memory#证据锚点]] |
| [[Non-Parametric Memory]] | 模型外部可检索知识 | 查询时由 retriever 取回 | 文档索引、向量库、知识库、数据库 | passages / chunks / records 进入上下文 | [[Non-Parametric Memory#证据锚点]] |

## 最容易混淆的边界

### Memory vs Agent State

[[Agent State]] 回答“当前任务走到哪一步、下一步依据是什么”。它可以保存工具结果、错误、审批状态和临时草稿，但这些内容不一定值得未来复用。

[[Memory]] 回答“哪些信息在未来仍可能有价值，以及如何被保存、检索、更新和治理”。一次任务结束后，state 可能被丢弃、归档为 [[Trace]]，或抽取一小部分进入长期 memory。

### Long-term Memory vs Semantic / Episodic Memory

[[Long-term Memory]] 是能力层：跨会话保存、检索和治理。[[Semantic Memory]] 和 [[Episodic Memory]] 是长期记忆中的内容角色：前者偏稳定事实、偏好、概念和关系；后者偏事件、轨迹和经验样例。

一个失败任务可以先作为 episodic memory 保存；如果多次出现同类失败，[[Memory Reflection]] 才可能把它提炼为 semantic memory，例如“这个工具在某种网络环境下不稳定”。

### Memory Reflection vs Reflexion

[[Memory Reflection]] 是记忆库维护流程：从历史中筛选、压缩、合并、冲突处理并决定是否写入长期记忆。[[Reflexion]] 更偏任务失败后，用评价反馈生成语言反思来改善下一次尝试。

两者可以连接，但不应混同：Reflexion 的 reflective text 可能成为 episode 或经验输入；Memory Reflection 决定它是否应该变成长期记忆。

### Parametric / Non-Parametric Memory vs Agent Memory

[[Parametric Memory]] / [[Non-Parametric Memory]] 来自 RAG 论文语境，核心边界是“知识在模型参数里，还是在模型外部可检索存储里”。

Agent 工程里的 [[Memory]] 范围更宽：还包括用户偏好、项目状态、历史 episode、写入策略、删除、权限和审计。不要把 non-parametric memory 简化成“Agent 的全部记忆”，也不要把 parametric memory 当成用户可治理记忆。

## 执行时序 / 机制差异

```text
During current run:
  goal/tool outputs/errors -> Agent State -> next action/context

After or across runs:
  trace/episode/user fact -> Memory Reflection -> Semantic or Long-term Memory -> future retrieval

RAG knowledge path:
  external documents/index -> Non-Parametric Memory -> Retriever -> Context -> Generator

Model knowledge path:
  training -> Parametric Memory -> generation prior
```

一个现代 Agent 可能同时使用四条路径：state 维持当前任务，long-term memory 记住用户和项目，RAG 检索外部资料，parametric memory 提供语言和常识先验。可靠性来自把这些路径拆开治理，而不是把所有东西都叫 memory。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把 Agent 想成一个长期合作的研究助理：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Agent State]] | 今天桌上的任务清单、临时草稿、刚查到的结果 | 任务结束后未必保留 |
| [[Episodic Memory]] | 工作日志：某天做了什么、哪里失败 | 记录经历，不自动变成稳定事实 |
| [[Semantic Memory]] | 助理手册：用户偏好、项目事实、术语表 | 需要确认、更新和冲突处理 |
| [[Memory Reflection]] | 每周复盘：从日志里提炼规则 | 总结可能错，应该有写入门槛 |
| [[Long-term Memory]] | 可长期维护的档案柜 | 不是所有聊天历史都应该进去 |
| [[Non-Parametric Memory]] | 外部资料库和图书馆 | 可检索资料不等于用户记忆 |
| [[Parametric Memory]] | 助理已经学过的常识和语言能力 | 不能直接追溯或删除某条事实 |

## 现代系统如何吸收或限制

### 来源支持

- [[Memory]]、[[Long-term Memory]]、[[Semantic Memory]]、[[Episodic Memory]] 和 [[Memory Reflection]] 的概念卡共同支持：现代 Agent memory 需要 store、scope、检索、写入策略、冲突处理、删除和证据边界。
- [[Agent State]] 支持：当前任务状态应和跨任务 memory 分开，只有必要片段进入上下文。
- [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]] 相关卡支持：parametric / non-parametric memory 是 RAG 论文中的知识来源边界。

### 工程综合 / inference

现代系统通常把 memory 拆成至少四层：runtime state、episodic trace/history、semantic/long-term store、external retrieval store。写入长期记忆时要有触发条件、来源、作用域、过期/删除和用户确认策略；检索记忆时要通过 context engineering 决定哪些片段真的进入模型上下文。

### 仍需警惕的外推

不同框架会把 thread、checkpoint、store、session、profile、facts、episodes 等词用得不同。本页只沉淀学习边界，不把某一产品的字段名上升为通用定义。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 长任务中断后继续执行 | [[Agent State]] / checkpoint | 需要恢复当前 run 的控制状态和中间结果 | 不要把临时错误日志永久写入 memory |
| 系统要记住用户偏好或项目事实 | [[Long-term Memory]] + [[Semantic Memory]] | 信息未来可复用，且应带来源和作用域 | 一次性偏好被永久化会污染后续任务 |
| 想复盘某次失败尝试 | [[Episodic Memory]] / [[Trace]] | 需要保存当时发生过的路径 | episode 太多会淹没真正可复用经验 |
| 想从多次失败中提炼规则 | [[Memory Reflection]] | 需要把经历压缩成候选长期记忆 | evaluator 或总结错误会固化坏经验 |
| 想回答外部文档事实问题 | [[Non-Parametric Memory]] / [[RAG]] | 外部资料可更新、可引用、可权限治理 | 检索失败或资料过期仍会误导回答 |
| 模型凭常识即可回答 | [[Parametric Memory]] | 参数知识提供语言和常识先验 | 无来源、难更新，不适合作为唯一事实依据 |

## 它们共同不是什么

- 都不是“把所有历史塞进上下文窗口”。上下文只是本次调用可见内容，memory 还包括写入、治理和检索。
- 都不是事实正确性的保证。记忆可以过期、冲突、权限不清或被错误总结。
- 都不是完整 Agent framework。memory 还要和 tool calling、state、trace、evaluation、guardrails 和 human-in-the-loop 配合。
- 都不是越多越好。没有证据边界的记忆会让 Agent 更稳定地犯错。

## 证据锚点

- Concept anchors: [[Memory#证据锚点]], [[Agent State#证据锚点]], [[Long-term Memory#证据锚点]], [[Episodic Memory#证据锚点]], [[Semantic Memory#证据锚点]], [[Memory Reflection#证据锚点]], [[Parametric Memory#证据锚点]], [[Non-Parametric Memory#证据锚点]]
- Source examples: [[LangGraph Memory 官方文档]], [[Letta Memory 官方文档]], [[Zep Memory 官方文档]], [[Mem0 Memory 官方文档]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Evidence type: concept-card synthesis + official docs source notes + RAG paper source note + engineering synthesis + learning analogy.
- Confidence: medium-high for state / long-term / semantic / episodic / reflection boundaries; medium for product-level memory behavior because API 和自动写入策略变化较快。
- Boundary: parametric / non-parametric memory 的术语边界来自 RAG 论文语境；Agent memory 的治理边界是跨现有概念卡和现代工程实践的综合。

## 复习触发

1. 为什么 [[Agent State]] 不是 [[Memory]] 的同义词？给一个“应该留在 state、不该进长期记忆”的例子。
2. [[Semantic Memory]] 和 [[Episodic Memory]] 最小区别是什么？一次失败经历怎样可能转成语义记忆？
3. [[Memory Reflection]] 为什么不是“模型随便总结一下”？它至少需要哪些输入和写入门槛？
4. [[Non-Parametric Memory]] 和 [[RAG]] 是什么关系？为什么它不是 Agent 的全部记忆？
5. 为什么不能把 [[Parametric Memory]] 当成可审计的用户记忆？

## 相关链接

- [[Memory]]
- [[Agent State]]
- [[Long-term Memory]]
- [[Episodic Memory]]
- [[Semantic Memory]]
- [[Memory Reflection]]
- [[Parametric Memory]]
- [[Non-Parametric Memory]]
- [[RAG]]
- [[Context Engineering]]
- [[Trace]]
- [[Evaluation]]
- [[LLM Wiki 工作流]]
