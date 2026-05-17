---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - rag
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/03_RAG/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 03_RAG
last_checked: 2026-05-09
freshness: watch
sha256: 0c325c743a22c769c31ce871d27d3dad59dba125010cd2b98ff4efea3101e7c9
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Self-RAG]]"
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[Hybrid Search]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Context Engineering]]"
  - "[[Observability]]"
  - "[[Query Rewrite]]"
  - "[[Knowledge Graph]]"
---

# [[RAG]]检索优化与高级范式（重排/图谱/自适应检索/[[Vector Database|向量库]]）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Self-RAG]]
- [[RAG]]
- [[GraphRAG]]
- [[Neo4j]]
- [[Hybrid Search]]
- [[Retriever]]
- [[Reranking]]
- [[Vector Database]]
- [[Embedding]]
- [[Context Engineering]]
- [[Observability]]
- [[Query Rewrite]]
- [[Knowledge Graph]]

## 题目正文

### 1. 子问题：RAG检索优化与高级范式（重排/图谱/自适应检索/向量库）

主问题：如何持续提升 RAG 的召回质量与问答效果？

口述答案：
优化路径通常是“召回更准 + 排序更稳 + 上下文更干净”。可用[[Hybrid Search|混合检索]]（向量+关键词）、重排模型、多[[Query Rewrite|查询改写]]、HyDE、元数据过滤、[[Knowledge Graph|知识图谱]]增强等手段。遇到 Lost in the Middle，要做上下文重排和压缩。向量库选型上，FAISS 适合单机实验，pgvector 适合和关系数据强耦合，Milvus 适合大规模服务化。

常见追问：

1. 何时引入图数据库而不是纯向量库？
2. 检索“慢和贵”怎么优化？
3. 向量库上线后看哪些核心指标？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
