---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - spring
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 08_Spring与SpringBoot
last_checked: 2026-05-09
freshness: watch
sha256: 2bf048b421ccbcb5532375eb637de44bcbc1ae1605f71ce366c861ed141fe96f
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Audit Log]]"
  - "[[Trace]]"
---

# 事务传播常见用法？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/08_Spring与SpringBoot/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/08_Spring%E4%B8%8ESpringBoot/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `08_Spring与SpringBoot`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Audit Log]]
- [[Trace]]

## 题目正文

### 3. 事务传播常见用法？

事务传播记成**方法 A 调方法 B 时，B 要不要共用 A 的事务**, `REQUIRED` 复用当前事务，是最常见默认选择, 常用作主业务链路(下单,扣库存, 写订单)；`REQUIRES_NEW` 会挂起外层事务并开启新事务，常用于[[Audit Log|审计日志]]、补偿记录等需独立提交场景。

最常用两个：

1. `REQUIRED`（默认）

- 有事务就加入当前事务  
- 没事务就新开一个

含义：A 和 B 通常“一荣俱荣、一损俱损”，任一抛异常都可能一起回滚。  

适合：主业务链路（下单、扣库存、写订单）。

1. `REQUIRES_NEW`

- 不管外层有没有事务，B 都新开事务  
- 外层事务会被挂起，B 提交/回滚后再恢复外层

含义：B 的提交结果与 A 解耦，A 后续失败也不影响 B 已提交。  

适合：审计日志、操作留痕、补偿记录（必须落库）。

你还要顺带记两个常见点：

1. 为什么“写了 `@Transactional` 还不生效”

同类内部自调用不会走代理，传播行为也不会生效。

1. `REQUIRES_NEW` 不能滥用

会增加事务数量、连接占用和锁竞争；只给“必须独立提交”的小操作用。

面试一句话：  

`REQUIRED` 保证主流程原子性`REQUIRES_NEW` 用来做与主事务解耦的独立落库；选型本质是‘一致回滚’还是‘独立留痕’。”

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
