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
url: https://xiaolinnote.com/sql/sql_part1/06-update-delete.html
source: https://xiaolinnote.com/sql/sql_part1/06-update-delete.html
last_checked: 2026-05-17
freshness: watch
sha256: f6fa57b4dda939da0f8b01e76f25601b3e1c8000f3237c600cd7c42f85dedfdd
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 06｜修改与删除：如何更新或删除数据？

原始链接：https://xiaolinnote.com/sql/sql_part1/06-update-delete.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 06｜修改与删除：如何更新或删除数据？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 15 分钟约 4417 字2025/8/31

---

# [06｜修改与删除：如何更新或删除数据？](#_06-修改与删除-如何更新或删除数据)

大家好，我是小林。

在前面的章节中，我们学习了如何查询数据和插入数据，但数据是动态变化的。用户的年龄会增长，商品的价格会调整，库存数量会变化，有些数据可能不再需要而需要删除。UPDATE和DELETE语句就是用来处理这些数据变更操作的。

你有没有想过，当你在电商网站上修改收货地址时，系统是如何更新你的用户信息的？当商家调整商品价格时，数据库中的价格数据是如何被修改的？当你删除购物车中的商品时，这些商品记录是如何被移除的？这些操作背后都是UPDATE和DELETE语句在工作。

在这一章中，我们将学习如何安全地更新和删除数据。从基本的UPDATE条件更新开始，到使用表达式进行复杂计算，再到DELETE删除操作和与TRUNCATE的区别。最重要的是，我们还会学习如何避免常见的错误，特别是那个可怕的"遗漏WHERE条件"的错误，它可能会导致整个表的数据被意外更新或删除。

准备好了吗？让我们开始学习数据修改和删除的奥秘吧！

## [6.1 UPDATE 基础](#_6-1-update-基础)

UPDATE语句用于修改表中已存在的数据。最基本的UPDATE语法包括指定要更新的表、要设置的列和值，以及一个可选的WHERE条件来限制哪些行需要更新。

让我们先创建一个简单的产品表来演示UPDATE操作：

```
-- 创建产品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    sales_count INT DEFAULT 0,
    status ENUM('active', 'inactive', 'discontinued') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 插入一些示例数据
INSERT INTO products (name, category, price, stock, sales_count) VALUES 
('iPhone 15', '手机', 5999.00, 100, 1500),
('小米13', '手机', 3999.00, 150, 2300),
('华为P60', '手机', 4999.00, 80, 800),
('MacBook Pro', '笔记本', 12999.00, 50, 300),
('ThinkPad X1', '笔记本', 8999.00, 30, 450),
('iPad Air', '平板', 4599.00, 120, 1200),
('Surface Pro', '平板', 6999.00, 40, 600),
('AirPods Pro', '耳机', 1899.00, 200, 2800),
('小米手环', '智能穿戴', 299.00, 300, 3500),
('华为手表', '智能穿戴', 1299.00, 90, 1100);
```

最基本的UPDATE操作是更新单个列的值。比如，我们想将iPhone 15的价格调整为5899元：

```
UPDATE products
SET price = 5899.00
WHERE name = 'iPhone 15';
```

执行结果：

```
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

这个查询告诉了我们一些重要信息：找到了1条匹配的记录，修改了1条记录。让我们验证一下更新结果：

```
SELECT name, price FROM products WHERE name = 'iPhone 15';
```

执行结果：

```
+-----------+----------+
| name      | price    |
+-----------+----------+
| iPhone 15 |  5899.00 |
+-----------+----------+
1 row in set (0.00 sec)
```

可以看到，iPhone 15的价格已经从原来的5999.00更新为5899.00。

UPDATE语句可以同时更新多个列，多个列之间用逗号分隔。比如，我们想同时更新MacBook Pro的价格和库存：

```
UPDATE products
SET price = 12499.00, stock = 60
WHERE name = 'MacBook Pro';
```

这个查询同时更新了price和stock两个列。

在实际应用中，我们经常需要根据条件来更新数据。WHERE子句就是用来指定更新条件的，它支持我们在WHERE章节中学到的所有条件表达式。比如，我们想将所有价格低于1000元的产品状态设置为'inactive'：

```
UPDATE products
SET status = 'inactive'
WHERE price < 1000;
```

执行结果：

```
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0
```

这个查询更新了2条记录，让我们看看哪些产品被更新了：

```
SELECT name, price, status FROM products WHERE price < 1000;
```

执行结果：

```
+--------------+----------+------------+
| name         | price    | status     |
+--------------+----------+------------+
| 小米手环     |   299.00 | inactive   |
| 华为手表     |  1299.00 | inactive   |
+--------------+----------+------------+
2 rows in set (0.00 sec)
```

可以看到，小米手环和华为手表的价格都低于1000元，它们的状态被更新为'inactive'。

UPDATE语句的强大之处在于它可以使用表达式进行计算。这在很多业务场景中非常有用。比如，我们可以将所有手机类产品的价格下调10%：

```
UPDATE products
SET price = price * 0.9
WHERE category = '手机';
```

这个查询使用了表达式price \* 0.9来计算新的价格。让我们看看更新结果：

```
SELECT name, category, price FROM products WHERE category = '手机';
```

执行结果：

```
+-----------+-----------+----------+
| name      | category  | price    |
+-----------+-----------+----------+
| iPhone 15 | 手机      |  5309.10 |
| 小米13    | 手机      |  3599.10 |
| 华为P60   | 手机      |  4499.10 |
+-----------+-----------+----------+
3 rows in set (0.00 sec)
```

可以看到，所有手机的价格都变成了原来的90%。

另一个常见的应用场景是计数器更新。比如，每次产品售出时，我们需要减少库存并增加销量。我们可以这样做：

```
UPDATE products
SET stock = stock - 1, sales_count = sales_count + 1
WHERE id = 1;
```

这个查询同时减少了库存并增加了销量，两个操作在一个事务中完成，确保数据的一致性。

在进行UPDATE操作之前，特别是复杂的UPDATE操作，养成先用SELECT验证条件的习惯是非常重要的。这样可以确保我们要更新的记录是正确的，避免误更新其他记录。

比如，在执行批量更新之前，我们可以先用SELECT查看将要更新的记录：

```
-- 先查看哪些记录会被更新
SELECT name, price, status FROM products WHERE price > 8000;
```

如果确认这些记录是我们要更新的，然后再执行UPDATE：

```
-- 确认无误后执行更新
UPDATE products
SET status = 'premium'
WHERE price > 8000;
```

这种"先验证后更新"的习惯可以大大减少误操作的风险。

## [6.2 DELETE 基础](#_6-2-delete-基础)

DELETE语句用于从表中删除数据。与UPDATE一样，DELETE通常需要配合WHERE子句来指定要删除哪些记录，否则会删除表中的所有数据。

最基本的DELETE语法是DELETE FROM table\_name WHERE condition。让我们从简单的例子开始，删除特定产品：

```
DELETE FROM products
WHERE name = '小米手环';
```

执行结果：

```
Query OK, 1 row affected (0.01 sec)
```

这个查询删除了名称为'小米手环'的产品记录。让我们验证一下删除结果：

```
SELECT * FROM products WHERE name = '小米手环';
```

执行结果：

```
Empty set (0.00 sec)
```

查询返回空结果，说明该记录已经被成功删除。

DELETE语句支持复杂的条件表达式，就像WHERE子句一样。比如，我们可以删除所有价格低于500元且状态为'inactive'的产品：

```
DELETE FROM products
WHERE price < 500 AND status = 'inactive';
```

在实际应用中，我们经常需要根据多个条件来删除数据。比如，删除某个时间段内创建的未激活用户：

```
DELETE FROM users
WHERE status = 'inactive' 
AND created_at < '2025-01-01'
AND last_login_at < '2024-12-01';
```

需要注意的是，DELETE操作是不可逆的（除非你有数据库备份）。在执行DELETE操作之前，特别是批量删除，强烈建议先用SELECT语句验证要删除的记录：

```
-- 先查看将要删除的记录
SELECT * FROM products WHERE category = '智能穿戴' AND status = 'inactive';

-- 确认无误后执行删除
DELETE FROM products
WHERE category = '智能穿戴' AND status = 'inactive';
```

与DELETE相关的一个命令是TRUNCATE，它也用于删除表中的数据，但与DELETE有几个重要的区别。TRUNCATE的语法更简单：

```
TRUNCATE TABLE products;
```

TRUNCATE与DELETE的主要区别在于：

1. **速度**：TRUNCATE比DELETE快得多，因为它不记录每一行的删除操作，而是直接删除整个表的数据并重建表。
2. **事务**：TRUNCATE不能回滚，而DELETE可以回滚。
3. **自增计数器**：TRUNCATE会重置自增计数器，而DELETE不会。
4. **触发器**：TRUNCATE不会激活DELETE触发器，而DELETE会。

让我们看看TRUNCATE对自增计数器的影响。假设我们有一个测试表：

```
-- 创建测试表
CREATE TABLE test_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

-- 插入几条数据
INSERT INTO test_table (name) VALUES ('test1'), ('test2'), ('test3');

-- 查看当前数据
SELECT * FROM test_table;
```

执行结果：

```
+----+-------+
| id | name  |
+----+-------+
|  1 | test1 |
|  2 | test2 |
|  3 | test3 |
+----+-------+
3 rows in set (0.00 sec)
```

现在使用DELETE删除所有数据：

```
DELETE FROM test_table;

-- 插入新数据
INSERT INTO test_table (name) VALUES ('test4');

-- 查看数据
SELECT * FROM test_table;
```

执行结果：

```
+----+-------+
| id | name  |
+----+-------+
|  4 | test4 |
+----+-------+
1 row in set (0.00 sec)
```

可以看到，DELETE后自增计数器继续从4开始。现在让我们用TRUNCATE测试：

```
-- 先重建表
DROP TABLE IF EXISTS test_table;
CREATE TABLE test_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

INSERT INTO test_table (name) VALUES ('test1'), ('test2'), ('test3');

-- 使用TRUNCATE
TRUNCATE TABLE test_table;

-- 插入新数据
INSERT INTO test_table (name) VALUES ('test4');

-- 查看数据
SELECT * FROM test_table;
```

执行结果：

```
+----+-------+
| id | name  |
+----+-------+
|  1 | test4 |
+----+-------+
1 row in set (0.00 sec)
```

可以看到，TRUNCATE后自增计数器被重置，新插入的记录id从1开始。

在实际应用中，DELETE和TRUNCATE各有用途。DELETE适合删除部分记录或需要回滚的操作，TRUNCATE适合清空整个表且不需要保留自增计数器的场景。

## [6.3 避免遗漏 WHERE 的坑](#_6-3-避免遗漏-where-的坑)

在所有SQL错误中，遗漏WHERE条件可能是最危险的一个。一个简单的疏忽就可能导致整个表的数据被意外更新或删除，造成灾难性的后果。在这一节中，我们将学习几种防护措施来避免这种错误。

最经典的错误是在UPDATE或DELETE时忘记写WHERE子句：

```
-- 危险的语句：会更新所有记录
UPDATE products SET price = 0;

-- 致命的语句：会删除所有数据
DELETE FROM products;
```

为了避免这种错误，我们可以采取以下几种防护措施：

**第一种防护措施是养成先写SELECT验证条件的习惯**。在执行UPDATE或DELETE之前，先用相同的WHERE条件执行SELECT，确保只选中了我们想要操作的记录：

```
-- 第一步：验证条件
SELECT COUNT(*) FROM products WHERE category = '手机' AND price > 5000;

-- 第二步：查看具体记录
SELECT name, price FROM products WHERE category = '手机' AND price > 5000;

-- 第三步：确认无误后执行更新
UPDATE products 
SET status = 'high_end' 
WHERE category = '手机' AND price > 5000;
```

**第二种防护措施是使用事务**。事务让我们能够在一个安全的环境中测试操作，如果发现错误可以回滚：

```
-- 开始事务
START TRANSACTION;

-- 执行更新操作
UPDATE products SET price = price * 1.1 WHERE category = '手机';

-- 验证结果
SELECT name, price FROM products WHERE category = '手机' LIMIT 5;

-- 如果结果正确，提交事务
-- COMMIT;

-- 如果结果错误，回滚事务
-- ROLLBACK;
```

在实际应用中，我们可以在事务中执行操作，验证结果后再决定是提交还是回滚。这提供了一个安全网，让我们能够撤销错误的操作。

**第三种防护措施是使用LIMIT子句**。虽然这不是标准的做法，但在某些情况下可以限制受影响的行数：

```
-- 限制最多更新10条记录
UPDATE products SET status = 'inactive' WHERE price < 100 LIMIT 10;
```

这样可以防止意外更新大量记录，但需要注意，LIMIT可能会漏掉一些应该被更新的记录。

**第四种防护措施是启用MySQL的安全更新模式**。MySQL有一个安全更新模式，当启用时，如果在UPDATE或DELETE中没有使用WHERE子句或者WHERE子句中没有使用索引列，操作会被拒绝：

```
-- 启用安全更新模式
SET SQL_SAFE_UPDATES = 1;

-- 现在危险的UPDATE会被拒绝
UPDATE products SET price = 0;
-- ERROR 1175 (HY000): You are using safe update mode...

-- 使用索引列的WHERE子句可以正常工作
UPDATE products SET price = 0 WHERE id = 1;
```

**第五种防护措施是在应用程序中使用预处理语句**。预处理语句不仅可以防止SQL注入，还可以帮助我们更好地控制数据操作：

```
# Python示例
cursor.execute("""
    UPDATE products 
    SET price = %s, stock = %s 
    WHERE id = %s
""", (new_price, new_stock, product_id))
```

**第六种防护措施是定期备份数据**。即使采取了所有预防措施，错误仍然可能发生。定期备份确保在最坏的情况下我们也能够恢复数据。

在实际开发中，通常会结合多种防护措施。比如，在生产环境中，我们会启用安全更新模式，使用事务进行操作，并且有定期的数据备份策略。

还有一个好的做法是在执行重要操作之前，先备份数据：

```
-- 创建备份表
CREATE TABLE products_backup_20250831 AS SELECT * FROM products;

-- 然后执行更新操作
UPDATE products SET price = price * 1.05 WHERE category = '手机';
```

如果更新出现问题，我们可以从备份表中恢复数据。

## [练习题](#练习题)

### [练习1：条件更新与表达式](#练习1-条件更新与表达式)

将products表中所有"笔记本"类别的产品价格下调5%，库存增加10个，并显示更新前后的数据对比。

查看答案

```
-- 先查看更新前的数据
SELECT name, category, price, stock FROM products WHERE category = '笔记本';

-- 执行更新
UPDATE products 
SET price = price * 0.95, stock = stock + 10 
WHERE category = '笔记本';

-- 查看更新后的数据
SELECT name, category, price, stock FROM products WHERE category = '笔记本';
```

### [练习2：批量删除](#练习2-批量删除)

删除products表中所有价格低于500元且销量少于1000的产品，先查看要删除的记录再执行删除。

查看答案

```
-- 先查看要删除的记录
SELECT name, price, sales_count FROM products 
WHERE price < 500 AND sales_count < 1000;

-- 确认无误后执行删除
DELETE FROM products 
WHERE price < 500 AND sales_count < 1000;

-- 验证删除结果
SELECT COUNT(*) FROM products WHERE price < 500 AND sales_count < 1000;
```

### [练习3：安全更新操作](#练习3-安全更新操作)

在事务中更新products表中"手机"类别的状态为"premium"，价格增加100元，如果发现错误能够回滚。

查看答案

```
-- 开始事务
START TRANSACTION;

-- 执行更新
UPDATE products 
SET status = 'premium', price = price + 100 
WHERE category = '手机';

-- 验证结果
SELECT name, status, price FROM products WHERE category = '手机';

-- 如果结果正确，提交事务
-- COMMIT;

-- 如果结果错误，回滚事务
-- ROLLBACK;
```

## [常见坑](#常见坑)

### [坑1：UPDATE时忘记WHERE条件](#坑1-update时忘记where条件)

这是最危险的SQL错误之一，忘记WHERE条件会导致整个表的数据被更新。

**错误示例**：

```
-- 会更新所有产品的价格！
UPDATE products SET price = 0;
```

**纠正方法**：养成先写SELECT验证条件的习惯，使用事务进行测试：

```
-- 先验证条件
SELECT COUNT(*) FROM products WHERE category = '手机';

-- 在事务中测试
START TRANSACTION;
UPDATE products SET price = price * 1.1 WHERE category = '手机';
-- 检查结果后决定提交或回滚
```

### [坑2：DELETE时忽略外键约束](#坑2-delete时忽略外键约束)

在有外键关系的表中，DELETE操作可能会因为外键约束而失败，或者导致级联删除。

**纠正方法**：先了解表的外键关系，必要时临时关闭外键检查：

```
-- 临时关闭外键检查（慎用）
SET FOREIGN_KEY_CHECKS = 0;
-- 执行删除操作
DELETE FROM products WHERE id = 1;
-- 重新启用外键检查
SET FOREIGN_KEY_CHECKS = 1;
```

### [坑3：在UPDATE中使用子查询时的性能问题](#坑3-在update中使用子查询时的性能问题)

在UPDATE语句中使用子查询可能会导致性能问题，特别是子查询返回大量数据时。

**纠正方法**：考虑使用JOIN替代子查询，或者先执行子查询将结果存储在临时变量中：

```
-- 使用JOIN的方式
UPDATE products p
JOIN (SELECT category, AVG(price) as avg_price FROM products GROUP BY category) avg
ON p.category = avg.category
SET p.price_level = CASE WHEN p.price > avg.avg_price THEN 'high' ELSE 'low' END;
```

## [速记卡](#速记卡)

- **UPDATE语法**：UPDATE table\_name SET column1 = value1, column2 = value2 WHERE condition
- **DELETE语法**：DELETE FROM table\_name WHERE condition
- **表达式更新**：可以使用数学运算、字符串函数等复杂表达式
- **WHERE的重要性**：忘记WHERE会更新/删除所有记录，这是最危险的SQL错误
- **先验证后执行**：先用SELECT验证WHERE条件，再执行UPDATE/DELETE
- **事务保护**：使用START TRANSACTION和COMMIT/ROLLBACK提供安全操作环境
- **TRUNCATE vs DELETE**：TRUNCATE更快但不能回滚，会重置自增计数器
- **安全更新模式**：SET SQL\_SAFE\_UPDATES = 1 可以防止无WHERE的更新/删除

## [章节总结](#章节总结)

在这一章中，我们学习了如何修改和删除数据库中的数据，这是数据管理中至关重要的技能。UPDATE语句让我们能够更新现有数据，支持单列更新、多列更新和表达式计算，能够满足各种业务场景的需求。

DELETE语句用于删除数据，配合WHERE子句可以精确地删除指定的记录。我们还了解了DELETE与TRUNCATE的区别，TRUNCATE适合清空整个表且不需要保留自增计数器的场景，而DELETE更适合删除部分记录。

最重要的是，我们学习了如何避免遗漏WHERE条件的致命错误。通过先验证后执行、使用事务保护、启用安全更新模式等多种防护措施，我们可以大大降低误操作的风险。

数据修改和删除操作虽然强大，但也伴随着风险。在实际应用中，我们必须时刻保持谨慎，遵循最佳实践，确保数据的安全性和完整性。掌握了这些技能，你就能够安全地进行数据维护操作，为应用程序提供可靠的数据支持。

在下一章中，我们将开始学习SQL的进阶内容，探索更复杂的数据查询和处理技术。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [06｜修改与删除：如何更新或删除数据？](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#_06-修改与删除-如何更新或删除数据)
- [6.1 UPDATE 基础](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#_6-1-update-基础)
- [6.2 DELETE 基础](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#_6-2-delete-基础)
- [6.3 避免遗漏 WHERE 的坑](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#_6-3-避免遗漏-where-的坑)
- [练习题](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#练习题)
- [练习1：条件更新与表达式](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#练习1-条件更新与表达式)
- [练习2：批量删除](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#练习2-批量删除)
- [练习3：安全更新操作](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#练习3-安全更新操作)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#常见坑)
- [坑1：UPDATE时忘记WHERE条件](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#坑1-update时忘记where条件)
- [坑2：DELETE时忽略外键约束](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#坑2-delete时忽略外键约束)
- [坑3：在UPDATE中使用子查询时的性能问题](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#坑3-在update中使用子查询时的性能问题)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/06-update-delete.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
