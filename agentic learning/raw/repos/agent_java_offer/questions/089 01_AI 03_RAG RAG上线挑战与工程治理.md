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
sha256: 0f99fe2d8613299c0c85e881278b705b27721e8ce5a53d44f89e9a6d614519b3
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[RAG Evaluation]]"
  - "[[Evaluation]]"
  - "[[Retriever]]"
  - "[[RAG]]"
  - "[[Durable Execution]]"
  - "[[Observation]]"
  - "[[Document Ingestion]]"
  - "[[RAG 主题]]"
---

# RAG上线挑战与工程治理

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[RAG Evaluation]]
- [[Evaluation]]
- [[Retriever]]
- [[RAG]]
- [[Durable Execution]]
- [[Observation]]
- [[Document Ingestion]]
- [[RAG 主题]]

## 题目正文

### 1. 子问题：RAG上线挑战与工程治理

主问题：RAG 在生产环境最常见的坑和治理策略是什么？

口述答案：
生产挑战主要是三类：数据新鲜度、稳定性、可解释性。文档更新后索引滞后会导致“答旧不答新”；检索链路抖动会造成时延和空召回；回答不可追溯会影响业务信任。治理上要做增量更新、索引版本化、灰度发布、回滚开关、失败补偿和可观测看板。

常见追问：

1. 增量更新如何保证排序与质量不崩？
2. 没有索引快照时如何止损？
3. 如何做检索质量回归测试？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
