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
sha256: b0df2217c46da76ea609c57c4ae85037a21c597647c823d84c6b5bbe71e3b54f
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Chunking]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[LLM]]"
  - "[[RAG 主题]]"
---

# RAG 系统在实际部署中可能面临哪些挑战？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Vector Database]]
- [[Embedding]]
- [[Chunking]]
- [[Document Ingestion]]
- [[RAG]]
- [[LLM]]
- [[RAG 主题]]

## 题目正文

### 3. 子问题：RAG 系统在实际部署中可能面临哪些挑战？

答：

1. **数据维护(Data Pipeline Complexity):**
  - **分块策略的泛化性：** 一个在PDF上效果很好的分块策略，可能在处理HTML或JSON数据时效果很差。为异构数据源设计和维护一套鲁棒的分块策略非常困难。
  - **知识库的实时更新：** 如何高效地保持向量索引与源数据的同步？当源文档被修改或删除时，需要有可靠的机制来更新或废弃对应的向量，这涉及到复杂的ETL（Extract, Transform, Load）流程。
2. **延迟与成本 (Performance Bottlenecks: Latency & Cost):**
  - **延迟：** RAG的“检索+生成”两步天然比直接调用LLM要慢。在实时交互场景下，检索和LLM生成的延迟都必须被极致优化。
  - **成本：**
    - **计算成本：** 大规模文档的嵌入、向量数据库的运行、LLM的API调用，都是持续的成本支出。
    - **存储成本：** 向量索引本身会占用大量的存储空间，尤其是高维度的嵌入。
3. **安全隐私 (Security & Privacy):**
  - **访问控制：** 在企业环境中，不同的用户对不同的文档有不同的访问权限。RAG系统必须能够集成这套权限体系，确保用户只能检索到他们有权查看的文档内容。
  - **提示注入：** 恶意用户可能会在查询中嵌入恶意指令，或者被索引的文档本身可能包含恶意内容，这些都可能用来攻击或操纵RAG系统。

## 4. 补充原问：RAG 流程和原理

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
