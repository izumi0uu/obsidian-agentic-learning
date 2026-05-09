---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/11_%E5%88%86%E5%B8%83%E5%BC%8F%E4%BA%8B%E5%8A%A1%E4%B8%8E%E9%AB%98%E5%8F%AF%E7%94%A8/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/11_分布式事务与高可用/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "11_分布式事务与高可用"
last_checked: 2026-05-09
freshness: watch
sha256: 0a25b234752bc3b9029d85fb400502ea029a9213a49fa17953e60a2938141e6e
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# Seata / TCC 框架理解

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/11_分布式事务与高可用/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/11_%E5%88%86%E5%B8%83%E5%BC%8F%E4%BA%8B%E5%8A%A1%E4%B8%8E%E9%AB%98%E5%8F%AF%E7%94%A8/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `11_分布式事务与高可用`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

### Seata / TCC 框架理解

Seata 的角色通常分为：
- `TC`：协调器，维护全局事务状态；
- `TM`：事务发起者，负责开始/提交/回滚全局事务；
- `RM`：资源管理器，管理各分支事务并向 TC 汇报。

它的核心流程是：
- TM 向 TC 申请一个全局事务 ID；
- 各分支事务把自己注册到这个全局事务里；
- 成功则统一提交，失败则由 TC 驱动各分支回滚。

面试里可以补一句：
- 强一致核心链路更适合 TCC；
- 大部分互联网业务更常用“可靠消息 + 幂等 + 补偿 + 对账”这套最终一致方案。

## 补充原文：接口幂等怎么设计

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
