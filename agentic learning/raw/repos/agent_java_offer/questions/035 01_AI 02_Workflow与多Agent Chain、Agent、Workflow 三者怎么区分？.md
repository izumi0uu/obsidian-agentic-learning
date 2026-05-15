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
sha256: 4f078bf4c3a7c4a8933ffff1504f300817fb6bad2acb2fb88fee46a63f7c7636
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
  - "[[Approval Gate]]"
  - "[[Guardrails]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Agent Framework]]"
  - "[[Durable Execution]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[Tool Calling]]"
  - "[[Trace]]"
  - "[[Observability]]"
---

# Chain、[[Agent]]、[[Agent Workflow|Workflow]] 三者怎么区分？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Least Privilege Tools]]
- [[Tool Permissioning]]
- [[Approval Gate]]
- [[Guardrails]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Agent Framework]]
- [[Durable Execution]]
- [[Agent Loop]]
- [[Agent]]
- [[Tool Calling]]
- [[Trace]]
- [[Observability]]

## 题目正文

### 7. 子问题：Chain、Agent、Workflow 三者怎么区分？

答：
Chain 是固定顺序管道，适合确定性流程；Agent 是模型驱动决策，适合开放任务；Workflow（特别是 LangGraph）是显式状态机，适合把 Agent 决策放进可控节点里。我的实践是“固定流程优先 Chain，复杂闭环用 LangGraph Workflow 托管 Agent”。

追问：你会如何限制 Agent 的自由度，避免乱[[Tool Calling|调用工具]]？

对，首先是工具白名单和最少[[Least Privilege Tools|最小权限]]的放行。然后还有是限制最大部署、最大调用次数、超时和成本，以及超阈值的容量降低降级。就是写作操作加密等件，以及高风险动作必须人工来审批。再配合全链路的监控和日常告警，可以做到可追溯、可回滚、可治理。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
