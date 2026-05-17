---
type: source
source_type: repo
title: browser-use/browser-use
url: https://github.com/browser-use/browser-use
author: browser-use
site: github.com
topic:
  - agent
  - browser
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Browser Agent]]"
  - "[[Computer Use]]"
  - "[[Tool Registry]]"
---

# browser-use GitHub Repo

## 为什么收

browser-use 是浏览器 Agent 的热门开源项目，目标是让网站可被 AI Agent 操作。它适合观察 browser agent 的 action space、工具注册和失败恢复。

## 一句话

browser-use 是把浏览器自动化封装给 LLM/Agent 使用的开源项目。

## 先读什么

- README：项目定位和最小示例。
- docs：Agent、Browser、tools、profile/auth。
- examples / benchmark：看真实 web task 如何组织。

## 可以拆成概念卡

- [[Browser Agent]]
- [[Computer Use]]
- [[Tool Registry]]

## 我的疑问

- 什么时候 browser-use 适合生产，什么时候应该改写成 Playwright 脚本？
- 浏览器 Agent 的 benchmark 应该如何避免只测 demo 网站？

## 边界提醒

browser-use 是项目，不是通用标准。学习时关注它暴露了哪些浏览器动作、如何保持状态、如何处理登录和页面不稳定。
