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
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/03_RAG/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 03_RAG
last_checked: 2026-05-09
freshness: watch
sha256: 7a4c6d8c455c972b36dca8fa4ab375469e9f5d7fe8157d07c66111898f2c8e83
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[RAG]]"
  - "[[LLM]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[RAG 主题]]"
---

# 了解搜索系统吗？和 [[RAG]] 有什么区别？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/03_RAG/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/03_RAG/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `03_RAG`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[RAG]]
- [[LLM]]
- [[RAG Citation Faithfulness]]
- [[RAG 主题]]

## 题目正文

### 6. 子问题：了解搜索系统吗？和 RAG 有什么区别？

答：

搜索系统的目标是“找文档”，输出是候选结果列表；

RAG 的目标是“给答案”，输出是基于证据融合后的自然语言结果。

两者不是替代关系，RAG 本质上是在搜索之上叠加了[[LLM]]的生成层。

工程上常见组合是先检索再生成，并保留引用来源，让用户既能快速拿答案，也能回查证据。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
