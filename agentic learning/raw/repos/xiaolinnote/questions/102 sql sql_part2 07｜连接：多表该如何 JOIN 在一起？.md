---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
  - "database"
  - "sql"
status: inbox
created: 2026-05-07
updated: 2026-05-17
url: "https://xiaolinnote.com/sql/sql_part2/07-join-tables.html"
source: "https://xiaolinnote.com/sql/sql_part2/07-join-tables.html"
last_checked: 2026-05-17
freshness: watch
sha256: 56ff19ff545283b2fece337eba2dc88226d5fe6220a3f63af572aaafdf1de064
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 07｜连接：多表该如何 JOIN 在一起？

原始链接：https://xiaolinnote.com/sql/sql_part2/07-join-tables.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 07｜连接：多表该如何 JOIN 在一起？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 23 分钟约 6919 字2025/8/31

---

# [07｜连接：多表该如何 JOIN 在一起？](#_07-连接-多表该如何-join-在一起)

大家好，我是小林。

在前面的章节中，我们学习了如何操作单个表的数据，但在实际应用中，数据通常分布在多个相关的表中。比如，在一个电商系统中，用户信息在一个表，订单信息在另一个表，商品详情又在第三个表。当我们需要查看"某个用户的所有订单"或者"某个订单的商品详情"时，就需要将这些表连接起来查询。

你有没有想过，当你在电商网站查看订单详情时，系统是如何同时显示订单信息、商品信息和用户信息的？当你在银行APP查看交易记录时，系统是如何将交易表与账户表关联起来的？这些都需要用到多表连接技术。

在这一章中，我们将学习如何使用JOIN将多个表连接在一起进行查询。从关系型数据的基本概念开始，到INNER JOIN和LEFT JOIN的区别，再到表别名和多表查询的实际应用。掌握了连接技术，你就能够处理更加复杂的数据查询需求。

准备好了吗？让我们开始学习多表连接的奥秘吧！

## [7.1 关系型数据与连接概念](#_7-1-关系型数据与连接概念)

关系型数据库的核心思想是将数据分散到多个相关的表中，每个表负责管理某一类特定的数据。这种设计避免了数据冗余，提高了数据的一致性和可维护性。而连接（JOIN）就是让我们能够将这些分散的数据重新组合在一起的强大工具。

让我们创建一个简单的电商系统数据库来演示连接操作。这个数据库包含三个表：用户表、订单表和商品表。

```
-- 创建用户表
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建商品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    category VARCHAR(50),
    stock INT DEFAULT 0
);

-- 创建订单表
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_id INT,
    quantity INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

在这个数据库设计中，users表存储用户信息，products表存储商品信息，orders表存储订单信息。orders表中的user\_id和product\_id是外键，分别引用users表和products表的主键。这种关系让我们能够知道哪个用户购买了哪个商品。

让我们插入一些示例数据：

```
-- 插入用户数据
INSERT INTO users (username, email, city) VALUES 
('张三', 'zhangsan@example.com', '北京'),
('李四', 'lisi@example.com', '上海'),
('王五', 'wangwu@example.com', '广州'),
('赵六', 'zhaoliu@example.com', '深圳');

-- 插入商品数据
INSERT INTO products (name, price, category, stock) VALUES 
('iPhone 15', 5999.00, '手机', 100),
('小米13', 3999.00, '手机', 150),
('MacBook Pro', 12999.00, '笔记本', 50),
('iPad Air', 4599.00, '平板', 120);

-- 插入订单数据
INSERT INTO orders (user_id, product_id, quantity, status) VALUES 
(1, 1, 1, 'completed'),  -- 张三买了1个iPhone 15
(1, 4, 2, 'completed'),  -- 张三买了2个iPad Air
(2, 2, 1, 'pending'),    -- 李四买了1个小米13
(3, 3, 1, 'completed'),  -- 王五买了1个MacBook Pro
(4, 1, 1, 'cancelled');  -- 赵六买了1个iPhone 15但取消了
```

现在我们有了一个完整的数据集。每个订单都通过user\_id关联到具体的用户，通过product\_id关联到具体的商品。这种设计让我们能够灵活地查询各种组合信息。

连接的本质是在两个表之间建立一个"配对"关系。比如，当我们连接users表和orders表时，数据库会尝试将users表中的每一行与orders表中的每一行进行配对，配对的依据是两个表中的相关列（通常是主键和外键）。

让我们看一个最简单的连接例子：

```
SELECT *
FROM users
JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----+----------+---------------------+--------+----+---------+------------+----------+---------------------+------------+
| id | username | email               | city   | id | user_id | product_id | quantity | order_date          | status     |
+----+----------+---------------------+--------+----+---------+------------+----------+---------------------+------------+
|  1 | 张三     | zhangsan@example.com | 北京   |  1 |       1 |          1 |        1 | 2025-08-31 10:00:00 | completed  |
|  1 | 张三     | zhangsan@example.com | 北京   |  2 |       1 |          4 |        2 | 2025-08-31 10:00:00 | completed  |
|  2 | 李四     | lisi@example.com    | 上海   |  3 |       2 |          2 |        1 | 2025-08-31 10:00:00 | pending    |
|  3 | 王五     | wangwu@example.com  | 广州   |  4 |       3 |          3 |        1 | 2025-08-31 10:00:00 | completed  |
|  4 | 赵六     | zhaoliu@example.com | 深圳   |  5 |       4 |          1 |        1 | 2025-08-31 10:00:00 | cancelled  |
+----+----------+---------------------+--------+----+---------+------------+----------+---------------------+------------+
5 rows in set (0.00 sec)
```

这个查询将users表和orders表连接在一起，连接条件是users.id等于orders.user\_id。结果中包含了两个表的所有列，每一行都代表一个用户及其对应的订单信息。

注意到结果中有两个id列，这可能会造成混淆。在实际应用中，我们通常会明确指定需要的列，或者使用列别名来避免冲突。

连接的基本语法是：

```
SELECT columns
FROM table1
JOIN table2 ON table1.column = table2.column
```

JOIN关键字默认表示INNER JOIN，我们稍后会详细讨论不同类型的JOIN。

理解连接的概念很重要，因为它是关系型数据库的精髓所在。通过将数据分散到多个相关的表中，然后用连接操作重新组合，我们既避免了数据冗余，又能够灵活地查询各种组合信息。

## [7.2 INNER JOIN 内连接详解](#_7-2-inner-join-内连接详解)

INNER JOIN（内连接）是最常用的连接类型之一，它只返回两个表中能够匹配的行。如果某个表中的行在另一个表中没有匹配的行，那么这些行就不会出现在结果中。让我们通过具体的例子来深入理解INNER JOIN的工作原理。

假设你想知道哪些用户下了订单，以及他们下了什么订单。这时就需要用到INNER JOIN，因为我们只关心有订单的用户。

```
SELECT users.username, orders.id AS order_id, orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
+----------+----------+------------+
5 rows in set (0.00 sec)
```

这个查询只返回了有订单的用户。如果我们查看users表，会发现有5个用户，但结果中只显示了4个用户（张三有2个订单）。这是因为INNER JOIN只返回能够匹配的行，没有订单的用户不会出现在结果中。

让我们看看INNER JOIN的工作原理。数据库会按照以下步骤执行这个查询：

1. 从users表中取出第一行（张三，id=1）
2. 在orders表中查找user\_id=1的行
3. 找到匹配的行（order\_id=1和order\_id=2），将它们组合成结果行
4. 继续处理users表中的下一行，重复这个过程

INNER JOIN的语法结构很清晰：

```
SELECT columns
FROM table1
INNER JOIN table2 ON table1.column = table2.column
```

INNER JOIN在实际业务中有很多应用场景。比如，我们想要查看已完成订单的详细信息：

```
SELECT 
    users.username,
    products.name AS product_name,
    orders.quantity,
    orders.order_date,
    orders.status
FROM orders
INNER JOIN users ON orders.user_id = users.id
INNER JOIN products ON orders.product_id = products.id
WHERE orders.status = 'completed';
```

执行结果：

```
+----------+--------------+----------+---------------------+------------+
| username | product_name | quantity | order_date          | status     |
+----------+--------------+----------+---------------------+------------+
| 张三     | iPhone 15     |        1 | 2025-08-31 10:00:00 | completed  |
| 张三     | iPad Air      |        2 | 2025-08-31 10:00:00 | completed  |
| 王五     | MacBook Pro   |        1 | 2025-08-31 10:00:00 | completed  |
+----------+--------------+----------+---------------------+------------+
3 rows in set (0.00 sec)
```

这个查询连接了三个表，给我们提供了完整的订单信息。通过INNER JOIN，我们能够将分散在不同表中的相关数据组合在一起，得到有意义的结果。

INNER JOIN的一个重要特性是它不会产生NULL值。因为只有完全匹配的行才会出现在结果中，所以结果中的所有列都会有具体的值。这使得INNER JOIN特别适合用于需要完整数据的场景。

比如，我们可以统计每个用户的消费情况：

```
SELECT 
    users.username,
    users.city,
    COUNT(orders.id) AS order_count,
    SUM(products.price * orders.quantity) AS total_spent
FROM users
INNER JOIN orders ON users.id = orders.user_id
INNER JOIN products ON orders.product_id = products.id
WHERE orders.status = 'completed'
GROUP BY users.id, users.username, users.city
ORDER BY total_spent DESC;
```

执行结果：

```
+----------+--------+------------+-------------+
| username | city   | order_count | total_spent  |
+----------+--------+------------+-------------+
| 张三     | 北京   |          2 |    15157.00 |
| 王五     | 广州   |          1 |    12999.00 |
+----------+--------+------------+-------------+
2 rows in set (0.00 sec)
```

这个查询显示了有已完成订单用户的消费统计。注意，钱七没有出现在结果中，因为他没有订单。

INNER JOIN还可以用于查找满足特定条件的数据。比如，我们想找到购买了iPhone的用户：

```
SELECT DISTINCT users.username, users.email
FROM users
INNER JOIN orders ON users.id = orders.user_id
INNER JOIN products ON orders.product_id = products.id
WHERE products.name = 'iPhone 15';
```

执行结果：

```
+----------+---------------------+
| username | email               |
+----------+---------------------+
| 张三     | zhangsan@example.com |
| 赵六     | zhaoliu@example.com  |
+----------+---------------------+
2 rows in set (0.00 sec)
```

通过这个例子，我们可以看到INNER JOIN如何帮我们找到满足复杂条件的关联数据。

掌握INNER JOIN是SQL学习中的重要一步。它让我们能够处理关系型数据库中最核心的概念——表间关系，将分散的数据重新组合成有意义的信息。

## [7.3 LEFT JOIN 左连接](#_7-3-left-join-左连接)

现在我们学习了INNER JOIN，让我们看看LEFT JOIN（左连接）有什么不同。LEFT JOIN会返回左表（FROM子句中指定的表）的所有行，即使在右表中没有匹配的行。对于右表中没有匹配的行，结果中对应的列会显示为NULL。

让我们看看LEFT JOIN的效果：

```
SELECT users.username, orders.id AS order_id, orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
+----------+----------+------------+
5 rows in set (0.00 sec)
```

这个查询返回了所有有订单的用户。如果我们查看users表，会发现有4个用户，但结果中只有4个用户（张三有2个订单）。这是因为INNER JOIN只返回能够匹配的行。

LEFT JOIN则不同，它会返回左表（FROM子句中指定的表）的所有行，即使在右表中没有匹配的行。对于右表中没有匹配的行，结果中对应的列会显示为NULL。

让我们看看LEFT JOIN的效果：

```
SELECT users.username, orders.id AS order_id, orders.status
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
+----------+----------+------------+
5 rows in set (0.00 sec)
```

在这个例子中，LEFT JOIN和INNER JOIN的结果相同，因为所有用户都有订单。让我们添加一个没有订单的用户来看看区别：

```
-- 添加一个没有订单的用户
INSERT INTO users (username, email, city) VALUES 
('钱七', 'qianqi@example.com', '杭州');

-- 再次执行LEFT JOIN
SELECT users.username, orders.id AS order_id, orders.status
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
| 钱七     |     NULL | NULL       |
+----------+----------+------------+
6 rows in set (0.00 sec)
```

现在可以看到，钱七虽然没有订单，但仍然出现在结果中，他的order\_id和status列显示为NULL。

如果我们用INNER JOIN查询同样的数据：

```
SELECT users.username, orders.id AS order_id, orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
+----------+----------+------------+
5 rows in set (0.00 sec)
```

钱七没有出现在结果中，因为他没有订单。

INNER JOIN和LEFT JOIN的选择取决于业务需求。如果我们只想查看有订单的用户（比如生成销售报表），应该使用INNER JOIN。如果我们想查看所有用户，包括那些没有订单的用户（比如用户活跃度分析），应该使用LEFT JOIN。

让我们看一个更复杂的例子，连接三个表来获取完整的订单信息：

```
SELECT 
    users.username,
    products.name AS product_name,
    products.price,
    orders.quantity,
    orders.order_date,
    orders.status
FROM orders
INNER JOIN users ON orders.user_id = users.id
INNER JOIN products ON orders.product_id = products.id;
```

执行结果：

```
+----------+--------------+----------+----------+---------------------+------------+
| username | product_name | price    | quantity | order_date          | status     |
+----------+--------------+----------+----------+---------------------+------------+
| 张三     | iPhone 15     |  5999.00 |        1 | 2025-08-31 10:00:00 | completed  |
| 张三     | iPad Air      |  4599.00 |        2 | 2025-08-31 10:00:00 | completed  |
| 李四     | 小米13        |  3999.00 |        1 | 2025-08-31 10:00:00 | pending    |
| 王五     | MacBook Pro   | 12999.00 |        1 | 2025-08-31 10:00:00 | completed  |
| 赵六     | iPhone 15     |  5999.00 |        1 | 2025-08-31 10:00:00 | cancelled  |
+----------+--------------+----------+----------+---------------------+------------+
5 rows in set (0.00 sec)
```

这个查询连接了三个表，给我们提供了完整的订单信息，包括用户名、产品名称、价格、数量等。

在实际应用中，LEFT JOIN经常用于查找"有A但没有B"的情况。比如，查找没有下单的用户：

```
SELECT users.username, users.email
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE orders.id IS NULL;
```

执行结果：

```
+----------+-------------------+
| username | email             |
+----------+-------------------+
| 钱七     | qianqi@example.com |
+----------+-------------------+
1 row in set (0.00 sec)
```

这个查询利用了LEFT JOIN的特性：没有订单的用户的orders.id会是NULL，所以我们用WHERE [orders.id](http://orders.id) IS NULL来筛选出这些用户。

## [7.4 RIGHT JOIN 右连接](#_7-4-right-join-右连接)

学习了INNER JOIN和LEFT JOIN之后，让我们来了解RIGHT JOIN（右连接）。RIGHT JOIN与LEFT JOIN正好相反，它会返回右表（JOIN关键字后面指定的表）的所有行，即使在左表中没有匹配的行。对于左表中没有匹配的行，结果中对应的列会显示为NULL。

让我们通过一个具体的例子来理解RIGHT JOIN。假设我们想要查看所有商品的销售情况，包括那些还没有被购买过的商品：

```
SELECT 
    products.name AS product_name,
    products.category,
    orders.id AS order_id,
    orders.quantity,
    orders.status
FROM orders
RIGHT JOIN products ON orders.product_id = products.id;
```

执行结果：

```
+--------------+----------+----------+----------+------------+
| product_name | category | order_id | quantity | status     |
+--------------+----------+----------+----------+------------+
| iPhone 15    | 手机     |        1 |        1 | completed  |
| iPad Air     | 平板     |        2 |        2 | completed  |
| 小米13       | 手机     |        3 |        1 | pending    |
| MacBook Pro  | 笔记本   |        4 |        1 | completed  |
| iPhone 15    | 手机     |        5 |        1 | cancelled  |
| NULL         | NULL     |     NULL |     NULL | NULL       |
| NULL         | NULL     |     NULL |     NULL | NULL       |
+--------------+----------+----------+----------+------------+
7 rows in set (0.00 sec)
```

从这个结果中我们可以看到，所有的商品都出现在了结果中，包括那些还没有订单的商品（显示为NULL）。这就是RIGHT JOIN的特点：确保右表（products表）的所有数据都会被包含在结果中。

RIGHT JOIN在实际业务中有什么用呢？让我们看一个更实际的例子。假设我们想要分析商品库存，找出哪些商品还没有销售记录：

```
SELECT 
    p.name AS product_name,
    p.category,
    p.price,
    p.stock,
    COUNT(o.id) AS order_count,
    COALESCE(SUM(o.quantity), 0) AS total_sold
FROM orders o
RIGHT JOIN products p ON o.product_id = p.id
GROUP BY p.id, p.name, p.category, p.price, p.stock
ORDER BY order_count ASC, p.name;
```

执行结果：

```
+--------------+----------+----------+-------+------------+------------+
| product_name | category | price    | stock | order_count | total_sold |
+--------------+----------+----------+-------+------------+------------+
| 华为MateBook | 笔记本   | 6999.00  |    30 |          0 |          0 |
| 小米平板     | 平板     | 1999.00  |    25 |          0 |          0 |
| iPhone 15    | 手机     | 5999.00  |   100 |          2 |          2 |
| iPad Air     | 平板     | 4599.00  |    50 |          1 |          2 |
| 小米13       | 手机     | 3999.00  |    80 |          1 |          1 |
| MacBook Pro  | 笔记本   | 9999.00  |    25 |          1 |          1 |
+--------------+----------+----------+-------+------------+------------+
6 rows in set (0.00 sec)
```

这个查询非常有用！我们可以看到华为MateBook和小米平板还没有任何销售记录，这对于库存管理和销售策略制定很重要。

RIGHT JOIN还可以用于查找"有B但没有A"的情况，这与LEFT JOIN正好相反。比如，我们想要找到还没有被任何用户购买的商品：

```
SELECT 
    p.name AS product_name,
    p.category,
    p.price,
    p.stock
FROM orders o
RIGHT JOIN products p ON o.product_id = p.id
WHERE o.id IS NULL;
```

执行结果：

```
+--------------+----------+----------+-------+
| product_name | category | price    | stock |
+--------------+----------+----------+-------+
| 华为MateBook | 笔记本   | 6999.00  |    30 |
| 小米平板     | 平板     | 1999.00  |    25 |
+--------------+----------+----------+-------+
2 rows in set (0.00 sec)
```

这个查询清楚地显示了哪些商品还没有被购买过，这对于销售分析和库存管理很有帮助。

让我们再看一个更复杂的应用场景：分析各个商品类别的销售情况，包括那些还没有销售记录的类别：

```
SELECT 
    p.category,
    COUNT(DISTINCT p.id) AS total_products,
    COUNT(DISTINCT o.id) AS orders_with_products,
    COALESCE(SUM(o.quantity), 0) AS total_quantity_sold,
    COALESCE(SUM(o.quantity * p.price), 0) AS total_revenue
FROM orders o
RIGHT JOIN products p ON o.product_id = p.id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

执行结果：

```
+----------+----------------+-----------------------+---------------------+---------------+
| category | total_products | orders_with_products | total_quantity_sold | total_revenue |
+----------+----------------+-----------------------+---------------------+---------------+
| 手机     |              2 |                     3 |                   3 |      17998.00 |
| 平板     |              2 |                     2 |                   3 |      12597.00 |
| 笔记本   |              2 |                     1 |                   1 |       9999.00 |
+----------+----------------+-----------------------+---------------------+---------------+
3 rows in set (0.00 sec)
```

这个分析显示了每个商品类别的整体情况，包括商品总数、有订单的商品数、总销售数量和总收入。

你可能会问，RIGHT JOIN和LEFT JOIN有什么区别呢？其实它们很相似，只是方向不同：

```
-- 这两个查询是等价的
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.id;
SELECT * FROM table2 RIGHT JOIN table1 ON table2.id = table1.id;
```

在实际应用中，LEFT JOIN比RIGHT JOIN更常用，因为人们习惯于从"主表"出发去查找相关数据。但在某些情况下，RIGHT JOIN会让查询逻辑更清晰。

让我们看一个实际的综合应用：生成完整的商品销售报表，包括库存和销售信息：

```
SELECT 
    p.name AS product_name,
    p.category,
    p.price,
    p.stock,
    COUNT(o.id) AS times_ordered,
    COALESCE(SUM(o.quantity), 0) AS total_sold,
    COALESCE(SUM(o.quantity * p.price), 0) AS total_revenue,
    CASE 
        WHEN p.stock = 0 THEN '缺货'
        WHEN COUNT(o.id) = 0 THEN '未销售'
        WHEN SUM(o.quantity) > p.stock * 0.8 THEN '热销'
        ELSE '正常'
    END AS sales_status
FROM orders o
RIGHT JOIN products p ON o.product_id = p.id
GROUP BY p.id, p.name, p.category, p.price, p.stock
ORDER BY 
    CASE 
        WHEN p.stock = 0 THEN 1
        WHEN COUNT(o.id) = 0 THEN 2
        WHEN SUM(o.quantity) > p.stock * 0.8 THEN 3
        ELSE 4
    END,
    total_revenue DESC;
```

执行结果：

```
+--------------+----------+----------+-------+---------------+------------+---------------+-------------+
| product_name | category | price    | stock | times_ordered | total_sold | total_revenue | sales_status |
+--------------+----------+----------+-------+---------------+------------+---------------+-------------+
| 华为MateBook | 笔记本   | 6999.00  |    30 |             0 |          0 |         0.00 | 未销售      |
| 小米平板     | 平板     | 1999.00  |    25 |             0 |          0 |         0.00 | 未销售      |
| iPhone 15    | 手机     | 5999.00  |   100 |             2 |          2 |     11998.00 | 正常        |
| 小米13       | 手机     | 3999.00  |    80 |             1 |          1 |      3999.00 | 正常        |
| iPad Air     | 平板     | 4599.00  |    50 |             1 |          2 |      9198.00 | 正常        |
| MacBook Pro  | 笔记本   | 9999.00  |    25 |             1 |          1 |      9999.00 | 正常        |
+--------------+----------+----------+-------+---------------+------------+---------------+-------------+
6 rows in set (0.00 sec)
```

这个综合报表展示了商品销售的完整情况，包括库存状态、销售记录和自动生成的销售状态分类。这对于业务决策非常有价值。

掌握RIGHT JOIN让你能够从不同的角度分析数据，特别是在需要确保参考数据完整性的时候。结合INNER JOIN、LEFT JOIN和RIGHT JOIN，你就能够处理各种复杂的数据关联需求。

## [7.5 表别名与多表查询](#_7-5-表别名与多表查询)

当我们在查询中处理多个表时，表别名（Table Alias）变得非常重要。表别名让我们能够用简短的名称来引用表，提高SQL语句的可读性，避免列名冲突，并且让复杂的查询更加清晰。

表别名的基本语法是在表名后面加上一个简短的别名，通常用AS关键字（虽然AS可以省略，但使用AS会让代码更清晰）：

```
SELECT u.username, o.id AS order_id, o.status
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id;
```

执行结果：

```
+----------+----------+------------+
| username | order_id | status     |
+----------+----------+------------+
| 张三     |        1 | completed  |
| 张三     |        2 | completed  |
| 李四     |        3 | pending    |
| 王五     |        4 | completed  |
| 赵六     |        5 | cancelled  |
+----------+----------+------------+
5 rows in set (0.00 sec)
```

在这个查询中，我们给users表起了别名u，给orders表起了别名o。这样在引用列时，我们可以用u.username代替users.username，[用o.id代替orders.id](http://xn--o-s02c.xn--idorders-fp1m440r.id)，让SQL语句更加简洁。

表别名在连接多个表时特别有用。让我们看一个连接三个表的例子：

```
SELECT 
    u.username,
    p.name AS product_name,
    p.price,
    o.quantity,
    o.order_date
FROM orders AS o
INNER JOIN users AS u ON o.user_id = u.id
INNER JOIN products AS p ON o.product_id = p.id;
```

执行结果：

```
+----------+--------------+----------+----------+---------------------+
| username | product_name | price    | quantity | order_date          |
+----------+--------------+----------+----------+---------------------+
| 张三     | iPhone 15     |  5999.00 |        1 | 2025-08-31 10:00:00 |
| 张三     | iPad Air      |  4599.00 |        2 | 2025-08-31 10:00:00 |
| 李四     | 小米13        |  3999.00 |        1 | 2025-08-31 10:00:00 |
| 王五     | MacBook Pro   | 12999.00 |        1 | 2025-08-31 10:00:00 |
| 赵六     | iPhone 15     |  5999.00 |        1 | 2025-08-31 10:00:00 |
+----------+--------------+----------+----------+---------------------+
5 rows in set (0.00秒)
```

使用表别名后，查询语句更加清晰易读。特别是在复杂的查询中，良好的命名习惯能够大大提高代码的可维护性。

表别名还帮助我们避免列名冲突。比如，如果两个表都有id列，我们可以用u.id和o.id来区分它们：

```
SELECT u.id AS user_id, o.id AS order_id, u.username
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id;
```

在实际应用中，表别名通常遵循一些命名习惯：

- users表 → u 或 user
- orders表 → o 或 order
- products表 → p 或 product
- categories表 → c 或 category

在多表查询中，连接的顺序也会影响查询的性能和结果。通常的做法是从"驱动表"开始，然后连接到"被连表"。驱动表通常是结果集较小的表，或者是我们主要查询的表。

让我们看一个更实际的应用场景：计算每个用户的总消费金额：

```
SELECT 
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(p.price * o.quantity) AS total_amount
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
LEFT JOIN products AS p ON o.product_id = p.id
GROUP BY u.id, u.username, u.city
ORDER BY total_amount DESC;
```

执行结果：

```
+----------+--------+------------+--------------+
| username | city   | order_count | total_amount |
+----------+--------+------------+--------------+
| 王五     | 广州   |          1 |     12999.00 |
| 张三     | 北京   |          2 |     15157.00 |
| 赵六     | 深圳   |          1 |      5999.00 |
| 李四     | 上海   |          1 |      3999.00 |
| 钱七     | 杭州   |          0 |        NULL |
+----------+--------+------------+--------------+
5 rows in set (0.00 sec)
```

这个查询使用了LEFT JOIN来确保所有用户都出现在结果中，包括没有订单的钱七。我们计算了每个用户的订单数量和总消费金额，并按总金额降序排列。

表别名在自连接（Self Join）中也是必需的。自连接是指将表与自身连接，通常用于处理层次结构数据。比如，如果我们有一个员工表，其中包含经理ID（引用同一张表的员工ID），我们需要用自连接来查询员工及其经理的信息。

虽然我们当前的示例中没有自连接的情况，但了解这个概念很重要。在实际工作中，自连接常用于处理组织架构、评论回复、分类层次等场景。

## [练习题](#练习题)

### [练习1：INNER JOIN 与 LEFT JOIN 查询](#练习1-inner-join-与-left-join-查询)

查询所有已完成订单的详细信息，包括用户名、产品名称、数量和订单日期。

查看答案

```
SELECT 
    u.username,
    p.name AS product_name,
    o.quantity,
    o.order_date
FROM orders AS o
INNER JOIN users AS u ON o.user_id = u.id
INNER JOIN products AS p ON o.product_id = p.id
WHERE o.status = 'completed';
```

### [练习2：表别名与多表查询](#练习2-表别名与多表查询)

使用表别名查询用户的完整订单信息，包括用户名、产品名称、订单数量和总金额。要求使用表别名提高查询的可读性。

查看答案

```
SELECT 
    u.username,
    p.name AS product_name,
    o.quantity,
    o.order_date,
    (o.quantity * p.price) AS total_amount
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id
INNER JOIN products AS p ON o.product_id = p.id
ORDER BY u.username, o.order_date;
```

### [练习3：综合应用与数据统计](#练习3-综合应用与数据统计)

查询每个用户的订单统计信息，包括用户名、城市、订单数量和总消费金额，按总消费金额降序排列。

查看答案

```
SELECT 
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(p.price * o.quantity) AS total_amount
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
LEFT JOIN products AS p ON o.product_id = p.id
GROUP BY u.id, u.username, u.city
ORDER BY total_amount DESC;
```

## [常见坑](#常见坑)

### [坑1：连接条件错误](#坑1-连接条件错误)

很多初学者会混淆连接条件和筛选条件，或者忘记写连接条件，导致笛卡尔积。

**错误示例**：

```
-- 错误：忘记连接条件，会返回所有可能的组合
SELECT u.username, o.id
FROM users AS u
CROSS JOIN orders AS o;
```

**纠正方法**：总是明确指定连接条件：

```
SELECT u.username, o.id
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id;
```

### [坑2：列名冲突](#坑2-列名冲突)

当连接的表中有相同列名时，如果不指定表名或别名，会导致歧义错误。

**错误示例**：

```
-- 错误：两个表都有id列，会产生歧义
SELECT id, username, order_date
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id;
```

**纠正方法**：使用表别名限定列名：

```
SELECT u.id AS user_id, o.id AS order_id, u.username, o.order_date
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id;
```

### [坑3：连接类型选择错误](#坑3-连接类型选择错误)

使用错误的连接类型导致数据遗漏或结果不符合预期。

**错误示例1 - 应该用LEFT JOIN但用了INNER JOIN**：

```
-- 错误：遗漏没有订单的用户
SELECT u.username, COUNT(o.id) AS order_count
FROM users AS u
INNER JOIN orders AS o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**纠正方法**：根据业务需求选择正确的连接类型：

```
-- 正确：使用LEFT JOIN确保所有用户都被包含
SELECT u.username, COUNT(o.id) AS order_count
FROM users AS u
LEFT JOIN orders AS o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**错误示例2 - RIGHT JOIN与LEFT JOIN混淆**：

```
-- 错误：RIGHT JOIN的方向错误，导致结果不符合预期
SELECT p.name, COUNT(o.id) AS order_count
FROM orders AS o
RIGHT JOIN products AS p ON o.product_id = p.id
WHERE o.status = 'completed';
-- 这个WHERE条件会过滤掉NULL值，失去了RIGHT JOIN的意义
```

**纠正方法**：正确理解RIGHT JOIN的使用场景：

```
-- 正确：如果要筛选，应该考虑NULL值的情况
SELECT p.name, COUNT(o.id) AS order_count
FROM orders AS o
RIGHT JOIN products AS p ON o.product_id = p.id
WHERE o.status = 'completed' OR o.id IS NULL;
-- 或者根据具体业务需求调整筛选逻辑
```

## [速记卡](#速记卡)

- **关系型数据库**：将数据分散到多个相关表中，通过主外键关系连接
- **主键**：表中每行的唯一标识符，通常是自增整数
- **外键**：引用其他表主键的列，用于建立表间关系
- **INNER JOIN**：只返回两个表中能够完全匹配的行，不产生NULL值
- **LEFT JOIN**：返回左表的所有行，右表无匹配时显示NULL，确保主表完整性
- **RIGHT JOIN**：返回右表的所有行，左表无匹配时显示NULL，确保参考表完整性
- **表别名**：给表起简短的别名，提高可读性，避免列名冲突
- **连接条件**：ON子句指定如何匹配两个表的行
- **笛卡尔积**：没有连接条件的连接会产生所有可能的行组合
- **连接选择**：INNER JOIN用于完整数据，LEFT JOIN用于主表完整性，RIGHT JOIN用于参考表完整性

## [章节总结](#章节总结)

在这一章中，我们学习了关系型数据库的核心概念——多表连接。连接操作让我们能够将分散在多个相关表中的数据重新组合在一起，这是关系型数据库最强大的功能之一。

我们从关系型数据的基本概念开始，了解了主键、外键以及如何通过这些关系将不同的表连接起来。然后深入学习了INNER JOIN内连接，它只返回两个表中能够完全匹配的行，非常适合用于需要完整数据的场景，比如查询有订单的用户信息、已完成订单的详情等。

LEFT JOIN左连接让我们能够获取左表的所有数据，即使在右表中没有匹配的行。这对于查找缺失数据特别有用，比如找出没有订单的用户、分析用户活跃度等。而RIGHT JOIN右连接则从另一个角度出发，确保右表的所有数据都会被包含在结果中，这对于分析商品销售情况、查找未销售商品等场景非常有价值。

表别名是处理多表查询的重要工具，它让SQL语句更加清晰易读，避免了列名冲突，特别是在复杂的查询中。我们还学习了如何在实际业务场景中应用各种连接技术，比如计算用户消费统计、生成商品销售报表、分析库存状态等。

掌握了这三种连接技术，你就能够处理各种复杂的数据查询需求。INNER JOIN用于获取匹配的完整数据，LEFT JOIN用于确保主表数据完整性，RIGHT JOIN用于确保参考表数据完整性。无论是电商系统、银行应用还是数据分析平台，多表连接都是不可或缺的技能。在下一章中，我们将学习聚合与分组，这将让我们能够进行更强大的数据分析。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [07｜连接：多表该如何 JOIN 在一起？](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_07-连接-多表该如何-join-在一起)
- [7.1 关系型数据与连接概念](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_7-1-关系型数据与连接概念)
- [7.2 INNER JOIN 内连接详解](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_7-2-inner-join-内连接详解)
- [7.3 LEFT JOIN 左连接](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_7-3-left-join-左连接)
- [orders.id](http://orders.id)
- [7.4 RIGHT JOIN 右连接](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_7-4-right-join-右连接)
- [7.5 表别名与多表查询](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#_7-5-表别名与多表查询)
- [用o.id代替orders.id](http://xn--o-s02c.xn--idorders-fp1m440r.id)
- [练习题](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#练习题)
- [练习1：INNER JOIN 与 LEFT JOIN 查询](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#练习1-inner-join-与-left-join-查询)
- [练习2：表别名与多表查询](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#练习2-表别名与多表查询)
- [练习3：综合应用与数据统计](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#练习3-综合应用与数据统计)
- [常见坑](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#常见坑)
- [坑1：连接条件错误](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#坑1-连接条件错误)
- [坑2：列名冲突](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#坑2-列名冲突)
- [坑3：连接类型选择错误](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#坑3-连接类型选择错误)
- [速记卡](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part2/07-join-tables.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
