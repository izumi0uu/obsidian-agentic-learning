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
entry_type: "supplement-section"
direction: "01_AI"
category: "01_Agent基础"
last_checked: 2026-05-09
freshness: watch
sha256: dd185f809486816f458593dcc49aa1809b6d9200956341c040e6ad43ca77af45
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 补充原问：Agent 当前的局限是什么？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/01_Agent基础/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/01_Agent%E5%9F%BA%E7%A1%80/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `01_Agent基础`  
条目类型：`supplement-section`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Tool Calling]]
- [[Tool Use]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

## 4. 补充原问：Agent 当前的局限是什么？

### 1. 子问题：你觉得agent这个东西有什么缺点吗，因为目前人们普遍觉得agent好像也没有做出什么特别亮眼的产品或者功能
**口述答案（约300字）**：
我认为Agent当前的短板主要是“稳定性、可控性、成本”三件事。第一，稳定性：任务链路长、依赖外部工具多，任何一环抖动都会影响成功率。第二，可控性：模型是概率系统，复杂场景下会出现误判、过度调用工具甚至越权风险。第三，成本：多轮推理+检索+工具调用叠加，token和外部API成本上升很快。为什么看起来“没爆款”，本质是很多场景还没跨过“可用到可靠”的工程门槛。我的看法是Agent更适合流程明确、容错可设计、收益可量化的场景，比如内容生产、客服分流、内部效率工具。要做出亮点，关键不是堆模型，而是做强编排、评测和治理，把失败率和成本打下来。
**来源**：公开社区资料

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
