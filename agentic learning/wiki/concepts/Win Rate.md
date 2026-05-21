---
type: concept
topic:
  - evaluation
  - metric
status: growing
created: 2026-05-21
updated: 2026-05-21
last_checked: 2026-05-21
freshness: stable
conflicts: []
aliases:
  - 胜率
  - 胜率评估
  - Pairwise Win Rate
source:
  - "[[Evaluation 层次对比]]"
  - "[[raw/repos/agent_java_offer/questions/177 01_AI 06_评测与监控 在进行人工评估时，如何设计合理的评估准则和流程，以保证评估结果的客观性和一致性？]]"
evidence:
  - "[[Evaluation 层次对比#Win Rate vs Task Success Rate]]"
  - "[[Evaluation 层次对比#智能体评估体系组件图]]"
  - "[[raw/repos/agent_java_offer/questions/177 01_AI 06_评测与监控 在进行人工评估时，如何设计合理的评估准则和流程，以保证评估结果的客观性和一致性？#题目正文]]"
related:
  - "[[Evaluation]]"
  - "[[LLM-as-Judge]]"
  - "[[Task Success Rate]]"
  - "[[Eval Harness]]"
  - "[[Benchmark]]"
---

# Win Rate

## 一句话

Win Rate 是在同一批样本上比较两个版本、模型或输出时，统计 A 相对 B 胜出的比例；它回答“哪一个更好”，不直接回答“任务是否绝对完成”。

## 概念详解

Win Rate 出现在评测里，是因为很多 LLM / Agent 输出没有简单的标准答案。比如同一个问题，两个回答都部分正确，但一个更清晰、引用更稳、语气更合适，另一个更短但漏掉关键风险。此时用 exact match 或单个任务成功 checker 不一定能表达偏好差异，成对比较更自然：把 A 和 B 放在同一题、同一上下文、同一 rubric 下，让人类、规则或 [[LLM-as-Judge]] 判定 A 赢、B 赢或平局，再把结果汇总成胜率。

典型流程是：固定样本集，生成版本 A 和版本 B 的输出，打乱展示顺序，按 rubric 做 pairwise judgment，记录 Win / Loss / Tie，最后报告 A 的 win rate。Tie 的处理要事先说明：有的报告把 tie 排除在分母外，有的把 tie 记为 0.5 win，有的单独报告 tie rate。分母不同，胜率含义就会不同。

它的核心价值是比较改动方向：新 prompt 是否比旧 prompt 更好，新模型是否比旧模型更符合偏好，数据生成结果是否比 baseline 更可用。它尤其适合开放式输出、摘要、问答质量、数据生成质量、解释清晰度和人类偏好评估。

但 Win Rate 很容易被误读。它是相对指标，不是绝对正确率。A 赢过 B，可能只是 B 更差；两个版本都错时，A 仍然可能因为更流畅、更长或更讨 judge 喜欢而赢。对 Agent 系统来说，Win Rate 应该和 hard checker、[[Task Success Rate]]、trajectory / safety evaluation、人工校准和失败分类一起看。

## 它解决什么问题

Win Rate 解决的是开放式输出和版本比较中的相对偏好问题：

- 当没有唯一标准答案时，仍然可以比较哪个输出更符合 rubric。
- 当两个版本都不完美时，可以判断新版本是否整体更好。
- 当模型、prompt、RAG 策略或数据生成流程改动后，可以用相同样本集做 A/B 对比。
- 当人工绝对打分不稳定时，pairwise comparison 常比直接给 1-5 分更容易一致。

## 它不是什么

Win Rate 不是 [[Task Success Rate]]。Task Success Rate 问“任务是否成功完成”；Win Rate 问“两个候选里谁更好”。

它也不是 [[LLM-as-Judge]]。LLM-as-Judge 是产生判断的 evaluator；Win Rate 是把这些判断汇总后的指标。

它不是 [[Benchmark]]。Benchmark 定义任务集、运行协议和评分方式；Win Rate 只是可能出现在评估报告里的一个 metric。

它也不是事实正确性的保证。一个版本可以 win rate 高，但仍有 hallucination、越权工具调用、引用不支持结论或安全边界失败。

## 最小例子

```text
样本数: 100
比较对象: Prompt A vs Prompt B
裁判: 人工评审或 LLM Judge
结果:
  A wins: 55
  B wins: 30
  ties: 15

若 tie 排除:
  A win rate = 55 / (55 + 30) = 64.7%

若 tie 记 0.5:
  A win rate = (55 + 0.5 * 15) / 100 = 62.5%
```

报告里必须写清楚 tie 怎么算，否则两个 win rate 数字可能不可比。

## 常见误解 / 风险

- 误解：Win Rate 高说明答案正确。实际它只说明相对更偏好，不能替代事实校验。
- 误解：Win Rate 可以替代成功率。Agent 完成任务需要 checker；更受偏好的回答不等于任务完成。
- 误解：LLM Judge 给出的 win rate 天然客观。judge 可能偏好长回答、特定措辞、格式漂亮或与自己风格相似的输出。
- 风险：展示顺序会影响裁判。pairwise 评估通常要随机化 A/B 位置。
- 风险：样本分布会影响结论。简单题多会抬高 win rate，关键高风险题少会掩盖问题。
- 风险：tie 处理不透明会让报告难以复现。

## 边界细节

Win Rate 的最小边界是“同一输入上两个候选的相对比较”。它需要三个东西：成对样本、裁判或规则、汇总口径。没有 pairwise judgment，只报告平均分，不叫 Win Rate。

和相邻概念的区别：

- [[Task Success Rate]]：绝对任务完成比例。Win Rate 是相对偏好比例。
- [[LLM-as-Judge]]：评估器。Win Rate 是 judge、人类或规则 judgment 的汇总指标。
- [[Eval Harness]]：运行样本、收集输出、调用 scorer、保存报告的工程外壳。Win Rate 是 harness 可能产出的一个报告字段。
- [[Evaluation]]：更大的判断过程，包含任务、样本、规则、judge、人审、trace、报告和回归。Win Rate 只是其中一种指标。
- 人工验证：可以产生 Win/Loss/Tie，但人工验证也可以做绝对评分、冲突仲裁、rubric 校准和高风险审核。

从 taxonomy 看，本卡暂不写 `up`。虽然 Win Rate 明显属于 evaluation metric，但当前基线已经把 [[Task Success Rate]] 等指标类卡保持为 relation-only；后续如果建立稳定的 `Evaluation Metric` 父类，再通过 taxonomy 工具链统一处理。

## 现代性状态

- 判定：foundation / current-practice。
- 为什么：A/B、pairwise preference 和 win/loss/tie 汇总是评测中的稳定方法；LLM / Agent 时代让它更常和 [[LLM-as-Judge]]、人工偏好、数据生成质量和 prompt/model 版本对比结合。
- 稳定部分：必须固定样本、明确 rubric、记录裁判、处理 tie、报告分母。
- 易变部分：具体 judge 模型、pairwise prompt、去偏方法、在线 A/B 平台和报告口径会随平台变化。

## 现代系统怎么吸收 Win Rate 的价值 / 局限

现代系统通常把 Win Rate 放在 eval harness 或实验平台里：

- 离线比较 prompt / model / RAG 策略版本。
- 对开放式输出用 LLM judge 或人工评审生成 Win/Loss/Tie。
- 把 win rate 和 success rate、cost、latency、safety、citation faithfulness、trajectory evaluation 一起看。
- 对争议样本抽样人工复核，校准 judge 偏差。
- 把失败或低置信度 pair 写回 regression set，而不是只保留一个总胜率。

它的局限是：它比较的是两个候选之间的偏好，不保证任一候选足够好。对生产 Agent，硬约束仍然要用规则、测试、权限检查和人工审核守住。

## 证据锚点

- Topic synthesis: [[Evaluation 层次对比#Win Rate vs Task Success Rate]] 明确把 Win Rate 定义为 pairwise comparison metric，并和 [[Task Success Rate]] 切开。
- Diagram synthesis: [[Evaluation 层次对比#智能体评估体系组件图]] 把 LLM Judge、Win Rate 和人工验证放在数据生成质量评估的判定层，而不是 benchmark 层。
- Raw interview evidence: [[raw/repos/agent_java_offer/questions/177 01_AI 06_评测与监控 在进行人工评估时，如何设计合理的评估准则和流程，以保证评估结果的客观性和一致性？#题目正文]] 提到模型对比任务中成对比较通常比绝对打分更稳定。
- Evidence type: existing evaluation synthesis + interview raw source + engineering synthesis.
- Confidence: medium-high for metric boundary; medium for具体 tie 口径，因为不同平台/论文可能采用不同报告方式。
- Boundary: 本卡不追踪某个 leaderboard 的最新胜率；具体实验结果必须回到对应 source、样本集、judge prompt 和 tie 处理规则。

## 复习触发

- 为什么 Win Rate 高不等于任务成功率高？
- LLM-as-Judge 和 Win Rate 分别处在哪一层？
- 一个报告写 `A win rate = 65%` 时，你要追问哪些分母、tie 和 judge 细节？
- 如果两个版本都错，为什么其中一个仍可能赢？

## 相关链接

- [[Evaluation]]
- [[LLM-as-Judge]]
- [[Task Success Rate]]
- [[Eval Harness]]
- [[Benchmark]]
- [[Evaluation 层次对比]]
