---
type: source
source_type: paper
title: "MMSkills: Towards Multimodal Skills for General Visual Agents"
url: "https://arxiv.org/abs/2605.13527"
pdf: "assets/MMSkills - Towards Multimodal Skills for General Visual Agents.pdf"
extracted: "extracted/MMSkills - Towards Multimodal Skills for General Visual Agents.extracted.md"
arxiv: "https://arxiv.org/abs/2605.13527"
doi: "10.48550/arXiv.2605.13527"
author:
  - Kangning Zhang
  - Shuai Shao
  - Qingyao Li
  - Jianghao Lin
  - Lingyue Fu
  - Shijian Wang
  - Wenxiang Jiao
  - Yuan Lu
  - Weiwen Liu
  - Weinan Zhang
  - Yong Yu
site: arXiv
venue: "arXiv 2026"
pages:
topic:
  - agent
  - computer-use
  - visual-agent
  - skills
  - multimodal
  - frontier
created: 2026-05-14
updated: 2026-05-15
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source: "https://arxiv.org/abs/2605.13527"
related:
  - "[[Computer Use]]"
  - "[[GUI Grounding]]"
  - "[[Tool Use]]"
  - "[[Agent Workflow]]"
  - "[[Memory]]"
---

# MMSkills - Towards Multimodal Skills for General Visual Agents

## 原文信息

- 论文标题：MMSkills: Towards Multimodal Skills for General Visual Agents
- 作者：Kangning Zhang, Shuai Shao, Qingyao Li, Jianghao Lin, Lingyue Fu, Shijian Wang, Wenxiang Jiao, Yuan Lu, Weiwen Liu, Weinan Zhang, Yong Yu
- 提交日期：2026-05-13
- 学科：Artificial Intelligence (cs.AI)
- URL：<https://arxiv.org/abs/2605.13527>
- PDF：<https://arxiv.org/pdf/2605.13527>
- 本地 PDF：`assets/MMSkills - Towards Multimodal Skills for General Visual Agents.pdf`
- extracted：`extracted/MMSkills - Towards Multimodal Skills for General Visual Agents.extracted.md`

边界：这一页是 raw source note，只回答“论文原文摘要目前支持什么、精读时先看哪里”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把摘要级判断写成论文全文结论。

## 为什么收

这篇补 visual agent 的 skill 边界：多模态任务里的可复用技能不只是文本 prompt 或代码，还要包含状态识别、视觉证据和进展 / 失败判断。


本页来自 2026-05-14 对用户提供的 Hermes arXiv cs.AI recent Agent 论文补充清单录入，批次索引见 [[资料收集索引#第四轮补充：2026-05-14 arXiv Agent 论文 Hermes 补充]]，前沿判断见 [[03 前沿追踪#2026-05-14 arXiv Agent 论文 Hermes 补充]]。

## 一句话

MMSkills 把视觉 Agent 的可复用 procedure 表示为文本步骤、state cards 和 multi-view keyframes 组合的多模态技能包。

## 先读什么

1. Abstract：确认问题定义和作者自己的贡献边界。
2. Introduction / Motivation：看它要纠正哪类 Agent 误读。
3. Method / Framework：抓住可复用的机制，不急着抄结果数字。
4. Evaluation / Experiments：判断实验环境、指标和可外推范围。
5. Limitations / Discussion：防止把前沿预印本读成稳定工程标准。

## 需要我读的内容

### 必读

> 使用规则：当前只录入摘要级短证据；精读后再补 PDF 页码、section、figure 或 table。


#### 必读块 1：Abstract / multimodal procedural knowledge

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：确认 visual agent 的技能为什么需要图像状态和视觉证据。
      - 原文短摘：
        > multimodal procedural knowledge
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Computer Use]]
- [[GUI Grounding]]
- [[Tool Use]]
      - 证据边界：
        - 支撑 [[Computer Use]]；不要等同于 SKILL.md。
#### 必读块 2：Abstract / skill package structure

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：看每个 skill package 包含哪些 state-conditioned 组件。
      - 原文短摘：
        > state-conditioned package
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Computer Use]]
- [[GUI Grounding]]
- [[Tool Use]]
      - 证据边界：
        - 支撑 [[GUI Grounding]]；需正文核对格式。
#### 必读块 3：Abstract / trajectory-to-skill generation

      - 位置：arXiv abstract / 正文待精读定位
      - 为什么必读：理解如何从 public interaction experience 生成 reusable skills。
      - 原文短摘：
        > trajectory-to-skill Generator
      - 中文概括：
        - 第一轮只基于 arXiv 摘要录入；精读时要回到 PDF / HTML 核对 section、figure、table。
        - 这部分主要支撑本页的“为什么值得读”和概念拆分，不替代稳定概念卡。
      - 我需要理解的机制：
        1. 它把 Agent 问题切到哪一层。
        2. 它的输入、输出或评价信号是什么。
        3. 它不能外推到什么。
      - 支撑概念：
        - [[Computer Use]]
- [[GUI Grounding]]
- [[Tool Use]]
      - 证据边界：
        - 支撑 [[Memory]]；需看数据来源和泄漏风险。

### 选读

- Related Work：用于判断它和已有概念卡 / 对比页的关系。
- Appendix / artifact：只有在准备实现或复现实验时再读。

### 可以先跳过

- 第一轮可以先跳过完整实验细节和所有公式，只保留“它改变我哪个边界判断”。

### 读完要能回答

- 这篇论文把 Agent 问题切到哪一层：memory、planning、trajectory、multi-agent、evaluation、safety、tool use、RAG 还是 high-risk application？
- 它最容易被误读成什么？
- 它给当前 vault 哪张概念卡提供证据？

### 读完要更新

- 可能更新的概念卡：[[Computer Use]], [[GUI Grounding]], [[Tool Use]], [[Agent Workflow]], [[Memory]]
- 可能更新的 topic / map：[[Agent 主题]], [[Agent 知识地图]], [[03 前沿追踪]]。
- 如果精读后出现稳定概念，再从本 source note 拆卡；不要只凭标题创建弱概念卡。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| visual agents 的 reusable skills 需要多模态程序知识。 | Abstract | medium-high | [[Computer Use]] |
| state cards / keyframes 可以帮助运行时视觉决策。 | Abstract | medium | [[GUI Grounding]] |
| trajectory 可以被归纳成可复用 skill，但需要审计。 | Abstract | medium | [[Agent Workflow]] |

边界：这些 claim 当前主要来自 arXiv abstract；没有读到 section/page/figure 时，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：待精读正文后补。
- 输入 / 输出：第一轮只记录摘要级问题和预期产物。
- 关键步骤：见 [[MMSkills - Towards Multimodal Skills for General Visual Agents#需要我读的内容]]。
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

- PDF：`assets/MMSkills - Towards Multimodal Skills for General Visual Agents.pdf`
- Extracted Markdown：`extracted/MMSkills - Towards Multimodal Skills for General Visual Agents.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

- 已沉淀到 wiki 的概念：本轮先作为 source note 录入到 Hermes 补充来源批次。
- 还没处理的证据：PDF 正文、实验细节、limitations、artifact / code。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[Computer Use]] | 补视觉技能和 GUI 状态证据 | [[MMSkills - Towards Multimodal Skills for General Visual Agents#需要我读的内容]] | P1 |
| [[GUI Grounding]] | 补 state card / keyframe 边界 | [[MMSkills - Towards Multimodal Skills for General Visual Agents#需要我读的内容]] | P1 |
| [[Memory]] | 补 trajectory-to-skill 归纳边界 | [[MMSkills - Towards Multimodal Skills for General Visual Agents#需要我读的内容]] | P2 |

## 我的疑问

- MMSkills 和 Hermes / OMX 的文本 skill 概念有什么不同？
- 视觉 keyframe 会不会造成过度锚定和 UI 版本过期？
- 公共 trajectory 生成 skill 如何避免 benchmark leakage？

## 边界提醒

- 这里的 Skills 是 visual agent 的多模态程序知识包，不等同于 Hermes skills、OMX skills 或 SKILL.md registry 条目。
- 本页不是稳定概念卡；如果后续要写概念卡，必须回链到本页小节或 PDF section。
- 如果论文标题里的术语和现代 framework / docs 用法不同，以正文定义和工程证据为准。

## 原文摘录

> 本页只保留 `## 需要我读的内容` 中的极短摘录。精读后再补 section/page anchor，避免把摘要级判断伪装成全文证据。
