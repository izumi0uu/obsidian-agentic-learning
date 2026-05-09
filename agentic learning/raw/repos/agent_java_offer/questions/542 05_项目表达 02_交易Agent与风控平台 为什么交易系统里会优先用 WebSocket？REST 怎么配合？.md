---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "project-expression"
  - "agent"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "05_项目表达"
category: "02_交易Agent与风控平台"
last_checked: 2026-05-09
freshness: watch
sha256: a9089ea006d857a056d6d7a0773adf6f885281f82b5785db2a639d5a30bcd597
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# 为什么交易系统里会优先用 WebSocket？REST 怎么配合？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`05_项目表达` / `02_交易Agent与风控平台`  
条目类型：`question`  
父级题组：你最该准备的 12 道题
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

**7. 为什么交易系统里会优先用 WebSocket？REST 怎么配合？**
一个稳的回答应该是：
行情、订单状态、仓位变化适合 WebSocket 的低延迟实时推送；
查询历史、配置类接口、回补丢包适合 REST；
系统设计上经常是 **WebSocket 收实时流 + REST 做补数/对账**。
某交易平台 官方文档本身就把 WebSocket 当成核心接口，并支持通过 WebSocket 下单。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
