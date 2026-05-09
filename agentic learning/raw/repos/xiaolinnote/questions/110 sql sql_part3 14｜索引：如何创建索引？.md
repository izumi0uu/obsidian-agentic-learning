---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part3/14-indexing.html"
source: "https://xiaolinnote.com/sql/sql_part3/14-indexing.html"
last_checked: 2026-05-07
freshness: watch
sha256: c0e0b365ea65ec60d975bc5e847c25263fe9fd97a43fd7bccd28d34960786e77
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Database Index]]"
  - "[[SQL]]"
---
# 14｜索引：如何创建索引？

原始链接：https://xiaolinnote.com/sql/sql_part3/14-indexing.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[Database Index]]
- [[SQL]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 35 分钟约 10593 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了各种SQL查询和数据操作技术。但是你有没有想过，当我们在一个包含百万条记录的表中查询数据时，数据库是如何快速找到我们需要的记录的？如果数据库需要逐行扫描整个表来查找数据，那查询性能将会非常糟糕。当你在一个电商网站上搜索商品时，为什么能够在几秒钟内从数百万种商品中找到你想要的商品？当你在银行APP中查询交易记录时，为什么系统能够快速展示你的历史交易信息？

你有没有想过，当你在一本厚厚的书中查找某个知识点时，你会怎么做？你会直接一页一页地翻找，还是先查看目录，定位到相关章节，然后再去具体页面查找？在图书馆里找书时，你会盲目地在书架间徘徊，还是会先查询图书检索系统，确定书籍的位置后再去取书？

在这一章中，我们将学习数据库索引技术，它就像书的目录或图书馆的检索系统，能够大大提高数据查询的效率。从索引的基本概念和工作原理开始，到各种索引类型的特点和使用场景，再到索引的创建、删除和管理方法，以及索引使用中的最佳实践和常见误区。掌握了索引技术，你就能够让数据库查询性能得到质的提升。

准备好了吗？让我们开始学习索引的奥秘吧！

## [14.1 常见索引类型速览](#_14-1-常见索引类型速览)

数据库索引是提高查询性能的重要工具，它通过创建额外的数据结构来加速数据的查找。不同的索引类型有不同的特点和使用场景，了解这些索引类型有助于我们选择合适的索引策略。

让我们使用**第1章**中创建的users表来演示各种索引类型的使用。为了确保索引演示的完整性，我们首先检查users表的结构和数据：

```
-- 查看users表结构
DESC users;

-- 查看users表中的数据
SELECT * FROM users LIMIT 5;
```

如果users表为空或数据不完整，我们可以插入一些示例数据：

```
-- 插入索引演示所需的示例数据
INSERT INTO users (username, email, phone, age, city, registration_date, last_login, status, profile_text) VALUES 
('zhangsan', 'zhangsan@example.com', '13800138000', 25, '北京', '2025-01-15', '2025-08-30 10:30:00', 'active', '热爱编程的年轻人'),
('lisi', 'lisi@example.com', '13900139000', 30, '上海', '2025-02-20', '2025-08-29 15:45:00', 'active', '数据分析师'),
('wangwu', 'wangwu@example.com', '13700137000', 28, '广州', '2025-03-10', '2025-08-28 09:20:00', 'inactive', '产品经理'),
('zhaoliu', 'zhaoliu@example.com', '13600136000', 35, '深圳', '2025-04-05', '2025-08-31 14:15:00', 'active', '前端开发工程师'),
('qianqi', 'qianqi@example.com', '13500135000', 22, '杭州', '2025-05-12', '2025-08-27 16:30:00', 'banned', 'UI设计师'),
('sunba', 'sunba@example.com', '13400134000', 40, '成都', '2025-06-01', '2025-08-25 11:00:00', 'active', '后端开发工程师'),
('zhoujiu', 'zhoujiu@example.com', '13300133000', 26, '武汉', '2025-06-15', '2025-08-20 13:20:00', 'active', '测试工程师'),
('wushi', 'wushi@example.com', '13200132000', 32, '西安', '2025-07-01', '2025-08-15 08:45:00', 'inactive', '运维工程师');
```

\*\*主键索引（PRIMARY KEY）\*\*是最特殊的索引类型，它唯一标识表中的每一行记录。主键索引有以下特点：

- 自动创建，无需手动创建
- 值必须唯一，不能为NULL
- 一个表只能有一个主键
- 通常使用B+Tree数据结构实现

在上面的users表中，id字段就是主键索引。当我们根据id查询用户时，数据库会使用主键索引来快速定位记录：

```
-- 使用主键索引查询
SELECT * FROM users WHERE id = 5;
```

执行结果：

```
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+
| id | username | email             | phone       | age  | city   | registration_date   | last_login          | status   | profile_text    | created_at          |
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+
|  5 | qianqi   | qianqi@example.com | 13500135000 |   22 | 杭州   | 2025-05-12          | 2025-08-27 16:30:00 | banned   | UI设计师        | 2025-08-31 15:30:00 |
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+
1 row in set (0.00 sec)
```

\*\*唯一索引（UNIQUE）\*\*确保索引列中的值唯一，但允许NULL值。唯一索引适用于需要保证唯一性但不作为主键的字段，比如用户名、邮箱等：

```
-- 创建唯一索引
CREATE UNIQUE INDEX idx_unique_username ON users(username);
CREATE UNIQUE INDEX idx_unique_email ON users(email);

-- 尝试插入重复的用户名，会失败
INSERT INTO users (username, email, phone, age, city, registration_date, status) 
VALUES ('zhangsan', 'zhangsan2@example.com', '13800138001', 25, '北京', '2025-08-31', 'active');
```

这个插入操作会失败，因为用户名'zhangsan'已经存在，唯一索引约束会阻止重复值的插入。

\*\*普通索引（INDEX）\*\*是最常用的索引类型，它没有任何限制，主要用于提高查询性能。普通索引适用于经常用于查询条件、排序或分组的字段：

```
-- 创建普通索引
CREATE INDEX idx_city ON users(city);
CREATE INDEX idx_age ON users(age);
CREATE INDEX idx_status ON users(status);
```

\*\*联合索引（Composite Index）\*\*是在多个列上创建的索引，适用于经常同时查询多个条件的场景。联合索引遵循最左前缀原则，即查询条件必须包含索引的最左列才能使用索引：

```
-- 创建联合索引
CREATE INDEX idx_city_age ON users(city, age);
CREATE INDEX idx_status_registration ON users(status, registration_date);
```

联合索引的最左前缀原则意味着：

- `idx_city_age`索引可用于查询：`WHERE city = '北京'`、`WHERE city = '北京' AND age > 25`
- 但不能用于查询：`WHERE age > 25`（因为缺少最左列city）

让我们验证一下联合索引的使用：

```
-- 可以使用联合索引的查询
SELECT * FROM users WHERE city = '北京' AND age > 25;

-- 也可以使用联合索引的最左列
SELECT * FROM users WHERE city = '上海';

-- 但无法使用联合索引（缺少最左列）
SELECT * FROM users WHERE age > 30;
```

\*\*全文索引（FULLTEXT）\*\*专门用于在文本内容中进行关键词搜索，支持复杂的全文搜索功能：

```
-- 创建全文索引
CREATE FULLTEXT INDEX idx_profile_text ON users(profile_text);

-- 使用全文索引搜索
SELECT username, profile_text 
FROM users 
WHERE MATCH(profile_text) AGAINST('编程 开发');
```

\*\*哈希索引（HASH）\*\*在MySQL中主要用于Memory存储引擎，它只支持等值比较，不支持范围查询。哈希索引的查询速度非常快，但功能有限：

```
-- 创建内存表并演示哈希索引
DROP TABLE IF EXISTS memory_users;
CREATE TABLE memory_users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    INDEX idx_username_hash USING HASH (username)
) ENGINE = MEMORY;
```

不同的索引类型有不同的使用场景。主键索引用于唯一标识记录，唯一索引用于保证数据唯一性，普通索引用于提高查询性能，联合索引用于多条件查询，全文索引用于文本搜索，哈希索引用于内存表的快速查找。

理解这些索引类型的特点和适用场景，有助于我们设计出高效的索引策略。在实际应用中，我们通常需要根据具体的查询模式和业务需求来选择合适的索引类型。

## [14.2 创建与删除索引（语法与命名）](#_14-2-创建与删除索引-语法与命名)

索引的创建和管理是数据库性能优化的重要工作。正确的索引命名规范和创建方法能够让数据库管理更加清晰和高效。让我们学习如何创建、删除和管理索引。

索引的命名规范非常重要，良好的命名能够让索引的用途一目了然。通常的命名规则是：

- 主键索引：`pk_表名`
- 唯一索引：`uk_表名_字段名`
- 普通索引：`idx_表名_字段名`
- 联合索引：`idx_表名_字段名1_字段名2`

让我们基于之前创建的users表来演示索引的完整管理过程：

```
-- 首先查看当前的索引情况
SHOW INDEX FROM users;
```

使用`CREATE INDEX`语句创建索引是最常用的方法：

```
-- 创建普通索引
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_age ON users(age);
CREATE INDEX idx_users_registration_date ON users(registration_date);

-- 创建联合索引
CREATE INDEX idx_users_city_age ON users(city, age);
CREATE INDEX idx_users_status_registration ON users(status, registration_date);

-- 创建唯一索引
CREATE UNIQUE INDEX idx_users_email ON users(email);
```

使用`ALTER TABLE`语句也可以创建索引，这种方法更加灵活：

```
-- 使用ALTER TABLE创建索引
ALTER TABLE users ADD INDEX idx_users_city (city);
ALTER TABLE users ADD UNIQUE INDEX idx_users_username (username);
```

在创建表时也可以直接定义索引：

```
-- 创建新表时定义索引
DROP TABLE IF EXISTS new_users;
CREATE TABLE new_users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    age INT,
    city VARCHAR(50),
    INDEX idx_username (username),
    INDEX idx_city (city),
    UNIQUE INDEX idx_email (email),
    INDEX idx_city_age (city, age)
);
```

查看表的索引信息可以使用`SHOW INDEX`语句：

```
-- 查看表的索引信息
SHOW INDEX FROM users;
```

执行结果会显示所有索引的详细信息，包括索引名称、字段名称、索引类型、唯一性等。

删除索引使用`DROP INDEX`语句：

```
-- 删除索引
DROP INDEX idx_users_phone ON users;
DROP INDEX idx_users_age ON users;
```

使用`ALTER TABLE`也可以删除索引：

```
-- 使用ALTER TABLE删除索引
ALTER TABLE users DROP INDEX idx_users_city;
```

在删除索引之前，需要考虑以下几点：

1. 确认索引确实不再使用
2. 评估删除索引对查询性能的影响
3. 选择合适的维护窗口进行操作

在线上环境中添加或删除索引时需要注意：

- 大表的索引创建可能会锁定表，影响业务
- 可以使用`ALGORITHM=INPLACE`和`LOCK=NONE`来减少锁的影响
- 对于特别大的表，考虑使用pt-online-schema-change等工具

```
-- 在线添加索引（减少锁影响）
ALTER TABLE users 
ADD INDEX idx_users_city_status (city, status),
ALGORITHM=INPLACE, 
LOCK=NONE;
```

让我们演示索引的实际效果。首先，我们创建一个包含更多数据的users表来测试索引性能：

```
-- 清空表并插入更多测试数据
DELETE FROM users;

-- 插入更多测试数据
INSERT INTO users (username, email, phone, age, city, registration_date, last_login, status, profile_text) VALUES 
('user001', 'user001@example.com', '13800138001', 25, '北京', '2025-01-01', '2025-08-30 10:00:00', 'active', '普通用户'),
('user002', 'user002@example.com', '13800138002', 30, '上海', '2025-01-02', '2025-08-29 11:00:00', 'active', 'VIP用户'),
('user003', 'user003@example.com', '13800138003', 28, '广州', '2025-01-03', '2025-08-28 12:00:00', 'inactive', '普通用户'),
('user004', 'user004@example.com', '13800138004', 35, '深圳', '2025-01-04', '2025-08-27 13:00:00', 'active', '企业用户'),
('user005', 'user005@example.com', '13800138005', 22, '杭州', '2025-01-05', '2025-08-26 14:00:00', 'banned', '普通用户'),
('user006', 'user006@example.com', '13800138006', 40, '成都', '2025-01-06', '2025-08-25 15:00:00', 'active', 'VIP用户'),
('user007', 'user007@example.com', '13800138007', 26, '武汉', '2025-01-07', '2025-08-24 16:00:00', 'active', '普通用户'),
('user008', 'user008@example.com', '13800138008', 32, '西安', '2025-01-08', '2025-08-23 17:00:00', 'inactive', '企业用户'),
('user009', 'user009@example.com', '13800138009', 29, '南京', '2025-01-09', '2025-08-22 18:00:00', 'active', '普通用户'),
('user010', 'user010@example.com', '13800138010', 31, '天津', '2025-01-10', '2025-08-21 19:00:00', 'active', 'VIP用户');

-- 创建索引
CREATE INDEX idx_users_city ON users(city);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_users_city_status ON users(city, status);
```

现在我们可以测试索引的效果：

```
-- 测试索引查询
SELECT * FROM users WHERE city = '北京' AND status = 'active';

-- 使用EXPLAIN查看执行计划
EXPLAIN SELECT * FROM users WHERE city = '北京' AND status = 'active';
```

在执行计划的Extra列中，如果显示"Using index"，说明查询使用了索引。

索引的维护是一项重要的数据库管理工作。定期检查索引的使用情况，删除不必要的索引，优化索引结构，能够保持数据库的高性能运行。

## [14.3 如何选列与确定列顺序](#_14-3-如何选列与确定列顺序)

选择合适的索引列和确定正确的列顺序是索引设计的核心问题。好的索引设计能够大大提高查询性能，而不恰当的索引不仅无法提高性能，还可能增加写入成本和维护负担。

让我们基于users表来学习如何选择索引列和确定列顺序。首先分析表中字段的选择性：

```
-- 计算字段的选择性
SELECT 
    COUNT(DISTINCT username) AS distinct_usernames,
    COUNT(DISTINCT email) AS distinct_emails,
    COUNT(DISTINCT phone) AS distinct_phones,
    COUNT(DISTINCT city) AS distinct_cities,
    COUNT(DISTINCT age) AS distinct_ages,
    COUNT(DISTINCT status) AS distinct_status,
    COUNT(*) AS total_records
FROM users;
```

执行结果：

```
+-------------------+----------------+----------------+---------------+--------------+---------------+--------------+
| distinct_usernames | distinct_emails | distinct_phones | distinct_cities | distinct_ages | distinct_status | total_records |
+-------------------+----------------+----------------+---------------+--------------+---------------+--------------+
|                10 |             10 |             10 |             10 |            10 |             3 |           10 |
+-------------------+----------------+----------------+---------------+--------------+---------------+--------------+
1 row in set (0.00 sec)
```

**高选择性原则**是选择索引列的重要原则。选择性高的列（即包含大量不同值的列）更适合作为索引列。让我们计算每个字段的选择性比例：

```
-- 计算字段的选择性比例
SELECT 
    'username' AS field_name,
    COUNT(DISTINCT username) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT username) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users

UNION ALL

SELECT 
    'email' AS field_name,
    COUNT(DISTINCT email) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT email) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users

UNION ALL

SELECT 
    'city' AS field_name,
    COUNT(DISTINCT city) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT city) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users

UNION ALL

SELECT 
    'age' AS field_name,
    COUNT(DISTINCT age) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT age) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users

UNION ALL

SELECT 
    'status' AS field_name,
    COUNT(DISTINCT status) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT status) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users;
```

执行结果：

```
+-----------+----------------+--------------+-------------------+
| field_name | distinct_values | total_values | selectivity_ratio |
+-----------+----------------+--------------+-------------------+
| username   |             10 |           10 |             100.00 |
| email      |             10 |           10 |             100.00 |
| city       |             10 |           10 |             100.00 |
| age        |             10 |           10 |             100.00 |
| status     |              3 |           10 |              30.00 |
+-----------+----------------+--------------+-------------------+
5 rows in set (0.00 sec)
```

可以看到，status字段的选择性较低（30%），而其他字段的选择性都很高（100%）。

**覆盖查询条件**是另一个重要原则。索引应该覆盖经常用于WHERE条件、JOIN条件、ORDER BY排序和GROUP BY分组的字段。让我们分析一些典型的查询场景：

```
-- 查询场景1：按城市查询用户
SELECT * FROM users WHERE city = '北京';

-- 查询场景2：按状态查询用户
SELECT * FROM users WHERE status = 'active';

-- 查询场景3：按城市和状态查询用户
SELECT * FROM users WHERE city = '北京' AND status = 'active';

-- 查询场景4：按年龄范围查询用户
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

-- 查询场景5：按城市和年龄查询用户
SELECT * FROM users WHERE city = '上海' AND age > 30;
```

基于这些查询场景，我们应该创建以下索引：

```
-- 为单个查询条件创建索引
CREATE INDEX idx_users_city ON users(city);
CREATE INDEX idx_users_status ON users(status);
CREATE INDEX idx_users_age ON users(age);

-- 为组合查询条件创建联合索引
CREATE INDEX idx_users_city_status ON users(city, status);
CREATE INDEX idx_users_city_age ON users(city, age);
```

**区分度高的列放在前面**是联合索引设计的另一个重要原则。让我们分析不同字段组合的区分度：

```
-- 分析不同字段组合的区分度
SELECT 
    COUNT(DISTINCT city) AS city_distinct,
    COUNT(DISTINCT status) AS status_distinct,
    COUNT(DISTINCT CONCAT(city, status)) AS city_status_distinct,
    COUNT(DISTINCT CONCAT(city, age)) AS city_age_distinct
FROM users;
```

执行结果：

```
+---------------+---------------+---------------------+-------------------+
| city_distinct | status_distinct | city_status_distinct | city_age_distinct |
+---------------+---------------+---------------------+-------------------+
|            10 |             3 |                  30 |                10 |
+---------------+---------------+---------------------+-------------------+
1 row in set (0.00 sec)
```

可以看到，city字段的选择性高于status字段，所以在联合索引中应该将city放在前面。

**避免过度索引**也是重要的设计原则。不是每个字段都需要索引，过多的索引会增加写入成本和维护负担。让我们删除一些不必要的索引：

```
-- 删除不必要的索引
DROP INDEX idx_users_phone ON users;  -- phone字段很少作为查询条件
DROP INDEX idx_users_registration_date ON users;  -- registration_date查询较少
```

**前缀索引**适用于长字符串字段，可以减少索引大小。让我们为username字段创建前缀索引：

```
-- 为username创建前缀索引
CREATE INDEX idx_users_username_prefix ON users(username(10));

-- 查看前缀索引的效果
SELECT username, LEFT(username, 10) AS prefix_name
FROM users;
```

执行结果：

```
+-----------+-------------+
| username  | prefix_name |
+-----------+-------------+
| user001   | user001     |
| user002   | user002     |
| user003   | user003     |
| user004   | user004     |
| user005   | user005     |
| user006   | user006     |
| user007   | user007     |
| user008   | user008     |
| user009   | user009     |
| user010   | user010     |
+-----------+-------------+
10 rows in set (0.00 sec)
```

**函数索引**在某些情况下很有用，但需要注意函数会影响索引的使用：

```
-- 不推荐：在索引列上使用函数
SELECT * FROM users WHERE UPPER(username) = 'USER001';

-- 推荐：存储规范化值并建立索引
ALTER TABLE users ADD COLUMN username_upper VARCHAR(50);
UPDATE users SET username_upper = UPPER(username);
CREATE INDEX idx_users_username_upper ON users(username_upper);

-- 现在可以高效查询
SELECT * FROM users WHERE username_upper = 'USER001';
```

让我们验证索引的实际效果：

```
-- 使用EXPLAIN查看索引使用情况
EXPLAIN SELECT * FROM users WHERE city = '北京' AND status = 'active';

EXPLAIN SELECT * FROM users WHERE username_upper = 'USER001';

EXPLAIN SELECT * FROM users WHERE city = '上海' AND age > 30;
```

索引列选择和顺序确定是一个需要综合考虑的问题。我们需要分析查询模式、字段选择性、业务需求等多个因素，设计出既能提高查询性能，又不会过度增加维护成本的索引方案。

在实际应用中，应该遵循以下原则：

1. 为经常用于WHERE条件的字段创建索引
2. 为经常用于ORDER BY和GROUP BY的字段创建索引
3. 为经常用于JOIN条件的字段创建索引
4. 在联合索引中，将选择性高的字段放在前面
5. 避免为选择性低的字段单独创建索引
6. 定期检查索引的使用情况，删除不必要的索引

## [14.4 覆盖索引与"回表"](#_14-4-覆盖索引与-回表)

覆盖索引是数据库查询优化中的重要概念，它能够让查询直接从索引中获取所需数据，避免访问数据行，从而大大提高查询性能。理解覆盖索引和回表机制，有助于我们设计出更高效的索引策略。

覆盖索引是指索引包含了查询所需的所有字段，这样数据库可以直接从索引中获取数据，无需回表查询。回表是指当索引不包含查询所需的所有字段时，数据库需要先通过索引找到数据行的位置，然后再回表查询完整数据的过程。

让我们基于users表来演示覆盖索引的概念：

```
-- 当前users表的结构
DESC users;
```

执行结果：

```
+-------------------+-----------------------+------+-----+---------+----------------+
| Field             | Type                  | Null | Key | Default | Extra          |
+-------------------+-----------------------+------+-----+---------+----------------+
| id                | int                   | NO   | PRI | NULL    | auto_increment |
| username          | varchar(50)           | NO   |     | NULL    |                |
| email             | varchar(100)          | NO   |     | NULL    |                |
| phone             | varchar(20)           | YES  |     | NULL    |                |
| age               | int                   | YES  |     | NULL    |                |
| city              | varchar(50)           | YES  |     | NULL    |                |
| registration_date | date                  | NO   |     | NULL    |                |
| last_login        | timestamp             | YES  |     | NULL    |                |
| status            | enum('active','inactive','banned') | YES |     | active   |                |
| profile_text      | text                  | YES  |     | NULL    |                |
| created_at        | timestamp             | NO   |     | CURRENT_TIMESTAMP |                |
+-------------------+-----------------------+------+-----+---------+----------------+
12 rows in set (0.00 sec)
```

现在让我们创建一个普通索引并观察回表现象：

```
-- 创建普通索引
CREATE INDEX idx_users_city ON users(city);

-- 查询需要回表的示例
SELECT id, username, city, status, email
FROM users 
WHERE city = '北京';

-- 使用EXPLAIN查看执行计划
EXPLAIN SELECT id, username, city, status, email
FROM users 
WHERE city = '北京';
```

这个查询虽然使用了city索引，但索引中不包含username、status、email等字段，所以需要回表查询完整数据。

现在让我们创建覆盖索引：

```
-- 创建覆盖索引
CREATE INDEX idx_users_city_covering ON users(city, username, status, email);

-- 现在查询可以直接使用覆盖索引
SELECT id, username, city, status, email
FROM users 
WHERE city = '北京';

-- 使用EXPLAIN查看执行计划
EXPLAIN SELECT id, username, city, status, email
FROM users 
WHERE city = '北京';
```

在执行计划的Extra列中，如果显示"Using index"，说明查询使用了覆盖索引。

让我们创建更多的覆盖索引来优化不同类型的查询：

```
-- 为用户登录查询创建覆盖索引
CREATE INDEX idx_users_login_covering ON users(username, email, status, id);

-- 为城市统计查询创建覆盖索引
CREATE INDEX idx_users_city_stats ON users(city, status, age, id);

-- 为年龄分析查询创建覆盖索引
CREATE INDEX idx_users_age_analysis ON users(age, city, status, username);
```

覆盖索引的实际应用场景：

```
-- 场景1：用户登录验证（使用覆盖索引）
SELECT id, username, email, status
FROM users 
WHERE username = 'zhangsan' AND status = 'active';

-- 场景2：城市用户统计（使用覆盖索引）
SELECT city, status, COUNT(*) AS user_count, AVG(age) AS avg_age
FROM users 
WHERE city = '上海'
GROUP BY city, status;

-- 场景3：年龄段分析（使用覆盖索引）
SELECT age, city, COUNT(*) AS user_count
FROM users 
WHERE age BETWEEN 25 AND 35
GROUP BY age, city;
```

使用EXPLAIN验证这些查询是否使用了覆盖索引：

```
-- 验证场景1
EXPLAIN SELECT id, username, email, status
FROM users 
WHERE username = 'zhangsan' AND status = 'active';

-- 验证场景2
EXPLAIN SELECT city, status, COUNT(*) AS user_count, AVG(age) AS avg_age
FROM users 
WHERE city = '上海'
GROUP BY city, status;

-- 验证场景3
EXPLAIN SELECT age, city, COUNT(*) AS user_count
FROM users 
WHERE age BETWEEN 25 AND 35
GROUP BY age, city;
```

覆盖索引的优势：

1. **减少I/O操作**：无需访问数据行，直接从索引获取数据
2. **提高查询性能**：索引通常比数据表小，可以全部装入内存
3. **避免锁竞争**：只访问索引，减少对数据表的锁定

覆盖索引的限制：

1. **索引大小**：包含过多字段会增加索引大小，影响维护成本
2. **更新开销**：索引字段更新时需要维护索引，增加写入成本
3. **存储空间**：占用更多的磁盘空间

让我们演示覆盖索引的性能差异：

```
-- 不使用覆盖索引的查询
SELECT sql_no_cache id, username, city, status, email
FROM users 
WHERE city = '北京';

-- 使用覆盖索引的查询
SELECT sql_no_cache id, username, city, status, email
FROM users 
WHERE city = '北京';
```

**前缀索引**也可以用于覆盖索引，特别是对于长文本字段：

```
-- 为profile_text创建前缀索引用于覆盖
CREATE INDEX idx_users_profile_covering ON users(id, profile_text(50));
```

**延迟关联**是覆盖索引的一个高级应用，适用于需要访问大文本字段但查询条件相对简单的情况：

```
-- 使用延迟关联优化大文本查询
SELECT u.id, u.username, u.city, u.profile_text
FROM users u
JOIN (
    SELECT id 
    FROM users 
    WHERE city = '北京' 
    ORDER BY registration_date DESC 
    LIMIT 5
) AS temp ON u.id = temp.id;
```

这种写法先使用索引快速定位到符合条件的用户ID，然后再关联查询完整数据，避免了全表扫描。

覆盖索引是查询优化的重要手段，但需要权衡查询性能和写入成本。在实际应用中，我们应该为频繁执行的、性能要求高的查询创建合适的覆盖索引，同时避免过度索引导致的维护问题。

## [14.5 前缀匹配与函数对索引的影响](#_14-5-前缀匹配与函数对索引的影响)

索引的使用并不是绝对的，某些查询模式会导致索引失效，从而影响查询性能。了解前缀匹配和函数对索引的影响，有助于我们写出更高效的SQL查询。

让我们基于users表来演示不同查询模式对索引的影响：

```
-- 当前users表的索引
SHOW INDEX FROM users;
```

**前缀匹配**对索引的影响是LIKE查询中的重要概念。前缀匹配（pattern%）通常可以使用索引，而后缀匹配（%pattern）和中间匹配（%pattern%）通常无法使用索引：

```
-- 前缀匹配：可以使用索引
EXPLAIN SELECT * FROM users WHERE username LIKE 'user%';

-- 后缀匹配：无法使用索引
EXPLAIN SELECT * FROM users WHERE username LIKE '%001';

-- 中间匹配：无法使用索引
EXPLAIN SELECT * FROM users WHERE username LIKE '%ser%';

-- 精确匹配：可以使用索引
EXPLAIN SELECT * FROM users WHERE username = 'user001';
```

让我们执行这些查询并观察结果：

```
-- 前缀匹配查询
SELECT * FROM users WHERE username LIKE 'user%';
```

执行结果：

```
+----+-----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
| id | username  | email             | phone       | age  | city   | registration_date   | last_login          | status   | profile_text    | created_at          | username_upper |
+----+-----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
|  1 | user001   | user001@example.com | 13800138001 |   25 | 北京   | 2025-01-01          | 2025-08-30 10:00:00 | active   | 普通用户        | 2025-08-31 15:30:00 | USER001       |
|  2 | user002   | user002@example.com | 13800138002 |   30 | 上海   | 2025-01-02          | 2025-08-29 11:00:00 | active   | VIP用户          | 2025-08-31 15:30:00 | USER002       |
|  3 | user003   | user003@example.com | 13800138003 |   28 | 广州   | 2025-01-03          | 2025-08-28 12:00:00 | inactive | 普通用户        | 2025-08-31 15:30:00 | USER003       |
|  4 | user004   | user004@example.com | 13800138004 |   35 | 深圳   | 2025-01-04          | 2025-08-27 13:00:00 | active   | 企业用户        | 2025-08-31 15:30:00 | USER004       |
|  5 | user005   | user005@example.com | 13800138005 |   22 | 杭州   | 2025-01-05          | 2025-08-26 14:00:00 | banned   | 普通用户        | 2025-08-31 15:30:00 | USER005       |
|  6 | user006   | user006@example.com | 13800138006 |   40 | 成都   | 2025-01-06          | 2025-08-25 15:00:00 | active   | VIP用户          | 2025-08-31 15:30:00 | USER006       |
|  7 | user007   | user007@example.com | 13800138007 |   26 | 武汉   | 2025-01-07          | 2025-08-24 16:00:00 | active   | 普通用户        | 2025-08-31 15:30:00 | USER007       |
|  8 | user008   | user008@example.com | 13800138008 |   32 | 西安   | 2025-01-08          | 2025-08-23 17:00:00 | inactive | 企业用户        | 2025-08-31 15:30:00 | USER008       |
|  9 | user009   | user009@example.com | 13800138009 |   29 | 南京   | 2025-01-09          | 2025-08-22 18:00:00 | active   | 普通用户        | 2025-08-31 15:30:00 | USER009       |
| 10 | user010   | user010@example.com | 13800138010 |   31 | 天津   | 2025-01-10          | 2025-08-21 19:00:00 | active   | VIP用户          | 2025-08-31 15:30:00 | USER010       |
+----+-----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
10 rows in set (0.00 sec)
```

```
-- 后缀匹配查询
SELECT * FROM users WHERE username LIKE '%001';
```

执行结果：

```
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
| id | username | email             | phone       | age  | city   | registration_date   | last_login          | status   | profile_text    | created_at          | username_upper |
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
|  1 | user001  | user001@example.com | 13800138001 |   25 | 北京   | 2025-01-01          | 2025-08-30 10:00:00 | active   | 普通用户        | 2025-08-31 15:30:00 | USER001       |
+----+----------+-------------------+-------------+------+--------+---------------------+---------------------+----------+-----------------+---------------------+---------------+
1 row in set (0.00 sec)
```

**函数操作**对索引的影响也很重要。在索引列上使用函数通常会导致索引失效：

```
-- 在索引列上使用函数：索引失效
EXPLAIN SELECT * FROM users WHERE UPPER(username) = 'USER001';

-- 在索引列上使用函数：索引失效
EXPLAIN SELECT * FROM users WHERE LENGTH(username) = 7;

-- 在索引列上使用计算：索引失效
EXPLAIN SELECT * FROM users WHERE id + 1 = 2;

-- 在索引列上使用类型转换：索引失效
EXPLAIN SELECT * FROM users WHERE CONCAT(username, '@example.com') = email;
```

为了解决函数索引的问题，我们可以添加一个规范化的字段：

```
-- 添加规范化字段并创建索引
ALTER TABLE users ADD COLUMN username_upper VARCHAR(50);
UPDATE users SET username_upper = UPPER(username);
CREATE INDEX idx_users_username_upper ON users(username_upper);

-- 现在可以使用索引
EXPLAIN SELECT * FROM users WHERE username_upper = 'USER001';
```

**隐式类型转换**也会导致索引失效：

```
-- 字符串列与数字比较：可能导致索引失效
EXPLAIN SELECT * FROM users WHERE id = '1';  -- 字符串与数字比较

-- 正确的写法：保持类型一致
EXPLAIN SELECT * FROM users WHERE id = 1;
```

**NULL值处理**对索引的影响：

```
-- IS NULL查询可以使用索引
EXPLAIN SELECT * FROM users WHERE last_login IS NULL;

-- IS NOT NULL查询可以使用索引
EXPLAIN SELECT * FROM users WHERE last_login IS NOT NULL;
```

**OR条件**对索引的影响：

```
-- OR条件可能无法有效使用索引
EXPLAIN SELECT * FROM users WHERE username = 'user001' OR email = 'user002@example.com';

-- 替代方案：使用UNION
EXPLAIN SELECT * FROM users WHERE username = 'user001'
UNION
SELECT * FROM users WHERE email = 'user002@example.com';
```

**NOT操作**对索引的影响：

```
-- NOT EQUAL可能无法使用索引
EXPLAIN SELECT * FROM users WHERE username != 'user001';

-- 替代方案：使用具体的条件
EXPLAIN SELECT * FROM users WHERE username > 'user001' OR username < 'user001';
```

**范围查询**对索引的影响：

```
-- 范围查询可以使用索引，但可能影响后续字段的索引使用
EXPLAIN SELECT * FROM users WHERE id > 5 AND username = 'user006';

-- 在联合索引中，范围查询后面的字段可能无法使用索引
CREATE INDEX idx_id_username ON users(id, username);
EXPLAIN SELECT * FROM users WHERE id > 5 AND username = 'user006';
```

**排序操作**对索引的影响：

```
-- 如果ORDER BY使用索引列，可以避免filesort
EXPLAIN SELECT * FROM users WHERE city = '北京' ORDER BY id;

-- 如果ORDER BY不使用索引列，可能产生filesort
EXPLAIN SELECT * FROM users WHERE city = '北京' ORDER BY username;
```

让我们创建一个专门的测试来演示这些概念：

```
-- 创建测试索引
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_city_status ON users(city, status);

-- 测试前缀匹配
EXPLAIN SELECT * FROM users WHERE username LIKE 'user%';
EXPLAIN SELECT * FROM users WHERE username LIKE '%001';

-- 测试函数操作
EXPLAIN SELECT * FROM users WHERE UPPER(username) = 'USER001';
EXPLAIN SELECT * FROM users WHERE username_upper = 'USER001';

-- 测试OR条件
EXPLAIN SELECT * FROM users WHERE username = 'user001' OR email = 'user002@example.com';

-- 测试范围查询
EXPLAIN SELECT * FROM users WHERE id BETWEEN 3 AND 7;
```

理解这些索引失效的场景有助于我们写出更高效的SQL查询。在实际应用中，我们应该：

1. 避免在索引列上使用函数
2. 注意类型匹配，避免隐式类型转换
3. 尽量使用前缀匹配而不是后缀匹配
4. 考虑使用UNION替代复杂的OR条件
5. 合理设计联合索引，避免范围查询影响后续字段的使用

## [14.6 常见误区与索引清理](#_14-6-常见误区与索引清理)

索引使用中存在很多常见的误区，这些误区不仅无法提高查询性能，还可能增加系统负担。了解这些误区并掌握索引清理的方法，有助于我们维护高效的数据库系统。

让我们基于users表来演示常见的索引误区：

```
-- 首先查看当前的索引情况
SHOW INDEX FROM users;
```

**误区一：索引越多越好**

很多开发者认为索引越多，查询性能越好。实际上，过多的索引会带来很多问题：

- 增加写入成本：每次INSERT、UPDATE、DELETE都需要维护索引
- 占用存储空间：索引占用额外的磁盘空间
- 影响查询优化：过多的索引可能让优化器选择错误的执行计划

让我们创建一些不必要的索引来演示这个问题：

```
-- 创建不必要的索引
CREATE INDEX idx_users_registration_date ON users(registration_date);
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_users_last_login ON users(last_login);
CREATE INDEX idx_users_profile_text ON users(profile_text(50));

-- 查看索引数量
SELECT COUNT(*) AS index_count 
FROM information_schema.statistics 
WHERE table_name = 'users';
```

**误区二：重复和冗余索引**

重复索引是指在相同列上创建多个索引，冗余索引是指已有索引的前缀索引。这些索引不仅浪费空间，还会影响性能：

```
-- 创建重复索引
CREATE INDEX idx_users_username_duplicate ON users(username);  -- 与已有的idx_users_username重复

-- 创建冗余索引
CREATE INDEX idx_users_city ON users(city);  -- 如果已有idx_users_city_status，这是冗余的
CREATE INDEX idx_users_city_status ON users(city, status);

-- 识别重复索引
SELECT 
    s.table_name,
    s.index_name,
    s.column_name,
    s.seq_in_index
FROM information_schema.statistics s
WHERE s.table_name = 'users'
ORDER BY s.column_name, s.seq_in_index;
```

**误区三：低选择性字段的索引**

对于选择性很低的字段（如性别、状态等），创建索引可能效果不佳：

```
-- 计算字段的选择性
SELECT 
    'status' AS column_name,
    COUNT(DISTINCT status) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT status) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users

UNION ALL

SELECT 
    'city' AS column_name,
    COUNT(DISTINCT city) AS distinct_values,
    COUNT(*) AS total_values,
    ROUND(COUNT(DISTINCT city) / COUNT(*) * 100, 2) AS selectivity_ratio
FROM users;
```

**误区四：从不使用的索引**

很多索引创建后从未被使用，只是占用资源。我们可以使用Performance Schema来监控索引使用情况：

```
-- 查看索引使用情况（需要MySQL Performance Schema）
SELECT 
    object_schema,
    object_name,
    index_name,
    count_star,
    count_read,
    count_fetch
FROM performance_schema.table_io_waits_summary_by_index_usage
WHERE object_name = 'users'
ORDER BY count_star DESC;
```

**索引清理策略**：

1. **删除重复索引**：

```
-- 删除重复的username索引
DROP INDEX idx_users_username_duplicate ON users;
```

2. **删除冗余索引**：

```
-- 分析冗余索引
-- 如果已有idx_users_city_status，则单独的idx_users_city可能是冗余的
-- 但删除前需要确认没有查询只依赖city字段
```

3. **删除未使用的索引**：

```
-- 基于使用情况统计删除未使用的索引
-- 但需要确保这些索引在高峰期或特殊场景下不需要
```

4. **合并相关索引**：

```
-- 考虑将相关索引合并为更合理的联合索引
-- 例如，如果有idx_users_city和idx_users_status，可以考虑创建idx_users_city_status
```

让我们创建一个索引维护的存储过程：

```
-- 创建索引分析存储过程
DELIMITER //
CREATE PROCEDURE analyze_user_indexes()
BEGIN
    -- 显示当前所有索引
    SELECT 'Current Indexes' AS analysis_type, table_name, index_name, column_name, seq_in_index
    FROM information_schema.statistics
    WHERE table_name = 'users'
    ORDER BY index_name, seq_in_index;
    
    -- 显示可能的重复索引
    SELECT 'Potential Duplicates' AS analysis_type, 
           GROUP_CONCAT(index_name) AS duplicate_indexes,
           column_name
    FROM information_schema.statistics
    WHERE table_name = 'users'
    GROUP BY column_name
    HAVING COUNT(*) > 1;
    
    -- 显示索引使用情况（如果Performance Schema可用）
    SELECT 'Usage Statistics' AS analysis_type,
           object_name,
           index_name,
           count_star,
           count_read,
           CASE 
               WHEN count_star = 0 THEN 'Unused'
               WHEN count_star < 10 THEN 'Low Usage'
               ELSE 'Active'
           END AS usage_status
    FROM performance_schema.table_io_waits_summary_by_index_usage
    WHERE object_name = 'users'
    ORDER BY count_star DESC;
END //
DELIMITER ;

-- 执行分析
CALL analyze_user_indexes();
```

**索引优化的决策流程**：

1. **收集数据**：使用监控工具收集索引使用情况
2. **分析使用率**：识别长期未使用的索引
3. **评估依赖关系**：确认删除索引不会影响关键查询
4. **测试环境验证**：在测试环境中验证删除索引的影响
5. **分批删除**：在生产环境中分批删除，观察系统表现
6. **监控效果**：删除后持续监控系统性能

让我们清理一些不必要的索引：

```
-- 删除不必要的索引
DROP INDEX idx_users_registration_date ON users;
DROP INDEX idx_users_created_at ON users;
DROP INDEX idx_users_last_login ON users;
DROP INDEX idx_users_profile_text ON users;
DROP INDEX idx_users_username_duplicate ON users;

-- 验证清理结果
SHOW INDEX FROM users;
```

**索引监控和定期维护**：

```
-- 创建索引监控表
DROP TABLE IF EXISTS index_monitoring;
CREATE TABLE index_monitoring (
    id INT PRIMARY KEY AUTO_INCREMENT,
    table_name VARCHAR(100) NOT NULL,
    index_name VARCHAR(100) NOT NULL,
    check_date DATE NOT NULL,
    usage_count BIGINT DEFAULT 0,
    size_mb DECIMAL(10,2) DEFAULT 0,
    status ENUM('active', 'review', 'drop_candidate') DEFAULT 'active',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 记录当前索引状态
INSERT INTO index_monitoring (table_name, index_name, check_date, status)
SELECT 
    'users' AS table_name,
    index_name,
    CURDATE() AS check_date,
    'active' AS status
FROM information_schema.statistics
WHERE table_name = 'users'
AND index_name != 'PRIMARY';
```

索引清理是一个需要谨慎操作的过程。我们应该建立完善的监控机制，定期分析索引使用情况，在保证系统性能的前提下，删除不必要的索引，优化索引结构。

记住，索引优化是一个持续的过程，需要根据业务变化和查询模式的变化不断调整。合理的索引策略能够显著提高数据库性能，而不合理的索引则可能成为系统的负担。

## [练习题](#练习题)

### [练习1：创建合适的索引](#练习1-创建合适的索引)

为以下查询场景创建合适的索引，并解释为什么选择这些索引：

```
-- 查询1：按用户名查找用户
SELECT * FROM users WHERE username = 'user001';

-- 查询2：按邮箱和状态查找用户
SELECT * FROM users WHERE email = 'user001@example.com' AND status = 'active';

-- 查询3：按注册日期范围查询用户
SELECT * FROM users WHERE registration_date BETWEEN '2025-01-01' AND '2025-01-31';

-- 查询4：统计每个城市的用户数量
SELECT city, COUNT(*) AS user_count FROM users GROUP BY city;

-- 查询5：按用户名前缀搜索
SELECT * FROM users WHERE username LIKE 'user%';
```

查看答案

```
-- 为查询1创建唯一索引（用户名通常需要唯一）
CREATE UNIQUE INDEX idx_users_username ON users(username);

-- 为查询2创建联合索引
CREATE INDEX idx_users_email_status ON users(email, status);

-- 为查询3创建范围查询索引
CREATE INDEX idx_users_registration_date ON users(registration_date);

-- 为查询4创建分组查询索引
CREATE INDEX idx_users_city ON users(city);

-- 为查询5创建前缀搜索索引
CREATE INDEX idx_users_username_prefix ON users(username);

-- 解释：
-- 1. 用户名需要唯一性约束，使用唯一索引
-- 2. 邮箱和状态的联合查询，创建联合索引提高查询效率
-- 3. 日期范围查询，单字段索引即可
-- 4. 分组统计查询，在分组字段上创建索引
-- 5. 前缀搜索可以使用索引，提高搜索效率
```

### [练习2：优化索引设计](#练习2-优化索引设计)

分析下面的索引使用情况，找出问题并提出优化方案：

```
-- 当前users表的索引
SHOW INDEX FROM users;

-- 常见查询模式
SELECT * FROM users WHERE city = '北京' AND status = 'active';
SELECT * FROM users WHERE username_upper = 'USER001' AND status = 'active';
SELECT * FROM users WHERE age BETWEEN 25 AND 35 AND city = '上海';
SELECT city, status, COUNT(*) FROM users GROUP BY city, status;
SELECT * FROM users WHERE email = 'test@example.com';
```

查看答案

```
-- 优化后的索引方案：

-- 保留重要的单字段索引
CREATE UNIQUE INDEX idx_users_username ON users(username);
CREATE UNIQUE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_age ON users(age);

-- 创建重要的联合索引
CREATE INDEX idx_users_city_status ON users(city, status);
CREATE INDEX idx_users_city_age ON users(city, age);
CREATE INDEX idx_users_username_status ON users(username, status);

-- 为分组查询创建索引
CREATE INDEX idx_users_city_status_group ON users(city, status);

-- 删除不必要的索引
DROP INDEX idx_users_phone ON users;  -- 如果phone查询不频繁
DROP INDEX idx_users_registration_date ON users;  -- 如果日期范围查询不频繁

-- 优化说明：
-- 1. 保留了唯一性约束所需的索引
-- 2. 为常用查询模式创建了合适的联合索引
-- 3. 为分组统计查询创建了专门的索引
-- 4. 删除了不常用的索引，减少维护成本
```

### [练习3：识别索引失效的场景](#练习3-识别索引失效的场景)

分析下面的SQL查询，指出哪些会导致索引失效，并提出优化方案：

```
-- 查询1
SELECT * FROM users WHERE UPPER(username) = 'USER001';

-- 查询2
SELECT * FROM users WHERE email LIKE '%example.com';

-- 查询3
SELECT * FROM users WHERE id = '1';  -- id是INT类型

-- 查询4
SELECT * FROM users WHERE username = 'user001' OR email = 'user002@example.com';

-- 查询5
SELECT * FROM users WHERE registration_date + INTERVAL 7 DAY > '2025-01-01';
```

查看答案

```
-- 查询1：在索引列上使用函数，索引失效
-- 优化方案：使用已创建的username_upper字段
SELECT * FROM users WHERE username_upper = 'USER001';

-- 查询2：后缀匹配，索引失效
-- 优化方案：如果需要支持后缀搜索，考虑全文索引或存储反转字符串
CREATE FULLTEXT INDEX idx_users_email_fulltext ON users(email);
-- 或使用：SELECT * FROM users WHERE REVERSE(email) LIKE REVERSE('%example.com');

-- 查询3：隐式类型转换，索引失效
-- 优化方案：确保类型一致
SELECT * FROM users WHERE id = 1;  -- 使用数字而非字符串

-- 查询4：OR条件可能导致索引失效
-- 优化方案：使用UNION
SELECT * FROM users WHERE username = 'user001'
UNION
SELECT * FROM users WHERE email = 'user002@example.com';

-- 查询5：在索引列上使用计算，索引失效
-- 优化方案：将计算移到常量端
SELECT * FROM users WHERE registration_date > '2025-01-01' - INTERVAL 7 DAY;
```

## [常见坑](#常见坑)

### [坑1：索引不是越多越好](#坑1-索引不是越多越好)

很多初学者认为索引越多，查询性能越好。实际上，过多的索引会严重影响写入性能并增加维护成本。

**问题示例**：

```
-- 为每个字段都创建索引
CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_registration_date ON users(registration_date);
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_users_last_login ON users(last_login);
CREATE INDEX idx_users_profile_text ON users(profile_text(50));
```

**纠正方法**：根据查询需求选择性地创建索引：

```
-- 只为常用的查询条件创建索引
CREATE INDEX idx_users_city_status ON users(city, status);
CREATE INDEX idx_users_username_status ON users(username, status);
CREATE INDEX idx_users_email ON users(email);
```

### [坑2：忽略联合索引的最左前缀原则](#坑2-忽略联合索引的最左前缀原则)

很多开发者不理解联合索引的最左前缀原则，创建了索引却无法正确使用。

**问题示例**：

```
-- 创建联合索引
CREATE INDEX idx_users_city_age ON users(city, age);

-- 无法使用索引的查询
SELECT * FROM users WHERE age = 25;
```

**纠正方法**：理解并遵循最左前缀原则：

```
-- 能够使用索引的查询
SELECT * FROM users WHERE city = '北京' AND age = 25;
SELECT * FROM users WHERE city = '北京';

-- 如果需要按age查询，需要单独创建索引
CREATE INDEX idx_users_age ON users(age);
```

### [坑3：在索引列上使用函数或计算](#坑3-在索引列上使用函数或计算)

在索引列上使用函数或计算会导致索引失效，这是常见的错误。

**问题示例**：

```
-- 索引失效的查询
SELECT * FROM users WHERE UPPER(username) = 'USER001';
SELECT * FROM users WHERE LENGTH(username) = 7;
SELECT * FROM users WHERE YEAR(registration_date) = 2025;
```

**纠正方法**：避免在索引列上使用函数：

```
-- 索引有效的查询
SELECT * FROM users WHERE username_upper = 'USER001';
SELECT * FROM users WHERE username = 'user001';
SELECT * FROM users WHERE registration_date BETWEEN '2025-01-01' AND '2025-12-31';
```

## [速记卡](#速记卡)

- **索引**：提高查询性能的数据结构，类似于书的目录
- **主键索引**：唯一标识记录的特殊索引，自动创建
- **唯一索引**：确保列值唯一，允许NULL值
- **普通索引**：最基本的索引类型，用于提高查询性能
- **联合索引**：在多个列上创建的索引，遵循最左前缀原则
- **全文索引**：用于文本内容的全文搜索
- **哈希索引**：只支持等值比较，查询速度快但功能有限
- **覆盖索引**：包含查询所需所有字段的索引，避免回表
- **回表**：通过索引找到数据行位置后再查询完整数据的过程
- **最左前缀原则**：联合索引必须从最左列开始才能使用
- **前缀索引**：只索引字段的前N个字符，节省空间
- **选择性**：字段中不同值的比例，高选择性字段更适合索引
- **索引失效场景**：函数操作、隐式转换、后缀匹配等
- **索引优化原则**：根据查询需求创建，避免过度索引

## [章节总结](#章节总结)

在这一章中，我们学习了数据库索引的核心知识，这是数据库性能优化的重要内容。从索引的基本概念开始，我们了解了索引就像书的目录一样，能够大大提高数据查询的效率。

常见索引类型各有特点：主键索引用于唯一标识记录，唯一索引保证数据唯一性，普通索引提高查询性能，联合索引支持多条件查询，全文索引用于文本搜索，哈希索引提供快速等值查找。理解这些索引类型的特点，有助于我们在实际应用中选择合适的索引策略。

索引的创建和管理是数据库维护的重要工作。我们学习了如何使用CREATE INDEX和ALTER TABLE创建索引，如何遵循命名规范，如何查看和删除索引。良好的索引命名和管理习惯能够让数据库维护更加清晰和高效。

选择合适的索引列和确定正确的列顺序是索引设计的关键。高选择性原则、覆盖查询原则、区分度优先原则等都是设计索引时需要考虑的重要因素。合理的索引设计能够大大提高查询性能，而不恰当的索引则可能成为系统的负担。

覆盖索引是查询优化的重要手段。通过设计包含查询所需所有字段的索引，可以避免回表操作，显著提高查询性能。理解覆盖索引的概念，有助于我们设计出更高效的索引策略。

索引的使用有很多限制和注意事项。前缀匹配可以使用索引，但后缀匹配和中间匹配通常无法使用索引；在索引列上使用函数会导致索引失效；隐式类型转换、OR条件、NOT操作等都可能影响索引的使用。了解这些限制，有助于我们写出更高效的SQL查询。

索引使用中存在很多常见误区，如认为索引越多越好、忽视最左前缀原则、在索引列上使用函数等。识别这些误区并掌握索引清理的方法，有助于我们维护高效的数据库系统。

掌握了索引技术，你就能够让数据库查询性能得到质的提升。索引优化是一个持续的过程，需要根据业务变化和查询模式的变化不断调整。合理的索引策略是高性能数据库系统的基础。在下一章中，我们将开始实战应用，综合运用前面学到的知识解决实际问题。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [14｜索引：如何创建索引？](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-索引-如何创建索引)
- [14.1 常见索引类型速览](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-1-常见索引类型速览)
- [14.2 创建与删除索引（语法与命名）](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-2-创建与删除索引-语法与命名)
- [14.3 如何选列与确定列顺序](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-3-如何选列与确定列顺序)
- [14.4 覆盖索引与"回表"](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-4-覆盖索引与-回表)
- [14.5 前缀匹配与函数对索引的影响](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-5-前缀匹配与函数对索引的影响)
- [14.6 常见误区与索引清理](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#_14-6-常见误区与索引清理)
- [练习题](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#练习题)
- [练习1：创建合适的索引](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#练习1-创建合适的索引)
- [练习2：优化索引设计](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#练习2-优化索引设计)
- [练习3：识别索引失效的场景](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#练习3-识别索引失效的场景)
- [常见坑](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#常见坑)
- [坑1：索引不是越多越好](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#坑1-索引不是越多越好)
- [坑2：忽略联合索引的最左前缀原则](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#坑2-忽略联合索引的最左前缀原则)
- [坑3：在索引列上使用函数或计算](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#坑3-在索引列上使用函数或计算)
- [速记卡](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part3/14-indexing.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
