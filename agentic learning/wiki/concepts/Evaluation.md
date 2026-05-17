---
type: concept
topic:
  - agent
  - evaluation
status: growing
created: 2026-05-05
updated: 2026-05-17
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[GAIA Benchmark]]"
  - "[[SWE-bench]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]"
evidence:
  - "[[GAIA Benchmark#为什么收]]"
  - "[[GAIA Benchmark#Ingest 摘要]]"
  - "[[SWE-bench#为什么收]]"
  - "[[SWE-bench#Ingest 摘要]]"
  - "[[LangSmith Evaluation and Observability#一句话]]"
  - "[[LangSmith Evaluation and Observability#边界提醒]]"
  - "[[Langfuse Observability and Evaluation#一句话]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]"
related:
  - "[[LLM Training Pipeline]]"
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Eval Harness]]"
  - "[[LLM-as-Judge]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
---

# Evaluation

## 一句话

Evaluation 是用任务、数据集、指标、规则、人工判断和回归流程来判断 LLM / Agent 系统是否真的有效、稳定、安全，而不只是“看起来回答得不错”。

## 概念详解

Evaluation 出现的原因很直接：LLM 和 Agent 很容易在单个 demo 里显得聪明，但在真实任务、边界输入和长期迭代中暴露不稳定。一次成功不能证明系统可靠，一次流畅回答也不能证明任务完成。Evaluation 要把“感觉不错”变成可复查的证据：任务是否完成、过程是否安全、失败模式是什么、改动后有没有回归。

从论文 benchmark 看，[[GAIA Benchmark]] 和 [[SWE-bench]] 分别代表两类重要评估思想。GAIA 的 source note 强调真实世界助手任务：问题常需要推理、多步处理、网页浏览、文件处理或工具使用，并且更关注最终短答案是否正确，而不是只测模型知识。它提醒我们：通用 assistant 的能力不能只用静态问答衡量，还要看是否能完成真实任务。SWE-bench 则把代码 Agent 的评估放进真实 GitHub issue、代码库快照、patch 和测试环境中；source note 明确说输出是 patch，评估依赖测试是否通过，特别是 fail-to-pass tests。它提醒我们：代码 Agent 不是“生成一段看起来合理的代码”，而是要在 repo context 中解决真实问题并通过验证。

从工程平台看，evaluation 不只是一个 benchmark 分数，而是一套闭环。[[LangSmith Evaluation and Observability]] 的 source note 把 trace、dataset、evaluator、experiment 和 production monitoring 组织成评测与观测闭环，并提醒“Observability 只说明发生了什么，evaluation 才判断好不好”。[[Langfuse Observability and Evaluation]] 则强调 trace、session、prompt management、evaluation、score 和 dashboard；它的边界提醒是：平台不是概念本身，真正要学习的是 trace -> score -> experiment -> regression 的工作流。

所以 Evaluation 至少有四层：第一层是任务定义，明确系统应该完成什么；第二层是数据 / 样例，包括 benchmark、业务样例、边界案例和回归集；第三层是判断方法，包括自动指标、规则检查、测试、[[LLM-as-Judge]]、人工审查和用户反馈；第四层是运行机制，也就是 [[Eval Harness]] 如何跑样例、记录 trace、比较版本、沉淀失败。缺一层就容易误判：只有数据没有指标，不知道怎么判；只有 judge 没有 trace，不知道为什么错；只有 benchmark 没有业务样例，可能优化错方向；只有一次人工验收，没有回归集，后续改动会悄悄退化。

对 Agent 来说，Evaluation 比普通文本任务更复杂，因为 Agent 不只输出文本，还会调用工具、检索知识、修改文件、浏览网页、请求审批。它既要评最终结果，也要评过程：有没有调用不该调用的工具，是否忽略 observation，是否陷入循环，是否泄露敏感数据，是否在低置信度时升级给人类。也因此，Evaluation 必须和 [[Trace]]、[[Observability]]、[[Agent Loop]]、[[Tool Calling]] 和 guardrails 连在一起。

如果系统支持 skill / `SKILL.md`，evaluation 还要覆盖“做事方法是否选对”。错误 skill 可能让 Agent 在形式上完成流程，却优化错目标、扩大权限或生成不可验证产物。模型自我反思可以作为诊断材料，但不能作为通过标准；通过标准应来自任务样例、权限检查、trace、产物验证、回归集或人审。

## 它解决什么问题

Evaluation 解决的是“系统是否真的可靠”的判断问题。没有 evaluation，团队只能靠主观体验：今天这个 prompt 看起来好，明天换个输入又坏了；一个模型分数高，但在自己的业务流程里失败；一次 demo 成功，但上线后遇到边界场景就崩。

它还解决迭代问题。每次改 prompt、换模型、加工具、改检索策略，都可能让某些旧能力退化。Evaluation 把重要案例变成回归集，让系统能回答“这次改动到底变好、变坏，还是只是看起来不同”。

## 它不是什么

Evaluation 不只是问模型“你觉得自己做得好吗”。自评可以作为辅助信号，但不能替代测试、规则、人审、用户反馈或任务结果。

Evaluation 也不等于 benchmark。Benchmark 是一组外部标准任务，适合横向比较；真实系统还需要业务样例、失败样本、边界案例、回归集和线上监控。

Evaluation 也不是 [[Eval Harness]] 本身。Evaluation 是判断目标和方法；Eval Harness 是把样例、运行、记录、评分、比较和报告组织起来的工程装置。

## 最小例子

如果我要评估一个 Obsidian 学习 Agent，可以准备这些测试：

- 它能否把新概念放进正确目录？
- 它能否给概念卡补充“它不是什么”和“概念详解”？
- 它能否避免重复创建同义笔记？
- 它能否指出回答依据来自哪篇 source note？
- 它能否在不确定或证据不足时提出问题，而不是编造？
- 它能否在一个看似相关但不适用的 skill 被触发时，拒绝扩大范围、切回正确流程，并留下验证证据？

最小 harness 可以是：固定 10 个任务样例，每个任务保存输入、预期行为、允许修改范围、验收规则、实际 diff、失败原因和复盘结论。随着失败被发现，把失败样本加入回归集。

## 常见误解 / 风险

- 误解：一个总分就能代表质量。风险是总分会掩盖失败模式，例如安全边界差、少数关键任务失败或过程不可审计。
- 误解：benchmark 高分等于产品可靠。风险是 benchmark 分布和真实业务任务不同。
- 误解：LLM-as-Judge 可以替代所有评估。风险是 judge 本身有偏差、漂移、上下文遗漏和不可复现问题。
- 风险：没有 trace 时，只知道错了，不知道错在检索、工具、推理、权限、状态还是输出格式。
- 风险：没有回归集时，每次优化都可能把旧能力悄悄破坏。
- 风险：只看 Agent 的自我反思，会把“解释得合理”误判成“流程真的正确”。这在错误 skill、诱导性工具描述和不适用 workflow 中尤其危险。

## 边界细节

Evaluation 的对象可以是模型、prompt、工具、RAG pipeline、完整 Agent workflow 或线上产品体验。对象不同，评估方式也不同：模型可以看标准题，RAG 要看检索和引用，代码 Agent 要看 patch 和测试，工具型 Agent 要看 action 是否正确和安全。

和相邻概念的区别：

- [[Benchmark]] 是外部或固定任务集；Evaluation 是更大的判断过程。
- [[Task Success Rate]] 是一个指标；Evaluation 还要解释为什么成功或失败。
- [[LLM-as-Judge]] 是一种评估器；Evaluation 还可以包含规则、测试、人审和业务指标。
- [[Eval Harness]] 是运行和记录评估的工程系统；Evaluation 是判断目标、样例和标准。
- [[Observability]] 说明发生了什么；Evaluation 判断这件事好不好。

一个细边界：对 Agent，最终答案正确但过程危险，也不能算完全通过。例如答案对了，但它越权读取文件、泄露私密信息或绕过审批，这属于安全/过程评估失败。

另一个细边界：Agent 自称“这个 skill 适合”不等于 evaluation 通过。skill selection 需要单独评估，包括触发条件是否正确、是否遵守上级规则、是否使用允许工具、是否产生可审计 trace，以及最终产物是否满足任务验收。

## 现代性状态

- 判定：foundation / current-practice / frontier-adjacent
- 为什么：测试、实验设计和质量控制是基础地基；Agent/RAG/LLM 应用中的 dataset、trace、judge、online/offline eval、regression eval 是当前工程实践；具体 eval 平台、指标、judge prompt 和 agentic benchmark 仍在快速变化。
- 稳定部分：必须定义任务、样例、判断标准和复查机制。
- 易变部分：具体 benchmark、评测平台、judge 模型、评分 rubric、线上监控方式。
- 复查点：当新增主流 benchmark、平台能力或 Agent trace/eval 标准改变时，优先更新 [[Eval Harness]]、[[LLM-as-Judge]]、[[Trajectory Evaluation]] 和相关 source note。

## 现代系统怎么吸收 Evaluation 的价值 / 局限

现代系统通常把 evaluation 接进开发和上线流程：

- 在开发阶段，用离线 dataset / regression suite 比较 prompt、模型、工具或 RAG 改动。
- 在运行阶段，用 trace、user feedback、manual labeling、online score 发现线上失败。
- 在发布阶段，把关键 eval 接入 CI、发布门禁或人工 review。
- 在复盘阶段，把失败 trace 转成新样例，加入回归集。

Evaluation 的局限是：它永远只能覆盖一部分任务分布。benchmark 可能被刷分，judge 可能漂移，业务样例可能过窄，人工审查可能不一致。因此现代系统需要多种信号组合，而不是迷信单一指标。

## 证据锚点

- Paper benchmark source: [[GAIA Benchmark]]
- Anchors: [[GAIA Benchmark#为什么收]], [[GAIA Benchmark#Ingest 摘要]]
- Paper benchmark source: [[SWE-bench]]
- Anchors: [[SWE-bench#为什么收]], [[SWE-bench#Ingest 摘要]]
- Official/community practice sources: [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]], [[OpenAI - A Practical Guide to Building Agents]]
- Anchors: [[LangSmith Evaluation and Observability#一句话]], [[LangSmith Evaluation and Observability#边界提醒]], [[Langfuse Observability and Evaluation#一句话]]
- Skill registry source: [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]
- Evidence type: benchmark paper source notes + official/community platform docs + engineering synthesis.
- Confidence: medium
- Boundary: GAIA/SWE-bench 支持“真实任务/patch/tests”评估思路；LangSmith/Langfuse 支持 trace/dataset/evaluator/score/monitoring 的工程闭环；“四层 Evaluation 结构”是本 vault 的工程综合理解。

## 复习触发

- 为什么单个 benchmark 分数不足以代表 evaluation？
- Observability、Trace、Eval Harness、LLM-as-Judge 和 Evaluation 分别负责什么？
- 如果一个 Agent 最终答案正确，但越权调用了工具，evaluation 应该怎么判？
- 为什么“Agent 反思说自己选对了 skill”不能替代 skill selection evaluation？

## 相关链接

- [[Agent]]
- [[LLM Training Pipeline]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[RAG]]
- [[Memory]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Eval Harness]]
- [[LLM-as-Judge]]
- [[Trace]]
- [[Observability]]
