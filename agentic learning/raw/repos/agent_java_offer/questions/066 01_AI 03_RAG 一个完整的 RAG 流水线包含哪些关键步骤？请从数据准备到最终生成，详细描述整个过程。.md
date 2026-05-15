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
sha256: f61f764e182a762d1228c27f6a43aba300dac31533aa89387ca2382eec773758
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
  - "[[Evaluation]]"
  - "[[Query Rewrite]]"
  - "[[Top-K]]"
  - "[[Prompt]]"
  - "[[LLM Training Pipeline]]"
  - "[[Transformer]]"
  - "[[RAG 主题]]"
---

# 一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。

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
- [[Evaluation]]
- [[Query Rewrite]]
- [[Top-K]]
- [[Prompt]]
- [[LLM Training Pipeline]]
- [[Transformer]]
- [[RAG 主题]]

## 题目正文

### 3. 子问题：一个完整的 RAG 流水线包含哪些关键步骤？请从数据准备到最终生成，详细描述整个过程。

答：
完整链路分离线和在线两段。离线阶段做数据加载、清洗切块、向量化、建索引；在线阶段做查询改写、向量检索、重排、上下文组装、生成回答。面试建议强调“检索前处理”和“检索后重排”这两个提升点，线上还要有评估回流和索引更新机制，否则质量会逐步衰减。

- 一个完整的RAG流水线可以分为两个主要阶段：**离线的数据准备（索引）阶段** 和 **在线的查询（推理）阶段**。
**阶段一：数据准备 / 索引流水线 (Offline / Indexing Pipeline)** 这个阶段的目标是构建一个可供检索的知识库，它通常是一次性或周期性执行的。
  1. **数据加载（Load）：** 从各种数据源加载原始文档。数据源可以是PDF文件、Word文档、网页、Notion数据库、Confluence页面、数据库表格等。
  2. **文本切块（Split / Chunk）：** 将加载进来的长文档切割成更小的、语义完整的文本块（chunks）。这一步至关重要，因为后续的检索和生成都是以这些小块为单位的。
  3. **嵌入（Embed）：** 使用一个预训练的文本嵌入模型（Embedding Model，如BERT, BGE, M3E等），将每一个文本块转换成一个高维的数字向量（vector）。这个向量捕捉了文本块的语义信息。
  4. **存储（Store）：** 将每个文本块的内容及其对应的嵌入向量存储到一个专门的数据库中，最常见的就是**向量数据库（Vector Database）**，如FAISS, ChromaDB, Pinecone等。数据库会为这些向量建立索引，以便进行高效的相似度搜索。
  **阶段二：查询 / 推理流水线 (Online / Inference Pipeline)** 这个阶段是当用户提出问题时实时执行的。
  1. **用户提问（User Query）：** 系统接收用户输入的自然语言问题。
  2. **查询嵌入（Embed Query）：** 使用与**步骤三中完全相同**的嵌入模型，将用户的提问也转换成一个查询向量。
  3. **向量检索（Retrieve）：** 将这个查询向量与向量数据库中存储的所有文本块向量进行相似度计算（通常是余弦相似度或点积）。系统会找出与查询向量最相似的Top-K个文本块向量，并将它们对应的原始文本块内容检索出来。
  4. **（可选）重排序（Re-rank）：** 为了进一步提升检索质量，可以引入一个重排序模型。它会对初步检索出的Top-K个文本块进行更精细的打分和排序，选出与问题真正最相关的Top-N个（N < K）。
  5. **增强与生成（Augment & Generate）：**
    - 将重排序后最优的N个文本块内容，与用户的原始问题一起，按照一个预设的模板（Prompt Template）组合成一个增强提示。
    - 将这个增强提示发送给LLM，由LLM基于提供的上下文和自身知识，生成最终的、流畅的、有根据的回答。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
