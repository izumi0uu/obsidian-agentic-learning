---
type: concept
topic:
  - agent
  - context
  - memory
  - workflow
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
aliases:
  - 上下文投影
  - context projection
source:
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Long-Horizon Context Engineering]]"
  - "[[GSSC Pipeline]]"
  - "[[Memory]]"
  - "[[Trace]]"
evidence:
  - "[[Agent State#概念详解]]"
  - "[[Agent State#现代系统怎么吸收 Agent State 的价值 / 局限]]"
  - "[[Context Engineering#概念详解]]"
  - "[[Long-Horizon Context Engineering#边界细节]]"
  - "[[GSSC Pipeline#现代系统怎么吸收 GSSC 的价值]]"
related:
  - "[[Context Engineering]]"
  - "[[Agent State]]"
  - "[[Memory]]"
  - "[[Trace]]"
  - "[[Context Window]]"
  - "[[Long-Horizon Context Engineering]]"
  - "[[GSSC Pipeline]]"
relations:
  - type: mechanism_for
    target: "[[Context Engineering]]"
    note: 把系统持有的信息投影成模型本轮可见、可用、可预算的上下文。
  - type: projects_from
    target: "[[Agent State]]"
    note: 从当前 run 的状态中选择、压缩、排序本轮决策需要的片段。
  - type: draws_from
    target: "[[Memory]]"
    note: 记忆只有被选中并投影进上下文时才影响本轮回答。
  - type: draws_from
    target: "[[Trace]]"
    note: trace 可作为失败复盘、长任务继续或审计解释时的候选材料。
---

# Context Projection

## 一句话

Context Projection 是把 [[Agent State]]、[[Memory]]、[[Trace]]、结构化 notes、工具结果和文件引用等系统持有的信息，选择、压缩、排序成模型本轮可见上下文的机制。

## 概念详解

Context Projection 解决的是一个很细但很关键的问题：系统“拥有”信息，不等于模型本轮“看见”信息。现代 Agent 往往有 state schema、checkpoint、memory store、trace、文件系统、检索结果和人工审批记录；这些材料如果全部塞进 prompt，会挤爆 [[Context Window]]，也会把旧错误、低价值日志和无关细节带进当前决策。Projection 的工作就是把这些外部或内部状态投影成当前模型调用真正需要的一小片上下文。

它通常包含四个动作。第一是选择来源：当前 step 需要 state、memory、trace summary、RAG evidence、tool result 还是结构化 note。第二是过滤和排序：保留与当前目标、约束、失败恢复和证据判断最相关的片段。第三是压缩：把长 trace、历史工具输出或旧阶段结论压成带来源的摘要。第四是打包：把材料放进 prompt 的合适区域，例如 task brief、current state、selected memory、evidence、constraints 或 output contract。

和 [[Context Engineering]] 的关系是：Context Engineering 是更大的上下文治理问题；Context Projection 是其中靠近 runtime 的投影步骤。它回答“系统已经保存了很多东西，本轮到底投影哪些给模型”。和 [[Agent State]] 的关系是：state 保存运行事实，projection 决定哪些 state 字段进入下一次模型调用。和 [[Memory]] 的关系是：memory 是候选材料，只有被投影进上下文才会影响本轮输出。和 [[Trace]] 的关系是：trace 是完整发生记录，projection 常把它压成当前需要的失败摘要、证据链或恢复依据。

证据边界：这张卡是工程综合卡。现有 source notes 和概念卡支持现代 Agent framework 把 state、trace、memory、context builder 显式化；`Context Projection` 这个命名在本 vault 中用于切开“持有信息”和“本轮可见输入”的边界，不声称它已经是所有框架的统一标准 API 名。

## 它解决什么问题

- 防止 state、memory、trace 变成另一个大上下文垃圾桶。
- 让模型每轮只看到和当前决策有关的事实、证据、约束和下一步依据。
- 让长任务在 compaction、恢复、子代理汇总后仍能保留关键上下文。
- 让上下文错误更容易 debug：是候选信息没保存，还是保存了但没有投影进本轮输入。

## 它不是什么

Context Projection 不是 [[Agent State]] 本身。State 是系统持有的运行事实；projection 是把其中一部分变成模型输入。

它也不是 [[Context Window]]。Context Window 是容量边界；projection 是在这个边界里选择和组织材料。

它也不是 [[Memory]] 或 [[Trace]]。Memory 和 trace 是候选来源；projection 是使用它们的当前步骤。

它也不是泛泛的 context assembly。Context assembly 可以指 RAG 证据拼装、prompt packing 或完整上下文构建；Context Projection 更强调“从系统持有的状态/记忆/轨迹投影到本轮模型可见切片”。`state projection` 是它的窄用法：只从 state 投影；不是本卡的稳定 alias。

## 最小例子

```text
Current task:
  "继续修复失败测试"

System holds:
  state: current phase, changed files, failing test name, next step
  memory: repo conventions, user's preferences
  trace: last 30 tool calls and errors
  notes: known blockers and decisions

Context projection:
  include current phase + failing test + changed files
  include one repo convention relevant to tests
  summarize only the last failure from trace
  omit old search logs and unrelated notes
```

这里的关键不是把所有资料都放进上下文，而是把“继续当前决策需要什么”投影出来。

## 常见误解 / 风险

- 误解：系统保存得越多，模型就越聪明。保存只是候选池；投影错了，模型仍然看不到关键事实。
- 误解：直接把完整 state 塞回 prompt 最稳。完整 state 往往包含过期、敏感、重复或低价值信息，会污染决策。
- 误解：projection 只是摘要。摘要只是压缩手段之一；更重要的是选择、排序、来源标注和预算分配。
- 风险：投影只保留结论不保留证据，后续模型会继承错误判断。
- 风险：投影规则不可见时，失败复盘很难判断是 memory 不存在、retrieval 失败，还是投影阶段丢了关键字段。

## 边界细节

可以把相邻概念切成一条链：

```text
state / memory / trace / notes
  -> candidate context
  -> context projection
  -> prompt / model-visible context
  -> model output
```

[[GSSC Pipeline]] 可以看作更通用的上下文构建流程：Gather 收集候选，Select 选择，Structure 组织，Compress 压缩。Context Projection 更像这条流程在 Agent runtime 里的具体视角：候选材料来自 state、memory、trace、notes 和工具结果，目标是生成当前模型调用的可见切片。

在长任务里，projection 的质量往往比窗口大小更关键。窗口很大但投影混乱，模型会被噪声淹没；窗口较小但投影准确，模型仍能稳定推进当前阶段。

## 层级归属

本卡暂不直接写 `up`。它和 [[Context Engineering]] 是机制/实践关系，和 [[Agent State]]、[[Memory]]、[[Trace]] 是来源关系；当前用 `relations` 表达，等待 taxonomy 候选生成、判定和 dry-run 后再决定是否需要稳定父类。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：现代 Agent 需要把持久状态、记忆、轨迹和工具结果选择性放入当前模型上下文。
- 易变部分：不同 harness 可能叫 context builder、prompt packer、memory selector、state projector、compaction hook 或 context manager；命名和 API 尚未统一。
- 复查点：当主流 Agent framework 对 state/memory/trace 到 model context 的投影步骤形成稳定 API 或术语时，更新本卡边界。

## 现代系统怎么吸收 Context Projection 的价值

现代系统通常不会把 projection 做成一个孤立按钮，而是藏在 runtime 和 context builder 里：读 state、取 memory、压 trace、筛 tool result、控制 token budget，然后把结果打包成 prompt 区块。可靠系统还会记录为什么某些信息被放入或丢弃，方便调试“模型为什么不知道这件事”。

它的局限是：projection 不能创造不存在的信息，也不能保证被选中的信息一定正确。它依赖好的 state schema、memory 写入策略、trace 质量、权限过滤和评估闭环。

## 证据锚点

- Concept anchor: [[Agent State#概念详解]]
- Concept anchor: [[Agent State#现代系统怎么吸收 Agent State 的价值 / 局限]]
- Concept anchor: [[Context Engineering#概念详解]]
- Concept anchor: [[Long-Horizon Context Engineering#边界细节]]
- Concept anchor: [[GSSC Pipeline#现代系统怎么吸收 GSSC 的价值]]
- Evidence type: vault concept synthesis + engineering inference.
- Confidence: medium.
- Boundary: 证据支持“state / memory / trace / context builder 需要分层治理”；本卡把其中“系统持有信息到本轮可见上下文”的步骤命名为 Context Projection。

## 复习触发

1. 为什么 Agent State 不等于模型当前看见的 context？
2. 如果模型忘记了一个工具返回，你怎么判断是 state 没保存、trace 没记录，还是 projection 没放进去？
3. Context Projection 和 RAG context assembly 的边界是什么？
4. 为什么 `state projection` 是 Context Projection 的窄用法，而不是完全同义词？

## 相关链接

- [[Context Engineering]]
- [[Agent State]]
- [[Memory]]
- [[Trace]]
- [[Context Window]]
- [[Long-Horizon Context Engineering]]
- [[GSSC Pipeline]]
