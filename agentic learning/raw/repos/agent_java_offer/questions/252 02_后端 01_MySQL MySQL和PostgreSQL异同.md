---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - java
  - backend
  - mysql
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/02_后端/01_MySQL/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 02_后端
category: 01_MySQL
last_checked: 2026-05-09
freshness: watch
sha256: 6c597ad386d265ae12d4d065736b98ee3a4c74842ffe3f83d38b17341b2dd713
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# MySQL和PostgreSQL异同

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/01_MySQL/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/01_MySQL/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `01_MySQL`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 题目正文

### 3. MySQL和PostgreSQL异同

**1. 定位差异**

1. `MySQL`：工程化和生态非常成熟，互联网 OLTP 默认选型，团队上手快。
2. `PostgreSQL`：功能更“全能型”，SQL 标准支持更强，适合复杂数据模型和复杂查询。

**2. 关键技术差异**

1. SQL/特性：

MySQL 常用能力够用；PostgreSQL 在高级 SQL、窗口分析、复杂约束、函数能力上通常更强。  
2. 数据类型：  
PostgreSQL 对 `JSONB`、数组、范围类型、地理空间（PostGIS）支持很强。  
3. 索引能力：  
MySQL 以 B+Tree 为主；PostgreSQL 有更丰富索引体系（GIN/GiST/BRIN/表达式索引/部分索引）。  
4. 事务并发：  
两者都支持 MVCC。MySQL（InnoDB）在典型事务场景成熟稳定；PostgreSQL 在复杂并发和复杂查询下可玩性更高。  
5. 扩展生态：  
MySQL 生态偏“业务系统工程化”；PostgreSQL 扩展能力强（如 PostGIS、Timescale）。

**场景怎么选**

1. 选 `MySQL`：

高并发交易、常规 CRUD、团队经验主要在 MySQL、希望快速稳定落地。  
2. 选 `PostgreSQL`：  
复杂报表/复杂 SQL、地理空间、半结构化数据、需要更强约束和扩展能力。  
3. 大厂常见做法：  
核心交易链路 MySQL，某些分析/地理/复杂建模模块用 PostgreSQL（按场景拆分）。

**4. 面试可直接说的一句话**
如果是标准互联网交易系统我优先 MySQL；如果是地理空间、复杂 SQL、JSON 深度检索这类需求，我会选 PostgreSQL。核心是按业务复杂度和团队成本做取舍。




---

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
