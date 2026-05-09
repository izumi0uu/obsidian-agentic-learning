---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "framework"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "08_框架协议与工程化"
last_checked: 2026-05-09
freshness: watch
sha256: 0297a40373dbc747e48129509a11f5fccc776e793f0e098799ca99a300928659
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
---

# 为什么选择 Spring AI 框架？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Tool Calling]]
- [[Tool Use]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent]]

## 题目正文

### 1. 子问题：为什么选择 Spring AI 框架？

**口述答案（约300字）**：
我选择Spring AI主要是基于团队技术栈和工程效率。第一，它和Spring生态天然兼容，依赖注入、配置管理、监控链路都能复用，接入成本低。第二，它对模型调用、Prompt模板、向量存储、工具调用有统一抽象，能减少重复造轮子。第三，对Java后端团队友好，便于把AI能力和原有业务服务做一体化部署与治理。它不是唯一选择，LangChain/LangGraph在Agent编排上生态更活跃；但在我们场景里，Spring AI让“后端工程规范+AI能力”结合更顺滑。我的选型原则是：先看团队熟练度和交付周期，再看框架能力边界，必要时允许混合方案而不是框架宗教。
**来源**：公开社区资料

## 10. 补充问：多模型支持架构如何设计

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
