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
sha256: ddb60f43ba25fa2c846c854d163af16eed88bce716a99bb47252a81b2d4a596e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[A2A]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Framework]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 了解 A2A 框架吗？它和普通 Agent 框架的区别在哪，挑一个最关键的不同点说明。

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[A2A]]
- [[Multi-agent Orchestration]]
- [[Agent Framework]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

### 4. 子问题：了解 A2A 框架吗？它和普通 Agent 框架的区别在哪，挑一个最关键的不同点说明。

答：
A2A（Agent-to-Agent）最关键在“协议层”, A2A是一个通讯协议，类似于HTTP那样的底层协议，它关注的是**多个异构Agent之间的通信和协作**。它试图定义一套**通用的标准、协议和语言**，使得由不同开发者、使用不同技术栈、为了不同目标而构建的Agent们，能够相互发现、理解和协作。

 一句话总结：前者解决“群体协作标准”，后者解决“个体执行能力”。多团队、多技术栈协作时，A2A 的价值会明显放大。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
