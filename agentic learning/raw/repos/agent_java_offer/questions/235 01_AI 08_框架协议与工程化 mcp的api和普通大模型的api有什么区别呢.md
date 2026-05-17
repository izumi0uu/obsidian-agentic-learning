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
sha256: 1143c2cf063e798d747688a7f11c084630574c4c6ec4d4cb284c62747e022f2a
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[MCP]]"
  - "[[LLM]]"
  - "[[Agent Framework]]"
---

# mcp的api和普通[[LLM|大模型]]的api有什么区别呢

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]
- [[Tool Calling]]
- [[Tool Use]]
- [[MCP]]
- [[LLM]]
- [[Agent Framework]]

## 题目正文

### 1. 子问题：mcp的api和普通大模型的api有什么区别呢

**口述答案（约300字）**：
普通大模型API本质是“输入文本，输出文本”；[[MCP]] API是“输入任务上下文，输出可执行工具行为”。区别可以从三点说。第一，交互对象不同：普通API主要和模型交互，MCP还要和工具生态交互。第二，数据结构不同：普通API重点是prompt和response，MCP强调工具schema、参数校验、执行结果和错误码。第三，工程目标不同：普通API追求回答质量，MCP追求“可执行性+可治理性”。在面试里我会补一句：两者不是替代关系，而是组合关系。常见模式是模型负责决策，MCP负责执行和回填。这样可以把模型能力延伸到真实系统，同时保持安全边界和审计能力。落地时建议把[[Tool Calling|工具调用]]封成统一执行器，避免业务代码里散落调用逻辑。
**来源**：公开社区资料

## 7. 补充问：SSE 原理与作用

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
