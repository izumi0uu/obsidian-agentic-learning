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
sha256: c52de5bbc40c0abcc0c07a9548dfddbebea2bc25eaa1dbb53945ac7601801698
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Planning]]"
  - "[[Agent]]"
---

# 评估指标:如何评估一个AlAgent的好坏?除了准确率,还会关注哪些指标(如推理速度、成本、幻觉率)

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
- [[Planning]]
- [[Agent]]

## 题目正文

### 1.[[Evaluation|评估指标]]:如何评估一个AlAgent的好坏?除了准确率,还会关注哪些指标(如推理速度、成本、幻觉率)

效率层面的一个指标，一个是托管的费用以及调用外国 API 的费用。还有一个是系统完成一次任务的整体耗时，以及推理任务，推理执行任务的一个步骤数。
还有一个是鲁棒性层面的指标。就是说系统在调用工具，工具会出现一些异常超时或者返回信息不符合预期的时候，系统会怎么样？思考推理进行下一步的动作。以及当外界条件出现一些噪声的时候，这个系统的[[Task Success Rate|成功率]]是否会保持在一个比较稳定的水平？
还有个是自主性，人工干预次数: 一个是看这个系统有运行一个复杂任务时候，人工介入的一个情况。行为可解释性:还有一个是人工的去看这个系统整个的推理思考过程，它是不是符合逻辑。计划偏离度:还有一个思路就是这个系统如果是先[[Planning|规划]]后执行，可以它执行的步骤和它，看看是否按它的，完全按它的规划来，还是有所偏离。

## 4. 补充原问：意图识别准确率如何定义与计算？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
