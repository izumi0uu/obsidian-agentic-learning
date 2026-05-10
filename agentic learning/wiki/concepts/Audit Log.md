---
type: concept
topic:
  - observability
  - security
  - evaluation
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Policy Engine]]"
  - "[[Tool Permissioning]]"
---

# Audit Log

## 一句话

Audit Log 是为安全、合规和复盘保存的 Agent 行动记录：它记录谁在什么时候让系统做了什么、用到哪些权限、是否经过批准、结果是什么。

## 概念详解

Audit Log 出现的原因，是 Agent 不再只是生成文本，而会调用工具、访问数据、修改代码、发送消息或触发外部系统。只要系统能行动，就需要一份能在事后回答“发生过什么”的记录。对学习者来说，它是理解生产 Agent 边界的一个重要信号：真正上线的 Agent 不只需要能力，还需要可追责性。

它通常记录关键动作，而不是每个 token：用户、会话、agent、工具名、动作类型、参数摘要、权限来源、审批人或审批策略、结果、失败原因、风险等级、时间戳和关联 trace id。这样在事故复盘、合规审查、权限争议或安全事件中，可以从审计日志回到对应 [[Trace]]，再看更细的 span、prompt、工具返回和状态变化。

边界在于：Audit Log 的目标不是调试体验最丰富，而是可靠、可查、防篡改、可按权限读取。它经常需要比普通 trace 更长的保留期、更严格的访问控制和更少的敏感原文暴露。


一个实用判断是：如果 trace 像“黑匣子飞行记录”，Audit Log 更像“监管可读的关键动作账本”。它不必保存所有中间 token，却必须在关键边界上说清楚：谁授权、系统依据什么策略行动、动作影响了什么资源、失败后有没有回滚或升级。这个差异会直接影响字段设计：trace 可以为开发者优化，audit log 必须为安全、合规、争议处理和长期责任链优化。

审计日志还会影响用户信任：当用户问“为什么系统替我做了这个动作”时，团队不能只回答模型当时这么判断，而要拿出可读、可验证、权限明确的行动记录。

## 它解决什么问题

Agent 调用了什么工具、访问了什么数据、谁批准了高风险动作、输出了什么结果，都需要事后可查。否则出错后无法定位责任和根因。

对 evaluation harness 来说，Audit Log 还能把“评测时系统是否遵守权限和确认流程”变成可检查证据，而不是只看最终答案。

## 它不是什么

Audit Log 不等于完整 [[Trace]]。

Trace 偏调试和观测，可能包含详细 prompt、token、工具返回和中间状态；Audit Log 更偏合规和关键动作记录。Trace 可以很细，Audit Log 要能长期保存、审计和授权读取。

Audit Log 也不是 [[Observability]] 平台本身。Observability 负责实时观察、分析和告警；Audit Log 是其中面向责任、合规和安全复盘的一类证据。

## 最小例子

```text
time, user, agent, tool, action, parameters_summary, approval, result, risk_level, trace_id
2026-05-10T09:30Z, ida, coding-agent, git, commit, "3 files", human-approved, success, medium, tr_123
```

如果 Agent 删除了文件，audit log 应该能看到删除动作、触发者、被删路径摘要、是否经过确认、结果和关联 trace。

## 常见误解和风险

- 记录太少无法审计：只写“工具调用成功”没有参数摘要、用户、审批和结果，事后很难判断是否越权。
- 记录太多可能泄露敏感数据：把完整 prompt、密钥、个人数据或业务数据写入长期审计日志，会制造新的安全风险。
- 审计日志本身要防篡改和控制访问，否则攻击者可以先越权，再删除证据。
- “有 audit log”不代表系统安全；它只是事后可查，还需要 [[Tool Permissioning]]、policy engine、approval gate 和告警。

## 边界细节

Audit Log 和相邻概念可以这样切开：

- [[Trace]]：适合调试和评测，保存过程细节；Audit Log 保存关键行动证据。
- [[Observability]]：适合实时看系统健康、错误、成本和延迟；Audit Log 适合责任链和合规复盘。
- [[Policy Engine]] / [[Tool Permissioning]]：运行时决定能不能做；Audit Log 记录做没做、谁批准、结果如何。
- Evaluation harness：可以读取 audit log 检查“高风险动作是否经过确认”“是否访问了禁止数据”，但评测判断本身不等于日志。

设计审计日志时，最重要的边界不是“字段越全越好”，而是“足够追责，同时不把敏感内容长期暴露”。

## 现代性状态

- 判定：current-practice。
- 为什么：审计日志是安全和合规系统的稳定基础；在 Agent 场景中，它被重新用于工具调用、权限确认、数据访问和自动化行动的可追责记录。
- 稳定部分：关键动作、权限、审批、结果和关联 trace id 需要被记录。
- 易变部分：具体字段、脱敏策略、保留周期和平台集成会随产品、法规和组织安全要求变化。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#为什么收]]
- Evidence type: source note + security/observability engineering synthesis.
- Confidence: medium
- Boundary: 审计日志的稳定核心是可追责行动记录；具体字段、保留期、防篡改实现和合规要求属于组织/产品层决策。

## 复习触发

- 为什么 Audit Log 不能直接替代 [[Trace]]？
- 如果一个 Agent 发送外部邮件，audit log 至少应该记录哪些字段？
- “记录越多越安全”错在哪里？

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Policy Engine]]
- [[Tool Permissioning]]
