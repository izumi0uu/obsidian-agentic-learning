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
sha256: 3b908ab9d759fe44e888e4939128d6c5d012ba39d53a3cc031597df01bcd311c
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Permissioning]]"
  - "[[Approval Gate]]"
  - "[[Guardrails]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[MCP]]"
---

# 一个普通的api，如何把他mcp化

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
- [[Trace]]
- [[Observability]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[MCP]]

## 题目正文

### 1. 子问题：一个普通的api，如何把他mcp化

**口述答案（约300字）**：
把普通API做成[[MCP]]，我会按“包装、约束、观测”三步走。第一步包装：把原API能力抽象成工具，定义清晰的输入输出schema，包括必填项、类型、枚举和错误码。第二步约束：加[[Tool Permissioning|权限控制]]、参数校验和幂等键，明确哪些场景可调用、谁可调用、失败如何处理。第三步观测：接入日志和指标，至少要能看调用[[Task Success Rate|成功率]]、P95时延、错误分布和重试次数。然后把工具描述注册到MCP Server，模型就能发现并调用。上线前我会做两类测试：契约测试保证schema不破，回放测试保证关键case稳定。这样“mcp化”不只是加一层协议，而是把接口变成可被模型稳定消费的标准能力。
**来源**：公开社区资料

## 9. 补充问：为什么选 Spring AI

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
