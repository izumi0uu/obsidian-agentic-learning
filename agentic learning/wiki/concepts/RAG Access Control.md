---
type: concept
topic:
  - rag
  - security
  - retrieval
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: watch
source:
  - "[[Microsoft RAG 官方文档]]"
  - "[[OWASP LLM Top 10 2025]]"
  - "[[OWASP Agentic Applications Top 10]]"
  - "[[Data Exfiltration]]"
evidence:
  - "[[Microsoft RAG 官方文档#一句话]]"
  - "[[Microsoft RAG 官方文档#我的疑问]]"
  - "[[OWASP LLM Top 10 2025#为什么收]]"
  - "[[OWASP Agentic Applications Top 10#边界提醒]]"
  - "[[Data Exfiltration#边界细节]]"
related:
  - "[[RAG]]"
  - "[[Tool Permissioning]]"
  - "[[Least Privilege Tools]]"
  - "[[Data Exfiltration]]"
  - "[[Indirect Prompt Injection]]"
---

# RAG Access Control

## 一句话

RAG Access Control 是在检索、上下文装配和输出前确保用户只能看到授权资料的治理边界；它不是生成后把敏感词遮掉。

## 概念详解

企业或团队 RAG 的风险不只是“答错”，还包括把用户无权访问的文档检索进上下文。只要模型看到了无权限资料，即使最终回答被过滤，系统内部也已经越过了知识边界；如果 trace、日志或工具参数保存了这些内容，还会扩大泄露面。

RAG Access Control 的关键是把权限作为 retrieval pipeline 的一等约束：ingestion 时保存文档 owner、tenant、classification、ACL、过期状态；检索时在召回前或召回中应用权限过滤；上下文装配时再次检查 source metadata；输出和日志层限制敏感内容外流。[[Microsoft RAG 官方文档]] 的 source note 已把企业 RAG 边界扩展到数据治理、索引策略、检索质量、权限和评估。OWASP 与 [[Data Exfiltration]] 相关卡则说明，一旦 Agent / RAG 能读私有资料，就必须同时考虑输出通道、工具调用和审计。

工程综合：RAG Access Control 是 [[Tool Permissioning]] 在知识检索层的对应物。工具权限限制“能做什么动作”，RAG 权限限制“能看什么证据”。两者都应该遵循最小权限，而不是让模型自行判断哪些资料应该忽略。

一个可靠的 RAG 权限设计不能只在最终答案阶段做过滤，因为模型看到未授权上下文本身就是越权。更稳的做法是在 ingestion、index、retriever、reranker、context assembly、logging 和 citation 层都保留权限约束：哪些文档可被召回、哪些片段可进入 prompt、哪些 trace 可以被谁查看。这样才能避免“检索正确但治理失败”的情况。
## 它解决什么问题

它解决多用户、多租户、企业文档和私有知识库里的越权检索问题：用户问一个普通问题时，retriever 不应把他无权看的合同、邮件、代码或客户数据放进上下文。

## 它不是什么

它不是只在最终答案上做脱敏。

它也不是 prompt 里写“不要泄露秘密”。权限必须进入索引、filter、retriever、context assembly、日志和审计层。

## 最小例子

```text
用户 A 查询 "本季度合同风险"
retriever filter: tenant=A.company AND document_acl contains user_A
只召回用户 A 有权看的合同 chunk
```

如果系统先全库检索再让模型“不要说无权限内容”，就是错误边界。

## 常见误解 / 风险

- 误解：生成后过滤就够了。模型和日志可能已经接触敏感资料。
- 误解：向量相似度检索天然尊重权限。向量库/索引需要显式 metadata filter 或隔离策略。
- 风险：chunk 继承权限错误，导致父文档权限丢失。
- 风险：多源检索合并时，某个数据源漏做权限过滤。
- 风险：trace / eval dataset 把敏感 chunk 保存成长期样本。

## 边界细节

和 [[Data Exfiltration]] 的边界：access control 是预防控制；data exfiltration 是越界泄露的结果风险。

和 [[Indirect Prompt Injection]] 的边界：间接注入可能诱导模型请求或泄露无权限资料；access control 应让模型即使被诱导也无法检索到这些资料。

和 [[RAG Evaluation]] 的边界：权限错误也应进入 RAG eval / audit，不只是安全团队的问题。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：RAG 必须在知识检索层尊重权限、租户和数据分类。
- 易变部分：具体向量库 filter、enterprise search ACL、日志脱敏、policy engine 和云产品能力会变化。
- 复查点：新增数据源时，要重新确认权限 metadata 是否在 ingestion、index、retriever 和 trace 中完整传播。

## 现代系统怎么吸收 RAG Access Control 的价值 / 局限

现代系统会把 access control 做成检索前置约束：索引按租户/权限隔离，retriever 查询带 metadata filter，context builder 二次校验，audit log 记录用户、source、chunk ID 和权限判断。对高风险数据，还会把 RAG 与 [[Policy Engine]]、[[Approval Gate]] 或人工审批结合。

局限是权限治理依赖上游数据质量：如果 ingestion 没有保存 ACL，后面很难补救。权限也不是一次性配置，文档共享、员工离职、项目归档和法律保留都会改变可见范围。

## 证据锚点

- Source anchor: [[Microsoft RAG 官方文档#一句话]]
- Source anchor: [[Microsoft RAG 官方文档#我的疑问]]
- Source anchor: [[OWASP LLM Top 10 2025#为什么收]]
- Source anchor: [[OWASP Agentic Applications Top 10#边界提醒]]
- Concept anchor: [[Data Exfiltration#边界细节]]
- Evidence type: official RAG source note + OWASP security source notes + engineering synthesis.

- Boundary: RAG Access Control 管知识访问边界，不等于 prompt injection 防御、普通 authentication，也不等于回答质量评估。
## 复习触发

1. 为什么 RAG 权限过滤应该发生在检索前或检索中，而不是生成后？
2. chunk 的权限应该从哪里来？如果父文档权限丢了会怎样？
3. RAG Access Control 和 Tool Permissioning 的类比是什么？

## 相关链接

- [[RAG]]
- [[RAG 可靠性与治理对比]]
- [[Data Exfiltration]]
- [[Tool Permissioning]]
- [[Least Privilege Tools]]
- [[Indirect Prompt Injection]]
