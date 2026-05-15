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
sha256: ef853c4efdb23e35558fb81347a16e8d8539d16309b15b8dfc4815b97f3c9586
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Transformer]]"
  - "[[LLM]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM 主题]]"
---

# 14 TensorFlow 和 Transformer 架构 是啥关系啊

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `05_模型调优与微调`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Transformer]]
- [[LLM]]
- [[LLM Training Pipeline]]
- [[LLM 主题]]

## 题目正文

### 2.14 TensorFlow 和 [[Transformer]] 架构 是啥关系啊

两者是“框架”和“模型架构”的关系：
- TensorFlow：深度学习框架（训练 / 推理工具链）；
- Transformer：神经网络架构（模型怎么设计）。

TensorFlow 是工程平台，Transformer 是算法结构；前者解决“怎么高效训练和上线”，后者定义模型内部计算方式（如自注意力）。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
