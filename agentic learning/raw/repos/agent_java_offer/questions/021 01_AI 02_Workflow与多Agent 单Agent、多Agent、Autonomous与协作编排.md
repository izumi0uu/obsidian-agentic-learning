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
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "02_Workflow与多Agent"
last_checked: 2026-05-09
freshness: watch
sha256: 9a71b6db059ca1a3ccf114323c1658ee4406aa30fba44084ec62dfe38deff365
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent State]]"
  - "[[A2A]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Workflow]]"
  - "[[Agent Loop]]"
---

# 单Agent、多Agent、Autonomous与协作编排

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent State]]
- [[A2A]]
- [[Multi-agent Orchestration]]
- [[Agent Workflow]]
- [[Agent Loop]]

## 题目正文

### 1. 子问题：单Agent、多Agent、Autonomous与协作编排

主问题：什么时候用单 Agent，什么时候用多 Agent，什么时候要降级半自动？

口述答案：
单 Agent 适合流程短、目标清晰、风险可控场景；多 Agent 适合复杂任务拆解与并行协作，比如 Planner/Executor/Critic 分工；Autonomous Agent 强调长链路自主闭环，但需要更强安全边界。多 Agent 的优势是上限高，但复杂度集中在通信协议、状态一致性和路由收敛。若涉及高风险动作、成功率持续下滑或链路不可解释，应降级到半自动工作流，让人工接管关键决策。

常见追问：

1. 多 Agent 最容易坏在哪一层？
2. A2A 协议与普通框架差异是什么？
3. 如何定义“该降级”的阈值？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
