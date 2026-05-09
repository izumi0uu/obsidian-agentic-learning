---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html"
source: "https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html"
last_checked: 2026-05-07
freshness: watch
sha256: 47259e56a6adb32f99e36cbfca4ffabdc64e02d0cd0289fde8b12422cfe6802c
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[SQL EXPLAIN]]"
  - "[[Query Plan]]"
  - "[[SQL]]"
---
# 加餐1｜EXPLAIN：只看哪5个字段就够了？

原始链接：https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[SQL EXPLAIN]]
- [[Query Plan]]
- [[SQL]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 15 分钟约 4411 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了各种SQL查询和操作技术。你有没有遇到过这样的情况：写的SQL查询运行得很慢，但不知道问题出在哪里？或者，两条看起来差不多的查询，一条执行得很快，另一条却很慢，这是为什么呢？

其实，MySQL在执行每条SQL语句时，都会先制定一个"执行计划"，就像我们出门前会先规划路线一样。有的路线是直接高速到达，有的则需要绕很多弯路。EXPLAIN命令就是让我们能够看到MySQL的"执行计划"，帮助我们理解查询是如何执行的，从而找出性能瓶颈。

你可能会问，EXPLAIN的输出信息那么多，看起来好复杂，我该从哪里看起呢？别担心，在这一章中，我将告诉你只需要关注5个关键字段，就能掌握80%的查询优化技巧。

准备好了吗？让我们一起揭开EXPLAIN的神秘面纱吧！

## [准备一条示例查询](#准备一条示例查询)

在开始学习EXPLAIN之前，我们需要先准备一些测试数据。让我们创建一个简单的电商订单系统数据库，包含用户表和订单表：

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

-- 创建订单表
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

-- 插入一些测试数据
INSERT INTO users (username, email, city) VALUES 
('张三', 'zhangsan@example.com', '北京'),
('李四', 'lisi@example.com', '上海'),
('王五', 'wangwu@example.com', '广州'),
('赵六', 'zhaoliu@example.com', '深圳'),
('钱七', 'qianqi@example.com', '杭州'),
('孙八', 'sunba@example.com', '成都'),
('周九', 'zhoujiu@example.com', '武汉'),
('吴十', 'wushi@example.com', '西安');

INSERT INTO orders (user_id, product_name, amount, status, order_date) VALUES 
(1, 'iPhone 15', 5999.00, 'completed', '2025-08-01 10:00:00'),
(1, 'AirPods', 1299.00, 'completed', '2025-08-02 14:30:00'),
(2, '小米13', 3999.00, 'completed', '2025-08-03 09:15:00'),
(3, 'MacBook Pro', 12999.00, 'pending', '2025-08-04 16:45:00'),
(4, 'iPad', 4599.00, 'completed', '2025-08-05 11:20:00'),
(5, '华为P60', 4999.00, 'cancelled', '2025-08-06 13:10:00'),
(6, 'Surface Pro', 8999.00, 'completed', '2025-08-07 15:30:00'),
(7, 'ThinkPad', 7999.00, 'completed', '2025-08-08 10:45:00'),
(8, '戴尔笔记本', 6999.00, 'pending', '2025-08-09 12:00:00'),
(1, 'Apple Watch', 2999.00, 'completed', '2025-08-10 17:15:00');

-- 添加一些索引以便演示
CREATE INDEX idx_user_id ON orders(user_id);
CREATE INDEX idx_status ON orders(status);
CREATE INDEX idx_order_date ON orders(order_date);
```

现在我们有了一个包含用户和订单的数据库。让我们执行一个稍微复杂一点的查询，然后用EXPLAIN来分析它的执行计划：

```
-- 查询2025年8月份北京用户的已完成订单总金额
SELECT 
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.city = '北京'
    AND o.status = 'completed'
    AND o.order_date BETWEEN '2025-08-01' AND '2025-08-31'
GROUP BY u.id, u.username, u.city
ORDER BY total_amount DESC;
```

这个查询涉及了连接、筛选、分组和排序，是一个比较典型的复杂查询。现在让我们用EXPLAIN来看看MySQL是如何执行这个查询的：

```
EXPLAIN SELECT 
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.city = '北京'
    AND o.status = 'completed'
    AND o.order_date BETWEEN '2025-08-01' AND '2025-08-31'
GROUP BY u.id, u.username, u.city
ORDER BY total_amount DESC;
```

执行结果如下：

```
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
| id | select_type | table | partitions | type | possible_keys       | key          | key_len | ref                 | rows   | filtered | Extra           |
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
|  1 | SIMPLE      | u     | NULL       | ALL  | NULL                | NULL         | NULL    | NULL                |      8 |    12.50 | Using where     |
|  1 | SIMPLE      | o     | NULL       | ref  | idx_user_id,idx_status,idx_order_date | idx_user_id | 5       | xiaolinnote.u.id   |      1 |     4.38 | Using where     |
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
2 rows in set (0.00 sec)
```

看到这个输出，你可能会觉得信息太多了，不知道从哪里看起。别担心，接下来我会告诉你只需要关注哪5个字段，就能快速理解查询的执行情况。

## [五个字段怎么读](#五个字段怎么读)

在EXPLAIN的输出中，有很多字段，但作为初学者，你只需要重点关注5个字段：`type`、`key`、`rows`、`filtered`、`Extra`。这5个字段能告诉你查询的性能状况。

### [type：访问方式优劣顺序](#type-访问方式优劣顺序)

`type`字段告诉我们MySQL是如何访问表的数据的，这是判断查询效率的重要指标。访问方式从好到坏的顺序是：

- `system` > `const` > `eq_ref` > `ref` > `range` > `index` > `ALL`

让我们逐个了解这些常见的类型：

**`system`和`const`**：这是最好的情况。`system`表示表只有一行，`const`表示通过索引一次就找到了。比如通过主键查询用户：

```
EXPLAIN SELECT * FROM users WHERE id = 1;
```

你会看到`type`为`const`，因为通过主键id=1直接就能定位到用户。

**`eq_ref`**：也很好，通常出现在连接查询中，表示通过唯一索引进行关联。比如：

```
EXPLAIN SELECT * FROM users JOIN orders ON users.id = orders.user_id WHERE users.id = 1;
```

**`ref`**：还不错，表示通过非唯一索引进行查找。比如：

```
EXPLAIN SELECT * FROM orders WHERE user_id = 1;
```

**`range`**：表示对索引进行范围查找。比如：

```
EXPLAIN SELECT * FROM orders WHERE amount > 5000;
```

**`index`**：表示扫描整个索引，比全表扫描好一些，但也不够理想。

**`ALL`**：这是最坏的情况，表示全表扫描。看到`ALL`就要警惕了，可能需要优化。

在我们的示例查询中，users表的`type`是`ALL`，这说明MySQL对users表进行了全表扫描，这就是一个可以优化的点。

### [key：实际使用的索引](#key-实际使用的索引)

`key`字段显示MySQL实际使用的索引名称。如果显示为`NULL`，说明没有使用索引。

在我们的示例中，orders表的`key`显示为`idx_user_id`，说明MySQL使用了user\_id上的索引。但users表的`key`是`NULL`，说明没有使用索引，这解释了为什么`type`是`ALL`。

看到`key`为`NULL`时，我们要考虑是否需要添加索引。比如，我们可以为users表的city字段添加索引：

```
CREATE INDEX idx_city ON users(city);
```

再次执行EXPLAIN，你会看到users表的`type`变成了`ref`，`key`变成了`idx_city`，这说明查询性能得到了改善。

### [rows：预估扫描行数](#rows-预估扫描行数)

`rows`字段是MySQL预估需要扫描的行数。这个数字越小越好，如果数字很大，说明查询可能需要扫描大量数据。

在我们的示例中，users表的`rows`是8，因为总共有8个用户；orders表的`rows`是1，因为通过user\_id索引每次大概能找到1条订单记录。

需要注意的是，`rows`是预估值，不是实际返回的行数。实际返回的行数可能会比`rows`少很多，特别是在有WHERE条件的情况下。

### [filtered：过滤比例](#filtered-过滤比例)

`filtered`字段表示符合查询条件的行的百分比。这个值越高越好，100%表示所有扫描的行都符合条件。

在我们的示例中，users表的`filtered`是12.50，表示大约12.5%的行符合WHERE条件（8个用户中只有1个是北京的）。orders表的`filtered`是4.38，表示大约4.38%的订单符合条件。

`filtered`值很低说明MySQL扫描了很多不符合条件的行，这也是一个可以优化的信号。通过更好的索引或者查询条件，可以提高`filtered`值。

### [Extra：额外信息](#extra-额外信息)

`Extra`字段提供了很多有用的额外信息。常见的值有：

**`Using index`**：这是个好消息！表示使用了覆盖索引，查询只需要通过索引就能完成，不需要回表。

**`Using where`**：表示使用了WHERE条件进行过滤。

**`Using filesort`**：这是个警告，表示MySQL需要额外进行排序操作，这可能会影响性能。

**`Using temporary`**：这是个严重警告，表示MySQL需要使用临时表，通常出现在复杂的GROUP BY或DISTINCT操作中。

在我们的示例中，两个表都显示了`Using where`，这是正常的，因为我们都有WHERE条件。

## [从计划到改写](#从计划到改写)

了解了这5个字段后，我们就可以开始优化查询了。让我演示一下如何从EXPLAIN的结果出发，进行查询优化。

### [第一步：发现问题](#第一步-发现问题)

从我们的EXPLAIN结果可以看到：

1. users表的`type`是`ALL`，说明进行了全表扫描
2. users表的`key`是`NULL`，说明没有使用索引
3. users表的`rows`是8，虽然不多，但如果用户量大了就会成为问题

### [第二步：添加合适的索引](#第二步-添加合适的索引)

问题很明显，我们需要为users表的city字段添加索引：

```
CREATE INDEX idx_city ON users(city);
```

### [第三步：验证优化效果](#第三步-验证优化效果)

再次执行EXPLAIN：

```
EXPLAIN SELECT 
    u.username,
    u.city,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.city = '北京'
    AND o.status = 'completed'
    AND o.order_date BETWEEN '2025-08-01' AND '2025-08-31'
GROUP BY u.id, u.username, u.city
ORDER BY total_amount DESC;
```

现在的结果会显示：

```
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
| id | select_type | table | partitions | type | possible_keys       | key          | key_len | ref                 | rows   | filtered | Extra           |
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
|  1 | SIMPLE      | u     | NULL       | ref  | idx_city            | idx_city     | 203     | const               |      1 |   100.00 | Using where     |
|  1 | SIMPLE      | o     | NULL       | ref  | idx_user_id,idx_status,idx_order_date | idx_user_id | 5       | xiaolinnote.u.id   |      1 |     4.38 | Using where     |
+----+-------------+-------+------------+------+---------------------+--------------+---------+---------------------+--------+----------+-----------------+
2 rows in set (0.00 sec)
```

对比优化前后的结果：

- users表的`type`从`ALL`变成了`ref`（全表扫描 → 索引查找）
- users表的`key`从`NULL`变成了`idx_city`（无索引 → 使用索引）
- users表的`rows`从8变成了1（扫描8行 → 扫描1行）
- users表的`filtered`从12.50变成了100.00（过滤12.5% → 过滤100%）

这是一个显著的性能提升！

### [更多优化技巧](#更多优化技巧)

让我们再看看几个常见的优化场景：

**场景1：避免函数操作导致索引失效**

```
-- 不好的写法：函数操作会阻止索引使用
EXPLAIN SELECT * FROM users WHERE UPPER(username) = 'ZHANGSAN';

-- 好的写法：直接比较
EXPLAIN SELECT * FROM users WHERE username = 'zhangsan';
```

**场景2：使用合适的索引顺序**

```
-- 如果经常需要按状态和日期查询，可以创建联合索引
CREATE INDEX idx_status_date ON orders(status, order_date);

EXPLAIN SELECT * FROM orders 
WHERE status = 'completed' 
    AND order_date BETWEEN '2025-08-01' AND '2025-08-31';
```

\*\*场景3：避免SELECT \*\*\*

```
-- 不好的写法：查询所有列
EXPLAIN SELECT * FROM users WHERE city = '北京';

-- 好的写法：只查询需要的列
EXPLAIN SELECT id, username, email FROM users WHERE city = '北京';
```

## [常见误区速记](#常见误区速记)

在使用EXPLAIN时，有一些常见的误区需要避免：

**误区1：rows不是返回行数**

很多初学者会误以为`rows`字段就是查询返回的行数。实际上，`rows`是MySQL预估需要扫描的行数，实际返回的行数可能会少很多。比如，即使`rows`显示1000，但如果WHERE条件很严格，可能最终只返回10行。

**误区2：看到filesort不必恐慌**

`Using filesort`听起来很吓人，但不一定意味着性能问题。如果排序的数据量很小，filesort的开销可能微不足道。只有当排序大量数据时，才需要考虑优化。

**误区3：force index慎用**

有些初学者发现MySQL没有使用他们期望的索引，就倾向于使用`FORCE INDEX`强制使用某个索引。这通常不是好主意，因为MySQL的查询优化器通常比我们更了解哪种索引更适合。数据分布变化后，现在的最优选择可能明天就不是了。

**误区4：只关注单个字段**

不要只看EXPLAIN输出的单个字段，要综合分析。比如，即使`type`是`ALL`，但如果`rows`很小，性能可能还是可以接受的。同样，即使使用了索引，但如果`filtered`很低，说明索引效果不好。

**误区5：忽略执行环境**

EXPLAIN的结果会根据数据量、数据分布、索引情况等因素变化。不要在测试环境看了一下EXPLAIN结果，就认为在生产环境也是一样的。最好在生产环境或者接近生产环境的数据量上进行测试。

## [练习题](#练习题)

### [练习1：分析并优化简单查询](#练习1-分析并优化简单查询)

分析以下查询的EXPLAIN结果，并尝试优化它：

```
EXPLAIN SELECT * FROM orders WHERE amount > 3000 AND status = 'completed';
```

查看答案

首先分析当前查询的EXPLAIN结果。如果没有合适的索引，可能会看到`type`为`ALL`或`range`。

优化方法：为amount和status创建联合索引

```
-- 创建联合索引
CREATE INDEX idx_amount_status ON orders(amount, status);

-- 再次分析
EXPLAIN SELECT * FROM orders WHERE amount > 3000 AND status = 'completed';
```

现在应该能看到更好的`type`值和使用了新的索引。

### [练习2：优化连接查询](#练习2-优化连接查询)

优化以下连接查询，确保两个表都使用合适的索引：

```
EXPLAIN SELECT u.username, o.product_name, o.amount 
FROM users u 
JOIN orders o ON u.id = o.user_id 
WHERE u.city = '上海' AND o.status = 'completed';
```

查看答案

这个查询需要为users表的city字段和orders表的user\_id、status字段创建索引：

```
-- 为users表创建city索引
CREATE INDEX idx_city ON users(city);

-- 为orders表创建联合索引
CREATE INDEX idx_user_status ON orders(user_id, status);

-- 分析优化后的查询
EXPLAIN SELECT u.username, o.product_name, o.amount 
FROM users u 
JOIN orders o ON u.id = o.user_id 
WHERE u.city = '上海' AND o.status = 'completed';
```

现在应该能看到两个表都使用了索引，`type`应该是`ref`。

### [练习3：识别并解决filesort问题](#练习3-识别并解决filesort问题)

分析以下查询，解决可能的filesort问题：

```
EXPLAIN SELECT username, email, city 
FROM users 
WHERE city = '北京' 
ORDER BY created_at DESC;
```

查看答案

这个查询可能会出现`Using filesort`，因为ORDER BY使用了created\_at字段，但WHERE条件使用的是city字段。

优化方法：创建包含city和created\_at的联合索引

```
-- 创建联合索引以避免filesort
CREATE INDEX idx_city_created ON users(city, created_at);

-- 分析优化后的查询
EXPLAIN SELECT username, email, city 
FROM users 
WHERE city = '北京' 
ORDER BY created_at DESC;
```

现在应该能看到`Extra`字段中没有`Using filesort`，说明排序操作使用了索引。

## [常见坑](#常见坑)

### [坑1：过度依赖EXPLAIN而不测试实际性能](#坑1-过度依赖explain而不测试实际性能)

很多初学者看了EXPLAIN结果就以为知道查询的性能了，但EXPLAIN只是预估，实际性能还需要通过真实的执行时间来验证。

**纠正方法**：结合EXPLAIN分析和实际的执行时间测试，使用`SHOW PROFILE`或者直接测量查询执行时间。

### [坑2：在小数据集上优化](#坑2-在小数据集上优化)

在测试数据量很小的情况下进行EXPLAIN分析，得到的优化方案可能在大数据量时并不适用。

**纠正方法**：使用接近生产环境的数据量进行测试，或者考虑数据增长趋势来设计索引策略。

### [坑3：忽略写入性能的影响](#坑3-忽略写入性能的影响)

为了查询性能创建过多索引，但忽略了索引对插入、更新、删除操作的影响。

**纠正方法**：权衡读写比例，对于写频繁的表，要谨慎创建索引，优先考虑对查询性能提升最大的索引。

## [速记卡](#速记卡)

- **EXPLAIN**：查看SQL执行计划的命令，帮助理解MySQL如何执行查询
- **type**：访问方式，从好到差：system/const > eq\_ref > ref > range > index > ALL
- **key**：实际使用的索引，NULL表示没有使用索引
- **rows**：预估扫描行数，越小越好，但不是实际返回行数
- **filtered**：过滤比例，越高越好，表示扫描行中符合条件的比例
- **Extra**：额外信息，Using index（好），Using filesort（注意），Using temporary（警告）
- **优化思路**：从type=ALL入手，添加合适索引，避免filesort和temporary
- **索引原则**：为WHERE、JOIN、ORDER BY的字段创建索引，考虑联合索引的左前缀原则

## [章节总结](#章节总结)

在这个加餐中，我们学习了MySQL的EXPLAIN命令，这是查询性能分析的重要工具。通过EXPLAIN，我们能够看到MySQL的执行计划，理解查询是如何被执行的，从而找出性能瓶颈。

我们重点介绍了5个关键字段：`type`、`key`、`rows`、`filtered`、`Extra`。这5个字段能够告诉我们查询的性能状况，比如是否使用了索引、需要扫描多少行、是否需要额外的排序或临时表等。通过分析这些字段，我们可以快速定位查询的性能问题。

通过实际的例子，我们演示了如何从EXPLAIN的结果出发，进行查询优化。从发现问题到添加合适的索引，再到验证优化效果，这是一个完整的优化流程。我们还介绍了更多的优化技巧，比如避免函数操作导致索引失效、使用合适的索引顺序、避免SELECT \* 等。

在使用EXPLAIN时，我们需要避免一些常见的误区，比如误以为rows就是返回行数、看到filesort就恐慌、滥用force index等。EXPLAIN只是预估，实际性能还需要通过真实测试来验证。

掌握了EXPLAIN的使用，你就具备了基本的查询性能分析能力。这不仅能帮助你优化自己的查询，还能让你更好地理解MySQL的工作原理。在今后的数据库工作中，EXPLAIN将成为你重要的工具，帮助你构建更高效的数据库应用。

记住，查询优化是一个持续的过程，需要结合实际的业务场景和数据特点来进行。随着数据量的增长和业务需求的变化，要定期检查和优化你的查询语句，确保系统始终保持良好的性能。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [加餐1｜EXPLAIN：只看哪5个字段就够了？](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#加餐1-explain-只看哪5个字段就够了)
- [准备一条示例查询](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#准备一条示例查询)
- [五个字段怎么读](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#五个字段怎么读)
- [type：访问方式优劣顺序](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#type-访问方式优劣顺序)
- [key：实际使用的索引](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#key-实际使用的索引)
- [rows：预估扫描行数](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#rows-预估扫描行数)
- [filtered：过滤比例](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#filtered-过滤比例)
- [Extra：额外信息](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#extra-额外信息)
- [从计划到改写](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#从计划到改写)
- [第一步：发现问题](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#第一步-发现问题)
- [第二步：添加合适的索引](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#第二步-添加合适的索引)
- [第三步：验证优化效果](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#第三步-验证优化效果)
- [更多优化技巧](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#更多优化技巧)
- [常见误区速记](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#常见误区速记)
- [练习题](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#练习题)
- [练习1：分析并优化简单查询](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#练习1-分析并优化简单查询)
- [练习2：优化连接查询](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#练习2-优化连接查询)
- [练习3：识别并解决filesort问题](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#练习3-识别并解决filesort问题)
- [常见坑](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#常见坑)
- [坑1：过度依赖EXPLAIN而不测试实际性能](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#坑1-过度依赖explain而不测试实际性能)
- [坑2：在小数据集上优化](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#坑2-在小数据集上优化)
- [坑3：忽略写入性能的影响](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#坑3-忽略写入性能的影响)
- [速记卡](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part5/supplement1-explain.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
