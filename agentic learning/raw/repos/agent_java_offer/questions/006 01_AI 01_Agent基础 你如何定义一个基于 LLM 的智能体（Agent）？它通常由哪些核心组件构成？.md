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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "01_Agent基础"
last_checked: 2026-05-09
freshness: watch
sha256: b76968998c8e937cad042bb80f064900418352984651c0a681c9fbae33b67f0b
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Planning]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Agent 主题]]"
---

# 你如何定义一个基于 LLM 的智能体（Agent）？它通常由哪些核心组件构成？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Memory]]
- [[Agent State]]
- [[Planning]]
- [[Agent Loop]]
- [[Agent]]
- [[LLM]]
- [[Agent 主题]]

## 题目正文

### 2. 子问题：你如何定义一个基于 LLM 的智能体（Agent）？它通常由哪些核心组件构成？

答：
我会把 Agent 定义为“以 LLM 为决策大脑、能在环境中持续闭环执行任务的系统”。与普通问答不同，它具备自主性和循环性。核心组件可讲四层：规划模块、记忆模块、工具模块，再加上底层 LLM 本身。面试时建议强调：真正拉开差距的是工程控制面，比如状态管理、异常恢复和可观测性。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
