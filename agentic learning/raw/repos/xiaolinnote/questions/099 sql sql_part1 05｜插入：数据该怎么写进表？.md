---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part1/05-insert-data.html"
source: "https://xiaolinnote.com/sql/sql_part1/05-insert-data.html"
last_checked: 2026-05-07
freshness: watch
sha256: f731405c5f0793f7b2465c86af2e528245e521ae0cb47b3e5ad1bb15a923110b
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[SQL INSERT]]"
  - "[[SQL]]"
---
# 05｜插入：数据该怎么写进表？

原始链接：https://xiaolinnote.com/sql/sql_part1/05-insert-data.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[SQL INSERT]]
- [[SQL]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 14 分钟约 4145 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了如何查询和筛选数据，但数据库不仅要能够读取数据，还要能够存储数据。当我们有了新的用户注册、新的商品上架、新的订单生成时，都需要将数据插入到数据库中。INSERT语句就是用来完成这个任务的。

你有没有想过，当你在电商网站注册账号时，你的用户信息是如何被保存到数据库中的？当你在社交媒体上发布一条动态时，这条动态是如何被存储的？当你在银行系统中进行一笔交易时，交易记录是如何被记录的？这些都是INSERT语句在幕后工作的结果。

在这一章中，我们将学习如何使用INSERT语句向表中插入数据。从最基本的单行插入开始，到高效的多行插入，再到处理默认值和自增列的特殊情况。掌握了这些技巧，你就能够将各种数据准确地存储到数据库中。

准备好了吗？让我们开始学习数据插入的奥秘吧！

## [5.1 单行插入](#_5-1-单行插入)

INSERT语句最基本的用法是向表中插入一行数据。最简单的语法是指定表名和要插入的值，但这种做法存在一定的风险，更推荐的做法是明确指定要插入的列名。

让我们创建一个简单的用户表来演示各种插入操作：

```
-- 创建用户表
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    city VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

最基本的插入语法是省略列名，只提供值：

```
INSERT INTO users VALUES (NULL, '张三', 'zhangsan@example.com', 25, '北京', NOW());
```

这种语法要求值的顺序必须与表中列的顺序完全一致，而且必须为每一列提供值（即使是有默认值的列）。这种写法存在几个问题：如果表结构发生变化（比如新增了一列），这个语句就会出错；而且代码可读性差，很难看出每个值对应哪个列。

更推荐的写法是明确指定列名：

```
INSERT INTO users (username, email, age, city)
VALUES ('李四', 'lisi@example.com', 30, '上海');
```

执行结果：

```
Query OK, 1 row affected (0.01 sec)
```

这种写法有很多好处：首先，代码可读性更好，能够清楚地看出每个值对应哪个列；其次，如果表结构新增了有默认值的列，这个语句仍然能够正常工作；最后，我们可以只为部分列提供值，其他列会使用默认值或NULL。

让我们验证一下插入的数据：

```
SELECT * FROM users;
```

执行结果：

```
+----+----------+---------------------+------+--------+---------------------+
| id | username | email               | age  | city   | created_at          |
+----+----------+---------------------+------+--------+---------------------+
|  1 | 张三     | zhangsan@example.com |   25 | 北京   | 2025-08-31 10:00:00 |
|  2 | 李四     | lisi@example.com    |   30 | 上海   | 2025-08-31 10:01:00 |
+----+----------+---------------------+------+--------+---------------------+
2 rows in set (0.00 sec)
```

可以看到，第二个插入语句中我们没有指定id和created\_at列，id列因为是自增主键，所以自动生成了值2；created\_at列因为有默认值CURRENT\_TIMESTAMP，所以自动填入了当前时间。

在实际应用中，明确指定列名还有一个重要的好处：可以避免敏感数据的安全问题。比如，如果表中有一个is\_admin列用来标识用户是否为管理员，使用省略列名的插入方式可能会意外地设置这个值，而明确指定列名则可以避免这种风险。

当我们插入的数据包含特殊字符时，需要注意正确处理。比如，如果要插入包含单引号的字符串：

```
INSERT INTO users (username, email, age, city)
VALUES ('王五的妹妹', 'wangwu@example.com', 28, '广州');
```

这个语句能够正常工作，因为字符串值用单引号括起来。但如果字符串中包含单引号，就需要使用转义字符：

```
INSERT INTO users (username, email, age, city)
VALUES ('O\'Reilly', 'oreilly@example.com', 35, '深圳');
```

在大多数编程语言中，我们都会使用参数化查询或预处理语句来处理数据插入，这样可以自动处理特殊字符的转义，同时还能防止SQL注入攻击。

## [5.2 多行插入](#_5-2-多行插入)

在实际应用中，我们经常需要一次性插入多行数据。MySQL允许我们在一个INSERT语句中插入多行数据，这比使用多个单行INSERT语句效率更高。

多行插入的语法是在VALUES后面提供多组值，每组值用括号括起来，组之间用逗号分隔：

```
INSERT INTO users (username, email, age, city) VALUES 
('赵六', 'zhaoliu@example.com', 22, '杭州'),
('钱七', 'qianqi@example.com', 28, '成都'),
('孙八', 'sunba@example.com', 35, '武汉'),
('周九', 'zhoujiu@example.com', 26, '西安'),
('吴十', 'wushi@example.com', 31, '南京');
```

执行结果：

```
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0
```

这种方式插入5行数据只执行了一次SQL语句，而如果使用5个单行INSERT语句，就需要执行5次SQL语句。多行插入的优势在于减少了网络往返和数据库的开销，特别是在需要插入大量数据时，性能优势更加明显。

让我们验证一下插入的数据：

```
SELECT * FROM users ORDER BY id;
```

执行结果：

```
+----+------------+---------------------+------+--------+---------------------+
| id | username   | email               | age  | city   | created_at          |
+----+------------+---------------------+------+--------+---------------------+
|  1 | 张三       | zhangsan@example.com |   25 | 北京   | 2025-08-31 10:00:00 |
|  2 | 李四       | lisi@example.com    |   30 | 上海   | 2025-08-31 10:01:00 |
|  3 | 赵六       | zhaoliu@example.com |   22 | 杭州   | 2025-08-31 10:02:00 |
|  4 | 钱七       | qianqi@example.com  |   28 | 成都   | 2025-08-31 10:02:00 |
|  5 | 孙八       | sunba@example.com   |   35 | 武汉   | 2025-08-31 10:02:00 |
|  6 | 周九       | zhoujiu@example.com |   26 | 西安   | 2025-08-31 10:02:00 |
|  7 | 吴十       | wushi@example.com   |   31 | 南京   | 2025-08-31 10:02:00 |
+----+------------+---------------------+------+--------+---------------------+
7 rows in set (0.00 sec)
```

可以看到，5条数据都成功插入了，id列自动递增，created\_at列自动填入了当前时间。

多行插入特别适合批量数据导入的场景。比如，我们需要从其他系统导入用户数据，或者批量初始化一些基础数据。使用多行插入可以大大提高数据导入的效率。

但是，多行插入也有一些限制和注意事项。首先，单条SQL语句的长度是有限制的，如果一次插入的行数太多，可能会超出这个限制。其次，如果其中一行数据有错误，整个语句都会失败，不会插入任何数据。因此，在实际应用中，我们通常会将大批量的数据分成较小的批次进行插入，比如每次插入1000行。

还有一个需要注意的地方是，多行插入中的每一行都必须有相同的列数，而且数据类型要匹配。比如，下面的语句是错误的：

```
-- 错误的示例：列数不一致
INSERT INTO users (username, email, age, city) VALUES 
('测试用户1', 'test1@example.com', 25),
('测试用户2', 'test2@example.com');  -- 缺少age和city值
```

正确的做法是为所有列提供值，或者使用DEFAULT关键字：

```
INSERT INTO users (username, email, age, city) VALUES 
('测试用户1', 'test1@example.com', 25, '北京'),
('测试用户2', 'test2@example.com', DEFAULT, DEFAULT);
```

这样第二行数据的age和city列就会使用默认值（NULL）。

在实际开发中，我们通常会在应用程序代码中构建多行插入的SQL语句。比如，在Python中，我们可以这样构建：

```
users_data = [
    ('user1', 'user1@example.com', 25, '北京'),
    ('user2', 'user2@example.com', 30, '上海'),
    # 更多用户数据...
]

sql = "INSERT INTO users (username, email, age, city) VALUES "
values_list = []
for user in users_data:
    values_list.append(f"('{user[0]}', '{user[1]}', {user[2]}, '{user[3]}')")

sql += ', '.join(values_list)
```

当然，在实际应用中，我们应该使用参数化查询来构建SQL语句，以防止SQL注入攻击。

## [5.3 默认值与自增列](#_5-3-默认值与自增列)

在数据库表设计中，默认值和自增列是两个非常重要的概念。它们能够简化数据插入的过程，确保数据的完整性，并且在很多情况下提供更好的性能。

默认值是在插入数据时，如果没有为某列提供值，数据库会自动使用的值。我们在前面的例子中已经看到了默认值的使用，比如created\_at列的默认值是CURRENT\_TIMESTAMP。

让我们创建一个更复杂的表来演示默认值的使用：

```
-- 创建产品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) DEFAULT 0.00,
    stock INT DEFAULT 0,
    status ENUM('active', 'inactive', 'discontinued') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

在这个表中，我们为多个列设置了默认值。price列的默认值是0.00，stock列的默认值是0，status列的默认值是'active'。特别值得注意的是updated\_at列，它不仅在插入时默认为当前时间，而且在每次更新记录时都会自动更新为当前时间。

让我们插入一些数据来测试默认值：

```
INSERT INTO products (name) VALUES 
('iPhone 15'),
('小米13'),
('华为P60');
```

在这个插入语句中，我们只提供了name列的值，其他列都会使用默认值。让我们查看插入的结果：

```
SELECT * FROM products;
```

执行结果：

```
+----+------------+----------+-------+------------+---------------------+---------------------+
| id | name       | price    | stock | status     | created_at          | updated_at          |
+----+------------+----------+-------+------------+---------------------+---------------------+
|  1 | iPhone 15  |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
|  2 | 小米13     |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
|  3 | 华为P60     |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
+----+------------+----------+-------+------------+---------------------+---------------------+
3 rows in set (0.00 sec)
```

可以看到，price和stock列都使用了默认值0，status列使用了默认值'active'，created\_at和updated\_at列都使用了当前时间。

自增列（AUTO\_INCREMENT）是MySQL中一个非常有用的特性，通常用于主键列。当我们插入新记录时，如果没有指定自增列的值，MySQL会自动为该列生成一个唯一的值，通常是当前最大值加1。

让我们看看自增列的工作方式：

```
INSERT INTO products (name, price, stock) VALUES 
('MacBook Pro', 12999.00, 50),
('iPad Air', 4599.00, 120);
```

现在查看表中的数据：

```
SELECT * FROM products;
```

执行结果：

```
+----+------------+----------+-------+------------+---------------------+---------------------+
| id | name       | price    | stock | status     | created_at          | updated_at          |
+----+------------+----------+-------+------------+---------------------+---------------------+
|  1 | iPhone 15  |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
|  2 | 小米13     |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
|  3 | 华为P60     |     0.00 |     0 | active     | 2025-08-31 10:03:00 | 2025-08-31 10:03:00 |
|  4 | MacBook Pro| 12999.00 |    50 | active     | 2025-08-31 10:04:00 | 2025-08-31 10:04:00 |
| 5 | iPad Air   |  4599.00 |   120 | active     | 2025-08-31 10:04:00 | 2025-08-31 10:04:00 |
+----+------------+----------+-------+------------+---------------------+---------------------+
5 rows in set (0.00 sec)
```

可以看到，新插入的两条记录的id分别是4和5，MySQL自动为我们生成了这些值。

有时候，我们可能需要手动指定自增列的值。比如，在数据迁移或特殊业务场景下，我们可以这样做：

```
INSERT INTO products (id, name, price, stock) 
VALUES (10, 'Surface Pro', 6999.00, 40);
```

这样插入的记录id就是10。但是，手动指定自增值需要小心，如果指定的值已经存在，会导致主键冲突错误：

```
-- 这会导致错误，因为id=1已经存在
INSERT INTO products (id, name, price, stock) 
VALUES (1, 'Test Product', 100.00, 10);
```

执行结果：

```
ERROR 1062 (23000): Duplicate entry '1' for key 'PRIMARY'
```

当我们手动指定了较大的自增值后，MySQL的自增计数器不会自动调整。这意味着下一次自动生成的值可能会与我们手动指定的值冲突。为了避免这个问题，我们可以手动调整自增计数器：

```
ALTER TABLE products AUTO_INCREMENT = 100;
```

这样，下一次自动生成的id就会从100开始。

在实际应用中，自增列的一个常见用途是作为关联表的外键。比如，在订单系统中，订单表会有一个自增的订单ID，订单明细表会引用这个订单ID。自增主键确保了每个订单都有唯一的标识符，便于管理和查询。

## [练习题](#练习题)

### [练习1：单行插入与默认值](#练习1-单行插入与默认值)

向users表中插入一个新用户，用户名为"新用户"，邮箱为"[newuser@example.com](mailto:newuser@example.com)"，年龄25岁，不指定城市，让数据库使用默认值。

查看答案

```
INSERT INTO users (username, email, age)
VALUES ('新用户', 'newuser@example.com', 25);
```

### [练习2：多行插入](#练习2-多行插入)

向products表中插入3个新产品，包括产品名称、价格和库存信息，让其他列使用默认值。

查看答案

```
INSERT INTO products (name, price, stock) VALUES 
('AirPods Pro', 1899.00, 200),
('小米手环', 299.00, 300),
('华为手表', 1299.00, 90);
```

### [练习3：手动指定自增值](#练习3-手动指定自增值)

向products表中插入一个产品，手动指定id为20，产品名称为"测试产品"，价格999元，库存50个。

查看答案

```
INSERT INTO products (id, name, price, stock)
VALUES (20, '测试产品', 999.00, 50);
```

## [常见坑](#常见坑)

### [坑1：省略列名导致的数据错位](#坑1-省略列名导致的数据错位)

很多初学者为了省事，在INSERT语句中省略列名，这样做很危险。如果表结构发生变化，比如新增了列或者调整了列顺序，会导致数据插入到错误的列中。

**错误示例**：

```
-- 危险的写法
INSERT INTO users VALUES (NULL, '用户名', 'email@example.com', 25);
```

**纠正方法**：始终明确指定列名：

```
INSERT INTO users (username, email, age)
VALUES ('用户名', 'email@example.com', 25);
```

### [坑2：多行插入中的部分失败](#坑2-多行插入中的部分失败)

在多行插入中，如果某一行数据有错误（比如违反约束），整个语句都会失败，不会插入任何数据。

**错误示例**：

```
-- 如果第二行有重复的邮箱，整个语句都会失败
INSERT INTO users (username, email, age) VALUES 
('用户1', 'user1@example.com', 25),
('用户2', 'user2@example.com', 30);  -- 假设这个邮箱已存在
```

**纠正方法**：在应用层进行数据验证，或者使用单行插入逐条处理，失败时记录日志。

### [坑3：忽略自增列的手动管理](#坑3-忽略自增列的手动管理)

手动指定自增值后，如果不及时调整自增计数器，可能导致后续的自动生成值与手动指定的值冲突。

**纠正方法**：在手动插入指定ID后，根据需要调整自增计数器：

```
-- 插入大ID后调整计数器
INSERT INTO products (id, name) VALUES (1000, '测试产品');
ALTER TABLE products AUTO_INCREMENT = 1001;
```

## [速记卡](#速记卡)

- **INSERT语法**：INSERT INTO table\_name (column1, column2) VALUES (value1, value2)
- **明确列名**：始终推荐明确指定列名，避免表结构变化导致的问题
- **默认值**：未指定值的列会使用默认值，没有默认值的列会使用NULL
- **多行插入**：VALUES (row1), (row2), (row3) ... 比多个单行插入更高效
- **自增列**：AUTO\_INCREMENT列会自动生成唯一值，通常用于主键
- **手动指定ID**：可以手动指定自增值，但要注意避免冲突
- **特殊列类型**：TIMESTAMP列可以设置ON UPDATE CURRENT\_TIMESTAMP自动更新
- **数据完整性**：使用约束（NOT NULL、UNIQUE等）确保数据质量

## [章节总结](#章节总结)

在这一章中，我们学习了如何向数据库表中插入数据，这是数据库操作中最基本也是最重要的技能之一。从单行插入开始，我们了解了明确指定列名的重要性，以及如何利用默认值来简化数据插入过程。

多行插入技术让我们能够高效地批量导入数据，相比多次执行单行插入，多行插入大大减少了网络开销和数据库负载。在实际应用中，合理使用多行插入可以显著提高数据导入的性能。

默认值和自增列是数据库设计中的重要概念。默认值为我们提供了处理缺失数据的灵活方式，确保数据完整性。自增列则为我们提供了生成唯一标识符的便捷方法，特别是在主键和外键关系中发挥着重要作用。

掌握了数据插入的技能，你就能够构建完整的数据管理功能。无论是用户注册、商品上架，还是订单处理，都离不开数据插入操作。在下一章中，我们将学习如何修改和删除现有数据，进一步完善我们的数据操作技能。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [05｜插入：数据该怎么写进表？](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#_05-插入-数据该怎么写进表)
- [5.1 单行插入](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#_5-1-单行插入)
- [5.2 多行插入](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#_5-2-多行插入)
- [5.3 默认值与自增列](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#_5-3-默认值与自增列)
- [练习题](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#练习题)
- [练习1：单行插入与默认值](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#练习1-单行插入与默认值)
- [练习2：多行插入](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#练习2-多行插入)
- [练习3：手动指定自增值](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#练习3-手动指定自增值)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#常见坑)
- [坑1：省略列名导致的数据错位](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#坑1-省略列名导致的数据错位)
- [坑2：多行插入中的部分失败](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#坑2-多行插入中的部分失败)
- [坑3：忽略自增列的手动管理](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#坑3-忽略自增列的手动管理)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/05-insert-data.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
