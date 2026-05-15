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
sha256: efcc48d5f698f13329dadbcc8f1d87586e33f78224375246c3cf983275b39215
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[Context Engineering]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[Non-Parametric Memory]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
---

# 谈谈对 RAG的理解，你认为它主要解决了哪些问题？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Reranking]]
- [[Retriever]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[Context Engineering]]
- [[Agent Loop]]
- [[Agent]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[Non-Parametric Memory]]
- [[Prompt]]
- [[Hallucination]]

## 题目正文

### 1. 子问题：谈谈对 RAG的理解，你认为它主要解决了哪些问题？

**口述答案（约300字）**：
我理解RAG是“检索增强生成”，核心价值是把外部知识在推理时注入模型，解决模型知识时效性差、专业领域覆盖不足和事实幻觉问题。它主要解决三类问题：第一，知识更新问题，不需要重新训练就能接入新资料；第二，可解释性问题，回答可附引用来源；第三，成本问题，相比全量微调，RAG迭代更快更便宜。它的边界也要讲清：RAG不能替代推理能力，召回不准时输出也会差，所以要重视分块、召回、重排和Prompt约束。我的实践原则是“先保障召回，再优化生成”，并用线上bad case持续回流，形成检索与提示词的双闭环优化。
**来源**：公开社区资料

## 6. 补充原问：知识库文档和切块

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
