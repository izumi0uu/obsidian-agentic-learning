---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "memory"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "04_上下文工程与记忆"
last_checked: 2026-05-09
freshness: watch
sha256: b6d70be6b923c4787f6bb8ab6809f98c1e3c7e0b63405ffbd1f1706f5ffce120
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Vector Database]]"
  - "[[Long-term Memory]]"
  - "[[Memory]]"
  - "[[Context Engineering]]"
  - "[[Agent Workflow]]"
  - "[[Planning]]"
  - "[[Tool Use]]"
  - "[[Knowledge Graph]]"
  - "[[Context Window]]"
  - "[[Prompt]]"
  - "[[LLM]]"
---

# Memory 是 Agent 的一个关键模块。请问如何为 Agent 设计短期记忆和长期记忆系统？可以借助哪些外部工具或技术？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[GraphRAG]]
- [[Neo4j]]
- [[RAG]]
- [[Embedding]]
- [[Vector Database]]
- [[Long-term Memory]]
- [[Memory]]
- [[Context Engineering]]
- [[Agent Workflow]]
- [[Planning]]
- [[Tool Use]]
- [[Knowledge Graph]]
- [[Context Window]]
- [[Prompt]]
- [[LLM]]

## 题目正文

### 2. 子问题：Memory 是 Agent 的一个关键模块。请问如何为 Agent 设计短期记忆和长期记忆系统？可以借助哪些外部工具或技术？

答：
短期记忆主要承载当前会话上下文窗口信息、工具返回和中间推理轨迹，保障任务连贯；长期记忆用于存用户偏好、历史经验和领域知识，支撑跨会话能力。落地上短期常用窗口/摘要机制，长期常用向量库做相似检索, 如RAG范式，也可结合 SQL 或知识图谱存结构化(NeoJ)事实。关键点是“写入策略+检索策略+淘汰策略”三者要同时设计。

- **工作流程：**
  1. **存储（Storing/Writing）：** 当Agent获得一个有价值的信息（如用户明确给出的偏好、一个成功解决问题的完整流程）时，它会使用一个**嵌入模型（Embedding Model）**将这段文本信息转换成一个高维向量。然后，将这个向量及其原始文本存入向量数据库。
  2. **检索（Retrieving/Reading）：** 在Agent进行规划或决策时，它会把当前的任务或问题也转换成一个查询向量。然后，用这个查询向量去向量数据库中进行**相似度搜索**，找出与当前情况最相关的历史记忆。
  3. **使用（Using）：** 检索到的记忆（原始文本）会被插入到LLM的Prompt中，作为额外的上下文，来指导LLM做出更明智的决策。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
