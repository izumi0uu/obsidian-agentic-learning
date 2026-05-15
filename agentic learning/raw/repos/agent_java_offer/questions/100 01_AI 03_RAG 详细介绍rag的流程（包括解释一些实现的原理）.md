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
sha256: d7a069da73137ff3ec3a424f9432d78bd52de72c3d4654311aad1cf63d9c14de
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[Embedding]]"
  - "[[Vector Database]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[LLM]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[LLM Gateway]]"
  - "[[RAG 主题]]"
---

# 详细介绍rag的流程（包括解释一些实现的原理）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Reranking]]
- [[Retriever]]
- [[Embedding]]
- [[Vector Database]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[LLM]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[Prompt]]
- [[Hallucination]]
- [[LLM Gateway]]
- [[RAG 主题]]

## 题目正文

### 1. 子问题：详细介绍rag的流程（包括解释一些实现的原理）

**口述答案（约300字）**：
RAG我一般分离线和在线两段讲。离线阶段先做数据接入和清洗，把PDF、Word、网页等转成统一文本；然后分块，通常按语义边界加重叠窗口，避免信息断裂；接着做Embedding写入向量库，并建立元数据索引。在线阶段是：用户问题先规范化，再做检索召回，拿到TopK候选后做重排，最后把“问题+高相关上下文+输出约束”拼成增强Prompt给大模型。核心原理是用向量相似度补充模型参数外知识，降低幻觉。工程上关键点有三类：第一是召回质量，靠分块策略、Embedding模型和重排一起保障；第二是时延，靠缓存、并行检索和限流；第三是可解释性，要求输出引用片段与来源。我的经验是先把召回率做上来，再调重排和Prompt，不然模型再强也会“无米下锅”。
**来源**：公开社区资料

## 5. 补充原问：RAG 主要解决什么问题？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
