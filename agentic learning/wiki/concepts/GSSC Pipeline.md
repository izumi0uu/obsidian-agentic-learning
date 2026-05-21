---
type: concept
topic:
  - agent
  - context
  - llm
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
aliases:
  - GSSC
  - Gather-Select-Structure-Compress
  - Gather Select Structure Compress
  - 上下文构建四阶段流水线
  - 收集-选择-结构化-压缩
  - 获取-选择-结构化-压缩
source:
  - "[[Hello-Agents Repo]]"
  - "[[122 01_AI 04_上下文工程与记忆 LLM 调优（训练调优 + Prompt 调优）怎么分层做？]]"
  - "[[Context Engineering]]"
evidence:
  - "[[Hello-Agents Repo#第九章上下文工程 / GSSC]]"
  - "[[122 01_AI 04_上下文工程与记忆 LLM 调优（训练调优 + Prompt 调优）怎么分层做？#题目正文]]"
  - "[[Context Engineering#概念详解]]"
related:
  - "[[Context Engineering]]"
  - "[[Context Window]]"
  - "[[Progressive Disclosure]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Context Projection]]"
  - "[[Prompt Engineering]]"
relations:
  - type: pattern_for
    target: "[[Context Engineering]]"
    note: 把上下文构建拆成 gather、select、structure、compress 四个工程阶段。
  - type: composes_with
    target: "[[Progressive Disclosure]]"
    note: 两者都服务按需控制上下文；GSSC 是构建流水线，Progressive Disclosure 是信息暴露策略。
---

# GSSC Pipeline

## 一句话

GSSC Pipeline 是一种上下文构建流水线：先 Gather 多源候选信息，再 Select 高价值信息，接着 Structure 成模型易用的上下文，最后在超预算时 Compress。

## 概念详解

GSSC 解决的是 [[Context Engineering]] 里最容易被说虚的问题：上下文不是“想到什么塞什么”，而应该有可复用的构建流程。Hello-Agents 第九章把 `ContextBuilder` 的核心写成 GSSC，也就是 Gather-Select-Structure-Compress，将上下文构建拆成四个阶段，让 Agent 每轮看到的信息更可控、更可调试。

第一步 **Gather** 是收集候选信息。候选可以来自系统指令、用户当前问题、对话历史、[[Memory]]、[[RAG]] 检索片段、工具结果、[[Agent State]]、自定义 context packet 或外部文件引用。Gather 的关键不是贪多，而是容错和覆盖面：先让可能有用的信息进入候选池，同时保留来源、类型、时间和 token 估算，方便后面筛选。

第二步 **Select** 是选择最值得进入窗口的信息。它通常要考虑相关性、时效、优先级、来源可信度、权限、token budget 和当前任务阶段。Select 是整条流水线的质量中枢：如果这里把无关内容选进来，后面的结构化和压缩只是在整理噪声；如果这里漏掉关键证据，模型即使格式很好也会答错。

第三步 **Structure** 是把选中的信息组织成清晰结构。常见结构包括 system instructions、task brief、selected memory、retrieved evidence、tool results、current state、constraints、output format。Structure 的价值是降低模型和人类调试的认知负担：出错时可以定位是证据区错了、状态区过期了，还是工具结果区不完整。

第四步 **Compress** 是超预算时的兜底压缩。它可以是截断、摘要、section-level compression、保留最近片段，或把深历史压成状态摘要。关键边界是：Compress 应该在 Gather/Select/Structure 之后才做，不能把它当成主策略。如果前面三个阶段已经把噪声放进来，压缩只会得到“更短的噪声”。

## 它解决什么问题

- 把上下文构建从临时 prompt 拼接变成可复用 pipeline。
- 明确哪个环节负责召回候选、哪个环节负责过滤、哪个环节负责组织、哪个环节负责预算兜底。
- 让上下文问题更容易 debug：是没收集到、选错了、结构乱了，还是压缩过度。
- 帮助面试或工程表达从“做上下文工程”落到具体执行步骤。

## 它不是什么

GSSC Pipeline 不是 [[Context Engineering]] 的同义词。Context Engineering 是更大的运行时信息治理问题；GSSC 是其中一种上下文构建流水线。

它也不是 [[RAG]] pipeline。RAG 通常聚焦外部知识检索与生成；GSSC 的候选信息更宽，包括系统指令、历史、memory、tool results、state 和 RAG evidence。

它也不是 [[Progressive Disclosure]]。Progressive Disclosure 关注信息何时逐层暴露；GSSC 关注一次上下文如何从候选池变成最终 prompt。两者可以组合：Gather 阶段收轻量引用，Select 后再按需展开细节。

它也不是“压缩算法”。Compress 只是第四步，而且是兜底。真正提升质量的通常是 Select 和 Structure。

## 最小例子

```text
Gather:
  system rules, user task, recent conversation, memory, retrieved docs, tool results

Select:
  keep task-critical rules, top evidence, fresh state, high-confidence memories

Structure:
  ## Task
  ## Constraints
  ## Evidence
  ## Current State
  ## Output Contract

Compress:
  if over budget, compress old tool results and low-priority evidence first
```

## 常见误解 / 风险

- 误解：Gather 越多越好。候选池太脏会加重 Select 负担，也会增加误选风险。
- 误解：Select 只看语义相似度。生产上下文还要看权限、时效、来源可信度、任务阶段和预算。
- 误解：Structure 只是格式化。结构会影响模型把什么当作规则、证据、状态或输出约束。
- 误解：Compress 可以补救前面所有问题。压缩无法恢复没选进来的关键事实，也无法把错误证据压成正确证据。
- 风险：如果 Select 阶段没有记录为什么选中/丢弃信息，后续很难复盘模型为什么错。

## 边界细节

和 [[Context Engineering]] 的边界：GSSC 是 Context Engineering 的一个实现框架，不覆盖权限治理、trace、evaluation、长期 memory 写入、工具执行策略等全部问题。

和 [[Prompt Engineering]] 的边界：Prompt Engineering 关注指令文本和输出约束；GSSC 关注这些指令与证据、历史、memory、工具结果如何一起组成本轮上下文。

和 [[Context Window]] 的边界：Context Window 是容量；GSSC 是容量内的信息选择和组织方法。窗口变大后仍然需要 GSSC，因为噪声、冲突和权限不会自动消失。

## 层级归属

本卡暂不直接写 `up`。它更像 [[Context Engineering]] 的实践模式 / pipeline，而不是严格下位概念；当前用 `relations: pattern_for` 表达关系，等待下一轮 taxonomy 生成、判定、dry-run 后再决定是否需要更稳定的父类。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：现代 Agent 和 RAG 应用需要显式管理上下文收集、选择、结构化和压缩。
- 易变部分：GSSC 这个缩写主要来自 Hello-Agents 教学与框架实现语境，不是行业统一标准；不同框架可能使用 retrieval、filtering、reranking、packing、compression 等不同命名。
- 复查点：如果后续 OpenAI / Anthropic / LangChain / LlamaIndex 等官方文档形成更稳定的上下文构建术语，应更新本卡的现代性和命名边界。

## 现代系统怎么吸收 GSSC 的价值

现代系统通常不会把 GSSC 四个词硬编码成唯一 API，而是把它吸收到 context builder、retriever pipeline、memory selector、prompt packer、[[Context Projection|state projector]] 或 compaction hook 里。判断一个系统是否具备类似 GSSC 的能力，不看它是否用了这个缩写，而看它是否能回答：

- 候选上下文从哪些来源来？
- 为什么这些信息被选中，哪些被丢弃？
- 最终上下文的结构是否可读、可调试、可审计？
- 超过预算时先压缩什么，哪些信息绝不能丢？

## 证据锚点

- Source: [[Hello-Agents Repo]]
- Anchor: [[Hello-Agents Repo#第九章上下文工程 / GSSC]]
- Source: [[122 01_AI 04_上下文工程与记忆 LLM 调优（训练调优 + Prompt 调优）怎么分层做？]]
- Anchor: [[122 01_AI 04_上下文工程与记忆 LLM 调优（训练调优 + Prompt 调优）怎么分层做？#题目正文]]
- Evidence type: repo tutorial source note + interview raw source + engineering synthesis.
- Confidence: medium
- Boundary: Hello-Agents 明确使用 GSSC 作为 ContextBuilder 流水线；agent_java_offer q122 把 Gather-Select-Structure-Compress 作为上下文工程组织方法。本卡不把 GSSC 写成行业标准，也不把它等同为全部 Context Engineering。

## 复习触发

- 如果一个 Agent 答错，是 Gather 没召回、Select 选错、Structure 混乱，还是 Compress 丢失了关键信息？
- 为什么 Compress 应该是兜底，而不是上下文工程的主要策略？
- GSSC 和 RAG pipeline 的边界是什么？

## 相关链接

- [[Context Engineering]]
- [[Context Window]]
- [[Progressive Disclosure]]
- [[RAG]]
- [[Memory]]
- [[Agent State]]
- [[Context Projection]]
- [[Prompt Engineering]]
