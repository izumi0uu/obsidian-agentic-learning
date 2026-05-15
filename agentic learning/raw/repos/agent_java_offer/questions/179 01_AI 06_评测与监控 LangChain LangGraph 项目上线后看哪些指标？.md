---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "evaluation"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "06_评测与监控"
last_checked: 2026-05-09
freshness: watch
sha256: f737a38d23d0d8db69188bf667909a1b27a5ccf9399b77948bcb8a8e3945973e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Retriever]]"
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
---

# LangChain / LangGraph 项目上线后看哪些指标？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `06_评测与监控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Retriever]]
- [[Agent Framework]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Agent]]

## 题目正文

### 1. 子问题：LangChain / LangGraph 项目上线后看哪些指标？

答：
我会分四类看：[[Task Success Rate|任务成功率]]（业务结果）、链路稳定性（错误率/重试率/中断率）、性能与成本（p95 时延、token 成本）、质量指标（幻觉率、格式通过率、人工接管率）。没有这套指标，就无法判断是模型问题还是编排问题。

追问：如果成功率下降，你会按什么顺序定位是 Prompt、检索、工具还是[[Agent Workflow|图编排]]的问题？

我按图编排→工具→检索→Prompt 的顺序做漏斗定位，先看编排流程收敛和可用性，再看语义质量，用固定回放集和分层指标做归因，

1. **图编排层（先查）**

看 `loop_ratestep_count_p95timeout_rateretry_rate`。

如果步数暴涨、回环增多、超时增多，优先判定是路由/终止条件问题。

1. **工具层**

看工具 `success_rate5xx/429schema校验失败率p95延迟`。

如果调用失败或慢，是工具可用性/契约问题。

1. **检索层**

看 `hit@k/recall@k`、空召回率、过滤后命中率、索引新鲜度。

如果召回质量掉了，答案成功率会同步下降，即使 Prompt 不变。

1. **Prompt 层（最后查）**

在“同一检索结果 + 同一工具返回”下做 Prompt A/B。

若前面都正常但输出格式、拒答边界、推理稳定性变差，才定位为 Prompt 回归。

**症状到根因的速判**

- 步数/超时突然上升：图编排
- 工具报错和慢调用上升：工具
- 空召回或错召回上升：检索
- 链路都健康但答案质量掉：Prompt

## 2. 补充原问：Agent 好坏如何评价？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
