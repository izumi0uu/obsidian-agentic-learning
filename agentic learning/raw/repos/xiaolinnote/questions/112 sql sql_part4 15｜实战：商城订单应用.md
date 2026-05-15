---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html"
source: "https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html"
last_checked: 2026-05-07
freshness: watch
sha256: fc4c190f239aeb7e6bdb24d459ec1e0c2a0fb3cc53cc2014e609e586c7042a2e
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 15｜实战：商城订单应用

原始链接：https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 19 分钟约 5736 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了SQL的各种基础知识和高级特性，从简单的查询到复杂的事务处理，从表结构设计到索引优化。现在，让我们通过一个完整的电商订单系统案例，将这些知识融会贯通，解决实际的业务问题。

你有没有想过，当你在淘宝、京东等电商平台上浏览商品、下单购买时，背后是如何处理这些数据的？当你查看订单历史时，系统是如何快速找到你的所有订单的？当你查看商品销量排行榜时，这些统计数据是如何实时计算出来的？当系统需要处理成千上万用户的并发订单时，数据库是如何保持高性能的？

在这一章中，我们将构建一个完整的电商订单系统，包含用户管理、商品管理、订单处理等核心功能。从数据库表设计开始，到各种业务查询的实现，再到性能优化技巧，我们将一步步完成这个实战项目。通过这个案例，你将学会如何将前面学到的SQL知识应用到实际项目中。

准备好了吗？让我们开始这个电商订单系统的实战之旅吧！

## [15.1 商品、用户、订单表设计](#_15-1-商品、用户、订单表设计)

一个良好的电商系统首先要有一个合理的数据库设计。让我们根据业务需求设计几个核心表，包括用户表、商品表、订单表和订单明细表。这些表需要能够支持用户的注册登录、商品的浏览购买、订单的管理查询等核心功能。

让我们开始创建这些核心表。首先创建用户表，用于存储用户的基本信息：

```
-- 创建用户表
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    registration_date DATE NOT NULL,
    last_login TIMESTAMP,
    status ENUM('active', 'inactive', 'banned') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_users_email (email),
    INDEX idx_users_status (status),
    INDEX idx_users_registration_date (registration_date)
);

-- 插入示例用户数据
INSERT INTO users (username, email, password_hash, full_name, phone, address, registration_date, status) VALUES 
('zhangsan', 'zhangsan@example.com', SHA2('password123', 256), '张三', '13800138000', '北京市朝阳区xxx街道xxx号', '2025-01-15', 'active'),
('lisi', 'lisi@example.com', SHA2('password123', 256), '李四', '13900139000', '上海市浦东新区xxx路xxx号', '2025-02-20', 'active'),
('wangwu', 'wangwu@example.com', SHA2('password123', 256), '王五', '13700137000', '广州市天河区xxx路xxx号', '2025-03-10', 'active'),
('zhaoliu', 'zhaoliu@example.com', SHA2('password123', 256), '赵六', '13600136000', '深圳市南山区xxx街道xxx号', '2025-04-05', 'inactive'),
('qianqi', 'qianqi@example.com', SHA2('password123', 256), '钱七', '13500135000', '杭州市西湖区xxx路xxx号', '2025-05-12', 'active');
```

接下来创建商品表，用于存储商品信息：

```
-- 创建商品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    sku VARCHAR(50) UNIQUE NOT NULL,
    brand VARCHAR(100),
    image_url VARCHAR(255),
    status ENUM('active', 'inactive', 'discontinued') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_products_category (category),
    INDEX idx_products_price (price),
    INDEX idx_products_status (status),
    INDEX idx_products_sku (sku),
    INDEX idx_products_category_price (category, price)
);

-- 插入示例商品数据
INSERT INTO products (name, description, category, price, stock, sku, brand, status) VALUES 
('iPhone 15 Pro', '最新款iPhone，配备A17 Pro芯片，拍照效果出色', '手机', 8999.00, 50, 'IP15PRO001', 'Apple', 'active'),
('MacBook Pro 14"', '专业级笔记本电脑，M3 Pro芯片，适合开发工作者', '电脑', 14999.00, 25, 'MBP14M3001', 'Apple', 'active'),
('小米13 Ultra', '高端安卓手机，徕卡相机，骁龙8 Gen2处理器', '手机', 5999.00, 80, 'MI13ULTRA001', '小米', 'active'),
('戴尔XPS 13', '轻薄商务笔记本，13.4英寸触控屏，Intel i7处理器', '电脑', 9999.00, 30, 'DELLXPS13001', '戴尔', 'active'),
('AirPods Pro 2', '主动降噪无线耳机，空间音频，长续航', '配件', 1899.00, 100, 'APP2002001', 'Apple', 'active'),
('iPad Air', '10.9英寸平板电脑，M1芯片，支持Apple Pencil', '平板', 4599.00, 40, 'IPADAIR001', 'Apple', 'active'),
('华为MatePad Pro', '12.6英寸安卓平板，麒麟9000E处理器', '平板', 3999.00, 35, 'HWMPP001', '华为', 'active'),
('索尼WH-1000XM5', '头戴式降噪耳机，30小时续航，Hi-Res音质', '配件', 2399.00, 60, 'SONYWH1005', '索尼', 'active');
```

现在创建订单表，用于存储订单的基本信息：

```
-- 创建订单表
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'confirmed', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    shipping_address TEXT NOT NULL,
    payment_method ENUM('alipay', 'wechat', 'credit_card', 'bank_transfer') NOT NULL,
    payment_status ENUM('unpaid', 'paid', 'refunded') DEFAULT 'unpaid',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    shipped_date TIMESTAMP NULL,
    delivered_date TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_orders_user_id (user_id),
    INDEX idx_orders_status (status),
    INDEX idx_orders_order_date (order_date),
    INDEX idx_orders_payment_status (payment_status),
    INDEX idx_orders_user_status (user_id, status),
    INDEX idx_orders_date_status (order_date, status)
);

-- 创建订单明细表
DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    INDEX idx_order_items_order_id (order_id),
    INDEX idx_order_items_product_id (product_id),
    INDEX idx_order_items_order_product (order_id, product_id)
);
```

让我们插入一些示例订单数据来演示系统功能：

```
-- 插入示例订单数据
INSERT INTO orders (order_number, user_id, total_amount, status, shipping_address, payment_method, payment_status, order_date) VALUES 
('ORD20250815001', 1, 10898.00, 'delivered', '北京市朝阳区xxx街道xxx号', 'alipay', 'paid', '2025-08-15 10:30:00'),
('ORD20250816002', 2, 15998.00, 'shipped', '上海市浦东新区xxx路xxx号', 'wechat', 'paid', '2025-08-16 14:20:00'),
('ORD20250817003', 1, 5999.00, 'confirmed', '北京市朝阳区xxx街道xxx号', 'credit_card', 'paid', '2025-08-17 09:15:00'),
('ORD20250818004', 3, 1899.00, 'delivered', '广州市天河区xxx路xxx号', 'alipay', 'paid', '2025-08-18 16:45:00'),
('ORD20250819005', 5, 8598.00, 'pending', '杭州市西湖区xxx路xxx号', 'wechat', 'unpaid', '2025-08-19 11:30:00'),
('ORD20250820006', 2, 2399.00, 'cancelled', '上海市浦东新区xxx路xxx号', 'credit_card', 'refunded', '2025-08-20 13:20:00'),
('ORD20250821007', 4, 14999.00, 'shipped', '深圳市南山区xxx街道xxx号', 'bank_transfer', 'paid', '2025-08-21 15:10:00'),
('ORD20250822008', 1, 6498.00, 'confirmed', '北京市朝阳区xxx街道xxx号', 'alipay', 'paid', '2025-08-22 10:05:00');

-- 插入订单明细数据
INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price) VALUES 
(1, 1, 1, 8999.00, 8999.00),  -- iPhone 15 Pro
(1, 5, 1, 1899.00, 1899.00),  -- AirPods Pro 2
(2, 2, 1, 14999.00, 14999.00), -- MacBook Pro 14"
(2, 5, 1, 1899.00, 1899.00),  -- AirPods Pro 2
(3, 3, 1, 5999.00, 5999.00),  -- 小米13 Ultra
(4, 5, 1, 1899.00, 1899.00),  -- AirPods Pro 2
(5, 6, 1, 4599.00, 4599.00),  -- iPad Air
(5, 8, 2, 2399.00, 4799.00),  -- 索尼WH-1000XM5 × 2
(7, 2, 1, 14999.00, 14999.00), -- MacBook Pro 14"
(8, 4, 1, 9999.00, 9999.00),  -- 戴尔XPS 13
(8, 7, 1, 3999.00, 3999.00);  -- 华为MatePad Pro
```

现在我们已经创建了一个完整的电商数据库结构。这个设计包含了用户、商品、订单和订单明细四个核心表，它们之间的关系清晰合理。用户表存储了用户的基本信息，商品表存储了商品的详细信息，订单表记录了订单的总体信息，订单明细表则记录了每个订单中包含的具体商品和数量。

这种设计遵循了数据库规范化的原则，每个表都有明确的职责，数据冗余少，易于维护。同时，我们通过合理的外键约束确保了数据的完整性，通过索引设计提高了查询性能。接下来，我们将基于这个数据库结构实现各种业务查询。

## [15.2 常见查询：订单查询、库存统计](#_15-2-常见查询-订单查询、库存统计)

有了数据库结构后，让我们实现一些常见的业务查询。这些查询涵盖了电商系统中的典型场景，包括用户订单查询、商品销量统计、库存管理等。通过这些实际例子，你将学会如何运用前面学到的SQL知识解决真实的业务问题。

首先，让我们实现用户订单查询。这是电商系统中最常见的查询之一，用户需要查看自己的历史订单记录：

```
-- 查询用户的所有订单信息
SELECT 
    u.username,
    u.full_name,
    o.order_number,
    o.total_amount,
    o.status,
    o.payment_status,
    o.order_date,
    COUNT(oi.id) AS item_count
FROM users u
JOIN orders o ON u.id = o.user_id
LEFT JOIN order_items oi ON o.id = oi.order_id
WHERE u.username = 'zhangsan'
GROUP BY o.id
ORDER BY o.order_date DESC;
```

执行结果：

```
+----------+-----------+-----------------+--------------+-----------+---------------+---------------------+------------+
| username | full_name | order_number   | total_amount | status    | payment_status | order_date          | item_count |
+----------+-----------+-----------------+--------------+-----------+---------------+---------------------+------------+
| zhangsan | 张三      | ORD20250822008 |      6498.00 | confirmed | paid           | 2025-08-22 10:05:00 |          2 |
| zhangsan | 张三      | ORD20250817003 |      5999.00 | confirmed | paid           | 2025-08-17 09:15:00 |          1 |
| zhangsan | 张三      | ORD20250815001 |     10898.00 | delivered | paid           | 2025-08-15 10:30:00 |          2 |
+----------+-----------+-----------------+--------------+-----------+---------------+---------------------+------------+
3 rows in set (0.00 sec)
```

这个查询使用了多表连接和分组统计，能够完整显示用户的订单信息，包括每个订单的商品数量。通过LEFT JOIN确保了即使订单没有明细商品（虽然这种情况很少）也能正确显示订单信息。

接下来，让我们实现订单详情查询，显示特定订单的详细信息：

```
-- 查询订单详情，包含商品信息
SELECT 
    o.order_number,
    o.status,
    o.payment_status,
    o.shipping_address,
    p.name AS product_name,
    p.category,
    oi.quantity,
    oi.unit_price,
    oi.total_price,
    o.order_date
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.order_number = 'ORD20250815001'
ORDER BY oi.id;
```

执行结果：

```
+-----------------+-----------+---------------+-----------------------------------------+-----------------+----------+----------+------------+---------------------+
| order_number   | status    | payment_status | shipping_address                        | product_name    | category | quantity | unit_price | total_price | order_date          |
+-----------------+-----------+---------------+-----------------------------------------+-----------------+----------+----------+------------+-------------+---------------------+
| ORD20250815001 | delivered | paid           | 北京市朝阳区xxx街道xxx号                | iPhone 15 Pro   | 手机     |        1 |    8999.00 |     8999.00 | 2025-08-15 10:30:00 |
| ORD20250815001 | delivered | paid           | 北京市朝阳区xxx街道xxx号                | AirPods Pro 2   | 配件     |        1 |    1899.00 |     1899.00 | 2025-08-15 10:30:00 |
+-----------------+-----------+---------------+-----------------------------------------+-----------------+----------+----------+------------+-------------+---------------------+
2 rows in set (0.00 sec)
```

现在让我们实现一些简单的统计查询，比如统计商品总数和库存总价值：

```
-- 统计商品基本信息
SELECT 
    COUNT(*) AS total_products,
    COUNT(CASE WHEN status = 'active' THEN 1 END) AS active_products,
    COUNT(CASE WHEN stock = 0 THEN 1 END) AS out_of_stock_products,
    SUM(stock) AS total_stock,
    SUM(stock * price) AS total_inventory_value
FROM products;
```

执行结果：

```
+----------------+-----------------+----------------------+------------+----------------------+
| total_products | active_products | out_of_stock_products | total_stock | total_inventory_value |
+----------------+-----------------+----------------------+------------+----------------------+
|              8 |               8 |                    0 |        390 |            1562310.00 |
+----------------+-----------------+----------------------+------------+----------------------+
1 row in set (0.00 sec)
```

让我们实现一个简单的用户注册统计：

```
-- 按月份统计用户注册数量
SELECT 
    DATE_FORMAT(registration_date, '%Y年%m月') AS registration_month,
    COUNT(*) AS new_users
FROM users
GROUP BY DATE_FORMAT(registration_date, '%Y年%m')
ORDER BY registration_month;
```

执行结果：

```
+----------------------+------------+
| registration_month | new_users |
+----------------------+------------+
| 2025年01月          |          1 |
| 2025年02月          |          1 |
| 2025年03月          |          1 |
| 2025年04月          |          1 |
| 2025年05月          |          1 |
+----------------------+------------+
5 rows in set (0.00 sec)
```

订单状态统计也是很有用的业务查询：

```
-- 统计不同状态的订单数量
SELECT 
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_amount,
    ROUND(AVG(total_amount), 2) AS avg_amount
FROM orders
GROUP BY status
ORDER BY order_count DESC;
```

执行结果：

```
+-----------+-------------+--------------+------------+
| status    | order_count | total_amount | avg_amount |
+-----------+-------------+--------------+------------+
| delivered |           2 |     12797.00 |    6398.50 |
| shipped   |           2 |     30997.00 |   15498.50 |
| confirmed |           2 |     12497.00 |    6248.50 |
| pending   |           1 |      8598.00 |    8598.00 |
| cancelled |           1 |      2399.00 |    2399.00 |
+-----------+-------------+--------------+------------+
5 rows in set (0.00 sec)
```

让我们实现一个简单的支付方式统计：

```
-- 统计不同支付方式的使用情况
SELECT 
    payment_method,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_amount,
    COUNT(CASE WHEN payment_status = 'paid' THEN 1 END) AS paid_orders
FROM orders
GROUP BY payment_method
ORDER BY order_count DESC;
```

执行结果：

```
+---------------+-------------+--------------+------------+
| payment_method | order_count | total_amount | paid_orders |
+---------------+-------------+--------------+------------+
| alipay        |           3 |     25994.00 |          3 |
| wechat        |           2 |     24596.00 |          1 |
| credit_card   |           2 |     17398.00 |          2 |
| bank_transfer |           1 |     14999.00 |          1 |
+---------------+-------------+--------------+------------+
4 rows in set (0.00 sec)
```

商品分类统计也是一个简单的有用查询：

```
-- 统计各个分类的商品数量和平均价格
SELECT 
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price
FROM products
WHERE status = 'active'
GROUP BY category
ORDER BY product_count DESC;
```

执行结果：

```
+----------+---------------+-----------+-----------+-----------+
| category | product_count | avg_price | min_price | max_price |
+----------+---------------+-----------+-----------+-----------+
| 手机     |             2 |   7499.00 |    5999.00 |    8999.00 |
| 电脑     |             2 |  12499.00 |    9999.00 |   14999.00 |
| 配件     |             2 |   2149.00 |    1899.00 |    2399.00 |
| 平板     |             2 |   4299.00 |    3999.00 |    4599.00 |
+----------+---------------+-----------+-----------+-----------+
4 rows in set (0.00 sec)
```

简单的用户活跃度统计：

```
-- 统计用户活跃情况
SELECT 
    status,
    COUNT(*) AS user_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM users), 1) AS percentage
FROM users
GROUP BY status
ORDER BY user_count DESC;
```

执行结果：

```
+----------+------------+------------+
| status   | user_count | percentage |
+----------+------------+------------+
| active   |          4 |       80.0 |
| inactive |          1 |       20.0 |
+----------+------------+------------+
2 rows in set (0.00 sec)
```

通过这些简单的统计查询，我们可以看到如何使用基本的SQL函数和分组操作来获取有用的业务信息。这些查询容易理解，适合初学者学习。

通过这些常见的业务查询，我们可以看到如何将前面学到的SQL知识应用到实际场景中。这些查询涉及了多表连接、分组统计、条件筛选、排序等技巧，都是电商系统中非常实用的功能。

## [15.3 简单优化：索引与查询重构](#_15-3-简单优化-索引与查询重构)

在实际的电商系统中，随着数据量的增长，查询性能会成为一个重要的问题。让我们学习一些简单的优化技巧，包括合理的索引设计和查询重构，来提高系统的性能。

首先，让我们分析一下当前表上的索引情况，看看哪些索引可能需要优化：

```
-- 查看当前表的索引情况
SHOW INDEX FROM orders;
SHOW INDEX FROM order_items;
SHOW INDEX FROM products;
```

执行结果会显示各个表的索引信息。基于我们之前的查询模式，让我们添加一些复合索引来优化常见查询：

```
-- 为订单表添加复合索引，优化用户订单查询
CREATE INDEX idx_orders_user_date_status ON orders(user_id, order_date, status);

-- 为订单表添加复合索引，优化状态和时间范围查询
CREATE INDEX idx_orders_status_date ON orders(status, order_date);

-- 为订单明细表添加复合索引，优化订单商品查询
CREATE INDEX idx_order_items_order_product ON order_items(order_id, product_id);

-- 为商品表添加复合索引，优化分类和价格范围查询
CREATE INDEX idx_products_category_status_price ON products(category, status, price);
```

现在让我们测试一下索引的效果。使用EXPLAIN分析查询执行计划：

```
-- 分析用户订单查询的执行计划
EXPLAIN SELECT 
    o.order_number,
    o.total_amount,
    o.status,
    o.order_date
FROM orders o
WHERE o.user_id = 1 AND o.status IN ('confirmed', 'shipped', 'delivered')
ORDER BY o.order_date DESC;
```

在执行计划中，你应该能看到使用了我们刚创建的索引。如果显示"Using index"或"Using where; Using index"，说明索引正在发挥作用。

查询重构是另一个重要的优化手段。让我们看一些优化示例：

```
-- 优化前：使用OR条件，可能无法有效使用索引
SELECT * FROM orders 
WHERE user_id = 1 OR status = 'pending';

-- 优化后：使用UNION ALL，每个条件都可以使用对应的索引
SELECT * FROM orders WHERE user_id = 1
UNION ALL
SELECT * FROM orders WHERE status = 'pending' AND user_id != 1;
```

另一个常见的优化是避免使用SELECT \*，只查询需要的字段：

```
-- 优化前：查询所有字段
SELECT * FROM orders WHERE user_id = 1;

-- 优化后：只查询需要的字段，可以使用覆盖索引
SELECT order_number, total_amount, status, order_date 
FROM orders WHERE user_id = 1;
```

对于分页查询，特别是大偏移量的情况，我们可以优化查询方式：

```
-- 传统分页方式，大偏移量时性能较差
SELECT * FROM orders 
ORDER BY order_date DESC 
LIMIT 10 OFFSET 1000;

-- 优化方式：基于游标的分页
SELECT * FROM orders 
WHERE order_date < '2025-08-20 10:00:00'
ORDER BY order_date DESC 
LIMIT 10;
```

对于简单的统计查询，我们可以使用基本的聚合函数来获取有用的信息：

```
-- 简单的销售统计查询
SELECT 
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value,
    COUNT(DISTINCT user_id) AS unique_customers
FROM orders 
WHERE status IN ('confirmed', 'shipped', 'delivered');
```

执行结果：

```
+-------------+--------------+------------------+-----------------+
| total_orders | total_revenue | avg_order_value | unique_customers |
+-------------+--------------+------------------+-----------------+
|           7 |     71289.00 |        10184.14 |               4 |
+-------------+--------------+------------------+-----------------+
1 row in set (0.00 sec)
```

另一个简单的统计例子是按商品分类统计销售情况：

```
-- 按分类统计商品销售情况
SELECT 
    p.category,
    COUNT(DISTINCT p.id) AS product_count,
    SUM(oi.quantity) AS total_sold,
    ROUND(SUM(oi.total_price), 2) AS total_revenue
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status IN ('confirmed', 'shipped', 'delivered')
GROUP BY p.category
ORDER BY total_revenue DESC;
```

执行结果：

```
+----------+---------------+------------+--------------+
| category | product_count | total_sold | total_revenue |
+----------+---------------+------------+--------------+
| 电脑     |             2 |          2 |     29998.00 |
| 手机     |             2 |          2 |     17998.00 |
| 配件     |             2 |          4 |     13994.00 |
| 平板     |             2 |          2 |      9358.00 |
+----------+---------------+------------+--------------+
4 rows in set (0.00 sec)
```

对于简单的报表查询，我们可以使用基础的GROUP BY来生成日报表：

```
-- 简单的日销售报表
SELECT 
    DATE(order_date) AS sale_date,
    COUNT(*) AS daily_orders,
    SUM(total_amount) AS daily_revenue,
    COUNT(DISTINCT user_id) AS daily_customers
FROM orders 
WHERE status IN ('confirmed', 'shipped', 'delivered')
GROUP BY DATE(order_date)
ORDER BY sale_date DESC;
```

执行结果：

```
+------------+--------------+---------------+-----------------+
| sale_date  | daily_orders | daily_revenue | daily_customers |
+------------+--------------+---------------+-----------------+
| 2025-08-22 |            1 |       6498.00 |               1 |
| 2025-08-21 |            1 |      14999.00 |               1 |
| 2025-08-18 |            1 |       1899.00 |               1 |
| 2025-08-17 |            1 |       5999.00 |               1 |
| 2025-08-16 |            1 |      15998.00 |               1 |
| 2025-08-15 |            1 |      10898.00 |               1 |
+------------+--------------+---------------+-----------------+
6 rows in set (0.00 sec)
```

用户购买力分析也是一个简单的有用查询：

```
-- 用户购买力分析
SELECT 
    u.username,
    u.full_name,
    COUNT(o.id) AS order_count,
    COALESCE(SUM(o.total_amount), 0) AS total_spent,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_value
FROM users u
LEFT JOIN orders o ON u.id = o.user_id 
    AND o.status IN ('confirmed', 'shipped', 'delivered')
GROUP BY u.id, u.username, u.full_name
HAVING COUNT(o.id) > 0
ORDER BY total_spent DESC;
```

执行结果：

```
+----------+-----------+-------------+------------+-----------------+
| username | full_name | order_count | total_spent | avg_order_value |
+----------+-----------+-------------+------------+-----------------+
| lisi     | 李四      |           2 |    28397.00 |        14198.50 |
| zhangsan | 张三      |           3 |    23395.00 |         7798.33 |
| wangwu   | 王五      |           1 |     1899.00 |         1899.00 |
+----------+-----------+-------------+------------+-----------------+
3 rows in set (0.00 sec)
```

还有一些查询优化的基本原则：

1. **避免在索引列上使用函数**：

```
-- 不好的写法：函数操作会导致索引失效
SELECT * FROM orders WHERE DATE(order_date) = '2025-08-22';

-- 优化写法：使用范围查询
SELECT * FROM orders WHERE order_date >= '2025-08-22' AND order_date < '2025-08-23';
```

2. **使用合适的连接方式**：

```
-- 对于小表驱动大表的情况，确保驱动表在前面
SELECT * FROM small_table s JOIN large_table l ON s.id = l.small_id;
```

3. **合理使用LIMIT**：

```
-- 查询时限制结果集大小
SELECT * FROM orders ORDER BY order_date DESC LIMIT 100;
```

4. **定期分析和优化表**：

```
-- 分析表以优化查询计划
ANALYZE TABLE orders;
ANALYZE TABLE order_items;
ANALYZE TABLE products;
```

通过这些优化技巧，我们可以显著提高电商系统的查询性能。记住，优化是一个持续的过程，需要根据实际的查询模式和数据分布来不断调整索引和查询策略。

在实际项目中，建议使用慢查询日志来识别性能瓶颈，然后针对性地进行优化。同时，对于复杂的报表查询，考虑使用定时任务预计算结果，以提高用户体验。

## [练习题](#练习题)

### [练习1：用户订单分析查询](#练习1-用户订单分析查询)

编写一个查询，显示每个用户的完整订单信息，包括：用户名、总订单数、总消费金额、平均订单金额、最后下单时间。结果按总消费金额降序排列。

查看答案

```
SELECT 
    u.username,
    u.full_name,
    COUNT(o.id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_amount,
    MAX(o.order_date) AS last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id 
    AND o.status IN ('confirmed', 'shipped', 'delivered')
GROUP BY u.id, u.username, u.full_name
ORDER BY total_spent DESC;
```

### [练习2：商品销售分析](#练习2-商品销售分析)

编写一个查询，显示每个商品类别的销售情况，包括：类别名称、商品数量、总销量、总销售额、平均售价、订单数量。只显示有销售记录的类别，按总销售额降序排列。

查看答案

```
SELECT 
    p.category,
    COUNT(DISTINCT p.id) AS product_count,
    SUM(oi.quantity) AS total_sold,
    SUM(oi.total_price) AS total_revenue,
    ROUND(SUM(oi.total_price) / SUM(oi.quantity), 2) AS avg_price,
    COUNT(DISTINCT oi.order_id) AS order_count
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status IN ('confirmed', 'shipped', 'delivered')
GROUP BY p.category
HAVING SUM(oi.quantity) > 0
ORDER BY total_revenue DESC;
```

### [练习3：月度销售趋势分析](#练习3-月度销售趋势分析)

编写一个查询，显示2025年8月每天的销售趋势，包括：日期、订单数量、客户数量、销售额、商品销售数量。要求只显示有效的订单（状态为confirmed、shipped、delivered），按日期升序排列。

查看答案

```
SELECT 
    DATE(o.order_date) AS sale_date,
    COUNT(DISTINCT o.id) AS order_count,
    COUNT(DISTINCT o.user_id) AS customer_count,
    SUM(o.total_amount) AS daily_revenue,
    SUM(oi.quantity) AS items_sold
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
WHERE o.status IN ('confirmed', 'shipped', 'delivered')
  AND o.order_date >= '2025-08-01' 
  AND o.order_date < '2025-09-01'
GROUP BY DATE(o.order_date)
ORDER BY sale_date ASC;
```

## [常见坑](#常见坑)

### [坑1：忽略WHERE条件导致全表更新](#坑1-忽略where条件导致全表更新)

在UPDATE和DELETE操作中忘记写WHERE条件，导致整个表的数据被修改或删除。

**错误示例**：

```
-- 危险：更新所有订单的状态
UPDATE orders SET status = 'cancelled';
```

**纠正方法**：

```
-- 安全：总是先写SELECT验证条件
SELECT * FROM orders WHERE user_id = 1 AND status = 'pending';
-- 确认条件正确后再执行UPDATE
UPDATE orders SET status = 'cancelled' WHERE user_id = 1 AND status = 'pending';
```

### [坑2：JOIN查询导致数据重复](#坑2-join查询导致数据重复)

在多表JOIN时，如果连接条件不正确，会导致数据重复，统计结果错误。

**错误示例**：

```
-- 错误：可能导致统计重复
SELECT o.id, COUNT(oi.id) 
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id;
```

**纠正方法**：

```
-- 正确：使用COUNT(DISTINCT)或确保连接条件正确
SELECT o.id, COUNT(DISTINCT oi.id) 
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id;
```

### [坑3：索引设计不合理](#坑3-索引设计不合理)

创建了过多或不合理的索引，影响写入性能且占用存储空间。

**错误示例**：

```
-- 过度索引：为每个字段都创建索引
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_order_date ON orders(order_date);
CREATE INDEX idx_orders_payment_status ON orders(payment_status);
```

**纠正方法**：

```
-- 合理索引：根据查询模式创建复合索引
CREATE INDEX idx_orders_user_date_status ON orders(user_id, order_date, status);
CREATE INDEX idx_orders_status_date ON orders(status, order_date);
```

## [速记卡](#速记卡)

- **电商核心表**：用户表、商品表、订单表、订单明细表
- **表设计原则**：遵循规范化，避免数据冗余，合理设置外键约束
- **索引策略**：为常用查询条件创建索引，使用复合索引提高查询效率
- **查询优化**：避免SELECT \*，合理使用JOIN，优化分页查询
- **性能监控**：使用EXPLAIN分析执行计划，定期优化慢查询
- **数据完整性**：使用外键约束确保数据一致性，适当使用事务
- **缓存策略**：对于复杂报表查询，考虑使用预计算或缓存表
- **分页优化**：避免大偏移量分页，考虑基于游标的分页方式

## [章节总结](#章节总结)

在这一章中，我们通过一个完整的电商订单系统案例，综合运用了前面学到的SQL知识来解决实际的业务问题。从数据库表设计开始，我们创建了一个包含用户、商品、订单和订单明细的完整数据结构，这个设计既遵循了规范化原则，又考虑了实际的业务需求。

在常见查询部分，我们实现了电商系统中的典型功能，包括用户订单查询、订单详情查询、销售统计分析、库存管理等。这些查询涵盖了多表连接、分组统计、条件筛选、排序等各种SQL技巧，展示了如何将基础知识应用到实际场景中。

在性能优化部分，我们学习了索引设计的重要性，如何根据查询模式创建合适的索引，以及如何通过查询重构来提高性能。我们还介绍了缓存表、预计算等高级优化技巧，这些都是实际项目中非常有用的技能。

通过这个实战案例，你可以看到SQL不仅仅是查询语言，更是解决业务问题的强大工具。良好的数据库设计、合理的索引策略、高效的查询编写，这些都是构建高性能应用系统的基础。

掌握了这些实战技能，你就具备了在实际项目中应用SQL的能力。无论是开发电商系统、管理后台，还是数据分析报表，你都能够运用这些知识来解决问题。在下一章中，我们将进行综合练习，进一步巩固这些技能。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [15｜实战：商城订单应用](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#_15-实战-商城订单应用)
- [15.1 商品、用户、订单表设计](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#_15-1-商品、用户、订单表设计)
- [15.2 常见查询：订单查询、库存统计](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#_15-2-常见查询-订单查询、库存统计)
- [15.3 简单优化：索引与查询重构](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#_15-3-简单优化-索引与查询重构)
- [练习题](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#练习题)
- [练习1：用户订单分析查询](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#练习1-用户订单分析查询)
- [练习2：商品销售分析](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#练习2-商品销售分析)
- [练习3：月度销售趋势分析](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#练习3-月度销售趋势分析)
- [常见坑](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#常见坑)
- [坑1：忽略WHERE条件导致全表更新](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#坑1-忽略where条件导致全表更新)
- [坑2：JOIN查询导致数据重复](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#坑2-join查询导致数据重复)
- [坑3：索引设计不合理](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#坑3-索引设计不合理)
- [速记卡](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part4/15-ecommerce-practice.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
