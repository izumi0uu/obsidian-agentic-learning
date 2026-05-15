---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "llm-training"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "05_模型调优与微调"
last_checked: 2026-05-09
freshness: watch
sha256: d84845609abb276c09e0c6a85b70ab043b508298d329235c02cb3c00a84a921e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[LLM 主题]]"
---

# [[LLM]]基础原理与后训练体系（SFT/RLHF/DPO）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `05_模型调优与微调`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[LLM Training Pipeline]]
- [[LLM]]
- [[LLM 主题]]

## 题目正文

### 1. 子问题：LLM基础原理与后训练体系（SFT/RLHF/DPO）

主问题：如何向面试官讲清 LLM 基础原理和后训练流程？

口述答案：
我会用三段讲：第一，预训练让模型学“语言与知识分布”；第二，SFT 让模型学“按指令回答”；第三，偏好对齐（RLHF/DPO）让模型更符合人类偏好与安全要求。RLHF 经典链路是 SFT -> 奖励模型 -> PPO；DPO 去掉了显式 RL 环节，训练更稳更轻。面试里关键是讲清“各阶段解决的问题不同”，而不是只背名词。

常见追问：

1. PPO 为什么难、DPO 为什么流行？
2. 后训练和微调是什么关系？
3. 没做过 RLHF，怎么讲不露怯？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
