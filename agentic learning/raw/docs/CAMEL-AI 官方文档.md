---
type: source
source_type: docs
title: "CAMEL-AI Documentation and Role-Playing Paper"
url: "https://docs.camel-ai.org/index"
author: CAMEL-AI
site: docs.camel-ai.org
topic:
  - agent
  - framework
  - multi-agent
  - camel
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
  - "https://arxiv.org/abs/2303.17760"
related:
  - "[[CAMEL]]"
  - "[[Agent Framework]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# CAMEL-AI 官方文档

## 为什么收

CAMEL 同时有论文时代的 role-playing / inception prompting 范式，也有后续框架化的 CAMEL-AI docs。它适合训练一个边界：CAMEL 不是普通“群聊框架”，它的历史核心是用角色设定和 inception prompting 让两个或多个 communicative agents 自主协作；现代 CAMEL-AI 又扩展成包含 agents、societies、interpreters、memory、RAG、synthetic data 等模块的多 Agent 框架。

## 先读什么

- CAMEL paper：Communicative Agents for “Mind” Exploration of Large Language Model Society
- CAMEL docs Introduction
- Societies / RolePlaying reference
- Prompts / role description templates

## 一句话

CAMEL 的原始核心是 role-playing：通过 inception prompting 给 communicative agents 设定角色、任务和约束，让它们在多轮对话中协作；现代 CAMEL-AI 则把它扩展成 modular multi-agent framework。

## 需要我读的内容

### 必读

#### 必读块 1：Role-playing / inception prompting

- 位置：CAMEL arXiv abstract
- 为什么必读：支撑 CAMEL 概念卡的地基定义。
- 原文短摘：论文摘要称其提出 role-playing，并用 inception prompting 引导 chat agents 完成任务、保持与人类意图一致。
- 中文概括：CAMEL 的关键不是“随便让两个 agent 聊天”，而是通过初始提示把角色、任务、终止和协作规则注入到会话里，减少角色翻转、跑题和无限对话。
- 支撑概念：[[CAMEL]], [[Multi-agent Orchestration]], role-playing
- 证据边界：这是论文层概念，不等同于现代 CAMEL-AI 全部框架能力。

#### 必读块 2：现代 CAMEL-AI 框架模块

- 位置：CAMEL docs Introduction / Core Components；RolePlaying reference
- 为什么必读：支撑“CAMEL 已从论文范式扩展成框架生态”的现代性判断。
- 原文短摘：文档把 CAMEL-AI 描述为 open-source modular framework，并列出 Agents、Societies、Interpreters、Memory、RAG、Synthetic Data 等组件；RolePlaying reference 将其定义为两个 agent 之间的 role playing。
- 中文概括：现代 CAMEL-AI 仍保留 role-playing/society 的核心线索，但已经把工具、代码解释器、记忆、检索和数据生成纳入框架生态。
- 支撑概念：[[CAMEL]], [[Agent Framework]], [[Agent Framework 编排范式对比]]
- 证据边界：官网的框架能力属于快速演进层；本 note 不证明每个模块的生产成熟度。

## 可以拆成概念卡

- [[CAMEL]]
- role-playing
- inception prompting
- agent society
- [[Agent Framework 编排范式对比]]

## 我的疑问

- CAMEL 的 role-playing 范式在现代 framework 中，是仍作为核心编排方式，还是已经变成众多模块之一？
- 它和 AutoGen 的 group chat 最小边界是什么：角色/任务 inception vs speaker/team orchestration？

## 边界提醒

CAMEL 的稳定概念边界来自 paper：role-playing + inception prompting。现代 CAMEL-AI framework 的模块能力需要按 docs 和 repo 持续复查，不应把 paper 里的实验范式直接等同于生产级多 Agent 平台。
