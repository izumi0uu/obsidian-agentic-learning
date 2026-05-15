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
sha256: 6261b8bf013c5d0de656f891763d2c9aae893d515faa5cf79c6f886769034b0f
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Agent State]]"
  - "[[ReAct]]"
  - "[[Planning]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[Durable Execution]]"
  - "[[Observation]]"
  - "[[Evaluation]]"
  - "[[Agent 主题]]"
---

# 当一个 Agent 需要在真实或模拟环境中（如机器人、游戏）执行任务时，它与纯粹基于软件工具的 Agent 有什么本质区别？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[Agent State]]
- [[ReAct]]
- [[Planning]]
- [[Agent Loop]]
- [[Agent]]
- [[Durable Execution]]
- [[Observation]]
- [[Evaluation]]
- [[Agent 主题]]

## 题目正文

### 3. 子问题：当一个 Agent 需要在真实或模拟环境中（如机器人、游戏）执行任务时，它与纯粹基于软件工具的 Agent 有什么本质区别？

答：
当Agent从纯粹的软件环境（调用API、读写文件）进入到真实或模拟的物理环境（如机器人、游戏）时，我们称之为**具身智能体（Embodied Agent）**。这种转变引入了几个本质的区别，极大地增加了任务的复杂性。

核心区别是“感知与行动的不确定性”。软件 Agent 处理的是结构化、可控接口；具身或仿真 Agent 面对的是高维噪声输入、部分可观测状态和连续动作误差，且需要实时闭环。更关键的是安全后果：软件错误多数可回滚，物理动作可能不可逆。因此评估标准会从“答对”升级为“安全、稳定、可恢复”。

## 2. 主干问题：ReAct 是什么，Agent 的规划能力怎么设计？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
