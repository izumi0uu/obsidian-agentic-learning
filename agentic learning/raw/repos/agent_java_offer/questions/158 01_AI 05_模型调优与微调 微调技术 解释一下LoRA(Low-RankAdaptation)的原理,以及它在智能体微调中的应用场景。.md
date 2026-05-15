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
sha256: 67bc8f1f0468de565320b66333c51da8bf044d9a0046304618e25a17a140574e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[RAG]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agent]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[LLM 主题]]"
---

# 微调技术:解释一下LoRA(Low-RankAdaptation)的原理,以及它在[[Agent|智能体]]微调中的应用场景。

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `05_模型调优与微调`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[RAG]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Agent]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[LLM 主题]]

## 题目正文

### 32.微调技术:解释一下LoRA(Low-RankAdaptation)的原理,以及它在智能体微调中的应用场景。

LoRA 的核心是：不改[[LLM|大模型]]原参数，只学一个“低秩增量”。
LoRA适合“行为和表达对齐”，不适合“实时知识更新”；

在智能体微调里的常见应用场景：
[[Tool Calling|工具调用]]格式稳定化：让模型更稳定地产生 JSON / function call。
角色风格一致化：如客服、投研、写作助手的语气和输出结构。
领域术语适配：金融、法律、医疗等垂类表达更专业。
多租户个性化：每个客户挂不同 LoRA adapter，而不是训多套大模型。

## 4. 补充原问：前沿论文与 [[RAG]]/Agent 工程启发

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
