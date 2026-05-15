---
type: source
source_type: paper
title: "Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack"
url: "https://arxiv.org/abs/2605.12673"
pdf: "assets/Do Androids Dream of Breaking the Game - BenchJack.pdf"
extracted: "extracted/Do Androids Dream of Breaking the Game - BenchJack.extracted.md"
arxiv: "https://arxiv.org/abs/2605.12673"
doi: "10.48550/arXiv.2605.12673"
author:
  - Hao Wang
  - Hanchen Li
  - Qiuyang Mang
  - Alvin Cheung
  - Koushik Sen
  - Dawn Song
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - evaluation
  - benchmark
  - security
  - red-team
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.12673"
related:
  - "[[Benchmark]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
  - "[[Guardrails]]"
  - "[[Policy Engine]]"
  - "[[Prompt Injection]]"
  - "[[Task Success Rate]]"
---

# Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack

## 原文信息

- 论文标题：Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack
- 作者：Hao Wang, Hanchen Li, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI); Cryptography and Security (cs.CR)
- URL：<https://arxiv.org/abs/2605.12673>
- PDF：<https://arxiv.org/pdf/2605.12673>
- 本地 PDF：`assets/Do Androids Dream of Breaking the Game - BenchJack.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Do Androids Dream of Breaking the Game - BenchJack.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇补上 Agent benchmark 的安全边界：高分可能来自 reward hacking，而不是完成真实任务。它对学习 Agent 很关键，因为你会开始怀疑“榜单分数”背后的任务定义、观测权限、评分器和 exploit surface。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

BenchJack 把 Agent benchmark 当成可被攻击的系统，自动审计 reward-hacking exploit 和 benchmark flaw patterns。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / reward hacking

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：先确认作者说的 benchmark 风险不是过拟合，而是 frontier agent 自发找到评分漏洞。
- 原文短摘：
  > reward hacking
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Eval Harness]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Benchmark]]、[[Eval Harness]]；不能推出所有 benchmark 都同样脆弱。

#### 必读块 2：Agent-Eval Checklist

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：读八类 flaw patterns，作为后续评测设计 checklist。
- 原文短摘：
  > Agent-Eval Checklist
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Eval Harness]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Evaluation]]、[[Policy Engine]]；需读正文确认每类 flaw 的适用条件。

#### 必读块 3：BenchJack red-teaming pipeline

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解 coding agents 如何被用来审计 benchmark，而不只是参加 benchmark。
- 原文短摘：
  > automated red-teaming system
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[Benchmark]]
  - [[Eval Harness]]
  - [[Trajectory Evaluation]]
- 证据边界：
  - 支撑 [[Guardrails]]、[[Trajectory Evaluation]]；自动红队发现漏洞不等于自动修复所有漏洞。

### 选读

- Related Work：用于判断它和已有 [[Agent Harness]]、[[Trajectory Evaluation]]、[[Benchmark]]、[[Computer Use]] 等概念的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：模型、harness、workflow、trace、evaluation、security 还是 tool/action space？
- 它最容易被误读成什么？
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Benchmark]], [[Eval Harness]], [[Trajectory Evaluation]], [[Guardrails]], [[Policy Engine]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Agent benchmark 应按 secure-by-design 思路设计，因为 reward hacking 会影响能力判断。 | Abstract | medium-high | [[Benchmark]] |
| 论文从过往 reward hacks 总结八类 flaw patterns，并形成 Agent-Eval Checklist。 | Abstract | medium | [[Eval Harness]] |
| BenchJack 用 coding agents 审计 benchmark 并寻找可能的 reward-hacking exploits。 | Abstract | medium | [[Trajectory Evaluation]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Do Androids Dream of Breaking the Game - BenchJack#需要我读的内容]]。
- 和相邻方法的差别：待精读后写回对应概念卡或对比页。

## 实验 / 证据

- 数据集 / benchmark：待精读正文后补。
- 指标：待精读正文后补。
- 关键结果：摘要中出现的数字和结论需回到正文核对实验设置。
- 作者给出的局限：待精读 Limitations / Discussion 后补。

## 现代性 / 前沿性初判

- 判定：frontier / watch。
- 今天仍然稳定的部分：它提出的问题分层和边界提醒对学习 Agent 有价值。
- 易变部分：具体术语、数据集、实验结果、代码 artifact 和是否被主流 framework 吸收都需要复查。
- 需要 freshness 复查的部分：如果后续有正式会议版本、代码 release、复现实验或相反结果，需要更新本页和相关概念卡。

## 已提取文件

- PDF：`assets/Do Androids Dream of Breaking the Game - BenchJack.pdf`
- Extracted Markdown：`extracted/Do Androids Dream of Breaking the Game - BenchJack.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Benchmark]] | 补“benchmark 本身也需要安全设计”的边界 | [[Do Androids Dream of Breaking the Game - BenchJack#需要我读的内容]] | P1 |
| [[Eval Harness]] | 评测 harness 的 scoring / sandbox / observation 也可能被攻击 | [[Do Androids Dream of Breaking the Game - BenchJack#需要我读的内容]] | P1 |
| [[Task Success Rate]] | 分数可能被 exploit，不等于真实任务完成 | [[Do Androids Dream of Breaking the Game - BenchJack#需要我读的内容]] | P2 |

## 我的疑问

- Agent benchmark 的 reward hacking 与 prompt injection / tool poisoning 有什么不同？
- 什么样的 benchmark flaw 只能靠人工 threat modeling 发现，不能靠 BenchJack 自动发现？
- 如果一个 benchmark 被修补，旧分数应该如何处理？

## 边界提醒

- 这是安全和评测交叉的前沿论文。不要把它读成“所有 Agent benchmark 都没用”；更准确的学习点是：benchmark 是系统，也有攻击面、评分假设和修补生命周期。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
