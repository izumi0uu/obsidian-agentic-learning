---
type: source
source_type: repo
title: "agent_java_offer"
url: "https://github.com/guoguo-tju/agent_java_offer"
author: guoguo-tju
site: github.com
topic:
  - interview
  - java
  - backend
  - agent
  - system-design
created: 2026-05-09
updated: 2026-05-09
last_checked: 2026-05-09
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agent]]"
  - "[[RAG]]"
  - "[[Agent Framework]]"
  - "[[Evaluation]]"
  - "[[Tool Calling]]"
---

# agent_java_offer Repo

## 为什么收

`agent_java_offer` 是一个面向 Java 后端转 AI Agent / 大模型应用工程的公开面试复习资料库。它把 AI Agent、RAG、上下文工程、评测、安全、框架协议、后端基础、系统设计、算法和项目表达组织成可复习、可口述、可追问的目录。

截至 2026-05-09，GitHub 页面显示仓库为 public，README 写明它的目标是把分散笔记重组为更适合复习、口述和深挖追问的结构化目录。

## 主源

- GitHub repo: <https://github.com/guoguo-tju/agent_java_offer>
- 入口文档：`docs/interview_prep/README.md`
- README 推荐快速路径：`01_AI` -> `02_后端` -> `03_系统设计` -> `05_项目表达`

## 已录入题库

- 相关知识回链：已为每个题目页补 `## 相关知识 wiki`；能明确匹配到现有概念卡/主题页的题目会直接链接，无直接对应关系的后端/算法题保留为 raw 缺口。

- 题目索引：[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]
- 抓取提交：`12bf4c915cca01f513e040935e1917d3687f8b35`
- 核心问答聚合文件：43
- 已生成 raw 题目条目：637
- 数据目录：`raw/repos/agent_java_offer/questions/`

录入粒度比原仓库文件更细：原仓库是“方向 -> 主题 -> 单文件问答”，这里进一步拆成 `question`、`followup-question`、`supplement-section` 和 `algorithm-problem`，方便像小林 Note 那样按单题检索。

## 一句话

它是“后端转 AI Agent”方向的面试复习索引和问答材料源，适合补表达和追问，不适合作为概念定义的唯一依据。

## 先读什么

1. 先看 `docs/interview_prep/README.md`，理解总导航和复习路线。
2. 如果目标是 AI Agent 面试，先读 `01_AI`，尤其是 Agent、workflow、多 Agent、RAG、上下文工程、记忆、评测、安全、框架协议与工程化。
3. 如果目标是后端转型，把 `02_后端` 和 `03_系统设计` 当作项目追问的底座。
4. 最后读 `05_项目表达`，练习把技术点组织成业务场景和项目叙事。

## 可以拆成概念卡

这份资料已经按面试题拆入 raw 层，但暂时不急着拆新概念卡，优先作为既有概念卡的面试表达补充：

- [[Agent]]
- [[Agent Framework]]
- [[RAG]]
- [[Context Engineering]]
- [[Memory]]
- [[Evaluation]]
- [[Tool Calling]]
- [[Guardrails]]

如果后续精读其中某个目录，可以再把“面试回答模板”和“概念本身”分开整理：概念卡负责定义和边界，面试材料负责口述顺序和追问点。

## 怎么放进我的学习路线

- 学完一张概念卡后，用这个仓库对应目录检查自己能否 2 分钟口述。
- 遇到“回答听起来顺，但概念不够准”的地方，回到 `wiki/concepts/` 和论文/官方文档校准。
- 遇到项目表达题，优先记录到 `maps/05 Query 写回队列.md` 或后续单独的面试复盘页，不要直接混进概念卡正文。

## 边界提醒

它是面试复习资料库，不是论文、标准、官方文档或框架源码。

它可以帮助回答“面试时怎么讲”，但不能单独决定“概念到底是什么”。涉及 [[RAG]]、[[Agent Framework]]、[[Tool Calling]]、[[Evaluation]]、[[Guardrails]] 等概念时，仍要回到主源证据校准。

仓库文档内容默认采用 CC BY-NC 4.0；转载、摘录、改编和再整理时要保留署名和许可证边界，且不应用于商业化分发。
