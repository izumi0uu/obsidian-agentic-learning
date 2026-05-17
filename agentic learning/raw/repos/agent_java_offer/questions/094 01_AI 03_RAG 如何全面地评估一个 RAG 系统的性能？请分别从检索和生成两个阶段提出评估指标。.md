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
updated: 2026-05-16
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/03_RAG/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 03_RAG
last_checked: 2026-05-09
freshness: watch
sha256: 41b10162e9d9babd43a258d9f6118728479cda0aadf25bea39f86fdab0765d60
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[LLM-as-Judge]]"
  - "[[Evaluation]]"
  - "[[Retriever]]"
  - "[[RAG]]"
  - "[[LLM]]"
  - "[[Observability]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[Hallucination]]"
  - "[[RAG 主题]]"
  - "[[Context Recall]]"
  - "[[Context Precision]]"
---

# 如何全面地[[Evaluation|评估]]一个 [[RAG]] 系统的性能？请分别从检索和生成两个阶段提出评估指标。

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[LLM-as-Judge]]
- [[Evaluation]]
- [[Retriever]]
- [[RAG]]
- [[LLM]]
- [[Observability]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[Hallucination]]
- [[RAG 主题]]
- [[Context Recall]]
- [[Context Precision]]
## 题目正文

### 2. 子问题：如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。

答：

- 将其拆分为**检索阶段**和**生成阶段**两个独立但又相互关联的部分进行评估，因为最终答案的质量是这两个阶段共同作用的结果。一个好的评估框架应该同时包含**客观的、自动化的指标**和**主观的、人工的评估**。

**第一阶段：检索性能评估 (Retrieval Evaluation)** 这个阶段的目标是评估我们的[[Retriever|检索器]]（Retriever）能否“**找得对、找得全**”。评估需要一个包含（问题，相关文档ID）的标注数据集。

- **核心指标：**
  1. **[[Context Precision|上下文精确率]] (Context Precision):** 衡量检索到的文档中有多少是真正与问题相关的。它反映了**检索结果的信噪比**。
  2. **[[Context Recall|上下文召回率]] (Context Recall):** 衡量所有相关的文档中，有多少被我们的检索器成功找回来了。它反映了**信息查找的全面性**。
- **其他常用排名指标：** 3. **Hit Rate:** 检索到的文档中是否至少包含一个相关文档。这是一个基础的“及格线”指标。 4. **MRR (Mean Reciprocal Rank):** 第一个相关文档排名的倒数的平均值。它衡量找到第一个正确答案的速度。 5. **nDCG@k (Normalized Discounted Cumulative Gain):** 最全面和常用的指标之一，它同时考虑了检索结果的**相关性等级**和它们在结果列表中的**排名**。
**第二阶段：生成性能评估 (Generation Evaluation)** 这个阶段的目标是评估[[LLM]]在给定上下文后，能否生成“**忠实、准确、有用**”的答案。
- **核心指标（通常需要LLM-as-a-Judge或人工评估）：**
  1. **可溯源性/zhong'cheng'd (Faithfulness / Groundedness):**
    - **评估问题：** 生成的答案是否完全基于所提供的上下文？是否存在捏造或[[Hallucination|幻觉]]？
  2. **答案相关性 (Answer Relevancy):**
    - **评估问题：** 生成的答案是否直接、清晰地回答了用户的原始问题？
  3. **答案正确性 (Answer Correctness):**
    - **评估问题：** 答案中的信息是否事实准确？（这是一个更严格的指标，因为有时即使忠于原文，原文也可能是错的）
- **自动化评估框架：**
  - 像 **RAGAS**, **ARES**, **TruLens** 这样的开源框架，它们使用LLM-as-a-Judge的思想，将上述的Faithfulness, Relevancy等指标自动化计算出来，极大地提高了评估效率。例如，RAGAS会生成问题、答案，并自动检查答案是否忠实于上下文。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
