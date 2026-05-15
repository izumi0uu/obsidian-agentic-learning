---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "memory"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "04_上下文工程与记忆"
last_checked: 2026-05-09
freshness: watch
sha256: 505e74be46fe212f5f3ada2ce77a2bb0915f5d69facb9db112c6fc04982cc6c7
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[RAG]]"
  - "[[Context Engineering]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[Agent]]"
  - "[[Durable Execution]]"
  - "[[Agent Workflow]]"
  - "[[Prompt]]"
  - "[[Agent 主题]]"
---

# [[Prompt]] Engineering 和微调策略如何协同？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[RAG]]
- [[Context Engineering]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[Agent]]
- [[Durable Execution]]
- [[Agent Workflow]]
- [[Prompt]]
- [[Agent 主题]]

## 题目正文

### 4. 子问题：Prompt Engineering 和微调策略如何协同？

答：
两者不是替代关系。Prompt 负责一次交互的快速约束行为和流程编排，微调负责模型长期固化能力与风格稳定。常见策略是“Prompt 先行、微调收口”：先用 Prompt 把问题定义清楚并沉淀失败样本，再用微调提升一致性和吞吐效率。

追问：如果微调后效果变差，你会按什么顺序回滚和排查？

微调劣化我会先回滚模型流量止损，优先卸载新 LoRA adapter；再按数据、训练、评测、服务四层做对照排查，最后用小流量灰度和自动回切机制重放上线。

- **数据层**：标注噪声、分布漂移、重复/污染、样本冲突。
- **训练层**：学习率过大、epoch 过多、过拟合、LoRA rank/alpha 不合理。
- **评测层**：离线集不代表线上，评测泄漏或口径错误。
- **系统层**：其实是 [[RAG]]/工具链路变了，不是微调本身问题。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
