---
type: source
source_type: docs
title: RAGFlow Documentation and GitHub README
url: https://ragflow.io/docs/dev/
author: InfiniFlow
site: ragflow.io
topic:
  - rag
  - agent
  - framework
  - document-ingestion
  - frontier
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: volatile
conflicts: []
status: seed
source:
  - https://ragflow.io/
  - https://ragflow.io/docs/dev/
  - https://github.com/infiniflow/ragflow
related:
  - "[[RAGFlow]]"
  - "[[RAG]]"
  - "[[Document Ingestion]]"
  - "[[Chunking]]"
  - "[[Hybrid Search]]"
  - "[[Reranking]]"
  - "[[Agentic RAG]]"
  - "[[Vector Database]]"
---

# RAGFlow 官方文档

## 为什么收

RAGFlow 是 InfiniFlow 维护的开源 RAG 引擎 / context layer 平台。它适合进入这个 vault，不是因为它重新定义了 [[RAG]]，而是因为它把文档理解、可视化切分、检索、重排、引用、API 和 Agent 能力放进一个端到端工程平台里。

这份 source 主要用于校准一个面试高频边界：RAGFlow 更接近“开箱即用的 RAG / 知识库平台”，不是普通向量数据库，也不是 LangChain / LlamaIndex 那种主要由代码组合的通用框架。

## 主源

- Official site: <https://ragflow.io/>
- Documentation: <https://ragflow.io/docs/dev/>
- GitHub repo: <https://github.com/infiniflow/ragflow>
- README checked on 2026-05-18: project describes RAGFlow as an open-source RAG engine that fuses RAG with Agent capabilities to create a context layer for LLMs.

## 一句话

RAGFlow 是一个端到端 RAG / context layer 平台：重点在复杂文档解析、可解释切分、多路召回、融合重排、引用溯源和可视化/接口化交付。

## 关键事实

- README 将 RAGFlow 定位为 open-source Retrieval-Augmented Generation engine，并强调融合 RAG 与 Agent capabilities，为 LLM 创建 context layer。
- README 的 key features 强调 deep document understanding、template-based chunking、grounded citations、heterogeneous data sources、automated RAG workflow、multiple recall paired with fused re-ranking。
- 支持的数据形态覆盖 Word、slides、excel、txt、images、scanned copies、structured data、web pages 等。
- README 说明 RAGFlow 默认使用 Elasticsearch 存储 full text 和 vectors，也可以切换到 InfiniFlow 的 Infinity。
- 自托管形态依赖 Docker / Docker Compose，并使用 MySQL、MinIO、Redis、Elasticsearch / Infinity 等后端组件；这说明它是完整平台栈，不是单个检索库。
- README 最新更新记录显示它在 2025-08-01 支持 agentic workflow and MCP，2025-12-26 支持 AI agent memory，说明具体 Agent 能力属于 volatile 产品层，需要定期复查。

## 可以拆成概念卡

- [[RAGFlow]]
- [[RAG]]
- [[Document Ingestion]]
- [[Chunking]]
- [[Hybrid Search]]
- [[Reranking]]
- [[Agentic RAG]]
- [[Vector Database]]

## 学习时先看

1. 先读 README 的 What is RAGFlow / Key Features，确认项目定位。
2. 再读 Quickstart / User Guides，理解 dataset、document parsing、chunking 和 chat / agent workflow 的操作边界。
3. 再读 deployment / configuration，确认它依赖哪些存储、搜索和对象存储组件。
4. 最后看 release notes / roadmap，只把快速变化能力写入 source note 或前沿追踪，不把某个版本特性写成稳定概念定义。

## 边界提醒

RAGFlow 不是 [[RAG]] 本身。RAG 是检索增强生成范式；RAGFlow 是实现、产品化和运营这条链路的开源平台。

RAGFlow 也不是 [[Vector Database]]。它可以使用 Elasticsearch / Infinity 等底层存储和搜索引擎，但它的学习价值在于把文档理解、切分、检索、重排、引用、API、UI 和 Agent workflow 组合起来。

不要把 `RAG Flow` 两个词自动当成 RAGFlow。前者经常只是“RAG 流程 / pipeline”的普通说法；只有指向 InfiniFlow 项目时才是本 source 的同一对象。

## 证据锚点候选

- GitHub README：What is RAGFlow, Key Features, System Architecture, Self-Hosting, Switch doc engine from Elasticsearch to Infinity。
- Documentation homepage：Quickstart / user guides / developer guides。
- GitHub Roadmap / release notes：适合追踪 agentic workflow、MCP、memory、document parser 等易变能力。

## 我的疑问

- RAGFlow 的 agentic workflow 和 MCP 能力，在生产上更像轻量 Agent 编排，还是更像 RAG app 的扩展工具层？
- 它的 deep document understanding 和 template-based chunking 在表格、扫描件和多模态 PDF 上如何评估质量？
- 当团队后续迁出 RAGFlow，用 LangChain / LlamaIndex / 自研 pipeline 重构时，哪些配置和评估样本可以迁移？
