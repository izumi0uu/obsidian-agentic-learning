---
type: source
source_type: paper
title: "Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry"
url: "https://arxiv.org/abs/2605.11418"
pdf: "assets/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.pdf"
extracted: "extracted/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.extracted.md"
arxiv: "https://arxiv.org/abs/2605.11418"
doi: "10.48550/arXiv.2605.11418"
author:
  - Shoumik Saha
  - Kazem Faghih
  - Soheil Feizi
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - skills
  - security
  - supply-chain
  - tooling
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.11418"
related:
  - "[[AGENTS.md]]"
  - "[[Tool Registry]]"
  - "[[MCP Registry]]"
  - "[[Tool Poisoning]]"
  - "[[Prompt Injection]]"
  - "[[Least Privilege Tools]]"
  - "[[Policy Engine]]"
  - "[[Agent Harness]]"
---

# Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry

## 原文信息

- 论文标题：Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry
- 作者：Shoumik Saha, Kazem Faghih, Soheil Feizi
- 提交日期：2026-05-12
- 学科：Artificial Intelligence (cs.AI); Cryptography and Security (cs.CR)
- URL：<https://arxiv.org/abs/2605.11418>
- PDF：<https://arxiv.org/pdf/2605.11418>
- 本地 PDF：`assets/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.pdf`（本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本）
- extracted：`extracted/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇对当前 vault 和 Codex/OMX 环境尤其贴近：Skill 描述不是被动文档，而会影响发现、选择和治理。它提醒我们，Agent 的能力扩展包本身也是供应链攻击面。

本页来自 2026-05-14 对 arXiv cs.AI recent 的 Agent 论文批次 1 录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文批次 1]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文批次 1-8]]。

## 一句话

SKILL.md 类自然语言元数据会影响 Agent skill 的发现、选择和治理，因此本身是语义供应链攻击面。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。

#### 必读块 1：Abstract / semantic supply-chain risk

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：先读为什么自然语言 metadata 会改变 skill registry 行为。
- 原文短摘：
  > semantic supply-chain risk
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[AGENTS.md]]
  - [[Tool Registry]]
  - [[MCP Registry]]
- 证据边界：
  - 支撑 [[Tool Registry]]、[[MCP Registry]]；不能把所有 skill registry 都视为同一实现。

#### 必读块 2：Discovery / Selection / Governance

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：理解攻击面分别在检索可见性、选择偏置和治理规避三个阶段。
- 原文短摘：
  > Discovery, Selection, Governance
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[AGENTS.md]]
  - [[Tool Registry]]
  - [[MCP Registry]]
- 证据边界：
  - 支撑 [[Policy Engine]]、[[Least Privilege Tools]]；需要正文看实验设置和防御建议。

#### 必读块 3：SKILL.md operational text

- 位置：arXiv abstract / 正文待精读定位
- 为什么必读：读作者为什么说 SKILL.md 不是普通说明书。
- 原文短摘：
  > not passive documentation
- 中文概括：
  - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
  - 这部分主要支撑本页的“为什么值得先读”和概念拆分，不替代稳定概念卡。
- 我需要理解的机制：
  1. 论文如何定义问题。
  2. 方法或标准把问题切到哪一层。
  3. 它不能外推到什么。
- 支撑概念：
  - [[AGENTS.md]]
  - [[Tool Registry]]
  - [[MCP Registry]]
- 证据边界：
  - 支撑 [[AGENTS.md]]、[[Agent Harness]]；这是对 skill registry 生态的风险判断，不等于禁用 skills。

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

- 可能更新的概念卡：[[AGENTS.md]], [[Tool Registry]], [[MCP Registry]], [[Tool Poisoning]], [[Prompt Injection]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Agent Skills 通过自然语言文件描述触发时机和使用方式，这带来语义供应链风险。 | Abstract | high | [[Tool Registry]] |
| 攻击可发生在 Discovery、Selection、Governance 三个 registry-facing 阶段。 | Abstract | medium-high | [[Policy Engine]] |
| 自然语言描述会影响 agent 找到、选择和加载哪些第三方能力。 | Abstract | medium-high | [[Agent Harness]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]。
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

- PDF：`assets/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.pdf`
- Extracted Markdown：`extracted/Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入，不创建批次型 map。
- 批次归档位置：[[资料收集索引]], [[前沿主源清单]], [[03 前沿追踪]]。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Tool Registry]] | skill registry 与 tool registry 的发现/选择治理边界 | [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]] | P1 |
| [[Tool Poisoning]] | 自然语言 metadata 也可能成为 poisoning surface | [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]] | P1 |
| [[AGENTS.md]] | 人类规则文件 / skill metadata 不是普通注释，而是 runtime 输入 | [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]] | P2 |

## 我的疑问

- Skill metadata 的安全审核应该检查语义、权限、代码，还是三者都检查？
- embedding-based discovery 如何防止关键词诱导式 visibility 攻击？
- 本 vault / Codex 技能使用时，哪些是人类信任边界，哪些应视为第三方 supply chain？

## 边界提醒

- 这篇适合作为 Agent skill registry 安全主源。不要读成“所有 skill 都危险所以不能用”；更精确的边界是：skill 描述、触发条件和治理标签会参与运行决策，因此需要 registry、review、least privilege 和 trace。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
