---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "security"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/07_%E5%AE%89%E5%85%A8%E4%B8%8E%E9%A3%8E%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/07_安全与风控/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "07_安全与风控"
last_checked: 2026-05-09
freshness: watch
sha256: ca790ba5e58a6bef6fece6684cee9fc074118b758cb6aab8cee4ffaaef071a1e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Sandbox Workspace]]"
  - "[[Code Execution Sandbox]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Guardrails]]"
---

# Human-in-the-loop 在 LangGraph 怎么落地？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/07_安全与风控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/07_%E5%AE%89%E5%85%A8%E4%B8%8E%E9%A3%8E%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `07_安全与风控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Sandbox Workspace]]
- [[Code Execution Sandbox]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Guardrails]]

## 题目正文

### 4. 子问题：[[Human-in-the-loop]] 在 LangGraph 怎么落地？

答：
我会在关键节点使用 interrupt 或审批节点，让系统在“高风险动作前”暂停，等待[[Approval Gate|人工确认]]后继续。典型场景是资金操作、批量发送、生产变更。这样保留自动化效率，同时把不可逆动作的最终控制权交给人。

## 2. 补充材料：为什么需要执行沙箱

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
