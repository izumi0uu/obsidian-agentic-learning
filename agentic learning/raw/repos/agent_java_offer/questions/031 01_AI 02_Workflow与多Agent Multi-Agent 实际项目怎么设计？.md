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
sha256: 098df7282d8cad4f46e75ece3dca6bc274f749e9699a4ae46a708f3d632fc7dc
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent State]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Handoff]]"
  - "[[Durable Execution]]"
  - "[[Agent Loop]]"
  - "[[Observation]]"
  - "[[Planning]]"
---

# Multi-Agent 实际项目怎么设计？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent State]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Multi-agent Orchestration]]
- [[Handoff]]
- [[Durable Execution]]
- [[Agent Loop]]
- [[Observation]]
- [[Planning]]

## 题目正文

### 5. 子问题：Multi-Agent 实际项目怎么设计？

答：
“角色分工 + 状态编排 + 失败恢复”三部分:

角色分工: 典型角色是 Planner（[[Planning|规划]]）、Executor（执行）、Critic（审校）、Tool Agent（外部能力）。

状态编排: 状态层用图或状态机管理节点流转，

失败恢复: 每个节点配超时、重试、步数上限、防循环, 高风险任务接人工接管（human-in-the-loop）。

每个 Agent 有明确输入输出契约，避免互相污染上下文。

上线后通过 trace 做全链路观测，重点看[[Task Success Rate|任务成功率]]、时延、成本和重试率。

核心思想是让 Agent 像微服务一样可组合、可回放、可治理。

追问：[[Multi-agent Orchestration|多 Agent 协作]]里最容易出问题的是哪一层？

最容易出问题的是**状态编排层（Orchestration）**，不是单个模型. 多 Agent 的失败大多发生在“[[Handoff|交接]]”.

LangGraph 能显著降低这类问题, 它的价值是把“多 Agent 协作”从隐式流程变成显式状态机，最容易出问题的编排层就更可控了。它主要帮你做这几件事：

1. 明确状态与节点边界：每个节点读写同一份状态，减少上下文串台。
2. 条件路由可控：用条件边和结束节点，避免无意回环。
3. 可恢复：checkpointer 支持中断后续跑，不用整条链重来。
4. 可插人工：关键节点可 interrupt 做人工审核。
5. 可观测：每步输入/输出可追踪，方便定位哪一层坏了。

但这些坑仍然会发生（框架不会替你解决）：

- I/O 契约没定义清楚
- [[Tool Calling|工具调用]]非幂等（重试导致重复副作用）
- 没有超时、最大步数、重试上限
- 状态字段设计混乱

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
