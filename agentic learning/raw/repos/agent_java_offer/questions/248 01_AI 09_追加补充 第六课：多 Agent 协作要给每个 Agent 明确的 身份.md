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
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/09_%E8%BF%BD%E5%8A%A0%E8%A1%A5%E5%85%85/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/09_追加补充/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 09_追加补充
last_checked: 2026-05-09
freshness: watch
sha256: 7e72d69a1dd6a034df27eadcbb33c400d6534a19445f4da13966ff30f72339ac
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Memory]]"
  - "[[Context Engineering]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 第六课：多 Agent 协作要给每个 Agent 明确的"身份"

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/09_追加补充/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/09_%E8%BF%BD%E5%8A%A0%E8%A1%A5%E5%85%85/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `09_追加补充`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Memory]]
- [[Context Engineering]]
- [[Multi-agent Orchestration]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

### **第六课：[[Multi-agent Orchestration|多 Agent 协作]]要给每个 [[Agent]] 明确的"身份"**

Claude Code 在生成子 Agent 时，会往它的上下文里注入一段非常强硬的指令：你是一个工人，不是经理，不许再派活给别人，直接干，汇报结果不超过500字。防止这个子agent再无限生成它的子agent。

对我们的启示是：**在多 Agent 架构里，每个 Agent 的职责边界必须在设计阶段就写死，而不是靠它自己"聪明地"判断**。协调者就只协调，执行者就只执行.

---

围绕它的安全机制、[[Context Engineering|上下文管理]]、[[Memory|记忆系统]]、多 Agent 协调、提示词工程——这些"配套设施"才是决定产品能不能真正好用的关键。Claude Code 用 51 万行代码告诉了我们这个答案，而我们不需要重走一遍，直接拿来用就好。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
