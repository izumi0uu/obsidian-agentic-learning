---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - evaluation
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 06_评测与监控
last_checked: 2026-05-09
freshness: watch
sha256: 45fa5ae11b202e7b15df9085ee5704f6d4b7d9510dadaf07568037b319f4ff9c
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent State]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Agent Robustness]]"
---

# 评估一个 Agent 为什么比评估一个基础 LLM 更加困难和复杂？评估的维度有哪些不同？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `06_评测与监控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent State]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Agent]]
- [[LLM]]
- [[Agent Robustness]]

## 题目正文

### 6. 子问题：[[Evaluation|评估]]一个 [[Agent]] 为什么比评估一个基础 [[LLM]] 更加困难和复杂？评估的维度有哪些不同？

答：
基础 LLM 多是单轮“输入-输出”评估，而 Agent 是多步交互系统，过程会影响结果，状态也持续变化，所以复杂度高很多。除了结果正确性，还要评估步骤效率、[[Tool Calling|工具调用]]质量、异常恢复能力、成本和时延。对LLM的评估更像是“**产品质量检测**”，而对Agent的评估更像是“**路况复杂的真实驾驶测试**”，不仅要看是否到达终点，更要看驾驶过程中的效率、安全性和应对突发状况的能力。

**评估维度的不同：**


| **评估维度**    | **基础 LLM**                                                                        | **Agent**                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **核心评估对象**  | **单个回答的质量** (Quality of a single response)                                        | **整个任务完成过程** (The entire task completion process)                                                                                                             |
| **主要维度**    | - **准确性 (Accuracy)** - **流畅性 (Fluency)** - **相关性 (Relevance)** - **安全性 (Safety)** | - **任务成功率 ([[Task Success Rate]]):** 能否最终完成目标？ - **效率 (Efficiency):** 完成任务花了多少资源？（见下文） - **鲁棒性 (Robustness):** 能否处理异常和错误？ - **自主性 (Autonomy):** 在没有人类干预的情况下能走多远？  |
| **新增的过程维度** | (无)                                                                               | - **成本 (Cost):** LLM调用次数、API费用、Token消耗。 - **延迟 (Latency):** 完成任务的总时间。 - **步骤数 (Number of Steps):** 任务分解和执行的步数。 - **纠错能力 (Error Recovery):** 从工具报错或错误状态中恢复的能力。 |
| **评估方法**    | 静态数据集上的[[Benchmark|基准测试]] (MMLU, HumanEval)                                                     | **交互式环境**中的基准测试 (WebArena, AgentBench)                                                                                                                        |

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
