---
type: concept
topic:
  - rag
  - ingestion
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Microsoft RAG 官方文档]]"
evidence:
  - "[[Agent 工程基础设施主源#文档解析和 ingestion]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
  - "[[Microsoft RAG 官方文档#边界提醒]]"
related:
  - "[[RAG]]"
  - "[[Chunking]]"
  - "[[Embedding]]"
  - "[[RAG Evaluation]]"
---

# Document Ingestion

## 一句话

Document Ingestion 是把 PDF、网页、表格、代码、图片说明等原始资料转换成可检索、可引用、可更新知识单元的流程。

## 概念详解

Document Ingestion 是 RAG 的入口层。它负责把“人能读的资料”变成“系统能检索和追溯的资料”。原始文件可能包含标题层级、页码、脚注、表格、图片、代码块、网页导航、广告、权限信息和版本信息；如果入口层没有保留这些结构，后面的 [[Chunking]]、[[Embedding]]、[[Retriever]] 和生成回答都会在脏数据上工作。

它通常包括几个步骤：抓取或上传资料，解析文本、表格和图片说明，清洗噪声，去重，识别标题/章节/页码，拆分 chunk，补 metadata，生成 embedding，写入向量库、全文索引或图数据库。生产系统还要处理增量更新、删除、版本回滚、权限过滤、数据过期、失败重试和质量评估。Microsoft 的 RAG source note 提醒，企业级 RAG 不只是“向量检索 + LLM”，还包括数据治理、索引、检索质量、权限和评估；这说明 ingestion 不是外围杂活，而是 RAG 正确性的上游约束。

Document Ingestion 的质量会决定 RAG 的上限。PDF 表格被解析成乱序文本，模型可能把列和值配错；网页抓取混入导航栏，retriever 会命中无关噪声；没有页码和 URL，答案无法引用；权限标签丢失，检索可能泄露私有内容；旧版本未删除，系统会引用过期政策。许多“模型幻觉”其实来自 ingestion 把坏上下文送到了模型面前。

证据边界：[[Agent 工程基础设施主源]] 支持 LlamaParse、Docling、Unstructured、Firecrawl 等文档解析和 ingestion 工具作为工程基础设施；[[Microsoft RAG 官方文档]] 支持企业 RAG 的治理、索引、权限和评估边界。具体工具能力和 API 会变化，所以这张卡只沉淀概念边界，不把某个工具写成通用定义。

## 它解决什么问题

RAG 的上限常常不是模型，而是资料进库质量。PDF 解析、表格结构、标题层级、页码、来源 URL、图片说明、去重和权限都会影响后续检索。

代表工具包括 LlamaParse、Docling、Unstructured、Firecrawl。

## 它不是什么

Document Ingestion 不是把文件全文复制进向量库。

它也不是一次性导入后就结束。生产知识库还要处理增量更新、删除、版本、权限和质量评估。

## 最小例子

```text
PDF -> parse text/table/image captions -> clean -> chunk -> metadata -> embedding -> index
```

## 常见误解 / 风险

- 表格被解析成乱序文本，答案会错。
- 页码和来源丢失，引用无法验证。
- OCR 错误会被后续 RAG 放大。
- 网页抓取可能带广告、导航和无关内容。
- 权限 metadata 丢失会让检索绕过访问控制。

## 边界细节

和 [[Chunking]] 的边界：ingestion 包含解析、清洗、去重、metadata、版本和权限；chunking 是其中把资料切成检索单元的一步。

和 [[Vector Database]] 的边界：vector database 保存和检索向量；ingestion 决定写进去的内容是否干净、可引用、可更新。

和 [[RAG Evaluation]] 的边界：eval 会暴露 ingestion 问题，例如应该命中的文档未被召回、引用无法定位、过期资料被召回。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 需要数据准备、索引、metadata 和权限治理。
- 易变部分：具体 parser、OCR、多模态表格解析、网页抓取和企业 connector 能力变化快。
- 复查点：当 source note 的 ingestion 工具列表更新时，只更新工具生态，不改 ingestion 的概念边界。

## 现代系统怎么吸收 Document Ingestion 的价值

现代系统把 ingestion 做成可重复 pipeline：有输入队列、解析器、质量检查、chunk 策略、metadata schema、索引写入、权限同步、删除/更新事件和监控。对个人 Obsidian wiki，最小版本是 raw note 保持不动，concept card 写清 evidence anchor；对企业 RAG，则需要数据治理和访问控制一起进入 ingestion。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#文档解析和 ingestion]]
- Source: [[Microsoft RAG 官方文档]]
- Anchor: [[Microsoft RAG 官方文档#一句话]]
- Anchor: [[Microsoft RAG 官方文档#边界提醒]]
- Evidence type: infrastructure source note + official docs source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 ingestion/数据治理/索引/权限/评估的重要性；具体工具名称是生态例子，不是 Document Ingestion 的稳定定义。

## 复习触发

- 为什么 RAG 的错误可能来自 ingestion，而不是模型？
- 解析 PDF 表格时最应该保留哪些 metadata？
- 个人知识库和企业 RAG 的 ingestion 边界有什么不同？

## 相关链接

- [[RAG]]
- [[Chunking]]
- [[Embedding]]
- [[RAG Evaluation]]
