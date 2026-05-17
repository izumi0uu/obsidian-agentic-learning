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
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 01_Agent基础
last_checked: 2026-05-09
freshness: watch
sha256: 6f0d07892d03a6f883b89b7fa46af3c2f43ef944d8595679df1b25bee30b4ee7
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[ReAct]]"
  - "[[Planning]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[Tool Calling]]"
  - "[[Durable Execution]]"
  - "[[Agent 主题]]"
---

# 请详细解释 [[ReAct]] 框架。它是如何将思维链和行动结合起来，以完成复杂任务的？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[ReAct]]
- [[Planning]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Agent Loop]]
- [[Agent]]
- [[Tool Calling]]
- [[Durable Execution]]
- [[Agent 主题]]

## 题目正文

### 2. 子问题：请详细解释 ReAct 框架。它是如何将思维链和行动结合起来，以完成复杂任务的？

答：
ReAct 的本质是把“推理”和“行动”交替执行，形成 Thought-Action-Observation 的循环。模型先思考下一步，再[[Tool Calling|调用工具]]，再根据返回结果调整策略，直到任务完成。它相比静态 CoT 的优势是可交互、可纠错、可解释，适合信息不完整或环境会变化的任务；代价是链路更长，线上要控制步数、超时和成本。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
