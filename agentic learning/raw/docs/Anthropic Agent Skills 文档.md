---
type: source
source_type: docs
title: Claude Agent Skills Documentation
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
author: Anthropic
site: platform.claude.com
topic:
  - agent
  - skills
  - tools
  - context-engineering
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Skills]]"
  - "[[Agent Harness]]"
  - "[[Progressive Disclosure]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
---

# Anthropic Agent Skills 文档

## 为什么收

这是校准 [[Agent Skills]] 的官方主源。它把 skill 解释为 Claude 可自动使用的能力包，而不是一段复制粘贴的 prompt；同时给出 `SKILL.md`、metadata、按需加载、脚本和参考资料的工程边界。

## 先读什么

- Agent Skills overview
- How Skills work
- Three types of Skill content, three levels of loading
- Skills architecture
- Custom Skills / API usage

## 一句话

Agent Skill 是由 `SKILL.md`、说明 metadata、可选脚本、模板和参考资料组成的能力包；Agent 根据任务相关性按需加载它。

## 关键事实

- Anthropic 文档把 Agent Skills 放在 Claude 的工具和虚拟机执行环境边界中：skill 可以包含指令、可执行代码和参考材料。
- Skill 的入口是 `SKILL.md`，其中 YAML frontmatter 的 `name` / `description` 用于发现和触发。
- 文档强调 progressive disclosure：启动时只加载轻量 metadata；任务匹配时加载 `SKILL.md` 正文；后续再按需读取额外文件或运行脚本。
- Skill 可以调用代码执行环境里的脚本，让确定性操作不必完全依赖模型生成 token。
- 这套能力在 Claude 产品/API 生态中仍属于快速变化接口；具体 beta header、API 字段和产品支持范围需要复查。

## 可以拆成概念卡

- [[Agent Skills]]
- [[Progressive Disclosure]]
- [[Agent Harness]]
- [[Tool Registry]]
- [[Tool Poisoning]]

## 边界提醒

Agent Skill 的核心是“能力包 / 做事方法封装”，不是 MCP server、不是 Tool Calling schema，也不是模型微调。它会影响 Agent 选择什么流程和资源，因此也属于供应链与权限治理面。

## 证据边界

官方文档和 Anthropic engineering post 支撑“skill 由 `SKILL.md`、metadata、脚本/资源和 progressive disclosure 组成”。安全结论还需要和 [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]、[[Tool Poisoning]]、[[Tool Registry]] 一起读，不能仅靠产品文档推出“所有 skill 都安全”。
