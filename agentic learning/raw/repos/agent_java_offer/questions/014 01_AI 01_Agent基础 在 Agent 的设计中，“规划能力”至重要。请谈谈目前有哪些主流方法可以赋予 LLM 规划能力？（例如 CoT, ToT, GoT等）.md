---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "01_Agent基础"
last_checked: 2026-05-09
freshness: watch
sha256: 3ec932c806f6b4f4d7164f84cc52da61513978e25a9172fe00a2a589e1b63a05
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Planning]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Agent Loop]]"
  - "[[Agent 主题]]"
---

# 在 [[Agent]] 的设计中，“[[Planning|规划]]能力”至重要。请谈谈目前有哪些主流方法可以赋予 [[LLM]] 规划能力？（例如 CoT, ToT, GoT等）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Planning]]
- [[Agent]]
- [[LLM]]
- [[Agent Loop]]
- [[Agent 主题]]

## 题目正文

### 3. 子问题：在 Agent 的设计中，“规划能力”至重要。请谈谈目前有哪些主流方法可以赋予 LLM 规划能力？（例如 CoT, ToT, GoT等）

答：

可按“线性到搜索”来讲：CoT 是单路径分步推理，成本低但容错弱；ToT 树状思考链路引入多分支探索和回溯，[[Task Success Rate|成功率]]更高但算力开销大；GoT 图结构进一步允许分支合并和循环优化，适合复杂依赖问题。

以及工程里常见多角色agent划分, 如: Planner-Executor 拆分，让规划与执行解耦成两个agent。总结可背：规划能力本质是用更多搜索换更高成功率。

## 3. 补充原问：AI Agent 的基本实现路径是什么？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
