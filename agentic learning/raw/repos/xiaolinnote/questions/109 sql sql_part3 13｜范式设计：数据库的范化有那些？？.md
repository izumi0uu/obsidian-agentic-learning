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
url: https://xiaolinnote.com/sql/sql_part3/13-normalization.html
source: https://xiaolinnote.com/sql/sql_part3/13-normalization.html
last_checked: 2026-05-17
freshness: watch
sha256: d1be894ad768b1cb202b34edc4e284d405a84ae7326216a70080a4650fe3e579
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 13｜范式设计：数据库的范化有那些？？

原始链接：https://xiaolinnote.com/sql/sql_part3/13-normalization.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 13｜范式设计：数据库的范化有那些？？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 28 分钟约 8362 字2025/8/31

---

# [13｜范式设计：数据库的范化有那些？？](#_13-范式设计-数据库的范化有那些)

大家好，我是小林。

在前面的章节中，我们学习了如何创建表、修改表结构，以及如何进行各种数据操作。但是，你有没有想过这样一个问题：我们应该如何设计表的结构，才能让数据存储既高效又可靠？当用户信息发生变化时，如果这个信息在多个地方重复存储，我们是否需要更新所有地方？如果订单信息中包含了大量的冗余数据，这会对数据库性能产生什么影响？

你有没有想过，当你在一个电商网站上修改收货地址时，为什么只需要修改一次，所有相关的订单记录都会使用新的地址？当你看到用户信息表中，每个用户的地址都只存储一次，而不是在每个订单中都重复存储，这背后有什么设计原则？当数据库设计中出现数据冗余时，会导致哪些问题，又该如何解决？

在这一章中，我们将学习数据库范式设计的理论知识。从为什么需要规范化开始，到第一范式、第二范式、第三范式的具体要求，再到实际应用中的范式选择。掌握了数据库范式设计，你就能够设计出更加合理和高效的数据库结构，避免数据冗余和更新异常等问题。

准备好了吗？让我们开始学习数据库范式设计的奥秘吧！

## [13.1 为什么需要规范化](#_13-1-为什么需要规范化)

数据库规范化是数据库设计的核心理论，它帮助我们设计出结构合理、数据冗余少、易于维护的数据库结构。那么，什么是规范化，为什么我们需要它呢？

让我们通过一个实际的例子来理解规范化的重要性。假设我们正在设计一个简单的订单管理系统，如果不考虑规范化，我们可能会设计出这样的表结构：

```
-- 创建一个未规范化的订单表
DROP TABLE IF EXISTS poorly_designed_orders;
CREATE TABLE poorly_designed_orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_number VARCHAR(20) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(100) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    customer_address TEXT NOT NULL,
    product1_name VARCHAR(100),
    product1_price DECIMAL(10,2),
    product1_quantity INT,
    product2_name VARCHAR(100),
    product2_price DECIMAL(10,2),
    product2_quantity INT,
    product3_name VARCHAR(100),
    product3_price DECIMAL(10,2),
    product3_quantity INT,
    total_amount DECIMAL(10,2),
    order_date DATE NOT NULL
);

-- 插入一些示例数据
INSERT INTO poorly_designed_orders (order_number, customer_name, customer_email, customer_phone, customer_address, 
    product1_name, product1_price, product1_quantity, product2_name, product2_price, product2_quantity, total_amount, order_date) 
VALUES 
('ORD001', '张三', 'zhangsan@example.com', '13800138000', '北京市朝阳区xxx街道xxx号', 
    'iPhone 15', 5999.00, 1, 'AirPods Pro', 1899.00, 1, 7898.00, '2025-08-01'),
('ORD002', '张三', 'zhangsan@example.com', '13800138000', '北京市朝阳区xxx街道xxx号', 
    'MacBook Pro', 12999.00, 1, NULL, NULL, NULL, 12999.00, '2025-08-02'),
('ORD003', '李四', 'lisi@example.com', '13900139000', '上海市浦东新区xxx路xxx号', 
    '小米13', 3999.00, 2, NULL, NULL, NULL, 7998.00, '2025-08-03');
```

让我们看看这个表设计存在哪些问题。首先，查询同一个客户的不同订单：

```
SELECT order_number, customer_name, customer_email, customer_address
FROM poorly_designed_orders
WHERE customer_name = '张三';
```

执行结果：

```
+-------------+--------------+-------------------+-----------------------------+
| order_number | customer_name | customer_email    | customer_address            |
+-------------+--------------+-------------------+-----------------------------+
| ORD001      | 张三         | zhangsan@example.com | 北京市朝阳区xxx街道xxx号    |
| ORD002      | 张三         | zhangsan@example.com | 北京市朝阳区xxx街道xxx号    |
+-------------+--------------+-------------------+-----------------------------+
2 rows in set (0.00 sec)
```

可以看到，张三的客户信息在每条订单记录中都重复存储。这种设计会导致以下几个严重问题：

**数据冗余**：同一个客户的信息在多个订单中重复存储，浪费存储空间。更严重的是，当客户信息发生变化时，比如张三搬家了，我们需要更新所有包含他的订单记录。

**更新异常**：假设张三的地址发生了变化，我们需要执行这样的更新：

```
UPDATE poorly_designed_orders 
SET customer_address = '北京市海淀区xxx街道xxx号' 
WHERE customer_name = '张三';
```

这个操作看似简单，但如果系统中有大量订单，更新操作会非常耗时，而且可能在更新过程中出现部分更新成功、部分失败的情况，导致数据不一致。

**插入异常**：如果我们想要添加一个新客户，但这个客户还没有下过订单，我们就无法将客户信息存入数据库，因为所有字段都与订单相关。

**删除异常**：如果我们删除了客户的最后一个订单，客户的详细信息也会随之丢失，因为我们没有单独的地方存储客户信息。

**扩展性问题**：每个订单只能包含最多3个产品，如果客户想要购买更多产品，我们就需要修改表结构，这在实际应用中是不可接受的。

规范化正是为了解决这些问题而提出的。通过将数据分解到多个相关的表中，每个表只关注一个特定的主题，我们可以消除数据冗余，避免各种异常情况。

让我们看看规范化后的设计是什么样的：

```
-- 创建客户表
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建产品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建订单表
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_number VARCHAR(20) UNIQUE NOT NULL,
    customer_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATE NOT NULL,
    status ENUM('pending', 'confirmed', 'shipped', 'delivered') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- 创建订单明细表
DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- 插入示例数据
INSERT INTO customers (name, email, phone, address) VALUES 
('张三', 'zhangsan@example.com', '13800138000', '北京市朝阳区xxx街道xxx号'),
('李四', 'lisi@example.com', '13900139000', '上海市浦东新区xxx路xxx号');

INSERT INTO products (name, price, stock) VALUES 
('iPhone 15', 5999.00, 100),
('AirPods Pro', 1899.00, 200),
('MacBook Pro', 12999.00, 50),
('小米13', 3999.00, 150);

INSERT INTO orders (order_number, customer_id, total_amount, order_date, status) VALUES 
('ORD001', 1, 7898.00, '2025-08-01', 'delivered'),
('ORD002', 1, 12999.00, '2025-08-02', 'shipped'),
('ORD003', 2, 7998.00, '2025-08-03', 'confirmed');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES 
(1, 1, 1, 5999.00),  -- 订单1：iPhone 15
(1, 2, 1, 1899.00),  -- 订单1：AirPods Pro
(2, 3, 1, 12999.00), -- 订单2：MacBook Pro
(3, 4, 2, 3999.00);  -- 订单3：小米13 × 2
```

现在，当我们需要更新客户信息时，只需要在customers表中更新一次：

```
UPDATE customers SET address = '北京市海淀区xxx街道xxx号' WHERE id = 1;
```

这个更新操作只需要修改一条记录，无论这个客户有多少个订单。这就是规范化的优势所在。

规范化带来的好处不仅仅体现在数据更新上，还体现在数据一致性和查询灵活性上。通过合理的数据分解，我们可以更容易地维护数据的完整性，避免数据冗余导致的矛盾。

在实际应用中，规范化是数据库设计的基础。它帮助我们建立清晰的数据结构，让数据管理变得更加高效和可靠。接下来，我们将学习具体的范式规则，了解如何一步步地将未规范化的表设计转换为规范化的结构。

## [13.2 数据库三大范式](#_13-2-数据库三大范式)

数据库范式是一系列规则，帮助我们设计出结构良好的数据库。这些范式按顺序递进，每一级范式都建立在前一级的基础上，提供更严格的数据组织要求。让我们通过实际的例子来理解这三个最重要的范式。

### [第一范式(1NF)](#第一范式-1nf)

第一范式是最基本的范式要求，它规定表中的每个字段都必须是原子的，不可再分的。同时，表中的每一行都必须是唯一的，可以通过主键来标识。

让我们看看违反第一范式的例子：

```
-- 违反第一范式的表设计
DROP TABLE IF EXISTS violation_1nf;
CREATE TABLE violation_1nf (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    courses VARCHAR(255),  -- 存储多个课程，用逗号分隔
    grades VARCHAR(255)    -- 存储多个成绩，用逗号分隔
);

-- 插入示例数据
INSERT INTO violation_1nf (student_name, courses, grades) VALUES 
('张三', '数学,语文,英语', '90,85,88'),
('李四', '物理,化学', '92,87');
```

这个设计违反了第一范式，因为courses和grades字段包含了多个值，不是原子的。这会导致很多问题，比如我们很难查询选修了特定课程的学生：

```
-- 查询选修了数学的学生（这种方法不可靠）
SELECT * FROM violation_1nf WHERE courses LIKE '%数学%';
```

执行结果：

```
+----+--------------+----------------+-------------+
| id | student_name | courses        | grades      |
+----+--------------+----------------+-------------+
|  1 | 张三         | 数学,语文,英语 | 90,85,88    |
+----+--------------+----------------+-------------+
1 row in set (0.00 sec)
```

这种查询方式很不可靠，如果有一个课程叫"高等数学"，LIKE查询会错误地匹配到它。而且，我们无法轻松地进行课程数量的统计，也无法保证课程和成绩的对应关系。

让我们将这个表转换为第一范式：

```
-- 符合第一范式的表设计
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS student_courses;
CREATE TABLE student_courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    grade DECIMAL(5,2),
    semester VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- 插入示例数据
INSERT INTO students (name, email) VALUES 
('张三', 'zhangsan@example.com'),
('李四', 'lisi@example.com');

INSERT INTO student_courses (student_id, course_name, grade, semester) VALUES 
(1, '数学', 90.00, '2025春季'),
(1, '语文', 85.00, '2025春季'),
(1, '英语', 88.00, '2025春季'),
(2, '物理', 92.00, '2025春季'),
(2, '化学', 87.00, '2025春季');
```

现在我们可以轻松地进行各种查询：

```
-- 查询选修了数学的学生
SELECT s.name, sc.course_name, sc.grade
FROM students s
JOIN student_courses sc ON s.id = sc.student_id
WHERE sc.course_name = '数学';

-- 统计每个学生的选课数量
SELECT s.name, COUNT(sc.course_name) AS course_count
FROM students s
LEFT JOIN student_courses sc ON s.id = sc.student_id
GROUP BY s.id, s.name;
```

执行结果：

```
+--------+-------------+-------+
| name   | course_name | grade |
+--------+-------------+-------+
| 张三   | 数学        | 90.00 |
+--------+-------------+-------+
1 row in set (0.00 sec)

+--------+--------------+
| name   | course_count |
+--------+--------------+
| 张三   |            3 |
| 李四   |            2 |
+--------+--------------+
2 rows in set (0.00 sec)
```

第一范式的要求可以总结为：

1. 每个字段都是原子的，不可再分
2. 每个记录都是唯一的，有主键标识
3. 字段的值都是标量，不是列表或集合

### [第二范式(2NF)](#第二范式-2nf)

第二范式建立在第一范式的基础上，它要求所有非主键字段都必须完全依赖于整个主键，而不是只依赖于主键的一部分。这个范式主要针对有复合主键的表。

让我们看一个违反第二范式的例子：

```
-- 违反第二范式的表设计
DROP TABLE IF EXISTS violation_2nf;
CREATE TABLE violation_2nf (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade DECIMAL(5,2),
    student_name VARCHAR(100),  -- 依赖于student_id
    course_name VARCHAR(100),  -- 依赖于course_id
    teacher_name VARCHAR(100), -- 依赖于course_id
    PRIMARY KEY (student_id, course_id)
);

-- 插入示例数据
INSERT INTO violation_2nf (student_id, course_id, grade, student_name, course_name, teacher_name) VALUES 
(1, 101, 90.00, '张三', '数学', '王老师'),
(1, 102, 85.00, '张三', '语文', '李老师'),
(2, 101, 88.00, '李四', '数学', '王老师');
```

这个表的主键是(student\_id, course\_id)的复合主键，但student\_name只依赖于student\_id，course\_name和teacher\_name只依赖于course\_id，这违反了第二范式。

这种设计会导致数据冗余。比如，如果同一个学生选修了多门课程，他的名字会在多个记录中重复存储。同样，同一门课程如果有多个学生选修，课程名称和教师姓名也会重复存储。

让我们将其转换为第二范式：

```
-- 符合第二范式的表设计
DROP TABLE IF EXISTS students_2nf;
CREATE TABLE students_2nf (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS courses_2nf;
CREATE TABLE courses_2nf (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    teacher_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL
);

DROP TABLE IF EXISTS enrollments;
CREATE TABLE enrollments (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade DECIMAL(5,2),
    semester VARCHAR(20),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students_2nf(id),
    FOREIGN KEY (course_id) REFERENCES courses_2nf(id)
);

-- 插入示例数据
INSERT INTO students_2nf (name, email) VALUES 
('张三', 'zhangsan@example.com'),
('李四', 'lisi@example.com');

INSERT INTO courses_2nf (name, teacher_name, credits) VALUES 
('数学', '王老师', 4),
('语文', '李老师', 3);

INSERT INTO enrollments (student_id, course_id, grade, semester) VALUES 
(1, 1, 90.00, '2025春季'),
(1, 2, 85.00, '2025春季'),
(2, 1, 88.00, '2025春季');
```

现在，学生信息只在students\_2nf表中存储一次，课程信息只在courses\_2nf表中存储一次，完全消除了数据冗余。

### [第三范式(3NF)](#第三范式-3nf)

第三范式建立在第二范式的基础上，它要求所有非主键字段都必须直接依赖于主键，而不能存在传递依赖。也就是说，非主键字段不能依赖于其他非主键字段。

让我们看一个违反第三范式的例子：

```
-- 违反第三范式的表设计
DROP TABLE IF EXISTS violation_3nf;
CREATE TABLE violation_3nf (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    department_name VARCHAR(100) NOT NULL,
    department_location VARCHAR(100),  -- 依赖于department_name，不是直接依赖于id
    building_name VARCHAR(100)         -- 可能依赖于department_location
);

-- 插入示例数据
INSERT INTO violation_3nf (student_name, department_name, department_location, building_name) VALUES 
('张三', '计算机系', '理科楼', 'A栋'),
('李四', '计算机系', '理科楼', 'A栋'),
('王五', '数学系', '理科楼', 'A栋'),
('赵六', '物理系', '实验楼', 'B栋');
```

在这个表中，department\_location依赖于department\_name，而不是直接依赖于主键id。如果我们需要更改计算机系的位置，需要更新多条记录。

让我们将其转换为第三范式：

```
-- 符合第三范式的表设计
DROP TABLE IF EXISTS students_3nf;
CREATE TABLE students_3nf (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    building VARCHAR(50) NOT NULL
);

-- 插入示例数据
INSERT INTO departments (name, location, building) VALUES 
('计算机系', '理科楼3层', 'A栋'),
('数学系', '理科楼2层', 'A栋'),
('物理系', '实验楼1层', 'B栋');

INSERT INTO students_3nf (name, email, department_id) VALUES 
('张三', 'zhangsan@example.com', 1),
('李四', 'lisi@example.com', 1),
('王五', 'wangwu@example.com', 2),
('赵六', 'zhaoliu@example.com', 3);
```

现在，如果我们需要更改计算机系的位置，只需要更新departments表中的一条记录：

```
UPDATE departments SET location = '理科楼4层' WHERE name = '计算机系';
```

### [范式设计的实际应用](#范式设计的实际应用)

让我们通过一个完整的例子来展示如何将一个未规范化的设计逐步转换为第三范式：

```
-- 原始的未规范化设计
DROP TABLE IF EXISTS original_orders;
CREATE TABLE original_orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_address VARCHAR(200),
    product_names VARCHAR(500),  -- 多个产品名称用逗号分隔
    product_quantities VARCHAR(200), -- 多个数量用逗号分隔
    product_prices VARCHAR(200),     -- 多个价格用逗号分隔
    order_date DATE,
    total_amount DECIMAL(10,2)
);

-- 转换为第一范式：分解原子字段
DROP TABLE IF EXISTS orders_1nf;
CREATE TABLE orders_1nf (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_address VARCHAR(200),
    product_name VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2),
    order_date DATE
);

-- 转换为第二范式：消除部分依赖
DROP TABLE IF EXISTS customers_2nf;
CREATE TABLE customers_2nf (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(200)
);

DROP TABLE IF EXISTS orders_2nf;
CREATE TABLE orders_2nf (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

DROP TABLE IF EXISTS order_items_2nf;
CREATE TABLE order_items_2nf (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(100),
    quantity INT,
    unit_price DECIMAL(10,2)
);

-- 转换为第三范式：消除传递依赖
DROP TABLE IF EXISTS customers_3nf;
CREATE TABLE customers_3nf (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address_id INT
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
    address_id INT PRIMARY KEY,
    street VARCHAR(200),
    city VARCHAR(100),
    zip_code VARCHAR(20)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    unit_price DECIMAL(10,2)
);

DROP TABLE IF EXISTS orders_3nf;
CREATE TABLE orders_3nf (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

DROP TABLE IF EXISTS order_items_3nf;
CREATE TABLE order_items_3nf (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT
);
```

通过这个完整的转换过程，我们可以看到规范化如何一步步地改善数据库设计。每个范式级别都解决了特定的问题，让数据结构变得更加合理和高效。

在实际应用中，大多数数据库设计都应该至少满足第三范式。这样可以最大限度地减少数据冗余，避免各种更新异常，保证数据的完整性和一致性。

## [13.3 反范式的常见场景](#_13-3-反范式的常见场景)

虽然规范化有很多好处，但在某些情况下，我们可能需要适当地反规范化，以提高查询性能。反规范化是有意识地在规范化设计中引入一定的冗余，以换取查询效率的提升。

让我们通过几个简单的场景来理解什么时候需要反规范化。

### [场景一：学生成绩单查询](#场景一-学生成绩单查询)

**问题描述：** 学校需要频繁查询学生的成绩单，包括学生姓名、课程名称、成绩等信息。如果严格按照规范化设计，每次查询都需要JOIN多个表，性能会很差。

**规范化设计（复杂但结构清晰）：**

```
-- 学生表
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL
);

-- 课程表  
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- 成绩表（规范化设计）
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**查询成绩单需要JOIN操作：**

```
-- 每次查询都需要JOIN，性能较差
SELECT s.student_name, c.course_name, g.score
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN courses c ON g.course_id = c.course_id
WHERE g.student_id = 1;
```

**反规范化设计（简单但存在冗余）：**

```
-- 反规范化的成绩表，直接存储学生姓名和课程名称
CREATE TABLE grades_denormalized (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    student_name VARCHAR(100) NOT NULL,    -- 冗余：学生姓名
    course_id INT NOT NULL,
    course_name VARCHAR(100) NOT NULL,   -- 冗余：课程名称
    score INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**反规范化后的查询：**

```
-- 查询简单快速，不需要JOIN
SELECT student_name, course_name, score
FROM grades_denormalized 
WHERE student_id = 1;
```

**哪里反规范化了？**

1. **student\_name字段冗余**：学生姓名已经存储在students表中，这里又存储了一次
2. **course\_name字段冗余**：课程名称已经存储在courses表中，这里又存储了一次

**为什么这样做？**

- 查询性能提升：不需要多表JOIN，查询速度更快
- 简化应用代码：直接获取所需信息，无需复杂的关联查询
- 适合读多写少的场景：成绩查询频繁，但修改较少

**缺点：**

- 数据冗余：占用更多存储空间
- 更新复杂：如果学生修改姓名，需要更新多个地方
- 数据一致性风险：可能出现学生姓名在不同地方不一致的情况

### [场景二：商品分类显示](#场景二-商品分类显示)

**问题描述：** 电商网站的商品列表页需要频繁显示商品名称、分类名称、价格等信息。如果每次查询都需要JOIN分类表，会影响页面加载速度。

**规范化设计：**

```
-- 商品表
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 分类表
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);
```

**规范化查询（需要JOIN）：**

```
-- 每次查询商品列表都需要JOIN分类表
SELECT p.product_name, c.category_name, p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE p.category_id = 5;
```

**反规范化设计：**

```
-- 反规范化的商品表，直接存储分类名称
CREATE TABLE products_denormalized (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category_id INT NOT NULL,
    category_name VARCHAR(100) NOT NULL,   -- 冗余：分类名称
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
```

**反规范化后的查询：**

```
-- 查询简单快速，不需要JOIN
SELECT product_name, category_name, price
FROM products_denormalized 
WHERE category_id = 5;
```

**哪里反规范化了？**

1. **category\_name字段冗余**：分类名称已经存储在categories表中，这里又存储了一次

**为什么这样做？**

- 提高查询性能：商品列表页访问频繁，减少JOIN操作
- 简化代码逻辑：直接获取分类名称，无需关联查询
- 缓存友好：可以直接缓存商品信息，包含分类名称

### [场景三：用户订单统计](#场景三-用户订单统计)

**问题描述：** 用户个人中心需要显示用户的订单统计信息：总订单数、总消费金额、平均订单金额等。如果每次都需要计算所有订单，性能会很差。

**规范化设计：**

```
-- 用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

-- 订单表
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_amount DECIMAL(10,2) NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**规范化查询（需要实时计算）：**

```
-- 每次都需要扫描所有订单来计算统计信息
SELECT 
    user_id,
    COUNT(*) AS total_orders,
    SUM(order_amount) AS total_spent,
    AVG(order_amount) AS avg_amount
FROM orders 
WHERE user_id = 1
GROUP BY user_id;
```

**反规范化设计：**

```
-- 反规范化的用户统计表
CREATE TABLE user_stats (
    user_id INT PRIMARY KEY,
    total_orders INT NOT NULL DEFAULT 0,        -- 冗余：订单总数
    total_spent DECIMAL(12,2) NOT NULL DEFAULT 0, -- 冗余：总消费金额
    avg_order_amount DECIMAL(10,2) NOT NULL DEFAULT 0, -- 冗余：平均订单金额
    last_order_date DATE,                        -- 冗余：最后订单日期
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**反规范化后的查询：**

```
-- 查询极快，直接读取预计算的统计数据
SELECT total_orders, total_spent, avg_order_amount
FROM user_stats 
WHERE user_id = 1;
```

**哪里反规范化了？**

1. **total\_orders字段冗余**：可以通过COUNT(\*)从orders表计算得出
2. **total\_spent字段冗余**：可以通过SUM(order\_amount)从orders表计算得出
3. **avg\_order\_amount字段冗余**：可以通过AVG(order\_amount)从orders表计算得出
4. **last\_order\_date字段冗余**：可以通过MAX(order\_date)从orders表计算得出

**为什么这样做？**

- 极大提升查询性能：统计信息预计算好，直接读取
- 减少数据库负载：避免频繁的聚合计算
- 适合统计场景：用户个人中心访问频繁，但订单变化相对较少

**维护机制：**

```
-- 当有新订单时，更新统计信息
UPDATE user_stats 
SET 
    total_orders = total_orders + 1,
    total_spent = total_spent + NEW.order_amount,
    avg_order_amount = total_spent / total_orders,
    last_order_date = NEW.order_date
WHERE user_id = NEW.user_id;
```

### [反规范化的注意事项](#反规范化的注意事项)

反规范化虽然能提高查询性能，但也带来了一些挑战：

**数据一致性问题**：由于同一数据在多个地方存储，需要确保这些数据的一致性。通常通过触发器、存储过程或应用层逻辑来维护。

**存储空间增加**：冗余数据会占用更多的存储空间，需要在性能和成本之间找到平衡。

**更新复杂性**：更新数据时需要更新多个地方，增加了系统的复杂性。

**数据过期风险**：如果更新机制出现问题，可能会导致数据不一致或过期。

在实际应用中，反规范化应该是一个有意识的设计决策，而不是随意的做法。通常在以下情况下考虑反规范化：

1. 查询性能成为系统瓶颈
2. 读操作远多于写操作
3. 数据更新频率较低
4. 有可靠的数据同步机制

反规范化的程度也需要仔细权衡。过度反规范化可能会导致严重的维护问题，而适度的反规范化则能在性能和可维护性之间取得良好的平衡。

## [练习题](#练习题)

### [练习1：识别范式违规](#练习1-识别范式违规)

分析下面的表结构，指出它违反了哪些范式，并将其转换为第三范式。

```
CREATE TABLE student_records (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    courses VARCHAR(500),  -- 存储多个课程，用逗号分隔
    grades VARCHAR(200),    -- 存储多个成绩，用逗号分隔
    department_name VARCHAR(100),
    department_head VARCHAR(100),  -- 系主任姓名
    building_location VARCHAR(100)
);
```

查看答案

这个表存在以下范式违规问题：

1. **违反第一范式**：courses和grades字段不是原子的，包含了多个值
2. **违反第二范式**：如果主键是student\_id，那么department\_name、department\_head、building\_location都依赖于student\_id，这部分是OK的
3. **违反第三范式**：department\_head依赖于department\_name，而不是直接依赖于student\_id，存在传递依赖

转换为第三范式的方案：

```
-- 学生表
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL
);

-- 课程表
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- 系别表
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    dept_head VARCHAR(100) NOT NULL,
    building_location VARCHAR(100) NOT NULL
);

-- 学生选课表
CREATE TABLE student_courses (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    grade DECIMAL(5,2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- 学生所属系别表
CREATE TABLE student_departments (
    student_id INT PRIMARY KEY,
    dept_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

### [练习2：设计规范化数据库](#练习2-设计规范化数据库)

为一个简单的博客系统设计符合第三范式的数据库结构，要求包含用户、文章、分类、评论等功能模块。

查看答案

```
-- 用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    bio TEXT,
    registration_date DATE NOT NULL,
    status ENUM('active', 'inactive', 'banned') DEFAULT 'active'
);

-- 分类表
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 文章表
CREATE TABLE posts (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    author_id INT NOT NULL,
    category_id INT,
    status ENUM('draft', 'published', 'archived') DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    published_at TIMESTAMP NULL,
    view_count INT DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 评论表
CREATE TABLE comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    author_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    status ENUM('pending', 'approved', 'spam') DEFAULT 'pending',
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

-- 标签表
CREATE TABLE tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 文章标签关联表
CREATE TABLE post_tags (
    post_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
```

### [练习3：简单的学生成绩管理系统设计](#练习3-简单的学生成绩管理系统设计)

设计一个简单的学生成绩管理系统，要求符合第三范式，包含学生信息、课程信息和成绩记录。分析表结构如何避免数据冗余和更新异常。

查看答案

```
-- 学生表（符合第三范式）
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL
);

-- 课程表（符合第三范式）
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credit_hours INT NOT NULL,
    department VARCHAR(50) NOT NULL
);

-- 教师表（符合第三范式）
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL
);

-- 成绩表（符合第三范式，消除传递依赖）
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    teacher_id INT NOT NULL,
    semester VARCHAR(20) NOT NULL,
    grade DECIMAL(5,2),
    gpa DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
    UNIQUE KEY (student_id, course_id, semester)  -- 确保学生每学期每门课程只有一个成绩
);

-- 插入示例数据
INSERT INTO students (student_id, student_name, email, phone, enrollment_date) VALUES
(1, '张三', 'zhangsan@example.com', '13800138000', '2025-09-01'),
(2, '李四', 'lisi@example.com', '13900139000', '2025-09-01'),
(3, '王五', 'wangwu@example.com', '13700137000', '2025-09-01');

INSERT INTO courses (course_id, course_name, credit_hours, department) VALUES
(101, '数据库原理', 4, '计算机系'),
(102, '数据结构', 3, '计算机系'),
(103, '算法设计', 3, '计算机系');

INSERT INTO teachers (teacher_id, teacher_name, email, department) VALUES
(201, '陈老师', 'chen@example.com', '计算机系'),
(202, '刘老师', 'liu@example.com', '计算机系'),
(203, '王老师', 'wang@example.com', '计算机系');

INSERT INTO grades (student_id, course_id, teacher_id, semester, grade, gpa) VALUES
(1, 101, 201, '2025秋季', 85.5, 3.5),
(1, 102, 202, '2025秋季', 92.0, 4.0),
(2, 101, 201, '2025秋季', 78.0, 3.0),
(2, 103, 203, '2025秋季', 88.5, 3.7),
(3, 102, 202, '2025秋季', 95.0, 4.0);

-- 查询示例：查询学生成绩单
SELECT 
    s.student_name,
    c.course_name,
    t.teacher_name,
    g.semester,
    g.grade,
    g.gpa
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN courses c ON g.course_id = c.course_id
JOIN teachers t ON g.teacher_id = t.teacher_id
WHERE s.student_id = 1
ORDER BY g.semester, c.course_name;

-- 查询示例：统计课程平均成绩
SELECT 
    c.course_name,
    COUNT(g.student_id) AS student_count,
    AVG(g.grade) AS average_grade,
    MAX(g.grade) AS highest_grade,
    MIN(g.grade) AS lowest_grade
FROM grades g
JOIN courses c ON g.course_id = c.course_id
GROUP BY c.course_id, c.course_name
ORDER BY average_grade DESC;
```

这个设计符合第三范式的要求：

1. **第一范式**：所有字段都是原子的，不可再分
2. **第二范式**：所有非主键字段都完全依赖于整个主键
3. **第三范式**：所有非主键字段都直接依赖于主键，没有传递依赖

避免了以下问题：

- 数据冗余：学生信息和课程信息只存储一次
- 更新异常：修改学生信息只需要更新students表
- 插入异常：可以单独添加学生或课程，不需要立即有成绩记录
- 删除异常：删除成绩记录不会影响学生或课程的基本信息

## [常见坑](#常见坑)

### [坑1：过度规范化导致性能问题](#坑1-过度规范化导致性能问题)

很多初学者认为规范化程度越高越好，但实际上过度规范化可能导致严重的性能问题。

**问题示例**：

```
-- 过度规范化的设计
CREATE TABLE users (user_id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE user_phones (user_id INT, phone_type VARCHAR(20), phone_number VARCHAR(20));
CREATE TABLE user_emails (user_id INT, email_type VARCHAR(20), email_address VARCHAR(100));
CREATE TABLE user_addresses (user_id INT, address_type VARCHAR(20), address TEXT);
```

**纠正方法**：在实际应用中，对于用户联系方式这种基本不会变化且数量固定的信息，可以适当反规范化：

```
-- 更实用的设计
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),  -- 主要邮箱
    phone VARCHAR(20),   -- 主要电话
    address TEXT         -- 主要地址
);
```

### [坑2：忽视范式之间的依赖关系](#坑2-忽视范式之间的依赖关系)

很多人试图直接跳到第三范式，而忽略了第一范式和第二范式的基础要求。

**问题示例**：

```
-- 错误：直接追求3NF而忽略了1NF
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    products_json JSON,  -- 违反1NF
    total_amount DECIMAL(10,2)
);
```

**纠正方法**：必须按顺序满足每个范式的要求，先确保字段原子性，再处理部分依赖，最后处理传递依赖。

### [坑3：盲目反规范化](#坑3-盲目反规范化)

有些开发者为了所谓的"性能提升"，随意进行反规范化，导致数据一致性问题。

**问题示例**：

```
-- 危险的反规范化
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_name VARCHAR(100));
CREATE TABLE order_items (order_item_id INT PRIMARY KEY, order_id INT, customer_name VARCHAR(100));
```

**纠正方法**：反规范化应该有明确的目的和可靠的数据同步机制，而不是随意复制数据。

## [速记卡](#速记卡)

- **第一范式(1NF)**：字段原子性，每个字段不可再分，每行唯一
- **第二范式(2NF)**：消除部分依赖，非主键字段完全依赖于整个主键
- **第三范式(3NF)**：消除传递依赖，非主键字段直接依赖于主键
- **规范化目的**：减少数据冗余，避免更新异常，保证数据一致性
- **反规范化**：有意识地引入冗余以提高查询性能
- **数据冗余**：同一数据在多个地方重复存储
- **更新异常**：插入、更新、删除操作可能导致数据不一致
- **传递依赖**：A→B→C，其中C依赖于A但通过B传递
- **部分依赖**：复合主键情况下，字段只依赖于主键的一部分
- **设计原则**：先规范化，后根据性能需求适度反规范化

## [章节总结](#章节总结)

在这一章中，我们学习了数据库范式设计的核心理论，这是数据库设计的重要基础。从为什么需要规范化开始，我们了解了数据冗余会带来的各种问题，包括更新异常、数据不一致、存储浪费等。

第一范式要求每个字段都是原子的，不可再分。这解决了数据存储的基本问题，让我们能够进行精确的查询和统计。通过将非原子字段分解为独立的关系表，我们消除了数据存储的混乱，为后续的规范化打下了基础。

第二范式要求消除部分依赖，确保所有非主键字段都完全依赖于整个主键。这在复合主键的情况下特别重要，通过将部分依赖的字段分离到独立表中，我们进一步减少了数据冗余，提高了数据的一致性。

第三范式要求消除传递依赖，确保非主键字段直接依赖于主键，而不是通过其他字段间接依赖。这解决了最深层次的数据冗余问题，让每个字段都只在一个地方存储，真正实现了"一个事实，一个地方"的设计原则。

我们也学习了反规范化的概念和应用场景。虽然规范化有很多好处，但在实际应用中，为了提高查询性能，我们可能需要有意识地引入一定的数据冗余。反规范化是一个权衡的过程，需要在性能和可维护性之间找到平衡点。

掌握了数据库范式设计，你就能够设计出结构合理、高效可靠的数据库系统。良好的数据库设计是应用成功的基础，它不仅影响数据的存储效率，还影响系统的性能、可维护性和扩展性。在下一章中，我们将学习索引的相关知识，这将进一步提升数据库的性能。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [13｜范式设计：数据库的范化有那些？？](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#_13-范式设计-数据库的范化有那些)
- [13.1 为什么需要规范化](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#_13-1-为什么需要规范化)
- [13.2 数据库三大范式](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#_13-2-数据库三大范式)
- [第一范式(1NF)](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#第一范式-1nf)
- [第二范式(2NF)](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#第二范式-2nf)
- [第三范式(3NF)](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#第三范式-3nf)
- [范式设计的实际应用](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#范式设计的实际应用)
- [13.3 反范式的常见场景](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#_13-3-反范式的常见场景)
- [场景一：学生成绩单查询](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#场景一-学生成绩单查询)
- [场景二：商品分类显示](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#场景二-商品分类显示)
- [场景三：用户订单统计](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#场景三-用户订单统计)
- [反规范化的注意事项](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#反规范化的注意事项)
- [练习题](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#练习题)
- [练习1：识别范式违规](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#练习1-识别范式违规)
- [练习2：设计规范化数据库](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#练习2-设计规范化数据库)
- [练习3：简单的学生成绩管理系统设计](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#练习3-简单的学生成绩管理系统设计)
- [常见坑](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#常见坑)
- [坑1：过度规范化导致性能问题](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#坑1-过度规范化导致性能问题)
- [坑2：忽视范式之间的依赖关系](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#坑2-忽视范式之间的依赖关系)
- [坑3：盲目反规范化](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#坑3-盲目反规范化)
- [速记卡](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part3/13-normalization.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
