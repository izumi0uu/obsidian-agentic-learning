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
sha256: fc5d958482dc6816a0249a88de7787ee9bd3b94fae93fd6127700ed683983be9
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Retriever]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[Agent Workflow]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[RAG Evaluation]]"
  - "[[Non-Parametric Memory]]"
  - "[[Prompt]]"
  - "[[Hallucination]]"
  - "[[RAG 主题]]"
---

# 请解释 [[RAG]] 的工作原理。与直接对 [[LLM]] 进行微调相比，RAG 主要解决了什么问题？有哪些优势？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Retriever]]
- [[Vector Database]]
- [[Embedding]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[Agent Workflow]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[RAG Evaluation]]
- [[Non-Parametric Memory]]
- [[Prompt]]
- [[Hallucination]]
- [[RAG 主题]]

## 题目正文

### 2. 子问题：请解释 RAG 的工作原理。与直接对 LLM 进行微调相比，RAG 主要解决了什么问题？有哪些优势？

答：
RAG 是“先检索、后生成”的模式：先从外部知识库召回相关片段，再把片段和问题一起喂给模型作答。它主要解决三件事：知识过时、领域私有知识缺失、[[Hallucination|幻觉]]不可控。相比微调，RAG 的优势是更新快、成本低、可追溯性强，业务文档变更时通常只需更新索引，不必重新训练大模型。

**RAG (Retrieval-Augmented Generation)** 的工作原理是一种“**先检索，后生成**”的模式，它将信息检索（Information Retrieval）与文本生成（Text Generation）相结合，来增强大型语言模型（LLM）的能力。

**工作流程如下：**

1. **检索（Retrieve）：** 当用户提出一个问题时，RAG系统首先不会直接将问题发送给LLM。相反，它会把用户的问题作为一个查询（Query），在一个外部的知识库（通常是[[Vector Database|向量数据库]]）中进行搜索，找出与问题最相关的几段信息（documents/chunks）。
2. **增强（Augment）：** 系统会将检索到的这些相关信息与用户的原始问题**拼接**在一起，形成一个内容更丰富、信息量更大的**增强[[Prompt|提示]]（Augmented Prompt）**。
3. **生成（Generate）：** 最后，将这个增强后的提示喂给LLM。LLM会基于其自身的知识和我们提供的上下文信息，生成一个更准确、更具事实性的回答。

**RAG主要解决了LLM的以下核心问题：**

1. **知识的静态性与过时性：** LLM的知识被“冻结”在其训练数据截止的那个时间点。RAG通过连接一个可以随时更新的外部知识库，使得LLM能够获取和利用最新的信息，解决了知识过时的问题。
2. **幻觉（Hallucination）：** LLM在回答其知识范围外或不确定的问题时，倾向于捏造事实。RAG通过提供具体的、相关的上下文，将LLM的回答“锚定”在这些事实依据上，显著降低了幻觉的产生。
3. **缺乏专业领域知识与私有知识：** 对LLM进行微调来注入特定领域的知识成本高昂且效果有限。RAG可以轻松地将模型与任何私有数据集（如公司内部文档、个人笔记）连接起来，使其成为一个领域专家。

**与微调（Fine-tuning）相比，RAG的优势：**

- **知识更新成本低：** 更新知识只需在数据库中添加或修改文档，无需重新训练昂贵的LLM。而微调则需要重新进行训练。
- **可追溯性与可解释性：** RAG可以清晰地展示出答案是基于哪些源文档生成的，用户可以点击查看来源进行事实核查。微调则像一个“黑盒”，无法知道知识的具体来源。
- **降低幻觉：** RAG通过提供事实依据，让回答有据可循。微调虽然能注入知识，但模型仍可能在不确定时产生幻觉。
- **个性化：** 可以为每个用户或每个请求动态地接入不同的知识源，实现高度的个性化服务

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
