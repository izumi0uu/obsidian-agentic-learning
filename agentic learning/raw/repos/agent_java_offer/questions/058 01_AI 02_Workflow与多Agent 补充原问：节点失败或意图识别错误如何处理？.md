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
entry_type: "supplement-section"
direction: "01_AI"
category: "02_Workflow与多Agent"
last_checked: 2026-05-09
freshness: watch
sha256: 96e265cc6c5bf3a4c9da9890d97bfba0a88534f3cfe8e6a28833a3d2c4387a79
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Reflexion]]"
  - "[[Memory Reflection]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 补充原问：节点失败或意图识别错误如何处理？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Reflexion]]
- [[Memory Reflection]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

## 6. 补充原问：节点失败或意图识别错误如何处理？

### 32.agent项目如果某个节点失败会怎么样，意图识别错了会怎么样

如果某个节点失败会怎么样
每个节点都有超时 + 最大次数，超过就走失败分支/降级路径/人工介入节点。
做错误分级：可重试（超时、429、临时网络）和不可重试（参数错、权限错、业务校验失败）。
用 checkpoint + 幂等键 保证断点恢复时不重复副作用（不重复下单/发消息）。

如果意图识别错了会怎么样
意图识别完之后，会先走一层校验层，或者说风险控制层。如果是高风险的意图，必须二次确认。然后在执行过程中可以做一致性校验。如果检索后工具返回的与意图不一致，要触发路由，要触发进行反思。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
