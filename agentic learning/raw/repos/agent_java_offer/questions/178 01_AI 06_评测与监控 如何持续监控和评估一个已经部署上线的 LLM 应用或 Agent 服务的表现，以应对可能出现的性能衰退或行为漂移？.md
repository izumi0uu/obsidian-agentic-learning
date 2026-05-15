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
sha256: c17caf6ebf9519dac20243390ac04e46a64ae00eb821518b505920228f3b65d5
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
---

# 如何持续监控和评估一个已经部署上线的 LLM 应用或 Agent 服务的表现，以应对可能出现的性能衰退或行为漂移？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/06_评测与监控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/06_%E8%AF%84%E6%B5%8B%E4%B8%8E%E7%9B%91%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `06_评测与监控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Agent Loop]]
- [[Agent]]

## 题目正文

### 10. 子问题：如何持续[[Observability|监控]]和评估一个已经部署上线的 LLM 应用或 [[Agent]] 服务的表现，以应对可能出现的性能衰退或行为漂移？

答：

一个完整的监控[[Evaluation|评估体系]]应包含以下几个层面：

1. **采集和监控（Automated Monitoring）：**

- 采集和监控指标，包括一次请求完整的所有的交互的数据，包括用户的输入、模型的中间思考过程、最终的输出以及调用的工具、延迟以及 token 的消耗等等。
- 很重要的一点就是用户的反馈，在产品的界面中嵌入一些用户反馈机制，比如说顶踩的按钮/打分和一些意见反馈等等。
- 还有一些间接指标: 输出指标中回答的长度、代码块的比例、JSON 格式错误率、拒绝回答率等，以及过程指标，agent的执行过程中的平均步数、[[Tool Calling|工具调用]]频率、工具调用失败率这些。

**2. 审核与分析（Review and Analysis）：**

- **自动化质量评估：**一个是用程序定期的抽样，从生产流量中随机抽取一小部分的样本，来做评估。还有一个思路就是用一个更强大的裁判的大模型，根据一套评估的准则，以及是否有害，是否跑题，对抽样样本进行自动打分。还有就将抽样样本与内户维护的一个高质量的一个黄金评估机进行对比，看模型在这些关键问题上的表现是否稳定。
- **定期人工审计：** 定期组织运营或评估团队，对生产环境中的随机样本、用户反馈的坏案例、以及自动化监控发现的异常案例进行深入的人工分析。

**3. 反馈闭环与模型迭代（Feedback Loop and Model Iteration）：**

- 将生产环境中发现的有价值的案例，特别是失败案例和用户不喜欢的案例，清洗标注后，持续的加入到评估集和微调数据集中，定期的进行模型的再训练和微调，以适应新的数据分布和用户需求，然后再上线新版本的 时候，注意用 AB 测试框架，小流量验证新版本是否优于旧版本，确定每次迭代都是正向的。

通过建立这样一个“**采集/监控 -> 分析 -> 迭代**”的闭环，我们可以主动地管理和维护线上服务的质量，而不是被动地等待用户投诉。

---

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
