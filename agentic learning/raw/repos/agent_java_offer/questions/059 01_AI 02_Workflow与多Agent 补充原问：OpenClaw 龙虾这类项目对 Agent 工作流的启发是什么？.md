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
sha256: 66accb98f6e43916c23b4699658ef41048c0e277c621626d84f5267cbae7d33a
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Long-term Memory]]"
  - "[[Memory]]"
  - "[[Agent Workflow]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 补充原问：OpenClaw/龙虾这类项目对 Agent 工作流的启发是什么？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/02_Workflow与多Agent/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/02_Workflow%E4%B8%8E%E5%A4%9AAgent/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `02_Workflow与多Agent`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]
- [[Long-term Memory]]
- [[Memory]]
- [[Agent Workflow]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

## 7. 补充原问：OpenClaw/龙虾这类项目对 Agent 工作流的启发是什么？

### 39.openclaw龙虾对agent技术的启发

第一，Gateway统一网关入口，跨渠道消息先标准化，再路由，避免每个渠道各写一套逻辑。
第二，会话隔离不串台：sessionKey、dmScope、每会话串行执行和队列并发上限，核心是防串台、防并发写冲突。
第三，三层记忆系统: “文件化+可检索”的，MEMORY.md 做长期记忆，memory/*.md 做日记忆，配 memory_search，可追溯、可审计。
第四，可托管运行：有心跳机制，保证龙虾会主动的思考工作。以及有定时任务块机制，确保周期任务统一调度。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
