---
type: map
topic:
  - rag
  - memory
  - context
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-15
source:
  - "[[Context Engineering]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Repo Context]]"
  - "[[Retriever]]"
  - "[[Chunking]]"
  - "[[Embedding]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[Agent 工程基础设施主源]]"
  - "[[SWE-bench]]"
evidence:
  - "[[Context Engineering#证据锚点]]"
  - "[[RAG#证据锚点]]"
  - "[[Memory#证据锚点]]"
  - "[[Repo Context#证据锚点]]"
  - "[[Retriever#证据锚点]]"
  - "[[Chunking#证据锚点]]"
  - "[[Embedding#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[RAG 类型对比]]"
  - "[[Agent Memory 类型对比]]"
  - "[[Retrieval 组件对比]]"
---

# Context RAG Memory 对比

## 一句话总览

这页回答：Context Engineering、RAG、Memory、Repo Context、Retriever、Chunking、Embedding 这些词为什么总在一起出现，但又不能互相替代。

最小边界：[[Context Engineering]] 决定本轮模型看见什么；[[RAG]] 是从外部知识库检索再生成的架构模式；[[Memory]] 是跨时间保存、检索和治理信息的能力；[[Repo Context]] 是代码 Agent 的任务相关代码库切片；[[Retriever]] 找候选资料；[[Chunking]] 决定资料单元怎么切；[[Embedding]] 提供语义相似检索的向量表示。

## 为什么这组值得对比

- 混淆风险：很多系统把“塞上下文”“做 RAG”“加记忆”“读 repo”都叫成 context，导致排错时不知道问题在信息来源、检索、排序还是上下文组织。
- 共同问题域：它们都围绕“模型这一轮应该看见哪些外部信息”。
- 不同介入点：有的是信息来源，有的是检索链路，有的是上下文编排，有的是跨任务保存。
- 证据密度：相关概念卡已有 RAG 论文、Microsoft RAG 文档、Agent 工程基础设施、SWE-bench 和 memory source notes 的证据锚点。
- 复习价值：能防止把 RAG 类型对比里的高级检索形态重复写成 context 问题；本页只切开信息进入上下文的层次。

边界：这页刻意不重复 [[RAG 类型对比]] 中 GraphRAG、Agentic RAG、Self-RAG 等类型谱系；重点是 context / retrieval / memory / repo context 的职责分层。

## 共同问题域

共同问题是：LLM 的输出强依赖本轮上下文，但上下文窗口有限、来源复杂、可信度不同、权限不同、更新频率不同。系统必须决定：哪些信息从文档库来，哪些从长期记忆来，哪些从当前任务 state 来，哪些从代码库结构来，以及怎样排序、压缩、引用和隔离。

```text
source documents -> ingestion/chunking/embedding -> retriever -> candidate evidence
long-term memory -> memory retriever/policy -------> candidate memory
repo files/tests -> repo context search -----------> candidate code evidence
current run state -------------------------------> task state summary
all candidates -> Context Engineering -> model context
```

这条链路说明：RAG、Memory 和 Repo Context 都可能成为 context 来源；Context Engineering 是最后的组织和约束层，不是某一个来源本身。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Context Engineering]] | 本轮模型输入的选择、排序、预算、来源和规则 | 模型调用前，持续随任务更新 | system 指令、state、memory、retrieved chunks、tool schema、权限 | 可读、可引用、受约束的模型上下文 | [[Context Engineering#证据锚点]] |
| [[RAG]] | 外部知识检索增强生成 | `query -> retrieve -> generate`，可加 rerank/eval | 用户问题、外部文档索引 | 带检索证据的回答上下文 | [[RAG#证据锚点]] |
| [[Memory]] | 跨时间保存、检索和治理信息 | 写入 / 检索跨多轮或跨会话 | 用户偏好、项目事实、经历、长期经验 | 可被未来任务选用的记忆片段 | [[Memory#证据锚点]] |
| [[Repo Context]] | 代码 Agent 的任务相关代码库切片 | 任务调查、编辑、验证中动态更新 | 文件、符号、调用关系、测试、配置、错误日志 | 代码修改所需的最小相关上下文 | [[Repo Context#证据锚点]] |
| [[Retriever]] | 从外部索引找候选资料 | 生成前或 agentic retrieval loop 中 | query、索引、过滤条件、权限 | top-k passages / chunks / records | [[Retriever#证据锚点]] |
| [[Chunking]] | 把资料切成检索和引用单元 | ingestion 阶段，影响后续 retrieval | PDF、网页、代码、表格、文档结构 | 带 metadata 的 chunks | [[Chunking#证据锚点]] |
| [[Embedding]] | 把内容转成语义向量 | 入库时和查询时 | chunk、query、图片或对象 | 向量表示，用于相似度检索 | [[Embedding#证据锚点]] |

## 最容易混淆的边界

### Context Engineering vs RAG

[[RAG]] 是一种外部知识进入生成的架构模式，重点是 retriever-generator 组合和外部索引。[[Context Engineering]] 更宽：它决定 RAG 检索结果、memory、state、tool schema、指令、引用规则和权限约束怎样进入本轮模型调用。

一个系统可以没有 RAG 但仍然需要 Context Engineering，例如只组织当前任务 state 和工具结果；也可以有 RAG 但 context 组织很差，导致检索到了正确资料却被埋在错误顺序、缺少引用或权限混乱的上下文里。

### RAG vs Memory

[[RAG]] 常从外部文档库检索资料来回答问题。[[Memory]] 更偏跨时间保存和治理信息，包含用户偏好、项目状态、经验总结、事件记忆、权限和删除机制。

两者会重叠：长期记忆可能用向量检索，外部文档库也可以被称为 non-parametric memory。但学习时要先问：这是“查资料来回答问题”，还是“保存未来要复用的历史/偏好/经验”？

### Repo Context vs 普通文档 RAG

[[Repo Context]] 是代码 Agent 的特殊上下文问题。它不只找语义相似文本，还要读文件布局、符号定义、调用关系、测试、配置、AGENTS 约束和错误日志。

普通文档 RAG 的 chunk 可能是一段说明文字；repo context 的切片可能是“报错堆栈 + 被测函数 + fixture + 配置 + 相关约定”。它有更强的结构和可验证反馈。

### Retriever / Chunking / Embedding vs Context Engineering

[[Retriever]]、[[Chunking]] 和 [[Embedding]] 是 RAG / retrieval 链路的组件。它们决定候选资料是否找得到、找得准、可引用。[[Context Engineering]] 在更后面：决定找到的资料是否进入上下文、放在哪里、是否压缩、是否带来源、是否和 memory/state 冲突。

## 执行时序 / 机制差异

```text
Ingestion path:
  raw document -> parse/clean -> Chunking -> Embedding -> index

Query path:
  user query -> Retriever -> candidate chunks -> rerank/filter -> Context Engineering -> model

Memory path:
  event/fact/preference -> memory write policy -> memory store -> memory retrieval -> Context Engineering

Repo path:
  task/logs -> file/symbol/test search -> Repo Context slice -> Context Engineering -> coding action
```

排错时要沿着路径问：资料是否被正确摄入？chunk 是否保留边界？embedding / retriever 是否找回正确候选？context 是否把候选组织清楚？memory 是否过期或越权？repo context 是否漏了测试或调用者？

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把模型调用想成一次开卷考试：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[RAG]] | 去资料库查到几页参考资料再作答 | 查到资料不等于用对资料 |
| [[Retriever]] | 图书管理员帮你找候选书页 | 管理员可能漏找或找错 |
| [[Chunking]] | 书页被切成可引用的段落卡片 | 切得太碎会丢上下文 |
| [[Embedding]] | 按语义相近给卡片编号 | 相似不等于正确 |
| [[Memory]] | 你之前确认过的偏好和项目规则 | 需要来源和更新机制 |
| [[Repo Context]] | 做代码题时必须看的相关文件和测试 | 代码有结构和运行反馈，不只是文本 |
| [[Context Engineering]] | 考前把资料、规则、草稿按优先级摆在桌上 | 摆放方式会影响答题，但不创造事实 |

## 现代系统如何吸收或限制

### 来源支持

- [[RAG]]、[[Retriever]]、[[Chunking]]、[[Embedding]] 支持：外部知识进入生成需要从 ingestion 到 retrieval 的完整链路，而不是只靠“向量库 + LLM”。
- [[Microsoft RAG 官方文档]] 和 [[Agent 工程基础设施主源]] 支持：现代 RAG 还涉及数据治理、索引、权限、检索质量、生成质量和评估。
- [[Memory]] 支持：长期信息需要写入、检索、更新、过期、权限和审计。
- [[Repo Context]] 和 [[SWE-bench]] 支持：代码 Agent 需要 repo-level evidence 和 patch validation。

### 工程综合 / inference

现代系统常把 RAG、memory 和 repo context 都做成候选 context 来源，再由 Context Engineering 统一处理优先级、预算、引用、权限和冲突。上下文窗口变大不取消这层工程：窗口越大，越需要防止错误资料、过期记忆和无关文件稀释关键证据。

### 仍需警惕的外推

本页不判断具体 embedding 模型、向量数据库、retriever 产品或 IDE agent 的优劣。那些属于实现选型和 freshness 更高的比较，应回到具体 source note 或后续前沿追踪。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 回答外部文档知识问题 | [[RAG]] + [[Retriever]] | 需要从可引用资料里找证据 | 检索结果可能不支持结论 |
| 文档检索命中率低 | [[Chunking]] / [[Embedding]] / [[Retriever]] | 失败可能在切分、表示或召回 | 只调 prompt 会掩盖上游问题 |
| 模型看到资料却答错 | [[Context Engineering]] | 可能是上下文排序、引用规则、压缩或冲突问题 | 正确资料被淹没或未显式要求使用 |
| 系统要记住用户偏好 | [[Memory]] | 需要跨会话写入和治理 | 不应混进普通文档 RAG 索引而无作用域 |
| Agent 长期记忆要落库 | [[Memory]] + [[Vector Database#Agent / RAG 选型边界]] | 偏好、配置、权限、当前状态更像结构化 state，通常适合关系库 / KV / 事件日志；对话摘要、文档 chunk、经验片段才适合向量召回 | 全部塞向量库会削弱确定性读写、权限、审计、删除和精确更新 |
| 代码 Agent 找不到该改哪里 | [[Repo Context]] | 需要文件、符号、测试和约定切片 | 语义相似文件不一定是正确修改点 |
| 上下文太大、噪音太多 | [[Context Engineering]] | 需要预算、优先级、压缩和来源边界 | 大窗口不等于高质量上下文 |

## 它们共同不是什么

- 都不是“把所有资料塞进 prompt”。
- 都不是事实正确性的自动保证；还需要 citation、evaluation、trace 和人工抽检。
- 都不是长期记忆的同义词；RAG 和 repo context 可能只是本次任务的信息来源。
- 都不是越多越好；无关 context 会增加误导、成本、延迟和权限风险。

## 证据锚点

- Concept anchors: [[Context Engineering#证据锚点]], [[RAG#证据锚点]], [[Memory#证据锚点]], [[Repo Context#证据锚点]], [[Retriever#证据锚点]], [[Chunking#证据锚点]], [[Embedding#证据锚点]]
- Source examples: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]], [[Microsoft RAG 官方文档]], [[Agent 工程基础设施主源]], [[SWE-bench]]
- Evidence type: concept-card synthesis + paper/docs/source-note evidence + coding-agent benchmark source + engineering synthesis + learning analogy.
- Confidence: medium-high for layer boundaries; medium for “什么时候用哪个判断”，因为实际取决于语料、权限、任务和评测结果。
- Boundary: 本页只比较 context 来源和组织层，不重复 [[RAG 类型对比]] 的 RAG 变体分类。

## 复习触发

1. 一个系统有 RAG，为什么仍可能需要单独的 Context Engineering？
2. [[Memory]] 和 [[RAG]] 都能检索信息，最小区别是什么？
3. 为什么 [[Repo Context]] 不是普通文档 RAG 的简单套用？
4. 如果答案引用了错误资料，你会先检查 [[Chunking]]、[[Retriever]] 还是 [[Context Engineering]]？为什么？
5. 上下文窗口扩大后，哪些问题不会自动消失？

## 相关链接

- [[Context Engineering]]
- [[RAG]]
- [[Memory]]
- [[Repo Context]]
- [[Retriever]]
- [[Chunking]]
- [[Embedding]]
- [[RAG 类型对比]]
- [[Agent Memory 类型对比]]
- [[Retrieval 组件对比]]
- [[LLM Wiki 工作流]]
