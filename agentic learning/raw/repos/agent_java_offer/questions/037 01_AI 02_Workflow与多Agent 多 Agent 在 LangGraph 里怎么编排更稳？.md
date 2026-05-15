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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "02_Workflow与多Agent"
last_checked: 2026-05-09
freshness: watch
sha256: 6c6fb5802979beb1b53777dcb8b425e328ab197e24548c658e992e9fffe0a8de
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Workflow]]"
  - "[[Agent Framework]]"
  - "[[Durable Execution]]"
  - "[[Observation]]"
  - "[[Planning]]"
  - "[[RAG Citation Faithfulness]]"
---

# 多 Agent 在 LangGraph 里怎么编排更稳？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent State]]
- [[Context Engineering]]
- [[Multi-agent Orchestration]]
- [[Agent Workflow]]
- [[Agent Framework]]
- [[Durable Execution]]
- [[Observation]]
- [[Planning]]
- [[RAG Citation Faithfulness]]

## 题目正文

### 8. 子问题：多 Agent 在 LangGraph 里怎么编排更稳？

答：
用 LangGraph 的主控图+专家节点模式：Planner 只拆解任务，Dispatcher 负责路由，Executor 只执行，Critic 只审校。核心是契约化通信和图层守卫。

全局状态只放最小字段，大文本走引用，避免上下文污染。

图上配置最大步数、重试上限、超时和预算.

写操作加幂等键并在做 checkpoint。这样即使失败也能从节点恢复，不会重复副作用。

上线后按任务成功率、改写率、时延和成本做节点级观测，持续收敛流程稳定性。

追问：多 Agent 最容易坏在哪一层？你如何监控？

多 Agent 先坏编排层，我会把监控重点放在路由收敛、重试行为和契约有效性上；一旦 loop 或 retry 异常，先熔断入口再排查节点

## 2. 补充材料：多步骤研究型工作流的产品化思路

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
