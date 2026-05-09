---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
  - "mysql"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/01_MySQL/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "01_MySQL"
last_checked: 2026-05-09
freshness: watch
sha256: 5590535696c642c7ce2616a32c3fdf9a52e75167c632db0ea434808ee54f671f
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent State]]"
---

# InnoDB 的 RR 如何避免幻读？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/01_MySQL/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `01_MySQL`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent State]]

## 题目正文

### 5. InnoDB 的 RR 如何避免幻读？

RC（Read Committed）：每条 SELECT 都拿一个新的快照（statement 级 Read View）。
RR（Repeatable Read）：事务第一次快照读后，后续快照读复用同一个快照（transaction 级 Read View）。
大多数 MySQL 线上默认 RR（InnoDB 默认），读一致性更强。
如果业务更追求并发、能接受读到“更新后已提交新值”，可考虑 RC。
关键交易链路常配合当前读（for update）确保强一致更新。

**先定义幻读**

- 同一个事务里，按同一条件查两次，第二次“多/少了行”（通常是别的事务插入了新行）。

**InnoDB 在 RR 下怎么避免幻读：分两种读法**

1. **快照读（普通 `select`）**

- 依赖 `MVCC + Read View`。  
- RR 下第一次快照读会固定一个一致性视图，后续同事务再查还是这个视图。  
- 所以你“看起来”不会出现幻读。

1. **当前读（`select ... for update` / `lock in share mode` / `update` / `delete`）**

- 依赖锁，不是纯 MVCC。  
- 用 **next-key lock = 记录锁(record lock) + 间隙锁(gap lock)** 锁住索引区间。  
- 这样其他事务不能往这个区间插入新行，从源头防止幻读。

---

**具体例子（最常考）**

- 条件：`age between 20 and 30`，且 `age` 有索引。  
- 事务A（RR）：`select * from t where age between 20 and 30 for update;`  
  - A 会对这个范围加 next-key 锁。
- 事务B：`insert into t(age,...) values(25,...)`  
  - 会被阻塞，直到 A 提交。
- 所以 A 在事务内再查这个范围，不会突然多出新行。

---

**面试 30 秒口述版**
“RC 是语句级快照，每次读最新已提交，所以可能不可重复读；RR 是事务级快照，同事务快照读结果可重复. RR 防幻读分两层：普通 `select` 走 MVCC 的一致性视图，事务内重复读结果稳定；`for update` 这类当前读走 next-key lock（记录锁+间隙锁）锁住索引区间，阻止其他事务在区间插入，从而真正避免幻读。”

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
