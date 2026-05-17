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
url: "https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html"
source: "https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html"
last_checked: 2026-05-17
freshness: watch
sha256: 262344fea7de31b4b3df41271a70cf98c12555935e9a9470267035440f08d87f
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 02｜查询：SELECT 要怎么写？

原始链接：https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 02｜查询：SELECT 要怎么写？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 13 分钟约 4020 字2025/8/31

---

# [02｜查询：SELECT 要怎么写？](#_02-查询-select-要怎么写)

大家好，我是小林。

恭喜你完成了第一章的学习！现在你已经掌握了数据库的基本概念，能够连接数据库并执行简单的查询。从这一章开始，我们将真正进入SQL的核心世界——查询数据。

你有没有想过，当我们面对一个包含成千上万条数据的表格时，如何精确地找到我们需要的信息？就像在一本厚厚的电话簿中查找某个人的号码，或者在庞大的商品库中找到心仪的商品。SQL的SELECT语句就是我们的"放大镜"和"过滤器"，帮助我们从海量数据中提取有价值的信息。

在这一章中，我们将学习SELECT查询的各种写法。从最简单的选择特定列，到使用通配符查询所有列，再到给列起别名让结果更易读，以及如何去除重复数据。这些看似简单的操作，实际上是你日后处理复杂数据查询的基础。

准备好了吗？让我们开始探索SELECT查询的奥秘吧！

## [2.1 选择列、\* 查询所有列](#_2-1-选择列、-查询所有列)

还记得我们在第一章中使用的`SELECT * FROM users;`吗？这个查询会返回users表中的所有列。但在实际工作中，我们往往只需要特定的列信息。这时，精确指定列名就是更好的选择。

让我们先创建一个更丰富的示例表来演示各种查询场景。为了保持数据库统一性，我们将基于第一章的users表进行扩展，创建一个简单的产品表：

```
-- 创建一个产品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入一些示例数据
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
```

现在，如果我们只想查看产品名称和价格，可以这样查询：

```
SELECT name, price FROM products;
```

执行结果如下：

```
+--------------+----------+
| name         | price    |
+--------------+----------+
| iPhone 15    |  5999.00 |
| 小米13       |  3999.00 |
| 华为P60      |  4999.00 |
| MacBook Pro  | 12999.00 |
| ThinkPad X1  |  8999.00 |
| iPad Air     |  4599.00 |
| Surface Pro  |  6999.00 |
| AirPods Pro  |  1899.00 |
| 小米手环     |   299.00 |
| 华为手表     |  1299.00 |
+--------------+----------+
10 rows in set (0.00 sec)
```

这个查询只返回了我们关心的两列数据，结果更加简洁清晰。精确选择列名有很多好处：减少数据传输量、提高查询效率、让结果更易读。

那么，什么时候应该使用`*`通配符呢？`SELECT *`会返回表中的所有列，这在某些场景下确实很有用。当你第一次接触一个新表时，使用`SELECT *`可以快速了解表的结构和数据内容。这就像拿到一本新书时，先翻看目录和前言，对全书有个整体印象。

```
SELECT * FROM products LIMIT 3;
```

执行结果：

```
+----+------------+-----------+----------+-------+---------------------+
| id | name       | category | price    | stock | created_at          |
+----+------------+-----------+----------+-------+---------------------+
|  1 | iPhone 15  | 手机      |  5999.00 |   100 | 2025-08-31 10:00:00 |
|  2 | 小米13     | 手机      |  3999.00 |   150 | 2025-08-31 10:00:00 |
|  3 | 华为P60    | 手机      |  4999.00 |    80 | 2025-08-31 10:00:00 |
+----+------------+-----------+----------+-------+---------------------+
3 rows in set (0.00 sec)
```

在开发过程中，当你需要快速验证数据或进行调试时，`SELECT *`也很方便。比如，你想确认某个记录是否真的存在，或者查看数据的完整情况。

但是，在生产环境中，我建议避免使用`SELECT *`。为什么呢？这不仅仅是性能问题，更是代码可维护性的考虑。想象一下，如果你的应用程序代码中大量使用了`SELECT *`，某天数据库表结构发生了变化，比如增加了一个新列或者删除了某个列，你的代码可能会出现意外行为。更糟糕的是，`SELECT *`会返回所有列，包括那些你根本不需要的列，这会增加网络传输的开销，降低查询性能。

通过合理选择列名和控制列的顺序，我们可以让查询结果更加符合实际需求，提高数据的可读性和实用性。比如，如果我们想按照价格从高到低的顺序显示产品信息，但只显示名称、类别和价格：

```
SELECT name, category, price
FROM products
ORDER BY price DESC;
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| MacBook Pro  | 笔记本    | 12999.00 |
| ThinkPad X1  | 笔记本    |  8999.00 |
| Surface Pro  | 平板      |  6999.00 |
| iPhone 15    | 手机      |  5999.00 |
| 华为P60      | 手机      |  4999.00 |
| iPad Air     | 平板      |  4599.00 |
| AirPods Pro  | 耳机      |  1899.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
| 小米13       | 手机      |  3999.00 |
| 小米手环     | 智能穿戴  |   299.00 |
+--------------+-----------+----------+
10 rows in set (0.00 sec)
```

## [2.2 列别名与简单表达式](#_2-2-列别名与简单表达式)

在实际工作中，我们经常需要对查询结果进行加工，比如计算总金额、拼接姓名、或者让列名更加易读。这时候，列别名就派上用场了。

列别名通过`AS`关键字来定义，它可以让结果集中的列名更加友好和专业。想象一下，你正在生成一份销售报表，直接使用数据库中的列名可能不够直观，而使用别名可以让报表更加专业和易读。

让我们先看一个简单的例子。假设我们想计算每个产品的总价值（价格 × 库存）：

```
SELECT name, price, stock, price * stock AS total_value
FROM products;
```

执行结果：

```
+--------------+----------+-------+-------------+
| name         | price    | stock | total_value |
+--------------+----------+-------+-------------+
| iPhone 15    |  5999.00 |   100 |   599900.00 |
| 小米13       |  3999.00 |   150 |   599850.00 |
| 华为P60      |  4999.00 |    80 |   399920.00 |
| MacBook Pro  | 12999.00 |    50 |   649950.00 |
| ThinkPad X1  |  8999.00 |    30 |   269970.00 |
| iPad Air     |  4599.00 |   120 |   551880.00 |
| Surface Pro  |  6999.00 |    40 |   279960.00 |
| AirPods Pro  |  1899.00 |   200 |   379800.00 |
| 小米手环     |   299.00 |   300 |    89700.00 |
| 华为手表     |  1299.00 |    90 |   116910.00 |
+--------------+----------+-------+-------------+
10 rows in set (0.00 sec)
```

在这个例子中，`price * stock AS total_value`创建了一个计算列，并将其命名为`total_value`。这样，结果集中的列名就更加直观了。

使用别名的最大好处是提高结果的可读性。让我们看一个更复杂的例子，生成一个产品报表：

```
SELECT 
    name AS '产品名称',
    category AS '产品类别',
    price AS '单价',
    stock AS '库存数量',
    price * stock AS '总价值',
    CASE 
        WHEN stock < 50 THEN '库存不足'
        WHEN stock < 100 THEN '库存正常'
        ELSE '库存充足'
    END AS '库存状态'
FROM products;
```

执行结果：

```
+--------------+-----------+----------+----------+-------------+--------------+
| 产品名称     | 产品类别  | 单价     | 库存数量 | 总价值     | 库存状态     |
+--------------+-----------+----------+----------+-------------+--------------+
| iPhone 15    | 手机      |  5999.00 |      100 |   599900.00 | 库存充足     |
| 小米13       | 手机      |  3999.00 |      150 |   599850.00 | 库存充足     |
| 华为P60      | 手机      |  4999.00 |       80 |   399920.00 | 库存正常     |
| MacBook Pro  | 笔记本    | 12999.00 |       50 |   649950.00 | 库存正常     |
| ThinkPad X1  | 笔记本    |  8999.00 |       30 |   269970.00 | 库存不足     |
| iPad Air     | 平板      |  4599.00 |      120 |   551880.00 | 库存充足     |
| Surface Pro  | 平板      |  6999.00 |       40 |   279960.00 | 库存不足     |
| AirPods Pro  | 耳机      |  1899.00 |      200 |   379800.00 | 库存充足     |
| 小米手环     | 智能穿戴  |   299.00 |      300 |    89700.00 | 库存充足     |
| 华为手表     | 智能穿戴  |  1299.00 |       90 |   116910.00 | 库存正常     |
+--------------+-----------+----------+----------+-------------+--------------+
10 rows in set (0.00 sec)
```

看到这样的结果，即使是非技术人员也能轻松理解每一列的含义。这就是别名的魅力所在！

别名不仅可以用于简单的算术运算，还可以与各种函数结合使用。让我们看一些实际应用场景。我们可以使用字符串拼接函数来创建更有意义的描述信息：

```
SELECT 
    CONCAT(name, ' (', category, ')') AS product_info,
    CONCAT('单价: ', price, '元') AS price_info
FROM products;
```

执行结果：

```
+-------------------------------------+------------------+
| product_info                        | price_info       |
+-------------------------------------+------------------+
| iPhone 15 (手机)                     | 单价: 5999.00元   |
| 小米13 (手机)                        | 单价: 3999.00元   |
| 华为P60 (手机)                       | 单价: 4999.00元   |
| MacBook Pro (笔记本)                 | 单价: 12999.00元  |
| ThinkPad X1 (笔记本)                 | 单价: 8999.00元   |
| iPad Air (平板)                      | 单价: 4599.00元   |
| Surface Pro (平板)                   | 单价: 6999.00元   |
| AirPods Pro (耳机)                   | 单价: 1899.00元   |
| 小米手环 (智能穿戴)                  | 单价: 299.00元    |
| 华为手表 (智能穿戴)                  | 单价: 1299.00元   |
+-------------------------------------+------------------+
10 rows in set (0.00 sec)
```

我们还可以使用数学函数和格式化函数来处理价格数据。比如，我们可以计算打折后的价格并格式化输出：

```
SELECT 
    name,
    price,
    ROUND(price * 0.9, 2) AS discounted_price,
    CONCAT(FORMAT(price * 0.9, 2), ' 元') AS formatted_price
FROM products
WHERE category = '手机';
```

执行结果：

```
+-----------+----------+------------------+------------------+
| name      | price    | discounted_price | formatted_price  |
+-----------+----------+------------------+------------------+
| iPhone 15 |  5999.00 |          5399.10 | 5,399.10 元      |
| 小米13    |  3999.00 |          3599.10 | 3,599.10 元      |
| 华为P60   |  4999.00 |          4499.10 | 4,499.10 元      |
+-----------+----------+------------------+------------------+
3 rows in set (0.00 sec)
```

通过合理使用列别名和表达式，我们可以让查询结果更加专业、易读和实用。这在生成报表、数据分析和业务智能应用中特别有用。

## [2.3 DISTINCT 去重](#_2-3-distinct-去重)

在数据分析中，我们经常需要获取唯一值，比如查看有哪些产品类别、哪些供应商，或者统计不重复的客户数量。这时候，DISTINCT关键字就派上用场了。

DISTINCT用于去除查询结果中的重复行，只返回唯一的值。想象一下，你有一个包含大量销售记录的表格，想要知道有多少不同的客户购买过产品，使用DISTINCT就能轻松得到答案。

让我们用products表来演示DISTINCT的用法：

```
SELECT DISTINCT category FROM products;
```

执行结果：

```
+-----------+
| category  |
+-----------+
| 手机      |
| 笔记本    |
| 平板      |
| 耳机      |
| 智能穿戴  |
+-----------+
5 rows in set (0.00 sec)
```

如果没有使用DISTINCT，查询结果会包含重复的类别：

```
SELECT category FROM products;
```

执行结果：

```
+-----------+
| category  |
+-----------+
| 手机      |
| 手机      |
| 手机      |
| 笔记本    |
| 笔记本    |
| 平板      |
| 平板      |
| 耳机      |
| 智能穿戴  |
| 智能穿戴  |
+-----------+
10 rows in set (0.00 sec)
```

DISTINCT不仅可以作用于单列，还可以作用于多列。当指定多列时，DISTINCT会去除这些列组合的重复值。让我们看看有哪些不同的产品类别和价格组合：

```
SELECT DISTINCT category, price FROM products;
```

执行结果：

```
+-----------+----------+
| category  | price    |
+-----------+----------+
| 手机      |  5999.00 |
| 手机      |  3999.00 |
| 手机      |  4999.00 |
| 笔记本    | 12999.00 |
| 笔记本    |  8999.00 |
| 平板      |  4599.00 |
| 平板      |  6999.00 |
| 耳机      |  1899.00 |
| 智能穿戴  |   299.00 |
| 智能穿戴  |  1299.00 |
+-----------+----------+
10 rows in set (0.00 sec)
```

可以看到，虽然有些类别相同，但每个"类别+价格"的组合都是唯一的。

DISTINCT还可以与聚合函数结合使用，这在统计不重复值的数量时特别有用。比如，我们想统计有多少种不同的产品类别：

```
SELECT COUNT(DISTINCT category) AS unique_categories FROM products;
```

执行结果：

```
+-------------------+
| unique_categories |
+-------------------+
|                 5 |
+-------------------+
1 row in set (0.00 sec)
```

这个查询告诉我们，总共有5个不同的产品类别。

在实际业务中，DISTINCT有很多应用场景。比如，我们可以分析不同价格区间的产品分布：

```
SELECT 
    CASE 
        WHEN price < 1000 THEN '经济型'
        WHEN price < 5000 THEN '中端型'
        WHEN price < 10000 THEN '高端型'
        ELSE '旗舰型'
    END AS price_range,
    COUNT(DISTINCT name) AS product_count
FROM products
GROUP BY 
    CASE 
        WHEN price < 1000 THEN '经济型'
        WHEN price < 5000 THEN '中端型'
        WHEN price < 10000 THEN '高端型'
        ELSE '旗舰型'
    END;
```

执行结果：

```
+-------------+---------------+
| price_range | product_count |
+-------------+---------------+
| 中端型      |             4 |
| 高端型      |             3 |
| 旗舰型      |             1 |
| 经济型      |             2 |
+-------------+---------------+
4 rows in set (0.00 sec)
```

这个查询帮助我们了解不同价格区间的产品分布情况，可以看到大部分产品集中在中端和高价位区间。

虽然DISTINCT很有用，但它也有性能成本。DISTINCT操作可能需要数据库进行排序或者使用哈希算法来去除重复值，这在处理大量数据时会消耗较多内存和CPU资源。在使用DISTINCT时，建议先通过WHERE子句过滤数据，再使用DISTINCT，这样可以提高查询效率。

通过合理使用DISTINCT，我们可以有效地去除重复数据，获得准确的统计信息，为数据分析提供有价值的基础。

## [练习题](#练习题)

### [练习1：查询产品信息](#练习1-查询产品信息)

查询products表中所有产品的名称、价格和库存，并按照价格从高到低排序。

查看答案

```
SELECT name, price, stock
FROM products
ORDER BY price DESC;
```

### [练习2：使用别名和表达式](#练习2-使用别名和表达式)

查询products表中每个产品的名称、价格、库存，并计算总价值（价格×库存），使用别名让列名更加易读。

查看答案

```
SELECT 
    name AS '产品名称',
    price AS '单价',
    stock AS '库存数量',
    price * stock AS '总价值'
FROM products;
```

### [练习3：多列去重](#练习3-多列去重)

查询products表中有哪些不同的产品类别和价格组合。

查看答案

```
SELECT DISTINCT category, price
FROM products;
```

## [常见坑](#常见坑)

### [坑1：在WHERE子句中使用列别名](#坑1-在where子句中使用列别名)

很多初学者会尝试在WHERE子句中使用列别名，这是错误的。因为SQL的执行顺序是先WHERE后SELECT，所以在WHERE执行时，别名还不存在。

**错误示例**：

```
SELECT name, price * 0.9 AS discounted_price
FROM products
WHERE discounted_price > 1000;
```

**纠正方法**：在WHERE中重复使用表达式，或者使用子查询：

```
-- 方法1：重复表达式
SELECT name, price * 0.9 AS discounted_price
FROM products
WHERE price * 0.9 > 1000;

-- 方法2：使用子查询
SELECT * FROM (
    SELECT name, price * 0.9 AS discounted_price
    FROM products
) AS temp
WHERE discounted_price > 1000;
```

### [坑2：DISTINCT的性能问题](#坑2-distinct的性能问题)

在大表上使用DISTINCT可能导致性能问题，特别是当结果集很大时。DISTINCT需要数据库进行额外的处理来去除重复值。

**纠正方法**：

- 先用WHERE子句过滤数据，再使用DISTINCT
- 考虑使用GROUP BY替代DISTINCT
- 为相关列创建合适的索引

### [坑3：忽略NULL值的处理](#坑3-忽略null值的处理)

DISTINCT会将NULL值视为一个独特的值，多个NULL值会被去重为一个。这可能导致统计结果与预期不符。

**纠正方法**：在使用DISTINCT之前，考虑是否需要处理NULL值，可以使用COALESCE函数提供默认值。

## [速记卡](#速记卡)

- **SELECT语句**：SQL中最常用的语句，用于从数据库中查询数据
- **列选择**：明确指定列名比使用\*更高效且更安全
- **列别名**：使用AS关键字为列起别名，提高结果可读性
- **表达式计算**：可以在SELECT中进行数学运算、字符串拼接等操作
- **DISTINCT**：去除重复值，可用于单列或多列
- **执行顺序**：SQL语句的执行顺序是FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY
- **性能考虑**：避免在大结果集上使用DISTINCT，先过滤再去重

## [章节总结](#章节总结)

在这一章中，我们深入学习了SELECT查询的各种写法，这是SQL学习的核心内容。从最基础的列选择开始，我们了解了如何精确地获取需要的数据，而不是盲目地使用SELECT \*。记住，在生产环境中，明确指定列名不仅是良好的编程习惯，也是性能优化的重要手段。

列别名和表达式计算让我们的查询结果更加灵活和实用。通过AS关键字，我们可以为列起一个更加友好的名字，让报表更加专业。表达式计算则让我们能够在查询中进行各种数学运算、字符串处理和日期操作，大大扩展了SQL的功能。

DISTINCT去重是数据分析中常用的技术，它帮助我们获取唯一值，进行准确的统计分析。我们学习了DISTINCT的基本用法、多列去重、与GROUP BY的比较，以及在实际业务中的应用场景。

这些看似简单的SELECT语句技巧，实际上是你日后处理复杂数据查询的基础。掌握了这些内容，你就能够应对大部分日常的数据查询需求。记住，学习SQL最重要的是多练习，建议你用不同的数据集来尝试这些查询技巧，加深理解。

下一章，我们将学习如何使用WHERE子句进行数据筛选，这是SQL查询中另一个核心概念。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [02｜查询：SELECT 要怎么写？](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#_02-查询-select-要怎么写)
- [2.1 选择列、* 查询所有列](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#_2-1-选择列、-查询所有列)
- [2.2 列别名与简单表达式](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#_2-2-列别名与简单表达式)
- [2.3 DISTINCT 去重](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#_2-3-distinct-去重)
- [练习题](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#练习题)
- [练习1：查询产品信息](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#练习1-查询产品信息)
- [练习2：使用别名和表达式](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#练习2-使用别名和表达式)
- [练习3：多列去重](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#练习3-多列去重)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#常见坑)
- [坑1：在WHERE子句中使用列别名](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#坑1-在where子句中使用列别名)
- [坑2：DISTINCT的性能问题](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#坑2-distinct的性能问题)
- [坑3：忽略NULL值的处理](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#坑3-忽略null值的处理)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/02-select-query-basics.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
