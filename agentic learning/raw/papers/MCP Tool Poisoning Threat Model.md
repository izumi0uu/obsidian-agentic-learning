---
type: source
source_type: paper
title: "Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning"
url: "https://arxiv.org/abs/2603.22489"
pdf: "assets/MCP Tool Poisoning Threat Model.pdf"
extracted: "extracted/MCP Tool Poisoning Threat Model.extracted.md"
author: Charoes Huang, Xin Huang, Ngoc Phu Tran, Amin Milani Fard
site: arxiv.org
topic:
  - security
  - mcp
  - agent
  - frontier
created: 2026-05-06
updated: 2026-05-15
last_checked: 2026-05-11
freshness: volatile
conflicts: []
status: seed
source: "https://arxiv.org/abs/2603.22489"
related:
  - "[[Tool Poisoning]]"
  - "[[MCP]]"
  - "[[Prompt Injection]]"
  - "[[Tool Registry]]"
---

# MCP Tool Poisoning Threat Model

## 为什么收

MCP 让工具可发现、可组合、可远程接入，也带来工具描述、工具返回值、权限和供应链层面的新攻击面。这篇新论文适合支撑 [[Tool Poisoning]] 的前沿风险卡。

## 一句话

MCP tool poisoning 关注恶意或被污染的工具描述/结果如何诱导模型执行非预期动作。


## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Tool poisoning 可以通过工具 metadata 注入恶意指令。 | arXiv abstract | high | [[Tool Poisoning]] |
| 论文建议结合 metadata、决策路径和运行时行为分析。 | arXiv abstract | medium | [[Trace]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。


## 现代性 / 前沿性初判

- frontier / volatile：MCP 安全和 tool poisoning 在 2026 仍快速演进。
- 稳定部分：工具描述和工具返回都应视为不可信输入。
- 易变部分：具体 MCP 安全最佳实践、签名、权限模型和平台实现会变化。
- freshness：volatile；需要定期复查。

## 先读什么

- Threat model：MCP host/client/server、LLM、external data store、authorization server。
- Prompt injection with tool poisoning：工具描述和返回内容如何影响模型。
- Mitigations：权限、确认、隔离和审计。


## 需要我读的内容

目标：理解 MCP tool poisoning 的威胁面来自工具元数据、工具结果和权限链路，而不只是用户 prompt。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / 工具元数据中的恶意指令

- 位置：arXiv abstract / 2603.22489 / last checked 2026-05-11
- 为什么必读：这里支撑 [[Tool Poisoning]] 的核心边界：攻击面可以藏在工具描述/metadata。
- 原文短摘：
  > malicious instructions are embedded in tool metadata
- 中文概括：
  - MCP 让工具被发现和描述，这些描述会进入模型上下文或工具选择过程。
  - 如果工具 metadata 被污染，模型可能在用户没写恶意 prompt 的情况下被诱导。
- 我需要理解的机制：
  1. tool metadata injection
  2. tool registry trust boundary
  3. prompt injection through tools
- 支撑概念：
  - [[Tool Poisoning]]
  - [[MCP]]
  - [[Prompt Injection]]
- 证据边界：
  - 这段只证明 metadata 是攻击面；不能说明所有 MCP 工具都不可信，也不能替代具体漏洞复现。

#### 必读块 2：Abstract / 分析与缓解方向

- 位置：arXiv abstract / 2603.22489 / last checked 2026-05-11
- 为什么必读：这里提示评估 tool poisoning 不能只看 prompt，还要看模型决策路径和工具行为。
- 原文短摘：
  > static metadata analysis, model decision path tracking, and runtime behavior testing
- 中文概括：
  - 论文把威胁建模扩展到工具元数据静态检查、模型选择工具的路径、运行时行为测试。
  - 这对应现代 Agent 安全里的 registry 审计、权限确认、trace 和 sandbox。
- 我需要理解的机制：
  1. metadata analysis
  2. decision path tracking
  3. runtime behavior testing
- 支撑概念：
  - [[Tool Registry]]
  - [[Trace]]
  - [[Tool Poisoning]]
- 证据边界：
  - 这些缓解方向是 threat modeling 入口，不是完整安全证明；具体 MCP host/client/server 实现仍需独立审计。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- 工具描述应该怎样进入 prompt，才能既可用又不完全可信？
- Tool registry 是否需要类似 package registry 的签名、版本和信任等级？

### 读完要更新

- [[Tool Poisoning]]
- [[MCP]]
- [[Prompt Injection]]
- [[Tool Registry]]
- [[Trace]]

## 已提取文件

- PDF：`assets/MCP Tool Poisoning Threat Model.pdf`
- Extracted Markdown：`extracted/MCP Tool Poisoning Threat Model.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[Tool Poisoning]]
- [[MCP]]
- [[Prompt Injection]]

## 我的疑问

- Tool registry 是否需要像 package registry 一样做签名、版本和信任等级？
- 工具描述应不应该被视为不可信输入？

## 边界提醒

Tool poisoning 和 prompt injection 经常组合出现：攻击者不一定直接控制用户 prompt，而是控制工具、工具说明或工具返回的内容。
