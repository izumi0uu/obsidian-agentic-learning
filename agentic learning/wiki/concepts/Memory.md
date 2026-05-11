---
type: concept
topic:
  - agent
  - memory
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
related:
  - "[[Agent]]"
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
---

# Memory

## 一句话

Memory 是 Agent 在当前任务和未来任务中保存、检索、更新并使用信息的机制；它让系统不只依赖一次 prompt 的上下文窗口。

## 概念详解

Agent 的 memory 不是“把所有聊天记录塞回 prompt”。它是一组围绕信息生命周期的工程能力：什么信息值得写入、写到哪里、下次如何检索、是否需要合并或覆盖旧信息、是否要过期、删除、审计，以及最终怎样进入当前 agent state 或模型上下文。

在 runtime 里，memory 通常被拆成几层：短期上下文负责当前回合可见内容，任务 state 负责当前 workflow 的步骤和中间结果，长期存储负责跨会话的信息，检索层负责把候选记忆找回来，策略层决定哪些记忆能影响当前回答。这样拆开后，Memory 才能和 [[Agent State]]、[[RAG]]、[[Long-term Memory]]、[[Semantic Memory]]、[[Episodic Memory]] 分清边界。

论文和 RAG 语境里常说的 parametric / non-parametric memory，强调的是“知识在模型参数里，还是在外部可检索存储里”。Agent 工程里的 memory 范围更宽：它还包括用户偏好、项目事实、任务轨迹、失败经验、权限和删除机制。因此同一个词 memory 在不同来源里不完全同义；读卡时要先问它在讲模型知识、外部知识库，还是跨会话 agent state。

现代框架和 memory service 的共同趋势，是把记忆从隐式聊天历史变成显式对象：有 scope（用户、线程、项目）、有写入触发、有检索策略、有来源和更新时间。这样做不是为了让 Agent “什么都记住”，而是为了让它在长期任务中能选择性地带回最相关、可解释、可撤销的信息。

对学习来说，关键不是背“Agent 有记忆”，而是判断：这条信息是当前任务临时状态、用户长期偏好、项目知识、过去失败经验，还是外部知识库资料？不同答案会对应不同写入位置、权限边界和验证方式。

还有一个容易忽略的边界：memory 的“召回”本身也是一种工具行为。检索哪些记忆、按什么权重排序、是否展示给用户、是否允许模型覆盖，都可能影响最终行动。因此 memory 不只是数据层，也和 [[Tool Permissioning]]、[[Observability]]、[[Evaluation]] 形成闭环：记忆被用错时，系统要能追溯是哪条记忆影响了决策。
## 它解决什么问题

没有记忆的 Agent 很难完成长期任务，也很难记住用户偏好、历史决策、项目状态和过去失败。它每次都像从零开始，容易重复问问题、重复试错，或在跨会话任务中丢失约束。

Memory 解决的是“信息怎样在时间上延续”的问题：当前上下文装不下、下次会话还要用、未来需要解释来源、旧信息可能要撤销，这些都不能只靠一次模型调用解决。

## 常见类型

- 短期记忆：当前上下文窗口里的信息，通常随会话和上下文裁剪变化。
- 长期记忆：保存到数据库、文件、向量库或知识图谱里的信息，支持跨会话调用。
- 任务记忆 / state：当前任务的步骤、状态、结果和待办，更接近 runtime checkpoint。
- 用户记忆：用户偏好、习惯、约束和长期目标，需要权限、可见性和删除机制。
- [[Semantic Memory]]：事实、偏好、概念和关系。
- [[Episodic Memory]]：过去事件、任务轨迹、失败经验和可回放片段。

## 它不是什么

Memory 不是上下文窗口。上下文窗口只是模型当下能看到的输入空间；memory 还包括写入、存储、检索、冲突解决、过期和权限。

Memory 也不等于 [[RAG]]。RAG 更偏向从外部知识库检索资料来回答问题；Memory 还包括用户偏好、任务过程、系统状态和过去交互经验。一个系统可以有 RAG 但没有用户长期记忆，也可以有用户偏好记忆但不做文档检索。

Memory 也不是“越多越好”。未验证、过期或权限不清的记忆会让 Agent 更自信地犯错。

## 最小例子

如果我多次告诉学习 Agent：“我完全零基础，请先解释边界再讲实现”，系统可以把这条偏好写成用户记忆。之后我问 [[MCP]] 或 [[Tool Calling]] 时，它会先解释“这不是什么”，再讲机制和例子。

这个例子里，偏好本身是 semantic/user memory；本轮回答里的步骤和草稿是短期上下文或 task state；如果系统记录“上次解释太抽象，用户没懂”，那更像 episodic memory。

## 风险

- 记住错误信息，并在未来反复放大。
- 记住过时偏好，没有过期或覆盖机制。
- 该忘的不忘，侵犯隐私或违反最小权限。
- 检索到的记忆和当前任务不相关，却被模型当成强约束。
- 把 runtime state、外部知识和用户偏好混在一个池子里，导致来源和权限不可解释。

## 边界细节

Memory 的边界要从“信息角色”而不是“存储位置”判断。同样存在数据库里的内容，可能是长期用户偏好，也可能是任务 checkpoint、文档索引或审计日志。

和 [[Agent State]] 的边界：state 更偏“当前 workflow 走到哪一步、工具结果是什么、下一步依据是什么”；memory 更偏“未来仍可能复用的信息”。长期任务会同时用到两者：state 让任务恢复，memory 让系统记住跨任务经验。

和 [[Evaluation]] 的边界：评测可以检查记忆是否有用、是否污染任务，但评测结果本身不自动成为 memory；只有被明确写入并带来源边界的经验，才应该进入记忆层。

## 现代性状态

Memory 是基础地基 + 当前工程实践。

- 基础地基：认知意义上的短期、长期、语义、情景记忆帮助我们描述 Agent 为什么需要跨时间信息。
- 当前工程实践：现代 Agent framework 会把 memory 拆成 state、store、retriever、policy、checkpoint、audit 等组件，而不是只靠 prompt 模板。
- 前沿 / 易变部分：具体框架的 memory API、自动写入策略、用户可控删除、隐私字段和多租户权限仍在快速变化；这些实现细节应看具体 source 的 freshness。

## 现代系统怎么吸收 Memory 的价值

现代系统通常不让模型自由“想记什么就记什么”。更常见的做法是：runtime 暴露受控的写入工具或 memory store，策略层决定哪些内容可写入，检索层在需要时把候选记忆注入上下文，observability/audit 层记录记忆从哪里来、何时被使用。

这样做的价值是把“记忆”从模糊的聊天印象变成可检查的工程对象：可以查看来源、撤销错误、限制权限、评估命中率，并把用户偏好和项目事实分开治理。

## 证据锚点

- Evidence type: official docs note — [[LangGraph Memory 官方文档]]。
- Boundary: 当前卡片使用的是 source note 小节级证据，支持 LangGraph 语境下 memory / store / thread 等概念边界；关于 Letta、Zep、Mem0 等产品实现差异不由本卡直接证明。
- Engineering synthesis: “memory 需要写入、检索、更新、过期、权限和审计”是从 agent runtime 设计角度综合出的学习边界，不应当当作某一个官方文档的逐字定义。
- Confidence: medium。

## 复习触发

- 如果上下文窗口已经能保存一段对话，为什么还需要 Memory？
- 如何区分用户偏好、项目知识、任务 state 和外部 RAG 文档？
- 记忆写入错误时，系统需要哪些删除、覆盖或审计能力？

## 相关链接

- [[Agent]]
- [[RAG]]
- [[Evaluation]]
- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]
