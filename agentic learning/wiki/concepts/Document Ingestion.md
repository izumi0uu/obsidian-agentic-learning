---
type: concept
topic:
  - rag
  - ingestion
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Chunking]]"
  - "[[Embedding]]"
  - "[[RAG Evaluation]]"
---

# Document Ingestion

## 一句话

Document Ingestion 是把 PDF、网页、表格、代码、图片说明等原始资料转换成可检索、可引用、可更新知识单元的流程。

## 它解决什么问题

RAG 的上限常常不是模型，而是资料进库质量。PDF 解析、表格结构、标题层级、页码、来源 URL、图片说明、去重和权限都会影响后续检索。

代表工具包括 LlamaParse、Docling、Unstructured、Firecrawl。

## 它不是什么

Document Ingestion 不是把文件全文复制进向量库。

它也不是一次性导入后就结束。生产知识库还要处理增量更新、删除、版本、权限和质量评估。

## 最小例子

```text
PDF -> parse text/table/image captions -> chunk -> metadata -> embedding -> index
```

## 常见误解和风险

- 表格被解析成乱序文本，答案会错。
- 页码和来源丢失，引用无法验证。
- OCR 错误会被后续 RAG 放大。
- 网页抓取可能带广告、导航和无关内容。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Chunking]]
- [[Embedding]]
- [[RAG Evaluation]]
