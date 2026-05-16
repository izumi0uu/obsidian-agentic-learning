---
type: concept
topic:
  - rag
  - ingestion
status: growing
created: 2026-05-06
updated: 2026-05-16
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Agent 工程基础设施主源#文档解析和 ingestion]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]"
related:
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Document Ingestion]]"
  - "[[Retriever]]"
  - "[[Parent-Child Chunking]]"
aliases:
  - "文档切分"
  - "切分策略"
  - "分块"
  - "chunk"
---

# Chunking

## 一句话

Chunking 是把长文档切成适合检索、引用和放入模型上下文的小片段。

## 概念详解

Chunking 解决的是 RAG 的“知识单元”问题。原始资料通常是 PDF、网页、表格、代码文件、会议记录或一整本手册；而检索系统需要比较的是较小、可定位、可排序、可引用的片段。如果直接把整份文档做 embedding，一个问题只命中文档整体，模型仍然不知道答案在第几段；如果切得太碎，片段会丢掉标题、上下文、表格含义和论证关系。

好的 chunk 不是简单按字符数切。它要尽量保持语义完整：标题和正文一起保留，步骤不要被切断，表格行列不要乱序，代码块不要被截成不可运行的片段，图片说明要和对应图像或段落建立关系。它还要携带 metadata：source、页码、section、URL、更新时间、权限标签、语言、文档版本。没有这些 metadata，后面的引用、权限过滤、去重和错误排查都会变难。

在 RAG pipeline 里，chunking 位于 [[Document Ingestion]] 和 [[Embedding]] 之间。它的输出会影响 retriever 能不能找回正确证据，也会影响 [[Reranking]] 和最终生成的上下文质量。许多 RAG 失败不是模型不会回答，而是 chunk 把答案和限定条件分开了；模型只看到一句结论，却没看到适用范围，就会生成过度泛化的答案。

证据边界：[[Agent 工程基础设施主源]] 支持文档解析/ingestion 工具链的重要性；经典 RAG 论文支持外部文档索引和 top-k retrieval 的基本结构。具体 chunk 大小、overlap、层级策略、表格处理方式，是工程综合，需要按数据类型和评测结果调整。


因此，chunking 是 RAG 质量的前置设计点，而不是导入脚本里的无关参数。
## 它解决什么问题

LLM 一次能看的上下文有限，向量检索也需要可比较的片段。切分太大，检索不准；切分太小，语义不完整。

## 它不是什么

Chunking 不是随便按固定字数切；也可以用 [[Parent-Child Chunking]] 这类层级切分。

它也不是越小越好。好的 chunk 要保留标题、层级、表格含义、引用来源和上下文边界。

## 最小例子

```text
一份 30 页 PDF
-> 按章节/标题/段落切分
-> 每个 chunk 保存 source、page、section、text、权限标签
-> embedding 和索引
```

## 常见误解 / 风险

- 表格、代码、公式和图片说明很容易被切坏。
- chunk overlap 可以补上下文，但会增加重复和成本。
- 没有 source metadata，后面很难引用和排错。
- 只调大 top-k 不能修复坏 chunk，只会召回更多坏上下文。

## 边界细节

和 [[Document Ingestion]] 的边界：ingestion 是从原始文件到可处理资料的整条入口流程；chunking 是其中“怎样切成检索单元”的步骤。

和 [[Embedding]] 的边界：embedding 把 chunk 变成向量；chunking 决定向量代表什么语义单元。embedding 再强，也不能恢复切分时丢掉的上下文。

和 [[Retriever]] 的边界：retriever 负责找片段；chunking 决定片段是否可找、可读、可引用。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 需要可检索、可引用的文档片段。
- 易变部分：不同工具对表格、图片、代码、多模态文档和 hierarchical chunking 的支持仍在变化。
- 复查点：当更换文档解析工具或 embedding 模型时，要重新评估 chunk 质量。

## 现代系统怎么吸收 Chunking 的价值

现代 RAG 系统通常把 chunking 做成可配置、可评测的 ingestion 策略：按标题层级切、按语义边界切、保留 overlap、为父子 chunk 建关联、对表格和代码使用特殊解析器，并在 evaluation 里检查“应该命中的证据 chunk 是否被召回”。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#文档解析和 ingestion]]
- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]
- Evidence type: infrastructure source note + paper source note + engineering synthesis.
- Confidence: medium
- Boundary: source notes 支持 ingestion 工具链和 RAG 外部索引边界；具体切分策略、metadata 字段和 overlap 权衡是工程综合，需要用本数据集评测。

## 复习触发

- 为什么 chunk 太大和太小都会伤害 RAG？
- 如果一个答案缺少限定条件，可能是哪种 chunking 错误造成的？
- chunk metadata 丢失会影响哪些后续环节？

## 相关链接

- [[RAG]]
- [[Embedding]]
- [[Document Ingestion]]
- [[Retriever]]
