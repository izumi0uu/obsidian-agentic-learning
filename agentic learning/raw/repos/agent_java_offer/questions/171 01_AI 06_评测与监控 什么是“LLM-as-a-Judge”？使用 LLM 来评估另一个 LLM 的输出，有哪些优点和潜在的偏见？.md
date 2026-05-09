---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "evaluation"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "06_评测与监控"
last_checked: 2026-05-09
freshness: watch
sha256: 303fe2879e60eea035e7285858754f7f1c8c64be12090764e8f25bb21a8305b4
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[LLM-as-Judge]]"
  - "[[Evaluation]]"
  - "[[LLM]]"
---

# 什么是“LLM-as-a-Judge”？使用 LLM 来评估另一个 LLM 的输出，有哪些优点和潜在的偏见？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `06_评测与监控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[LLM-as-Judge]]
- [[Evaluation]]
- [[LLM]]

## 题目正文

### 4. 子问题：什么是“LLM-as-a-Judge”？使用 LLM 来评估另一个 LLM 的输出，有哪些优点和潜在的偏见？

答：
LLM-as-a-Judge 是用强模型按预设 Rubric 去评估候选模型输出，优点是快、可规模化、口径相对统一。风险在于偏见：位置偏好、冗长偏好、风格偏好，以及裁判模型自身知识错误。实践上一般配“自动评审+人工抽检”，并做双盲与顺序打乱，减少系统性偏差。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
