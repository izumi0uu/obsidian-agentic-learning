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
sha256: 01ed27df9eb83b7a1c0769cffb64e2041a8ddaf335ab1d132bc06c329f6703e8
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[RAG]]"
  - "[[Observability]]"
  - "[[RAG Evaluation]]"
  - "[[Document Ingestion]]"
  - "[[Hallucination]]"
  - "[[RAG 主题]]"
---

# 向量检索（Milvus / FAISS / PGVector）怎么选型？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Vector Database]]
- [[Embedding]]
- [[RAG]]
- [[Observability]]
- [[RAG Evaluation]]
- [[Document Ingestion]]
- [[Hallucination]]
- [[RAG 主题]]

## 题目正文

### 7. 子问题：向量检索（Milvus / FAISS / PGVector）怎么选型？

答：

pgvector 适合向量检索和关系数据强耦合场景，能直接用 SQL 做联查和事务，接入成本最低

Milvus 适合大规模在线检索和高并发服务化，扩展性最好，但运维复杂度也最高。

FAISS 是库级方案，适合单机高性能和快速实验，但持久化、过滤、服务治理要自己补。

我的策略通常是先用 pgvector 快速落地，规模和 QPS 上来后再迁到 Milvus，FAISS 更多用于算法实验或内部检索模块。

追问：[[Vector Database|向量库]]上线后你会盯哪些核心指标？

1. **检索质量:** 看“检索命中率、答案可溯源率、[[Hallucination|幻觉]]率变化”
2. **时延与吞吐:** `p50/p95/p99` 查询时延（ANN检索时延 + 端到端时延）
3. **可用性与稳定性:** 错误率、可用性（SLA）、CPU、内存、磁盘
4. **数据新鲜度与索引健康:** 数据入库延迟、索引构建/更新延迟

## 3. 主干问题：[[RAG]] 上线后如何治理慢、贵、幻觉与回归问题？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
