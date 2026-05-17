---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - framework
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 08_框架协议与工程化
last_checked: 2026-05-09
freshness: watch
sha256: b52717c2a4c4d99af2d8a9c0fba710fcb98ead5f50932ca919edd4b3861540f9
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
  - "[[Approval Gate]]"
  - "[[Guardrails]]"
  - "[[Human-in-the-loop]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Durable Execution]]"
---

# 工具调用与可靠性治理（Function Calling）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Least Privilege Tools]]
- [[Tool Permissioning]]
- [[Approval Gate]]
- [[Guardrails]]
- [[Human-in-the-loop]]
- [[Audit Log]]
- [[Trace]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Durable Execution]]

## 题目正文

### 1. 子问题：工具调用与可靠性治理（[[Tool Calling|Function Calling]]）

主问题：LLM 如何调用工具？怎么把工具链路做稳？

口述答案：  
Function Calling 的本质是让模型在结构化工具说明书, 描述约束下输出“调用意图 + 参数”，由编排层真实执行并回填结果。要从“会调”走向“稳调”，需要三层治理：输入层做 schema 校验与默认值补齐，调用层做超时、重试、熔断、并发限额，结果层做幂等键、去重与统一错误码。重试策略要区分可重试和不可重试错误，避免高危写操作被重复执行。

常见追问：

1. 读接口和写接口重试策略怎么区分？
2. 如何避免工具调用越权？
  1. **[[Least Privilege Tools|最小权限]] + 白名单**
    当前任务必需工具，不给全量工具；每个工具用短期、范围受限的凭证（按用户/会话绑定）。
  2. **调用前二次鉴权（服务端强校验）**
    说“要调用”不算数，服务端必须再校验：角色权限、资源归属、参数是否合法（如 userId 只能操作自己的数据）。
  3. **高风险动作强制[[Approval Gate|人工确认]] + 可追溯**
    息、下单、删改数据这类动作必须 [[Human-in-the-loop|HITL]]；全链路[[Audit Log|审计日志]]+告警+一键熔断，异常时立刻停调用。
3. 工具故障时如何降级不拖垮主链路？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
