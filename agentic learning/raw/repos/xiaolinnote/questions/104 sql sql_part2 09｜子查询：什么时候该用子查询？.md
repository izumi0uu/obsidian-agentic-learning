---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - interview
  - database
  - sql
status: inbox
created: 2026-05-07
updated: 2026-05-17
url: https://xiaolinnote.com/sql/sql_part2/09-subqueries.html
source: https://xiaolinnote.com/sql/sql_part2/09-subqueries.html
last_checked: 2026-05-17
freshness: watch
sha256: 777799679ba8287ca70709e74f32de5b986a79c9b9f8092c718cdc48b58f0d32
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 09｜子查询：什么时候该用子查询？

原始链接：https://xiaolinnote.com/sql/sql_part2/09-subqueries.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 09｜子查询：什么时候该用子查询？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 16 分钟约 4898 字2025/8/31

---

# [09｜子查询：什么时候该用子查询？](#_09-子查询-什么时候该用子查询)

大家好，我是小林。

在前面的章节中，我们学习了各种SQL查询技术，包括基本的SELECT查询、WHERE筛选、ORDER BY排序、GROUP BY分组和JOIN连接等。这些技术已经能够解决大多数数据查询需求。但在某些复杂场景下，我们可能需要在一个查询中嵌套另一个查询，这就是子查询技术。

你有没有想过，当你在电商网站上看到"价格高于平均价格的商品"时，系统是如何计算出平均价格然后筛选出高于这个价格的商品的？当你需要查询"购买了某个产品的所有用户"时，如何先找到这些产品的ID再查询对应的用户信息？当你需要分析"销售业绩超过部门平均水平的员工"时，如何先计算出部门平均水平再进行比较？

在这一章中，我们将学习如何使用子查询来解决这些复杂的数据查询需求。从WHERE子句中的子查询开始，到FROM子句中的派生表，再到子查询与JOIN的性能取舍。掌握了子查询技术，你就能够构建更加灵活和强大的SQL查询，解决那些单层查询难以处理的复杂业务问题。

准备好了吗？让我们开始学习子查询的奥秘吧！

## [9.1 WHERE 子查询](#_9-1-where-子查询)

WHERE子查询是最常用的子查询类型，它允许我们在WHERE子句中使用嵌套查询来筛选数据。WHERE子查询可以分为单值子查询、集合子查询和相关子查询等不同类型。

让我们创建一个电商数据库来演示各种子查询的使用：

```
-- 创建用户表
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    registration_date DATE,
    total_spent DECIMAL(10,2) DEFAULT 0.00
);

-- 创建商品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);

-- 创建订单表
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- 插入示例数据
INSERT INTO users (username, email, city, registration_date, total_spent) VALUES 
('张三', 'zhangsan@example.com', '北京', '2025-01-15', 15998.00),
('李四', 'lisi@example.com', '上海', '2025-02-20', 8999.00),
('王五', 'wangwu@example.com', '广州', '2025-03-10', 21998.00),
('赵六', 'zhaoliu@example.com', '深圳', '2025-04-05', 4999.00),
('钱七', 'qianqi@example.com', '杭州', '2025-05-12', 32994.00),
('孙八', 'sunba@example.com', '成都', '2025-06-18', 12999.00),
('周九', 'zhoujiu@example.com', '武汉', '2025-07-22', 7596.00),
('吴十', 'wushi@example.com', '西安', '2025-08-01', 3093.00);

INSERT INTO products (name, category, price, stock) VALUES 
('iPhone 15', '手机', 5999.00, 100),
('小米13', '手机', 3999.00, 150),
('华为P60', '手机', 4999.00, 80),
('MacBook Pro', '笔记本', 12999.00, 50),
('ThinkPad X1', '笔记本', 8999.00, 30),
('iPad Air', '平板', 4599.00, 120),
('Surface Pro', '平板', 6999.00, 40),
('AirPods Pro', '耳机', 1899.00, 200),
('小米手环', '智能穿戴', 299.00, 300),
('华为手表', '智能穿戴', 1299.00, 90);

INSERT INTO orders (user_id, product_id, quantity, order_date, amount) VALUES 
(1, 1, 2, '2025-08-01', 11998.00),
(1, 4, 1, '2025-08-02', 12999.00),
(2, 5, 1, '2025-08-03', 8999.00),
(3, 4, 1, '2025-08-04', 12999.00),
(3, 6, 2, '2025-08-05', 9198.00),
(4, 3, 1, '2025-08-06', 4999.00),
(5, 1, 3, '2025-08-07', 17997.00),
(5, 2, 1, '2025-08-08', 3999.00),
(5, 7, 1, '2025-08-09', 6999.00),
(6, 4, 1, '2025-08-10', 12999.00),
(7, 8, 4, '2025-08-11', 7596.00),
(8, 9, 5, '2025-08-12', 1495.00),
(8, 10, 2, '2025-08-13', 2598.00);
```

单值子查询返回单个值，通常用于比较操作。比如，我们可以查询价格高于平均价格的所有商品：

```
SELECT name, category, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| iPhone 15    | 手机      |  5999.00 |
| MacBook Pro  | 笔记本    | 12999.00 |
| ThinkPad X1  | 笔记本    |  8999.00 |
| Surface Pro  | 平板      |  6999.00 |
+--------------+-----------+----------+
4 rows in set (0.00 sec)
```

这个查询首先执行子查询`SELECT AVG(price) FROM products`计算出所有商品的平均价格，然后在主查询中筛选出价格高于这个平均价格的商品。从结果可以看出，有4个商品的价格高于平均水平。

集合子查询返回多个值，通常与IN、ANY、ALL等操作符一起使用。比如，我们可以查询购买了手机类产品的所有用户：

```
SELECT DISTINCT u.username, u.city
FROM users u
WHERE u.id IN (
    SELECT DISTINCT o.user_id
    FROM orders o
    JOIN products p ON o.product_id = p.id
    WHERE p.category = '手机'
);
```

执行结果：

```
+----------+--------+
| username | city   |
+----------+--------+
| 张三     | 北京   |
| 钱七     | 杭州   |
+----------+--------+
2 rows in set (0.00 sec)
```

这个查询的执行过程是：先从子查询中找出所有购买了手机类产品的用户ID，然后在主查询中找出这些用户的用户名和城市。从结果可以看出，张三和钱七购买了手机类产品。

EXISTS子查询用于检查子查询是否返回任何行，它只返回TRUE或FALSE。比如，我们可以查询有订单记录的用户：

```
SELECT u.username, u.city, u.total_spent
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
);
```

执行结果：

```
+----------+--------+-------------+
| username | city   | total_spent |
+----------+--------+-------------+
| 张三     | 北京   |    15998.00 |
| 李四     | 上海   |     8999.00 |
| 王五     | 广州   |    21998.00 |
| 赵六     | 深圳   |     4999.00 |
| 钱七     | 杭州   |    32994.00 |
| 孙八     | 成都   |    12999.00 |
| 周九     | 武汉   |     7596.00 |
| 吴十     | 西安   |     3093.00 |
+----------+--------+-------------+
8 rows in set (0.00 sec)
```

这个查询使用EXISTS检查每个用户是否有对应的订单记录。EXISTS子查询通常比IN子查询更高效，特别是当子查询返回大量数据时，因为EXISTS在找到第一个匹配项后就会停止搜索。

NOT EXISTS用于检查子查询是否不返回任何行。比如，我们可以查询没有订单记录的用户：

```
SELECT u.username, u.city, u.registration_date
FROM users u
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
);
```

执行结果：

```
Empty set (0.00 sec)
```

这个查询返回空结果，说明所有用户都有订单记录。

在实际应用中，WHERE子查询经常用于解决复杂的业务问题。比如，查询消费金额高于平均消费水平的用户：

```
SELECT username, city, total_spent
FROM users
WHERE total_spent > (
    SELECT AVG(total_spent) 
    FROM users
)
ORDER BY total_spent DESC;
```

执行结果：

```
+----------+--------+-------------+
| username | city   | total_spent |
+----------+--------+-------------+
| 钱七     | 杭州   |    32994.00 |
| 王五     | 广州   |    21998.00 |
| 张三     | 北京   |    15998.00 |
| 孙八     | 成都   |    12999.00 |
+----------+--------+-------------+
4 rows in set (0.00 sec)
```

这个查询先计算出所有用户的平均消费金额，然后筛选出消费金额高于这个平均水平的用户。从结果可以看出，有4个用户的消费水平高于平均。

## [9.2 FROM 子查询（派生表）](#_9-2-from-子查询-派生表)

FROM子查询也称为派生表，它允许我们在FROM子句中使用子查询来创建一个临时表，然后对这个临时表进行进一步的查询操作。这在需要进行多步数据处理时非常有用。

派生表的基本语法是将子查询放在FROM子句中，并为其指定一个别名。比如，我们可以查询每个类别的平均价格，然后找出高于总体平均价格的类别：

```
SELECT category_name, avg_price, overall_avg
FROM (
    SELECT 
        p.category AS category_name,
        AVG(p.price) AS avg_price
    FROM products p
    GROUP BY p.category
) category_stats
CROSS JOIN (
    SELECT AVG(price) AS overall_avg
    FROM products
) overall_stats
WHERE category_stats.avg_price > overall_stats.overall_avg;
```

执行结果：

```
+---------------+------------+-------------+
| category_name | avg_price  | overall_avg |
+---------------+------------+-------------+
| 笔记本        | 10999.0000 | 5075.100000 |
| 手机          |  4999.0000 | 5075.100000 |
+---------------+------------+-------------+
2 rows in set (0.00 sec)
```

这个查询创建了两个派生表：category\_stats包含每个类别的平均价格，overall\_stats包含所有商品的总体平均价格。然后我们连接这两个派生表，筛选出平均价格高于总体平均价格的类别。

派生表在复杂的数据分析中非常有用。比如，我们可以查询每个用户的消费统计信息，包括订单数量、总消费金额和平均订单金额：

```
SELECT 
    user_id,
    username,
    city,
    order_count,
    total_amount,
    avg_order_amount
FROM (
    SELECT 
        u.id AS user_id,
        u.username,
        u.city,
        COUNT(o.id) AS order_count,
        SUM(o.amount) AS total_amount,
        AVG(o.amount) AS avg_order_amount
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    GROUP BY u.id, u.username, u.city
) user_stats
WHERE order_count > 0
ORDER BY total_amount DESC;
```

执行结果：

```
+---------+----------+--------+------------+-------------+------------------+
| user_id | username | city   | order_count | total_amount | avg_order_amount |
+---------+----------+--------+------------+-------------+------------------+
|       5 | 钱七     | 杭州   |          3 |    28995.00 |        9665.0000 |
|       1 | 张三     | 北京   |          2 |    24997.00 |       12498.5000 |
|       3 | 王五     | 广州   |          2 |    22197.00 |       11098.5000 |
|       6 | 孙八     | 成都   |          1 |    12999.00 |       12999.0000 |
|       2 | 李四     | 上海   |          1 |     8999.00 |        8999.0000 |
|       4 | 赵六     | 深圳   |          1 |     4999.00 |        4999.0000 |
|       7 | 周九     | 武汉   |          1 |     7596.00 |        7596.0000 |
|       8 | 吴十     | 西安   |          2 |     4093.00 |        2046.5000 |
+---------+----------+--------+------------+-------------+------------------+
8 rows in set (0.00 sec)
```

这个查询首先创建了一个派生表user\_stats，包含每个用户的消费统计信息，然后从这个派生表中筛选出有订单记录的用户，并按总消费金额降序排列。

派生表还可以用于排名分析。比如，我们可以查询消费金额排名前3的用户：

```
SELECT *
FROM (
    SELECT 
        u.username,
        u.city,
        u.total_spent,
        RANK() OVER (ORDER BY u.total_spent DESC) AS spending_rank
    FROM users u
) ranked_users
WHERE spending_rank <= 3;
```

执行结果：

```
+----------+--------+-------------+--------------+
| username | city   | total_spent | spending_rank |
+----------+--------+-------------+--------------+
| 钱七     | 杭州   |    32994.00 |            1 |
| 王五     | 广州   |    21998.00 |            2 |
| 张三     | 北京   |    15998.00 |            3 |
+----------+--------+-------------+--------------+
3 rows in set (0.00 sec)
```

这个查询使用窗口函数RANK()为用户按消费金额排名，然后从派生表中筛选出排名前3的用户。

派生表在处理复杂计算时特别有用。比如，我们可以查询每个类别中价格最高的产品，以及这些产品与类别平均价格的差异：

```
SELECT 
    p.name,
    p.category,
    p.price,
    category_avg.avg_price,
    (p.price - category_avg.avg_price) AS price_diff
FROM products p
JOIN (
    SELECT 
        category,
        AVG(price) AS avg_price,
        MAX(price) AS max_price
    FROM products
    GROUP BY category
) category_avg ON p.category = category_avg.category
WHERE p.price = category_avg.max_price;
```

执行结果：

```
+--------------+-----------+----------+------------+------------+
| name         | category  | price    | avg_price  | price_diff |
+--------------+-----------+----------+------------+------------+
| iPhone 15    | 手机      |  5999.00 | 4999.0000 |   1000.00 |
| MacBook Pro  | 笔记本    | 12999.00 | 10999.0000 |   2000.00 |
| Surface Pro  | 平板      |  6999.00 | 5799.0000 |   1200.00 |
| AirPods Pro  | 耳机      |  1899.00 | 1899.0000 |      0.00 |
| 华为手表     | 智能穿戴  |  1299.00 |  799.0000 |    500.00 |
+--------------+-----------+----------+------------+------------+
5 rows in set (0.00 sec)
```

这个查询使用派生表计算每个类别的平均价格和最高价格，然后与主表连接，找出每个类别中价格最高的产品，并计算这些产品与类别平均价格的差异。

派生表的一个优势是它能够将复杂的多步查询分解为逻辑清晰的步骤，提高查询的可读性和可维护性。但需要注意的是，派生表可能会影响查询性能，特别是在处理大量数据时。

## [9.3 子查询与 JOIN 的取舍](#_9-3-子查询与-join-的取舍)

在实际应用中，很多使用子查询的场景也可以用JOIN来实现。那么，什么时候应该使用子查询，什么时候应该使用JOIN呢？这需要根据具体场景来权衡可读性、性能和功能需求。

让我们通过几个例子来比较子查询和JOIN的用法。首先，查询购买了手机类产品的用户：

使用子查询的方式：

```
SELECT DISTINCT u.username, u.city
FROM users u
WHERE u.id IN (
    SELECT o.user_id
    FROM orders o
    JOIN products p ON o.product_id = p.id
    WHERE p.category = '手机'
);
```

使用JOIN的方式：

```
SELECT DISTINCT u.username, u.city
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id
WHERE p.category = '手机';
```

两个查询都返回相同的结果：

```
+----------+--------+
| username | city   |
+----------+--------+
| 张三     | 北京   |
| 钱七     | 杭州   |
+----------+--------+
2 rows in set (0.00 sec)
```

在这个例子中，JOIN的方式通常性能更好，因为数据库优化器可以更有效地处理连接操作。

再来看一个例子，查询消费金额高于平均水平的用户：

使用子查询的方式：

```
SELECT username, city, total_spent
FROM users
WHERE total_spent > (
    SELECT AVG(total_spent) 
    FROM users
);
```

这个查询很难用JOIN来实现，因为需要先计算聚合值再进行比较。在这种情况下，子查询是更自然的选择。

对于EXISTS子查询，有时候可以用JOIN替代，但需要小心处理重复数据。比如，查询有订单记录的用户：

使用EXISTS子查询：

```
SELECT u.username, u.city
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
);
```

使用JOIN的方式：

```
SELECT DISTINCT u.username, u.city
FROM users u
JOIN orders o ON u.id = o.user_id;
```

EXISTS的方式通常更高效，特别是当只需要检查是否存在匹配记录时，因为EXISTS在找到第一个匹配项后就会停止搜索。

在性能方面，通常的经验法则是：

- 对于简单的连接操作，JOIN通常比子查询性能更好
- 对于EXISTS和NOT EXISTS查询，子查询通常比对应的JOIN更高效
- 对于复杂的聚合比较，子查询可能是唯一的选择
- 现代数据库优化器在很多情况下能够将子查询重写为JOIN，所以性能差异可能不大

在可读性方面，需要考虑：

- 子查询通常更接近自然语言的表达方式，更容易理解业务逻辑
- JOIN在处理复杂连接时可能更清晰，特别是当涉及多个表时
- 派生表可以将复杂查询分解为逻辑步骤，提高可维护性

让我们再看一个更复杂的例子，查询每个用户最贵的订单信息：

使用子查询的方式：

```
SELECT u.username, p.name, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id
WHERE o.amount = (
    SELECT MAX(o2.amount)
    FROM orders o2
    WHERE o2.user_id = u.id
);
```

使用窗口函数的方式（现代数据库支持）：

```
SELECT username, product_name, amount
FROM (
    SELECT 
        u.username,
        p.name AS product_name,
        o.amount,
        ROW_NUMBER() OVER (PARTITION BY u.id ORDER BY o.amount DESC) AS rank_num
    FROM users u
    JOIN orders o ON u.id = o.user_id
    JOIN products p ON o.product_id = p.id
) ranked_orders
WHERE rank_num = 1;
```

两个查询都返回每个用户最贵的订单信息，但实现方式不同。子查询的方式更直观，而窗口函数的方式在某些情况下可能更高效。

在实际开发中，选择子查询还是JOIN应该考虑以下因素：

1. **业务逻辑的清晰度**：哪种方式更能准确表达业务需求
2. **性能要求**：在大数据量情况下哪种方式性能更好
3. **数据库特性**：不同数据库对子查询和JOIN的优化能力不同
4. **维护成本**：哪种方式更容易维护和修改

对于初学者来说，建议先掌握子查询的基本用法，然后在实践中逐步学习如何根据具体情况选择合适的实现方式。很多时候，可以先用子查询写出清晰表达业务逻辑的查询，如果性能不满足要求，再考虑优化为JOIN或其他方式。

## [练习题](#练习题)

### [练习1：WHERE子查询应用](#练习1-where子查询应用)

查询价格高于手机类别平均价格的所有非手机类产品，显示产品名称、类别和价格。

查看答案

```
SELECT name, category, price
FROM products
WHERE category != '手机' 
AND price > (
    SELECT AVG(price)
    FROM products
    WHERE category = '手机'
);
```

### [练习2：FROM子查询（派生表）](#练习2-from子查询-派生表)

查询每个类别的产品数量和平均价格，然后筛选出产品数量至少为2个且平均价格高于5000元的类别。

查看答案

```
SELECT category, product_count, avg_price
FROM (
    SELECT 
        category,
        COUNT(*) AS product_count,
        AVG(price) AS avg_price
    FROM products
    GROUP BY category
) category_stats
WHERE product_count >= 2 AND avg_price > 5000;
```

### [练习3：EXISTS子查询](#练习3-exists子查询)

查询那些购买过但从未购买过手机类产品的用户，显示用户名、城市和注册日期。

查看答案

```
SELECT u.username, u.city, u.registration_date
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.user_id = u.id
) AND NOT EXISTS (
    SELECT 1
    FROM orders o
    JOIN products p ON o.product_id = p.id
    WHERE o.user_id = u.id AND p.category = '手机'
);
```

## [常见坑](#常见坑)

### [坑1：子查询返回多行错误](#坑1-子查询返回多行错误)

当使用单值比较操作符（=、>、<等）时，如果子查询返回多行，会导致错误。

**错误示例**：

```
-- 错误：子查询可能返回多行
SELECT name, price
FROM products
WHERE price = (
    SELECT price
    FROM products
    WHERE category = '手机'
);
```

**纠正方法**：使用IN操作符或聚合函数：

```
-- 方法1：使用IN
SELECT name, price
FROM products
WHERE price IN (
    SELECT price
    FROM products
    WHERE category = '手机'
);

-- 方法2：使用聚合函数
SELECT name, price
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE category = '手机'
);
```

### [坯2：相关子查询的性能问题](#坯2-相关子查询的性能问题)

相关子查询（子查询引用外部查询的列）可能会导致性能问题，因为子查询需要为外部查询的每一行执行一次。

**性能问题示例**：

```
-- 可能性能较差的写法
SELECT u.username, u.city
FROM users u
WHERE u.total_spent > (
    SELECT AVG(u2.total_spent)
    FROM users u2
    WHERE u2.city = u.city
);
```

**优化方法**：考虑使用JOIN或派生表：

```
SELECT u.username, u.city
FROM users u
JOIN (
    SELECT city, AVG(total_spent) AS city_avg
    FROM users
    GROUP BY city
) city_avg ON u.city = city_avg.city
WHERE u.total_spent > city_avg.city_avg;
```

### [坑3：派生表的别名问题](#坑3-派生表的别名问题)

在MySQL中，派生表必须指定别名，否则会报错。

**错误示例**：

```
-- 错误：派生表缺少别名
SELECT category, avg_price
FROM (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
);
```

**纠正方法**：为派生表指定别名：

```
SELECT category, avg_price
FROM (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
) AS category_stats;
```

## [速记卡](#速记卡)

- **单值子查询**：返回单个值，与=、>、<等比较操作符一起使用
- **集合子查询**：返回多个值，与IN、ANY、ALL等操作符一起使用
- **EXISTS子查询**：检查是否存在匹配记录，只返回TRUE或FALSE
- **派生表**：FROM子句中的子查询，必须指定别名
- **相关子查询**：子查询引用外部查询的列，可能影响性能
- **子查询vsJOIN**：子查询更易读，JOIN通常性能更好
- **NULL值处理**：子查询中的NULL值需要注意，特别是使用NOT IN时
- **性能考虑**：大数据量时测试不同写法的性能，选择最优方案
- **数据库差异**：不同数据库对子查询的优化能力不同
- **现代优化器**：现代数据库能自动优化很多子查询为JOIN

## [章节总结](#章节总结)

在这一章中，我们学习了子查询这一强大的SQL技术，它让我们能够构建嵌套的查询来解决复杂的数据问题。从WHERE子查询开始，我们了解了单值子查询、集合子查询和EXISTS子查询的不同用途和语法特点。

WHERE子查询允许我们在筛选条件中使用嵌套查询，比如查询价格高于平均价格的商品、购买特定产品的用户等。EXISTS子查询提供了一种高效的方式来检查是否存在匹配记录，特别适合处理存在性检查的场景。

FROM子查询（派生表）让我们能够创建临时表进行多步数据处理，这在复杂的数据分析和统计中非常有用。我们可以通过派生表进行分组统计、排名分析、复杂计算等操作，将复杂的查询逻辑分解为清晰的步骤。

我们还探讨了子查询与JOIN的取舍问题。虽然很多子查询场景可以用JOIN替代，但两者各有优势。子查询通常更接近自然语言表达，逻辑更清晰；而JOIN通常性能更好，特别是在处理大量数据时。在实际应用中，我们需要根据业务需求、性能要求和维护成本来选择合适的实现方式。

掌握了子查询技术，你就能够处理更加复杂和灵活的数据查询需求。无论是复杂的业务报表、数据分析还是系统管理，子查询都是不可或缺的工具。在下一章中，我们将学习事务处理，这将让我们能够保证数据操作的一致性和可靠性。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [09｜子查询：什么时候该用子查询？](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#_09-子查询-什么时候该用子查询)
- [9.1 WHERE 子查询](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#_9-1-where-子查询)
- [9.2 FROM 子查询（派生表）](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#_9-2-from-子查询-派生表)
- [9.3 子查询与 JOIN 的取舍](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#_9-3-子查询与-join-的取舍)
- [练习题](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#练习题)
- [练习1：WHERE子查询应用](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#练习1-where子查询应用)
- [练习2：FROM子查询（派生表）](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#练习2-from子查询-派生表)
- [练习3：EXISTS子查询](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#练习3-exists子查询)
- [常见坑](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#常见坑)
- [坑1：子查询返回多行错误](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#坑1-子查询返回多行错误)
- [坯2：相关子查询的性能问题](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#坯2-相关子查询的性能问题)
- [坑3：派生表的别名问题](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#坑3-派生表的别名问题)
- [速记卡](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part2/09-subqueries.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
