---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "memory"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "04_上下文工程与记忆"
last_checked: 2026-05-09
freshness: watch
sha256: a35bfdcc228398d37e090bd373adcd908063de63f763238384605bc0bd729d22
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Agent State]]"
  - "[[Context Engineering]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[Tool Calling]]"
  - "[[Observation]]"
  - "[[Planning]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[Prompt]]"
  - "[[Agent 主题]]"
---

# rag和agent的prompt有什么区别，分为哪些部分，如何和ai交流的

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Trace]]
- [[Observability]]
- [[RAG]]
- [[Memory]]
- [[Agent State]]
- [[Context Engineering]]
- [[Durable Execution]]
- [[Agent]]
- [[Tool Calling]]
- [[Observation]]
- [[Planning]]
- [[RAG Citation Faithfulness]]
- [[Prompt]]
- [[Agent 主题]]

## 题目正文

### 1. 子问题：rag和agent的prompt有什么区别，分为哪些部分，如何和ai交流的

**口述答案（约300字）**：
RAG Prompt和Agent Prompt的目标不一样。RAG Prompt核心是“基于给定证据回答”，强调引用、边界和事实一致性；Agent Prompt核心是“驱动任务执行”，强调计划、工具选择、状态推进和失败处理。结构上我常用六段式：角色、任务、上下文、约束、示例、输出格式。RAG里上下文段最重，通常要求“仅依据检索片段回答，缺失就明确说不知道”；Agent里工具规范最重，要明确何时调用工具、入参格式、异常分支和停止条件。和模型交流时我会坚持两点：第一，结构化输入输出，比如JSON schema，减少歧义；第二，把策略写成可观测规则，比如“最多重试2次，超过则降级”。这样能把“提示词”从文案变成“可执行协议”，便于调试和复盘。
**来源**：公开社区资料

## 6. 补充原问：长期/短期记忆差异

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
