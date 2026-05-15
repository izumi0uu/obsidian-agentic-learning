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
sha256: 7fd1bf5851c3c9e237eefa81fdf12a0d87c6bc6ec8e20004b46a28d184e63bc8
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[Observation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[Top-K]]"
  - "[[Prompt]]"
  - "[[Token]]"
---

# LangGraph 里状态（State）怎么设计？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Vector Database]]
- [[Embedding]]
- [[Memory]]
- [[Agent State]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent]]
- [[Observation]]
- [[RAG Citation Faithfulness]]
- [[Top-K]]
- [[Prompt]]
- [[Token]]

## 题目正文

### 3. 子问题：LangGraph 里状态（State）怎么设计？

答：

1. State 只放“决策必需信息”，不放大段冗余文本。字段包括任务目标、中间结果、证据、错误码、重试计数、下一步动作。
2. 分层：业务数据、过程数据、观测数据分开。
3. 节点只读必要字段、只写自己负责字段，避免相互污染。
4. 大对象放外部存储（DB/[[Vector Database|向量库]]），State里放引用ID。

追问：如果状态越来越大导致 [[Token|token]] 成本上升，如何治理？

1. **状态分层**

把状态拆成`运行态（短期）/ 记忆态（长期）/ 证据态（可重取）`，只把运行态放进上下文。

1. **摘要替代原文**

对历史对话和中间结果做结构化摘要（结论、待办、风险），而不是全量拼接。

1. **外部化存储**

长文本、检索结果、工具原始返回存数据库/向量库，prompt里只放引用和[[Top-K|top-k]]片段。

1. **成本守门与告警**

设 token budget（输入/输出上限），监控 `avg/p95 token`、单请求成本、摘要命中率，超阈值自动降级（更短上下文或低成本模型）。

## 2. 主干问题：[[Prompt]] 工程和其他调优手段如何协同？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
