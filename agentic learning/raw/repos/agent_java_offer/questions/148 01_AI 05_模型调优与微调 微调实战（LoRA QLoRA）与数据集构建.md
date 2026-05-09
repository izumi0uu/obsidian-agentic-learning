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
sha256: 7f23733d0c6f5e4693d2a446be4af562ca99c8e2e336cce4f4a581766e68578a
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Retriever]]"
  - "[[RAG]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[LLM 主题]]"
---

# 微调实战（LoRA/QLoRA）与数据集构建

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `05_模型调优与微调`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Retriever]]
- [[RAG]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[LLM 主题]]

## 题目正文

### 1. 子问题：微调实战（LoRA/QLoRA）与数据集构建

主问题：LoRA/QLoRA 的原理、流程和上线方法是什么？

口述答案：
LoRA 通过低秩适配器在冻结基座模型下训练，QLoRA 进一步量化基座参数以降低显存成本，适合资源受限下快速迭代。实战里我更关注数据质量：覆盖真实失败样本、边界样本、格式样本；再配合离线评测、线上灰度和可回滚机制。微调不是万能药，若问题本质是检索错召回，先优化 RAG 往往更有效。

常见追问：

1. QLoRA 省资源的代价是什么？
2. 训练数据多少条才有意义？
3. 微调后效果变差怎么排查与回滚？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
