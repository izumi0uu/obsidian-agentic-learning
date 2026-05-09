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
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "01_Agent基础"
last_checked: 2026-05-09
freshness: watch
sha256: 56c2d01ef242852b3f004dbf4deea8f5943f5b26c80db1ff52ee76da2ae406c8
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent Workflow]]"
  - "[[ReAct]]"
  - "[[Planning]]"
  - "[[Observation]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# ReAct与规划能力（CoT/ToT/GoT）

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
- [[Agent Workflow]]
- [[ReAct]]
- [[Planning]]
- [[Observation]]
- [[Agent Loop]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

### 1. 子问题：ReAct与规划能力（CoT/ToT/GoT）

主问题：ReAct 是什么？如何给 Agent 规划能力？

口述答案：
ReAct 是 Thought-Action-Observation 循环：先思考、再调用工具、再根据观察结果迭代。它比单次 CoT 更适合信息不完整任务，因为它能边查边改。规划方法上，CoT 是单路径分解，成本低但容错弱；ToT 用树状分支提高成功率但更贵；GoT 进一步支持图结构合并与回溯，适合复杂依赖。工程上建议把“规划”和“执行”解耦：Planner 负责拆解，Executor 负责落地，减少模型一步到位失败。

常见追问：

1. 什么时候不该用复杂规划而该用固定流程？
2. 规划深度如何控制成本？
3. 如何避免“想太多、做太少”？

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
