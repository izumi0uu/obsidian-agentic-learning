---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - llm-training
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/05_%E6%A8%A1%E5%9E%8B%E8%B0%83%E4%BC%98%E4%B8%8E%E5%BE%AE%E8%B0%83/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/05_模型调优与微调/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 05_模型调优与微调
last_checked: 2026-05-09
freshness: watch
sha256: 2dbe327073a8abdf7c2f9c3210dabe0faa298952610900db9c640c4559058e63
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[RAG]]"
  - "[[Agent]]"
  - "[[LLM Training Pipeline]]"
  - "[[LLM]]"
  - "[[Durable Execution]]"
  - "[[Observability]]"
  - "[[LLM 主题]]"
---

# 熟悉模型微调（LoRA / QLoRA）流程吗？

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
- [[RAG]]
- [[Agent]]
- [[LLM Training Pipeline]]
- [[LLM]]
- [[Durable Execution]]
- [[Observability]]
- [[LLM 主题]]

## 题目正文

### 3. 子问题：熟悉模型微调（LoRA / QLoRA）流程吗？

答：
 LoRA/QLoRA 作为低成本模型微调行为的手段。

LoRA是在冻结基座模型参数前提下训练低秩适配器，QLoRA进一步把基座模型做4-bit量化，显著降低显存和训练成本。LoRA做的是模型输出行为和风格稳定性和一致性

落地时我会先定义验收指标，再做高质量数据构建，尤其补齐线上失败样本；训练阶段重点调 target modules 和 rank 等关键参数；[[Evaluation|评估]]不只看任务指标，还看安全和回归；上线采用灰度A/B和可回滚策略。

微调收益主要由数据质量和评估体系决定，如果这两块不扎实，微调很容易出现局部提升但整体退化

问：训练数据要多少才有意义？

答：没有绝对值，关键是“高质量+覆盖失败样本”；常见从几千到几万条高质量指令数据起步。

问：[[RAG]] 和 LoRA 怎么分工？

答：RAG解决“事实与时效”，LoRA解决“行为与风格”；通常先做RAG，再用LoRA补稳定性和格式一致性。

追问：QLoRA 为什么更省资源？主要代价是什么？

答: QLoRA进一步把基座模型做4-bit量化，显著降低显存和训练成本

## 3. 补充原问：LoRA 在 [[Agent]] 微调中的应用

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
