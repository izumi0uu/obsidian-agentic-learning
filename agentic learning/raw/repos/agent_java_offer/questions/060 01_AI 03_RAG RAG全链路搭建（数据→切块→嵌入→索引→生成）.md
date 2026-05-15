---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "rag"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/03_RAG/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "03_RAG"
last_checked: 2026-05-09
freshness: watch
sha256: 990f101dd5f7f3176806e86f3d8a29152c51e6e458524bc5f3fd45c62262f563
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Retriever]]"
  - "[[Embedding]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[Durable Execution]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Vector Database]]"
  - "[[RAG 主题]]"
---

# RAG全链路搭建（数据→切块→嵌入→索引→生成）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Retriever]]
- [[Embedding]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[Durable Execution]]
- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Vector Database]]
- [[RAG 主题]]

## 题目正文

### 1. 子问题：RAG全链路搭建（数据→切块→嵌入→索引→生成）

主问题：如何从零搭建一个可用的 RAG 系统？

口述答案：
RAG 标准链路是：数据采集清洗、切块、嵌入、索引构建、在线检索、上下文组装、生成回答。关键不在“跑通”，在“可治理”：切块要兼顾语义完整与召回粒度，嵌入模型要看领域适配和检索指标，索引要支持增量更新和版本回切。上线时要保留数据版本、embedding 版本和索引版本，保证问题可复现、可回放。

常见追问：

1. 切块大小与重叠长度怎么定？
2. 嵌入模型怎么评估与替换？
3. 索引全量重建成本高时怎么办？
  1. **增量索引，不重建全量**
    档做 chunk_id + content_hash，只对“新增/变更/删除”的分片重算 embedding 并更新索引。
  2. **双索引版本化（蓝绿）**
    构建新版本索引，线上继续读旧版本；新索引验收通过后原子切换，失败可一键回滚到旧版本。
  3. **热冷分层**
    据（最近变更）走实时小索引，冷数据保留大基线索引；查询时做融合，夜间再异步合并，降低白天重建压力。
  4. **元数据与向量解耦**
    期、作者这类过滤条件变化，不要重建向量索引；单独维护元数据倒排/数据库过滤层即可。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
