---
type: concept
topic:
  - evaluation
  - llm
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[LangSmith Evaluation and Observability#先读什么]]"
  - "[[LangSmith Evaluation and Observability#一句话]]"
  - "[[Langfuse Observability and Evaluation#为什么收]]"
  - "[[Langfuse Observability and Evaluation#先读什么]]"
  - "[[Langfuse Observability and Evaluation#一句话]]"
related:
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
---

# LLM-as-Judge

## 一句话

LLM-as-Judge 是用另一个模型或同类模型作为评估器，对输出、引用、格式或过程进行评分。

## 概念详解

LLM-as-Judge 出现的背景是：很多 LLM / Agent 输出很难只靠精确匹配或单元测试判断。摘要是否忠实、回答是否有帮助、概念卡解释是否清楚、RAG 引用是否真的支持答案、Agent 计划是否合理，这些任务带有语义性和主观性。如果完全依赖人工审查，成本高、速度慢；如果只用规则，又会漏掉语义质量。LLM-as-Judge 就是把一部分人工 rubric 判断转成模型辅助评分。

从机制上看，judge 至少需要四个部件：被评估对象、rubric、judge prompt / evaluator 配置、以及结果记录。Rubric 要说明什么叫好，例如忠实性、完整性、格式、引用支持、风险边界、是否遵循任务。Judge prompt 把 rubric 交给裁判模型，并要求它输出分数、标签、理由或结构化 JSON。结果记录要保存 judge 模型、prompt 版本、样例版本、输入输出和评分理由，方便复查和回归比较。没有 rubric 和版本记录的 judge，只是“再问一个模型怎么看”，可复现性很弱。

[[LangSmith Evaluation and Observability]] 的 source note 在 evaluators 中列出 human review、code rules、LLM-as-judge、trajectory evaluator；[[Langfuse Observability and Evaluation]] 的 source note 把 LLM-as-judge、user feedback、manual labeling、custom evals 放在 evaluation 视角下，并用 score 把判断绑定到 trace、observation、session 或 dataset run。这些来源支持一个关键边界：LLM-as-Judge 是 evaluator 家族中的一种，不是 [[Evaluation]] 的全部，更不是事实真理。

它的价值在于规模化语义检查：可以快速筛出可能不忠实、缺引用、格式差、解释不足或过程异常的样本；也可以在没有标准答案时给出弱监督信号。但风险同样明显：judge 会偏好流畅和长回答，可能受被评内容诱导，可能对不同表达不一致，可能随模型版本漂移，也可能把敏感 trace 发给外部模型。高风险场景必须用规则、测试、人工、业务指标和安全策略共同校准。

现代系统吸收 LLM-as-Judge 的方式，通常不是让它“拍板”，而是把它放进 eval harness 作为一个可版本化 scorer：规则能判的先用规则，代码能跑测试的先跑测试，引用能校验的做引用支持检查，主观语义再交给 judge 辅助；线上 judge 结果进入 score / monitoring，异常样本抽样给人类复核。证据边界：LangSmith / Langfuse source notes 支持 LLM-as-judge 作为 evaluator / score 工作流的一部分；偏差、漂移、隐私和校准这些风险来自本 vault 对评测实践的工程综合。

## 它解决什么问题

很多 Agent 任务没有简单的标准答案，比如“总结是否忠实”“回答是否有帮助”“计划是否合理”。LLM-as-Judge 能把一部分主观评估自动化。

## 它不是什么

LLM-as-Judge 不是绝对裁判。

它会有偏差、漂移、被 prompt 影响，也可能被被评估内容诱导。高风险任务仍需要规则、人工和真实业务指标。

## 最小例子

评估一张概念卡：

- 是否有“一句话”。
- 是否说明“它不是什么”。
- 例子是否最小。
- 是否把 raw source 和 wiki synthesis 混在一起。

其中结构项可用规则，解释质量可用 LLM-as-Judge 辅助。

## 常见误解 / 风险 / 边界细节

- 裁判模型也需要校准和评估。
- 评分 prompt 应该版本化。
- 不要把敏感 trace 原样发给外部裁判模型。
- 最好保留 rationale 或标签，方便人工复查。

## 边界细节

- LLM-as-Judge 适合做弱监督、批量筛查和辅助评分，不适合当唯一真理。
- 如果任务有明确规则，优先规则判定；如果涉及主观质量，再用 judge 辅助。
- judge 结果要当成“可疑信号”而不是最终裁定。

## 现代性状态

- 基础地基：自动评分思想来自测试、rubric 和人工审查流程。
- 当前工程实践：现代评测系统常把 judge 作为 rubric-backed evaluator 的一部分，而不是单独使用。
- 前沿 / 易变：具体 judge 模型、prompt、guardrail 和隐私处理方式变化快，应单独跟踪 `freshness`。

## 证据锚点

- Platform / community-practice sources: [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]]
- Anchors: [[LangSmith Evaluation and Observability#先读什么]], [[LangSmith Evaluation and Observability#一句话]], [[Langfuse Observability and Evaluation#先读什么]], [[Langfuse Observability and Evaluation#一句话]]
- Evidence type: evaluation platform source notes + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 LLM-as-judge 作为 evaluator / score 工作流的一部分；judge 偏差、漂移、隐私和校准策略是工程实践综合，不是单一来源原文定义。

## 复习触发

- 什么时候应该用规则而不是 judge？
- judge 为什么需要版本化和校准？
- 哪些内容不适合送给外部 judge 模型？

## 相关链接

- [[Evaluation]]
- [[Eval Harness]]
- [[Trajectory Evaluation]]
- [[Observability]]
