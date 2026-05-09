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
sha256: a7be8d9c7f8b920ecd542bb9aeaab7adce754991d8406d23be3f9beb1fb53850
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Self-RAG]]"
  - "[[RAG]]"
  - "[[Agentic RAG]]"
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Reflexion]]"
  - "[[Memory Reflection]]"
  - "[[Agent Workflow]]"
---

# 传统的 RAG 流程是“先检索后生成”，你是否了解一些更复杂的 RAG 范式，比如在生成过程中进行多次检索或自适应检索？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Self-RAG]]
- [[RAG]]
- [[Agentic RAG]]
- [[GraphRAG]]
- [[Neo4j]]
- [[Vector Database]]
- [[Embedding]]
- [[Reflexion]]
- [[Memory Reflection]]
- [[Agent Workflow]]

## 题目正文

### 5. 子问题：传统的 RAG 流程是“先检索后生成”，你是否了解一些更复杂的 RAG 范式，比如在生成过程中进行多次检索或自适应检索？

答：
有，典型是迭代检索和自适应检索。迭代检索会在初答后做反思，再发起二次检索补证据；自适应检索是在生成过程中遇到不确定点时动态触发检索。还有多源 Agentic RAG，会同时调用向量库、图谱、SQL 或搜索 API。它们共同目标是提升复杂问题准确率，但会增加流程复杂度和时延。

传统的“先检索后生成”（Retrieve-then-Read）范式虽然经典，但比较刻板。为了应对更复杂的问题和提升答案质量，研究界已经提出了多种更动态、更智能的RAG范式。

**1. 迭代式检索 (Iterative Retrieval) - 例如 Self-RAG, Corrective-RAG**

- **核心思想：** 将RAG从一个单向的流水线，变成一个**循环、自我修正**的过程。
- **工作流程：**
  1. **首次检索与生成：** 像传统RAG一样，进行检索并生成一个初步的答案。
  2. **反思与评估（Reflection）：** LLM会对初步生成的答案和检索到的上下文进行“反思”。它会评估：当前的信息是否足够支撑答案？答案是否还有不确定或缺失的部分？
  3. **二次检索：** 如果认为信息不足，LLM会**主动生成一个新的、更具针对性的查询**，进行新一轮的检索。例如，如果初步答案是“A公司的CEO是张三”，模型可能会反思“这个信息是否最新？”，然后生成一个新的查询“A公司2025年的CEO是谁？”
  4. **整合与精炼：** LLM会整合新旧检索到的所有信息，生成一个更完善、更准确的最终答案。

**2. 自适应检索 (Adaptive Retrieval) - 例如 FLARE, Self-Ask**

- **核心思想：** 不在生成前一次性检索所有信息，而是在**生成过程中“按需”检索**，实现“即时”（just-in-time）的信息获取。
- **工作流程：**
  1. **开始生成：** LLM根据问题开始直接生成答案。
  2. **预测不确定性：** 它会一边生成，一边预测接下来的内容。当它预测到即将生成一个事实性信息（如人名、日期、地点），但对此**不确定**（表现为下一个词的概率分布很平坦）时，它会**暂停**生成。
  3. **主动提问与检索：** 在暂停处，LLM会插入一个特殊的占位符（如 `[SEARCH]`），并主动提出一个需要查询的问题（例如，“法国的首都是哪里？”）。
  4. **获取信息并继续：** 系统执行这个查询，将检索到的答案（“巴黎”）填入，然后LLM基于这个新信息继续向下生成。
- **优势：** 这种方法非常高效，只在需要时才进行检索，避免了预先检索大量无关信息。

**3. 多源数据RAG (Multi-Source RAG)**

- **核心思想：** 让Agent能够智能地从**多种不同类型的数据源**中进行检索和整合。
- **工作流程：** Agent首先对问题进行分解，判断回答这个问题需要哪些信息。然后，它可能会决定：
  - 从**向量数据库**中检索相关的非结构化文档。
  - 从**知识图谱**中查询结构化的实体关系。
  - 调用**SQL数据库**来获取精确的统计数据。
  - 甚至调用**搜索引擎API**来获取实时信息。
- 最后，Agent会将从不同来源获取的所有信息进行综合，生成一个全面的答案。这本质上是一种**Agent驱动的RAG**。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
