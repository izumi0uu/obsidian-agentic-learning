---
type: map
topic:
  - rag
  - evaluation
  - security
  - governance
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-12
source:
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[RAG Access Control]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[OWASP LLM Top 10 2025]]"
  - "[[OWASP Agentic Applications Top 10]]"
evidence:
  - "[[RAG Evaluation#证据锚点]]"
  - "[[RAG Citation Faithfulness#证据锚点]]"
  - "[[RAG Access Control#证据锚点]]"
  - "[[Data Exfiltration#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[RAG]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[RAG Access Control]]"
  - "[[Trace]]"
---

# RAG 可靠性与治理对比

## 一句话总览

RAG 可靠性与治理不是单一指标，而是一组跨越 **检索质量、上下文装配、答案忠实度、引用支持、权限过滤、审计追踪** 的控制点：[[RAG Evaluation]] 判断系统是否答得好，[[RAG Citation Faithfulness]] 判断“引用是否真的支持结论”，[[RAG Access Control]] 判断“用户是否只检索到自己有权看的资料”。

最小边界：可靠性偏“答案是否基于正确证据”；治理偏“证据是否可访问、可审计、可回滚、可解释”。两者相互依赖，但不能互相替代。

## 为什么这组值得对比

这组概念容易混，因为生产 RAG 的失败经常表现成同一个表面症状：答案看起来合理，但其实可能是检索漏召回、上下文污染、引用不支持、权限泄漏或生成幻觉。只说“RAG 不准”会遮住真正故障点。

值得单独对比的原因：

- [[RAG Evaluation]] 是诊断框架，关注 retrieval / context / generation / citation 分层。
- [[RAG Citation Faithfulness]] 是更窄的忠实度切口，关注答案句子与引用证据之间的支持关系。
- [[RAG Access Control]] 是安全和合规切口，关注资料在检索前、中、后是否被正确过滤和审计。
- [[Trace]]、[[Observability]]、[[Audit Log]] 让这些判断可复现，而不是只靠一次人工读答案。

## 共同问题域

共同问题域是“外部知识进入模型上下文后，系统怎样证明它该被使用、被正确使用、只被授权使用”。它覆盖三条链：

```text
knowledge quality -> retrieval/context quality -> answer faithfulness
permission model  -> pre-retrieval filtering -> leakage prevention
runtime evidence  -> trace/audit/eval sample -> regression monitoring
```

## 核心区别表

| 概念 | 主要问法 | 介入位置 | 典型输入/输出 | 证据锚点 |
|---|---|---|---|---|
| [[RAG Evaluation]] | RAG 错在检索、上下文、引用还是生成？ | 离线评估、回归测试、线上抽样 | query、候选文档、上下文、答案、评分/标签 | [[RAG Evaluation#证据锚点]] |
| [[RAG Citation Faithfulness]] | 每个结论是否被它引用的 chunk 支持？ | 答案生成后、citation 校验、人工抽样 | answer sentence、citation、support/contradict/insufficient 判断 | [[RAG Citation Faithfulness#证据锚点]] |
| [[RAG Access Control]] | 用户是否只能检索和看到授权资料？ | ingestion metadata、retriever filter、post-check、audit | user/tenant/role、document ACL、filter、审计记录 | [[RAG Access Control#证据锚点]] |
| [[Data Exfiltration]] | 系统是否把不该泄漏的数据带出边界？ | tool/RAG/context/output 全链路 | 敏感字段、外发通道、policy decision | [[Data Exfiltration#证据锚点]] |
| [[Trace]] / [[Audit Log]] | 这次回答的证据路径能否复现？ | runtime 观测与责任记录 | spans、retrieval samples、tool calls、权限决策 | [[Trace#证据锚点]], [[Audit Log#证据锚点]] |

## 最容易混淆的边界

### RAG Evaluation vs Citation Faithfulness

[[RAG Evaluation]] 是整体诊断框架，可以评估召回、上下文质量、答案正确性和引用质量；[[RAG Citation Faithfulness]] 是其中一个更细的判断：**引用是否足以支持答案中的具体结论**。一个系统可能整体命中正确文档，但 citation 仍然不忠实。

### Citation Faithfulness vs Hallucination

[[Hallucination]] 描述模型输出与事实或证据不一致的结果；citation faithfulness 是面向 RAG 的证据支持检查。没有引用的回答也可能幻觉；有引用的回答也可能因为引用不支持结论而不 faithful。

### Access Control vs Guardrails

[[RAG Access Control]] 应优先在检索前和索引层执行权限过滤；[[Guardrails]] 更像输出、策略和行为约束层。只在生成后做遮盖，不等于权限安全，因为模型上下文里可能已经看到了不该看的内容。

### Audit Log vs Trace

[[Trace]] 偏调试和性能/质量复现，记录一次运行的检索、工具、上下文和模型调用；[[Audit Log]] 偏责任和合规，记录谁在何时访问了什么、做了什么决策。两者可以共享数据，但审计语义更严格。

## 执行时序 / 机制差异

```text
1. ingest: 文档解析、chunk、metadata、ACL、版本
2. retrieve: query rewrite/planning、metadata/ACL filter、hybrid search、rerank
3. assemble: 去重、上下文预算、引用标识、prompt 注入隔离
4. generate: 基于证据回答，保留 citation
5. verify: faithfulness、answer correctness、policy check
6. observe: trace、eval dataset、audit log、回归样本
```

关键边界：权限和敏感信息过滤越靠前越安全；faithfulness 和 answer quality 越靠近输出越容易检查语义，但不能补救前面已经泄漏的上下文。

## 现代系统如何吸收或限制

现代 RAG 平台通常把可靠性拆成评估集、trace、feedback、LLM-as-judge、人工抽样和回归测试；把治理拆成 metadata/ACL filter、tenant isolation、policy engine、audit log、PII/secret scanning 和 least privilege。这里的现代性状态是 **current-practice + frontier/watch**：评估和权限过滤是当前生产实践；自动 faithfulness judge、跨工具数据外泄检测和多租户 Agentic RAG 治理仍在快速演化。

工程综合 / inference：越是 agentic retrieval，多轮查询、工具调用和跨源综合越需要把每次检索、过滤、引用和模型判断写进 trace，否则错因会从“某个 top-k 不准”扩散成“整个 loop 不可解释”。

## 什么时候用哪个判断

- 答案事实错：先看 [[RAG Evaluation]]，分检索、上下文、生成、引用定位。
- 答案有引用但引用看不出支持结论：看 [[RAG Citation Faithfulness]]。
- 用户可能看到跨租户、跨角色或付费墙资料：看 [[RAG Access Control]] 和 [[Data Exfiltration]]。
- 线上偶发、难复现：补 [[Trace]]、[[Observability]] 和 eval sample capture。
- 合规、责任和事故复盘：补 [[Audit Log]]，不要只保留调试日志。

## 它们共同不是什么

- 不是“把 top-k 调大”就能解决的参数问题。
- 不是只靠更强模型就能解决的推理问题。
- 不是 citation 一出现就表示证据充分。
- 不是 guardrail 可以替代权限模型。
- 不是一次离线 benchmark 可以覆盖所有线上泄漏和过期索引风险。

## 证据锚点

- 概念卡：[[RAG Evaluation#证据锚点]], [[RAG Citation Faithfulness#证据锚点]], [[RAG Access Control#证据锚点]], [[Data Exfiltration#证据锚点]], [[Trace#证据锚点]], [[Audit Log#证据锚点]]。
- source notes：[[Microsoft RAG 官方文档]], [[OWASP LLM Top 10 2025]], [[OWASP Agentic Applications Top 10]], [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]]。
- 证据边界：本页的层次表和时序图是基于上述卡片的工程综合 / inference；具体产品能力、API 字段和安全清单需要按 source note 的 `last_checked` 复查。

## 复习触发

1. 一个 RAG 答案带了引用但仍然错，你如何区分 retrieval failure、citation unfaithfulness 和 hallucination？
2. 为什么权限过滤应该尽量发生在检索前，而不是等模型生成后再遮盖？
3. 如果线上只保存最终答案，没有保存检索候选和权限决策，哪类故障会不可复现？

## 相关链接

- [[RAG 主题]]
- [[RAG]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[RAG Access Control]]
- [[Hallucination]]
- [[Data Exfiltration]]
- [[Guardrails]]
- [[Trace]]
- [[Audit Log]]
