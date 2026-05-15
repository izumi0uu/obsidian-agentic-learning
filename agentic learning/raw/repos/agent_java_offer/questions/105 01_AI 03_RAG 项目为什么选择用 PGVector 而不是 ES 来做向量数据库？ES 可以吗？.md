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
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/03_RAG/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "03_RAG"
last_checked: 2026-05-09
freshness: watch
sha256: f56680722f16d0c8d9d3bcb1998f86b859af7806b0b5f365330dccea91d50e85
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[RAG]]"
  - "[[RAG 主题]]"
---

# 项目为什么选择用 PGVector 而不是 ES 来做[[Vector Database|向量数据库]]？ES 可以吗？

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
- [[RAG 主题]]

## 题目正文

### 1. 子问题：项目为什么选择用 PGVector 而不是 ES 来做向量数据库？ES 可以吗？

**口述答案（约300字）**：
ES可以做向量检索，但我选PGVector是因为我们的场景需要“向量检索和关系数据一体化”以及更低接入成本。第一，数据原本就在PostgreSQL体系，使用PGVector可以减少异构系统同步和一致性治理成本。第二，我们的规模和QPS在PGVector可承受范围内，优先工程简洁和可维护。第三，很多业务查询是“结构化过滤+向量相似度”组合，放在同库更顺滑。ES的优势在于大规模检索和复杂搜索生态，如果后续数据量上升到更高量级，ES或专用向量库会是候选。面试里我会强调：选型不是绝对优劣，而是“业务规模、团队运维能力、数据一致性成本”的综合权衡。
**来源**：公开社区资料

## 10. 补充原文：向量检索算法概览

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
