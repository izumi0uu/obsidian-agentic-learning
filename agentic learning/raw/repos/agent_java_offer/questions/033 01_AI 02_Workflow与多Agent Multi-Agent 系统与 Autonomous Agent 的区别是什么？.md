---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 02_Workflow与多Agent
last_checked: 2026-05-09
freshness: watch
sha256: cb82a3a656a9d6bc8984be5ddf783970deda359ea68fb7bdd08838e7c47361ff
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[Approval Gate]]"
  - "[[Human-in-the-loop]]"
  - "[[Planning]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Agent 主题]]"
---

# Multi-Agent 系统与 Autonomous [[Agent]] 的区别是什么？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Multi-agent Orchestration]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent Loop]]
- [[Agent]]
- [[Approval Gate]]
- [[Human-in-the-loop]]
- [[Planning]]
- [[Trace]]
- [[Observability]]
- [[Agent 主题]]

## 题目正文

### 6. 子问题：Multi-Agent 系统与 Autonomous Agent 的区别是什么？

答：

Autonomous Agent 强调单体自主闭环，适合流程清晰、低风险、成本敏感的任务；

Multi-Agent 强调多角色分工协作，适合复杂任务拆解、并行处理和交叉审校。

把agent想象成组织中的员工, 要看具体做的事情的大小和复杂度.

工程上两者最大差异在编排复杂度和故障域：单体方案简单但一旦决策偏差影响全链路；多 Agent 方案治理更复杂，但可以局部隔离和重试，整体上限更高。

追问：什么场景下你会从 Autonomous Agent 降级到半自动[[Agent Workflow|工作流]]？

当任务风险高、动作不可逆或系统指标恶化时，我会把 Autonomous Agent 降级为半自动：保留其检索和生成能力，但把最终执行权交给[[Approval Gate|人工审批]]，先保正确性和可追责。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
