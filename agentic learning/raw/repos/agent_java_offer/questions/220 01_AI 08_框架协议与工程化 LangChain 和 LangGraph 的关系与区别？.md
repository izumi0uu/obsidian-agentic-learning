---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - framework
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 08_框架协议与工程化
last_checked: 2026-05-09
freshness: watch
sha256: e833c4f7c99a4cbda2d48240fb52a4c6ffdba27b7ddcdc1ddc5df8580f79f5a0
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Retriever]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Agent Framework]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
---

# LangChain 和 LangGraph 的关系与区别？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Retriever]]
- [[Agent State]]
- [[Agent Workflow]]
- [[Agent Framework]]
- [[Durable Execution]]
- [[Agent]]

## 题目正文

### 5. 子问题：LangChain 和 LangGraph 的关系与区别？

答：
LangChain 更偏组件库和表达式编排（Prompt、Model、[[Retriever]]、Tools、Runnable），适合快速搭建链路。LangGraph 是面向有状态、多步骤、[[Durable Execution|可恢复]]任务的[[Agent Workflow|图编排]]框架，适合 [[Agent]] 工作流。两者不是替代关系，常见是用 LangChain 组件 + LangGraph 做状态机编排。

追问：什么时候必须从 LangChain Chain 升级到 LangGraph 图？

当流程从‘线性调用’变成‘有状态、有分支、可恢复、可治理’时，Chain 的表达力就不够了，这时候就该升级到 LangGraph 图。

## 3. 主干问题：LangGraph 生产治理要关注什么？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
