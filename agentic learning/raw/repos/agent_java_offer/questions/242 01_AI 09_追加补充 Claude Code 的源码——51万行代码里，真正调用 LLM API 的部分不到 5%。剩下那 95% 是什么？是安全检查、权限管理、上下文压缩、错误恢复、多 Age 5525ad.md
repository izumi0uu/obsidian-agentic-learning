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
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/09_%E8%BF%BD%E5%8A%A0%E8%A1%A5%E5%85%85/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/09_追加补充/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "followup-question"
direction: "01_AI"
category: "09_追加补充"
last_checked: 2026-05-09
freshness: watch
sha256: f32912cfc788066f007be160e5ff88d3e6ebb300e1bd832b8275f03680933766
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Agent 主题]]"
---

# Claude Code 的源码——51万行代码里，真正调用 LLM API 的部分不到 5%。剩下那 95% 是什么？是安全检查、权限管理、上下文压缩、错误恢复、多 Agent 协调。

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/09_追加补充/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/09_%E8%BF%BD%E5%8A%A0%E8%A1%A5%E5%85%85/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `09_追加补充`  
条目类型：`followup-question`  
父级题组：第一课：agent的工程特别重要，不不光光全是模型的能力，工程设计也很重要。
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Multi-agent Orchestration]]
- [[Agent]]
- [[LLM]]
- [[Agent 主题]]

## 题目正文

追问题目：Claude Code 的源码——51万行代码里，真正调用 [[LLM]] API 的部分不到 5%。剩下那 95% 是什么？是安全检查、权限管理、上下文压缩、错误恢复、[[Multi-agent Orchestration|多 Agent]] 协调。

出现位置：第一课：[[Agent|agent]]的工程特别重要，不不光光全是模型的能力，工程设计也很重要。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
