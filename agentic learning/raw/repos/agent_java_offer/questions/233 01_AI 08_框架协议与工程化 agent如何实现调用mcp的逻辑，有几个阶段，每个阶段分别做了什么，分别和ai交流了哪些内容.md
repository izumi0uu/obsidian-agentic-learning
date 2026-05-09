---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "framework"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "08_框架协议与工程化"
last_checked: 2026-05-09
freshness: watch
sha256: c453ed791290ad2417bd3957ec4efd80e02ef44f5c0094922312ae2b2dedd1b7
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Agent State]]"
  - "[[MCP]]"
  - "[[Tool Calling]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[Agent Framework]]"
---

# agent如何实现调用mcp的逻辑，有几个阶段，每个阶段分别做了什么，分别和ai交流了哪些内容

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]
- [[Agent State]]
- [[MCP]]
- [[Tool Calling]]
- [[Durable Execution]]
- [[Agent]]
- [[Agent Framework]]

## 题目正文

### 1. 子问题：agent如何实现调用mcp的逻辑，有几个阶段，每个阶段分别做了什么，分别和ai交流了哪些内容

**口述答案（约300字）**：
我一般拆成四个阶段。第一阶段是工具发现：通过MCP拿到可用工具清单和schema，告诉模型“有哪些能力可选”。第二阶段是工具决策：模型根据当前任务状态输出调用意图，包含工具名、参数和预期结果。第三阶段是执行与回填：运行工具，拿到结果或错误码，把结果标准化写回状态。第四阶段是结果吸收：模型读取工具结果，决定继续调用、改计划还是结束。和AI交流的内容分别是：工具目录、调用规范、执行结果和下一步策略。工程上我会补三点：参数校验、防越权和幂等。参数校验防止模型传错字段；防越权通过白名单和权限上下文控制；幂等保证重试不产生重复副作用。这样MCP不是“能调工具”，而是“可控、可审计、可恢复”地调工具。
**来源**：公开社区资料

## 5. 补充问：MCP 解决什么问题

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
