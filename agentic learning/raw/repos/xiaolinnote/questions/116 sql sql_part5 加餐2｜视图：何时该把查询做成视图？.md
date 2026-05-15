---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part5/supplement2-views.html"
source: "https://xiaolinnote.com/sql/sql_part5/supplement2-views.html"
last_checked: 2026-05-07
freshness: watch
sha256: 4562746944f37cf35f40cbf8e73670b086c90b7b88fc989b5a33688dd8bd6d51
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 加餐2｜视图：何时该把查询做成视图？

原始链接：https://xiaolinnote.com/sql/sql_part5/supplement2-views.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 15 分钟约 4474 字2025/8/31

---


大家好，我是小林。

在前面的学习中，我们经常需要写一些复杂的SQL查询，比如多表连接、分组统计等。你有没有遇到过这样的情况：同样的复杂查询需要在多个地方重复使用，或者想限制某些用户只能看到特定的数据列，或者希望简化复杂的查询逻辑？

想象一下，在一个电商系统中，财务部门经常需要查看"已完成订单的统计信息"，客服部门需要查看"用户的基本信息和订单状态"，而管理层需要查看"销售报表"。如果每个部门都需要重复编写复杂的连接查询，不仅效率低下，而且维护起来也很困难。

这时候，视图就派上用场了。视图就像是一个"保存好的查询"，我们可以把复杂的SQL语句保存为一个视图，然后像操作普通表一样来查询它。这样不仅能大大简化查询，还能提供更好的数据安全性。

在这一章中，我们将学习什么是视图，如何创建和使用视图，以及在实际工作中什么时候应该使用视图。准备好了吗？让我们一起进入视图的世界吧！

## [视图是什么 & 适用场景](#视图是什么-适用场景)

用最简单的话来说，**视图就是一个保存好的查询语句**。你可以把视图想象成一个"虚拟的表"，这个表不实际存储数据，而是每次查询时都动态执行底层的SQL语句来生成结果。

让我用一个生活中的例子来解释：假设你有一个很复杂的菜谱（复杂的SQL查询），每次做菜都要重新看一遍菜谱很麻烦。于是你把这个菜谱保存到手机里（创建视图），下次做菜时直接打开手机查看（查询视图），这样就方便多了。

视图有几个重要的适用场景：

**复用复杂查询**：当一个复杂的连接查询需要在多个地方使用时，我们可以把它保存为视图。比如，经常需要查询"用户及其订单信息"的统计：

```
-- 每次都要写这么长的查询
SELECT u.username, u.city, COUNT(o.id) as order_count, SUM(o.amount) as total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username, u.city;
```

如果这个查询经常使用，就可以创建为视图：

```
CREATE VIEW v_user_order_stats AS
SELECT u.username, u.city, COUNT(o.id) as order_count, SUM(o.amount) as total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username, u.city;
```

之后就可以简单地查询：

```
SELECT * FROM v_user_order_stats WHERE city = '北京';
```

**字段隔离**：当想让不同的用户看到不同的字段时，视图可以起到数据屏蔽的作用。比如，给客服部门一个只包含用户基本信息和订单状态的视图，而不包含敏感的金额信息：

```
CREATE VIEW v_customer_service AS
SELECT u.username, u.email, u.city, o.id as order_id, o.product_name, o.status
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**权限收口**：通过视图可以精确控制用户能访问哪些数据。比如，创建一个只能查看北京地区用户数据的视图，然后只给特定用户这个视图的访问权限。

当然，视图也不是万能的，有一些场景不适合使用视图：

- 表结构经常变化：如果底层表结构经常变动，维护视图会很麻烦
- 对性能要求极高的场景：视图每次查询都要重新执行底层SQL，可能影响性能
- 需要索引优化的复杂查询：视图本身不能创建索引

## [最小示例：创建/查询/删除](#最小示例-创建-查询-删除)

让我们通过一个完整的例子来学习视图的基本操作。首先，我们需要准备一些测试数据：

```
-- 创建测试表（如果还没有的话）
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 插入测试数据
INSERT INTO users (username, email, city, phone) VALUES 
('张三', 'zhangsan@example.com', '北京', '13800138000'),
('李四', 'lisi@example.com', '上海', '13900139000'),
('王五', 'wangwu@example.com', '广州', '13700137000'),
('赵六', 'zhaoliu@example.com', '深圳', '13600136000'),
('钱七', 'qianqi@example.com', '杭州', '13500135000');

INSERT INTO orders (user_id, product_name, amount, status, order_date) VALUES 
(1, 'iPhone 15', 5999.00, 'completed', '2025-08-01 10:00:00'),
(1, 'AirPods', 1299.00, 'completed', '2025-08-02 14:30:00'),
(2, '小米13', 3999.00, 'completed', '2025-08-03 09:15:00'),
(3, 'MacBook Pro', 12999.00, 'pending', '2025-08-04 16:45:00'),
(4, 'iPad', 4599.00, 'completed', '2025-08-05 11:20:00'),
(5, '华为P60', 4999.00, 'cancelled', '2025-08-06 13:10:00'),
(1, 'Apple Watch', 2999.00, 'completed', '2025-08-10 17:15:00');
```

现在让我们创建几个不同类型的视图：

### [创建用户订单统计视图](#创建用户订单统计视图)

```
-- 创建用户订单统计视图
CREATE VIEW v_user_order_stats AS
SELECT 
    u.id,
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_amount,
    MAX(o.order_date) AS last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username, u.city;
```

创建成功后，我们可以像查询普通表一样查询这个视图：

```
-- 查询所有用户的订单统计
SELECT * FROM v_user_order_stats;

-- 查询北京用户的订单统计
SELECT username, order_count, total_amount 
FROM v_user_order_stats 
WHERE city = '北京';

-- 查询订单金额超过5000的用户
SELECT username, city, total_amount
FROM v_user_order_stats
WHERE total_amount > 5000
ORDER BY total_amount DESC;
```

执行结果示例：

```
+----+----------+--------+------------+--------------+---------------------+
| id | username | city   | order_count | total_amount | last_order_date      |
+----+----------+--------+------------+--------------+---------------------+
|  1 | 张三     | 北京   |          3 |     10297.00 | 2025-08-10 17:15:00 |
|  2 | 李四     | 上海   |          1 |      3999.00 | 2025-08-03 09:15:00 |
|  3 | 王五     | 广州   |          1 |     12999.00 | 2025-08-04 16:45:00 |
|  4 | 赵六     | 深圳   |          1 |      4599.00 | 2025-08-05 11:20:00 |
|  5 | 钱七     | 杭州   |          1 |      4999.00 | 2025-08-06 13:10:00 |
+----+----------+--------+------------+--------------+---------------------+
```

### [创建客服专用视图](#创建客服专用视图)

```
-- 创建客服专用视图，隐藏敏感信息
CREATE VIEW v_customer_service AS
SELECT 
    u.username,
    u.city,
    o.id AS order_id,
    o.product_name,
    o.status,
    o.order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NOT NULL;
```

查询客服视图：

```
-- 客服查看所有订单信息
SELECT * FROM v_customer_service ORDER BY order_date DESC;

-- 客服查看待处理的订单
SELECT username, product_name, order_date
FROM v_customer_service
WHERE status = 'pending';
```

### [创建财务专用视图](#创建财务专用视图)

```
-- 创建财务专用视图，只包含已完成的订单
CREATE VIEW v_finance_report AS
SELECT 
    u.username,
    u.city,
    o.product_name,
    o.amount,
    o.order_date
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE o.status = 'completed';
```

查询财务视图：

```
-- 财务查看已完成订单的销售额
SELECT city, SUM(amount) as city_revenue
FROM v_finance_report
GROUP BY city
ORDER BY city_revenue DESC;

-- 财务查看每日销售趋势
SELECT DATE(order_date) as sale_date, SUM(amount) as daily_sales
FROM v_finance_report
GROUP BY DATE(order_date)
ORDER BY sale_date;
```

### [查看和删除视图](#查看和删除视图)

当我们创建了很多视图后，可以通过以下方式查看现有的视图：

```
-- 查看当前数据库中的所有视图
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- 查看特定视图的定义
SHOW CREATE VIEW v_user_order_stats;

-- 查看视图结构（像普通表一样）
DESCRIBE v_user_order_stats;
```

如果不再需要某个视图，可以删除它：

```
-- 删除视图
DROP VIEW v_customer_service;

-- 删除多个视图
DROP VIEW IF EXISTS v_user_order_stats, v_finance_report;
```

注意：删除视图只是删除了视图的定义，不会影响底层的数据表。

### [视图命名建议](#视图命名建议)

为了便于管理，建议遵循一定的视图命名规范：

- 使用`v_`前缀表示视图
- 名字要能反映视图的用途
- 例如：`v_user_stats`（用户统计）、`v_customer_orders`（客户订单）、`v_department_XXX`（部门专用）

```
-- 好的命名示例
CREATE VIEW v_sales_monthly AS ...;
CREATE VIEW v_hr_employee_summary AS ...;
CREATE VIEW v_inventory_low_stock AS ...;
```

## [可更新限制与 CHECK OPTION](#可更新限制与-check-option)

视图不仅可以用来查询，某些情况下还可以用来更新数据。但是，可更新的视图有一些限制条件。

### [可更新视图的基本条件](#可更新视图的基本条件)

一个视图要能被更新，需要满足以下条件：

- 不能包含聚合函数（COUNT、SUM、AVG等）
- 不能包含GROUP BY、HAVING子句
- 不能包含DISTINCT关键字
- 不能包含UNION操作符
- 通常只基于单个表（某些多表视图也可更新，但较复杂）

让我们创建一个简单的可更新视图：

```
-- 创建一个简单的用户信息视图（可更新）
CREATE VIEW v_user_basic AS
SELECT id, username, email, city
FROM users;
```

这个视图可以用来更新数据：

```
-- 通过视图更新用户邮箱
UPDATE v_user_basic 
SET email = 'zhangsan_new@example.com' 
WHERE username = '张三';

-- 通过视图插入新用户
INSERT INTO v_user_basic (username, email, city)
VALUES ('新用户', 'newuser@example.com', '南京');

-- 验证更新和插入结果
SELECT * FROM v_user_basic WHERE username IN ('张三', '新用户');
```

### [WITH CHECK OPTION 的作用](#with-check-option-的作用)

有时候，我们希望通过视图更新的数据必须符合视图的WHERE条件。这时就需要用到`WITH CHECK OPTION`。

```
-- 创建北京用户的视图，并使用CHECK OPTION
CREATE VIEW v_beijing_users AS
SELECT id, username, email, city
FROM users
WHERE city = '北京'
WITH CHECK OPTION;
```

现在，让我们测试一下这个视图的限制：

```
-- 这是允许的：更新北京用户的信息
UPDATE v_beijing_users 
SET email = 'zhangsan_beijing@example.com' 
WHERE username = '张三';

-- 这会被拒绝：试图将北京用户改为其他城市
UPDATE v_beijing_users 
SET city = '上海' 
WHERE username = '张三';
```

执行第二个UPDATE语句时，MySQL会报错：

```
ERROR 1369 (HY000): CHECK OPTION failed 'test.v_beijing_users'
```

这是因为`WITH CHECK OPTION`确保了通过视图更新的数据仍然符合视图的定义条件（city = '北京'）。

### [CHECK OPTION 的实际用途](#check-option-的实际用途)

`WITH CHECK OPTION`在实际工作中很有用，比如：

- **区域数据隔离**：只允许各地区经理更新自己区域的数据
- **状态管理**：只允许将订单状态从"pending"改为"completed"，不能改为其他状态
- **数据一致性**：确保数据始终符合业务规则

```
-- 订单状态管理的例子
CREATE VIEW v_pending_orders AS
SELECT id, user_id, product_name, amount, status
FROM orders
WHERE status = 'pending'
WITH CHECK OPTION;

-- 允许：将pending订单改为completed
UPDATE v_pending_orders SET status = 'completed' WHERE id = 4;

-- 拒绝：将pending订单改为cancelled（如果业务不允许）
-- UPDATE v_pending_orders SET status = 'cancelled' WHERE id = 4;
```

## [性能与调试](#性能与调试)

虽然视图很方便，但了解其性能特点也很重要。MySQL中的视图是"非物化"的，这意味着视图本身不存储数据，每次查询视图时都会重新执行底层的SQL语句。

### [视图的工作原理](#视图的工作原理)

让我们通过一个例子来理解视图的性能特点：

```
-- 创建一个包含连接的视图
CREATE VIEW v_user_orders AS
SELECT 
    u.username,
    u.city,
    o.product_name,
    o.amount,
    o.order_date
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- 查询视图
EXPLAIN SELECT * FROM v_user_orders WHERE city = '北京';
```

你会发现，MySQL实际执行的是视图底层的完整查询，而不是简单地从某个存储结果中读取数据。这意味着视图的性能等同于直接执行底层SQL的性能。

### [使用EXPLAIN分析视图](#使用explain分析视图)

我们可以使用EXPLAIN来分析视图的执行计划：

```
-- 分析视图查询的执行计划
EXPLAIN SELECT * FROM v_user_order_stats WHERE total_amount > 5000;
```

通过执行计划，你可以看到MySQL是如何优化视图查询的，这有助于发现性能问题。

### [避免嵌套视图](#避免嵌套视图)

一个常见的性能陷阱是创建嵌套视图（基于其他视图创建视图）：

```
-- 不好的做法：嵌套视图
CREATE VIEW v_level1 AS SELECT * FROM users WHERE city = '北京';
CREATE VIEW v_level2 AS SELECT * FROM v_level1 WHERE username LIKE '张%';
CREATE VIEW v_level3 AS SELECT * FROM v_level2 WHERE id > 10;
```

每个嵌套层都会增加查询的复杂性，可能导致性能问题。更好的做法是创建直接的视图：

```
-- 好的做法：直接创建最终需要的视图
CREATE VIEW v_beijing_zhang_users AS
SELECT * FROM users 
WHERE city = '北京' AND username LIKE '张%' AND id > 10;
```

### [视图vs物化视图](#视图vs物化视图)

需要说明的是，MySQL的视图都是非物化的。有些数据库系统（如Oracle、PostgreSQL）支持物化视图，物化视图会实际存储查询结果，定期刷新，适合用于报表等场景。

在MySQL中，如果需要类似物化视图的功能，通常需要通过定时任务将结果存入汇总表来实现。

## [练习题](#练习题)

### [练习1：创建统计视图](#练习1-创建统计视图)

创建一个视图`v_product_sales`，统计每个产品的销售情况，包括产品名称、销售数量、销售总额和平均价格。

查看答案

```
-- 创建产品销售统计视图
CREATE VIEW v_product_sales AS
SELECT 
    product_name,
    COUNT(*) as sales_count,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_price,
    COUNT(DISTINCT user_id) as unique_customers
FROM orders
WHERE status = 'completed'
GROUP BY product_name;

-- 查询视图验证结果
SELECT * FROM v_product_sales ORDER BY total_revenue DESC;
```

### [练习2：创建带权限控制的视图](#练习2-创建带权限控制的视图)

创建一个客服专用视图`v_customer_service_safe`，只包含用户名、城市、订单ID、产品名称、订单状态，并且使用CHECK OPTION确保客服只能查询到有订单的用户。

查看答案

```
-- 创建客服专用安全视图
CREATE VIEW v_customer_service_safe AS
SELECT 
    u.username,
    u.city,
    o.id as order_id,
    o.product_name,
    o.status,
    o.order_date
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WITH CHECK OPTION;

-- 测试视图
SELECT * FROM v_customer_service_safe WHERE city = '北京';

-- 注意：这个视图不能用于插入新数据，因为要求必须有对应的订单
```

### [练习3：创建可更新视图](#练习3-创建可更新视图)

创建一个可更新的用户信息视图`v_user_manage`，只包含用户名、邮箱、城市字段，并使用CHECK OPTION确保只能更新城市为"北京"或"上海"的用户。

查看答案

```
-- 创建可更新的用户管理视图
CREATE VIEW v_user_manage AS
SELECT username, email, city
FROM users
WHERE city IN ('北京', '上海')
WITH CHECK OPTION;

-- 测试更新操作
UPDATE v_user_manage 
SET email = 'new_email@example.com' 
WHERE username = '张三';

-- 测试插入操作
INSERT INTO v_user_manage (username, email, city)
VALUES ('上海用户', 'shanghai@example.com', '上海');

-- 验证结果
SELECT * FROM v_user_manage;
```

## [常见坑](#常见坑)

### [坑1：误以为视图会提高查询性能](#坑1-误以为视图会提高查询性能)

很多初学者认为视图会缓存查询结果，从而提高性能。实际上，MySQL的视图每次查询都会重新执行底层SQL，性能等同于直接执行底层查询。

**纠正方法**：如果性能很重要，考虑使用物化方案（如汇总表）或优化底层查询，而不是依赖视图来提升性能。

### [坑2：在视图上创建索引](#坑2-在视图上创建索引)

有些初学者试图在视图上创建索引来提高查询性能。

**纠正方法**：不能在视图上创建索引。要优化性能，应该在底层表的相关列上创建合适的索引。

### [坑3：过度复杂的嵌套视图](#坑3-过度复杂的嵌套视图)

创建多层嵌套的视图，导致查询难以理解和维护，性能也很差。

**纠正方法**：避免嵌套视图，直接创建最终需要的简单视图。如果逻辑复杂，考虑使用存储过程或应用层逻辑。

## [速记卡](#速记卡)

- **视图定义**：视图是保存的SQL查询，是一个虚拟表，不存储实际数据
- **主要用途**：复用复杂查询、字段隔离、权限控制、简化查询逻辑
- **创建语法**：`CREATE VIEW view_name AS SELECT ...`
- **查询语法**：`SELECT * FROM view_name WHERE ...`（和普通表一样）
- **删除语法**：`DROP VIEW view_name`
- **可更新视图**：不能包含聚合、GROUP BY、DISTINCT等，通常基于单表
- **CHECK OPTION**：确保通过视图更新的数据符合视图定义条件
- **性能特点**：非物化视图，每次查询都重新执行底层SQL
- **命名建议**：使用`v_`前缀，名称反映用途，如`v_user_stats`
- **避免嵌套**：不要创建基于其他视图的嵌套视图

## [章节总结](#章节总结)

在这个加餐中，我们学习了MySQL视图的概念和使用方法。视图就像是一个保存好的查询，它不存储实际数据，而是每次查询时动态执行底层的SQL语句来生成结果。

我们了解了视图的几个主要应用场景：复用复杂查询让我们能够把常用的复杂SQL保存为视图，大大简化了日常查询工作；字段隔离通过视图可以控制用户能看到的字段，隐藏敏感信息；权限收口通过视图可以精确控制用户的数据访问权限。

通过实际例子，我们学习了视图的完整操作流程：从创建视图、查询视图，到删除视图。我们还学习了可更新视图的概念和限制条件，以及如何使用`WITH CHECK OPTION`来确保数据更新的安全性。

在性能方面，我们了解到MySQL的视图是非物化的，每次查询都会重新执行底层SQL，这意味着视图的性能等同于直接执行底层查询的性能。我们学习了如何使用EXPLAIN来分析视图查询的执行计划，以及如何避免嵌套视图这个常见的性能陷阱。

视图是数据库设计中的一个重要工具，它能帮助我们构建更安全、更易维护的数据库应用。掌握了视图的使用，你就能够在复杂的数据管理场景中更加游刃有余，既能简化查询逻辑，又能保证数据安全。

在实际工作中，合理使用视图可以大大提高开发效率和数据安全性。但也要记住，视图不是万能的，要了解它的适用场景和限制条件，避免在不合适的场景中使用视图。结合索引优化和查询重构，视图会成为你数据库工具箱中的重要利器。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [加餐2｜视图：何时该把查询做成视图？](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#加餐2-视图-何时该把查询做成视图)
- [视图是什么 & 适用场景](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#视图是什么-适用场景)
- [最小示例：创建/查询/删除](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#最小示例-创建-查询-删除)
- [创建用户订单统计视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#创建用户订单统计视图)
- [创建客服专用视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#创建客服专用视图)
- [创建财务专用视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#创建财务专用视图)
- [查看和删除视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#查看和删除视图)
- [视图命名建议](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#视图命名建议)
- [可更新限制与 CHECK OPTION](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#可更新限制与-check-option)
- [可更新视图的基本条件](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#可更新视图的基本条件)
- [WITH CHECK OPTION 的作用](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#with-check-option-的作用)
- [CHECK OPTION 的实际用途](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#check-option-的实际用途)
- [性能与调试](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#性能与调试)
- [视图的工作原理](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#视图的工作原理)
- [使用EXPLAIN分析视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#使用explain分析视图)
- [避免嵌套视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#避免嵌套视图)
- [视图vs物化视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#视图vs物化视图)
- [练习题](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#练习题)
- [练习1：创建统计视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#练习1-创建统计视图)
- [练习2：创建带权限控制的视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#练习2-创建带权限控制的视图)
- [练习3：创建可更新视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#练习3-创建可更新视图)
- [常见坑](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#常见坑)
- [坑1：误以为视图会提高查询性能](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#坑1-误以为视图会提高查询性能)
- [坑2：在视图上创建索引](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#坑2-在视图上创建索引)
- [坑3：过度复杂的嵌套视图](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#坑3-过度复杂的嵌套视图)
- [速记卡](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part5/supplement2-views.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
