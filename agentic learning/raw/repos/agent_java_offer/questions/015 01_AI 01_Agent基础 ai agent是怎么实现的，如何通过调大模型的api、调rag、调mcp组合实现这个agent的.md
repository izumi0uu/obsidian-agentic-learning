---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "01_Agent基础"
last_checked: 2026-05-09
freshness: watch
sha256: 4ff688b97045bf5587ca106170f40fe29666f15d7a7e89df3ac49a5464083a53
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[RAG]]"
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[MCP]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Agent Workflow]]"
  - "[[Non-Parametric Memory]]"
  - "[[Prompt]]"
  - "[[LLM]]"
---

# ai agent是怎么实现的，如何通过调大模型的api、调rag、调mcp组合实现这个agent的

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[RAG]]
- [[Agent State]]
- [[Context Engineering]]
- [[Tool Calling]]
- [[Tool Use]]
- [[MCP]]
- [[Durable Execution]]
- [[Agent]]
- [[Agent Loop]]
- [[Agent Workflow]]
- [[Non-Parametric Memory]]
- [[Prompt]]
- [[LLM]]

## 题目正文

### 1. 子问题：ai agent是怎么实现的，如何通过调大模型的api、调rag、调mcp组合实现这个agent的

**口述答案（约300字）**：
我会把这题回答成“控制面+数据面”。控制面是状态机/图编排：定义节点、路由条件、重试策略和结束条件；数据面是每个节点具体怎么跑。大模型API负责推理与决策，RAG负责提供外部知识，MCP负责标准化工具调用。一个典型回路是：先由模型判断当前任务是否需要知识检索或调用工具；若需要，就先走RAG拿上下文，再走MCP调用外部能力，比如搜索、数据库查询、系统操作；工具结果回填到状态，再交给模型继续推理，直到满足结束条件。关键是“节点输入输出契约”要清晰，比如每个节点只读必要状态，只写自己产物，避免上下文污染。为了线上稳定，我会加步数上限、超时、幂等键和降级策略；为了可运维，我会打全链路trace，区分是Prompt问题、检索问题还是工具问题。
**来源**：公开社区资料

## 4. 补充原问：Agent 当前的局限是什么？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
