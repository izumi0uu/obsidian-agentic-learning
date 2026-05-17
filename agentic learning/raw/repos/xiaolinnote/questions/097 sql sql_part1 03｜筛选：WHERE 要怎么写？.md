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
url: "https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html"
source: "https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html"
last_checked: 2026-05-17
freshness: watch
sha256: d5db55f172153a1598e35bed4d71da2fafcb91e922082cb780d0f939df42bd88
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 03｜筛选：WHERE 要怎么写？

原始链接：https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 03｜筛选：WHERE 要怎么写？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 18 分钟约 5537 字2025/8/31

---

# [03｜筛选：WHERE 要怎么写？](#_03-筛选-where-要怎么写)

大家好，我是小林。

在前两章中，我们学习了如何使用SELECT查询数据，但很多时候我们并不需要表中的所有数据，而是需要找到符合特定条件的数据。比如，在商品表中找到价格大于1000元的商品，或者在用户表中找到年龄在25到35岁之间的用户。这时候，WHERE子句就派上用场了。

你有没有想过，当你在一个庞大的电商网站搜索商品时，网站是如何快速从数百万件商品中找到符合你要求的商品的？当你筛选价格区间、品牌、颜色等条件时，背后实际上就是WHERE子句在工作。WHERE子句就像是数据的"筛子"，帮我们从海量数据中精确地找到需要的信息。

在这一章中，我们将学习WHERE子句的各种用法。从简单的比较运算，到复杂的逻辑组合，再到范围查询、模糊匹配和空值处理。掌握了这些技巧，你就能够应对各种数据筛选需求，让查询结果更加精准。

准备好了吗？让我们开始学习WHERE子句的奥秘吧！

## [3.1 比较运算](#_3-1-比较运算)

WHERE子句最基础的用法就是使用比较运算符来筛选数据。MySQL支持多种比较运算符，包括等于、不等于、大于、小于等。这些运算符看起来很简单，但在实际使用中有一些细节需要注意。

让我们继续使用前一章的products表来演示各种WHERE筛选。为了确保数据完整，我们重新创建一下这个表：

```
-- 创建产品表
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入示例数据
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

最基本的比较运算符是等于号（=），它用来精确匹配某个值。比如，我们想找到所有手机类别的产品：

```
SELECT name, category, price
FROM products
WHERE category = '手机';
```

执行结果：

```
+-----------+-----------+----------+
| name      | category  | price    |
+-----------+-----------+----------+
| iPhone 15 | 手机      |  5999.00 |
| 小米13    | 手机      |  3999.00 |
| 华为P60   | 手机      |  4999.00 |
+-----------+-----------+----------+
3 rows in set (0.00 sec)
```

不等于运算符有两种写法：!=和<>，它们的功能完全相同。比如，我们想找到所有非手机产品：

```
SELECT name, category, price
FROM products
WHERE category != '手机';
```

或者使用<>：

```
SELECT name, category, price
FROM products
WHERE category <> '手机';
```

两个查询会返回相同的结果，包含除手机外的所有产品。

大于和小于运算符用于数值比较。比如，我们想找到价格大于5000元的产品：

```
SELECT name, category, price
FROM products
WHERE price > 5000;
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

大于等于和小于等于运算符包含边界值。比如，我们想找到价格在4000到6000元之间的产品（包含边界值）：

```
SELECT name, category, price
FROM products
WHERE price >= 4000 AND price <= 6000;
```

执行结果：

```
+-----------+-----------+----------+
| name      | category  | price    |
+-----------+-----------+----------+
| iPhone 15 | 手机      |  5999.00 |
| 小米13    | 手机      |  3999.00 |
| 华为P60   | 手机      |  4999.00 |
| iPad Air  | 平板      |  4599.00 |
+-----------+-----------+----------+
4 rows in set (0.00 sec)
```

在使用比较运算符时，有一个需要注意的地方是数据类型的隐式转换。MySQL会尝试在不同类型之间进行转换，但这有时会导致意外的结果。比如，如果我们将数字与字符串比较：

```
SELECT name, category, price
FROM products
WHERE price = '5999.00';
```

这个查询能够正常工作，因为MySQL会将字符串'5999.00'转换为数字5999.00进行比较。但是，最好避免依赖隐式转换，而是确保比较的数据类型一致。

字符串比较是按照字典顺序进行的，这在比较中文字符时尤其需要注意。比如，如果我们按照产品名称排序，结果可能不是我们期望的拼音顺序。在实际应用中，如果需要中文排序，可能需要使用特定的排序规则或拼音转换函数。

## [3.2 逻辑运算：AND / OR / NOT](#_3-2-逻辑运算-and-or-not)

在实际应用中，我们经常需要组合多个条件，这时候就需要使用逻辑运算符。AND、OR和NOT这三个逻辑运算符让我们能够构建复杂的筛选条件。

AND运算符要求所有条件都必须满足。比如，我们想找到价格大于4000元且库存大于100的产品：

```
SELECT name, category, price, stock
FROM products
WHERE price > 4000 AND stock > 100;
```

执行结果：

```
+-----------+-----------+----------+-------+
| name      | category  | price    | stock |
+-----------+-----------+----------+-------+
| iPhone 15 | 手机      |  5999.00 |   100 |
| iPad Air  | 平板      |  4599.00 |   120 |
+-----------+-----------+----------+-------+
2 rows in set (0.00 sec)
```

注意这里的条件是价格大于4000**且**库存大于100，两个条件必须同时满足。

OR运算符则只要求满足其中一个条件即可。比如，我们想找到价格大于10000元或者库存大于200的产品：

```
SELECT name, category, price, stock
FROM products
WHERE price > 10000 OR stock > 200;
```

执行结果：

```
+--------------+-----------+----------+-------+
| name         | category  | price    | stock |
+--------------+-----------+----------+-------+
| iPhone 15    | 手机      |  5999.00 |   100 |
| MacBook Pro  | 笔记本    | 12999.00 |    50 |
| AirPods Pro  | 耳机      |  1899.00 |   200 |
| 小米手环     | 智能穿戴  |   299.00 |   300 |
+--------------+-----------+----------+-------+
4 rows in set (0.00 sec)
```

这里的结果包含了价格大于10000元的MacBook Pro，以及库存大于200的小米手环（注意库存等于200的AirPods Pro没有被选中，因为条件是大于200）。

NOT运算符用于取反，它会把真变成假，假变成真。比如，我们想找到价格不大于4000元的产品：

```
SELECT name, category, price
FROM products
WHERE NOT price > 4000;
```

这等价于使用小于等于运算符：

```
SELECT name, category, price
FROM products
WHERE price <= 4000;
```

当我们组合使用AND和OR时，需要注意运算符的优先级。AND的优先级高于OR，这意味着AND会先被计算。如果不注意这一点，可能会得到意外的结果。

比如，我们想找到手机类别的产品，或者价格大于8000元的笔记本。如果这样写：

```
SELECT name, category, price
FROM products
WHERE category = '手机' OR category = '笔记本' AND price > 8000;
```

由于AND优先级高，这个查询实际执行的是：category = '手机' OR (category = '笔记本' AND price > 8000)，这可能会包含所有手机产品，而不仅仅是价格大于8000元的笔记本。

为了避免这种歧义，我们应该使用括号来明确指定运算顺序：

```
SELECT name, category, price
FROM products
WHERE (category = '手机' OR category = '笔记本') AND price > 8000;
```

这样就能正确找到价格大于8000元的手机或笔记本产品。

在实际工作中，当条件变得复杂时，建议使用括号来明确逻辑关系，即使有时括号可能不是必需的。这样可以提高代码的可读性，也避免因优先级问题导致的错误。

还有一种常见的复杂条件是"既不是A也不是B"，这可以用NOT配合OR来实现：

```
SELECT name, category, price
FROM products
WHERE NOT (category = '手机' OR category = '笔记本');
```

这会找到既不是手机也不是笔记本的产品，等价于使用AND连接两个NOT条件：

```
SELECT name, category, price
FROM products
WHERE category != '手机' AND category != '笔记本';
```

通过合理使用AND、OR和NOT，我们可以构建非常复杂的筛选条件，满足各种业务需求。关键是要理清条件之间的逻辑关系，适当使用括号来确保逻辑正确性。

## [3.3 范围与集合：BETWEEN / IN](#_3-3-范围与集合-between-in)

在数据筛选中，我们经常需要查询某个范围内的值或者某个集合中的值。BETWEEN和IN就是专门用于这类查询的运算符，它们能让我们的SQL语句更加简洁和易读。

BETWEEN运算符用于查询某个范围内的值，包括边界值。比如，我们想找到价格在3000到6000元之间的产品：

```
SELECT name, category, price
FROM products
WHERE price BETWEEN 3000 AND 6000;
```

执行结果：

```
+-----------+-----------+----------+
| name      | category  | price    |
+-----------+-----------+----------+
| iPhone 15 | 手机      |  5999.00 |
| 小米13    | 手机      |  3999.00 |
| 华为P60   | 手机      |  4999.00 |
| iPad Air  | 平板      |  4599.00 |
+-----------+-----------+----------+
4 rows in set (0.00 sec)
```

这个查询等价于使用AND连接两个比较条件：

```
SELECT name, category, price
FROM products
WHERE price >= 3000 AND price <= 6000;
```

使用BETWEEN的好处是代码更加简洁，语义也更加清晰。但要注意BETWEEN是包含边界值的，即闭区间。

BETWEEN也可以用于日期范围查询。比如，假设我们有一个包含日期的表，想找到某个时间段内的记录：

```
-- 添加一个日期列用于演示
ALTER TABLE products ADD COLUMN production_date DATE;
UPDATE products SET production_date = '2025-01-15' WHERE name = 'iPhone 15';
UPDATE products SET production_date = '2025-02-20' WHERE name = '小米13';
UPDATE products SET production_date = '2025-03-10' WHERE name = '华为P60';
UPDATE products SET production_date = '2025-01-08' WHERE name = 'MacBook Pro';
UPDATE products SET production_date = '2025-02-15' WHERE name = 'ThinkPad X1';

-- 查询2025年1月到2月生产的产品
SELECT name, production_date
FROM products
WHERE production_date BETWEEN '2025-01-01' AND '2025-02-28';
```

执行结果：

```
+--------------+------------------+
| name         | production_date  |
+--------------+------------------+
| iPhone 15    | 2025-01-15       |
| 小米13       | 2025-02-20       |
| MacBook Pro  | 2025-01-08       |
| ThinkPad X1  | 2025-02-15       |
+--------------+------------------+
4 rows in set (0.00 sec)
```

IN运算符用于查询某个集合中的值，它比使用多个OR条件更加简洁。比如，我们想找到手机、平板、笔记本这几个类别的产品：

```
SELECT name, category, price
FROM products
WHERE category IN ('手机', '平板', '笔记本');
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| iPhone 15    | 手机      |  5999.00 |
| 小米13       | 手机      |  3999.00 |
| 华为P60      | 手机      |  4999.00 |
| MacBook Pro  | 笔记本    | 12999.00 |
| ThinkPad X1  | 笔记本    |  8999.00 |
| iPad Air     | 平板      |  4599.00 |
| Surface Pro  | 平板      |  6999.00 |
+--------------+-----------+----------+
7 rows in set (0.00 sec)
```

这个查询等价于使用多个OR条件：

```
SELECT name, category, price
FROM products
WHERE category = '手机' OR category = '平板' OR category = '笔记本';
```

显然，使用IN运算符更加简洁，特别是当集合中有更多值时，优势更加明显。

IN运算符还可以与子查询配合使用，这使得它非常强大。比如，我们可以先查询出某个条件的结果，然后用这个结果作为IN的集合。虽然我们现在还没有学习子查询，但这是IN的一个重要用途。

NOT IN和NOT BETWEEN则是它们的反操作，用于查询不在指定范围或集合中的值。比如，我们想找到不属于手机、平板、笔记本类别的产品：

```
SELECT name, category, price
FROM products
WHERE category NOT IN ('手机', '平板', '笔记本');
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| AirPods Pro  | 耳机      |  1899.00 |
| 小米手环     | 智能穿戴  |   299.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
+--------------+-----------+----------+
3 rows in set (0.00 sec)
```

使用BETWEEN和IN时，有一个需要注意的地方是NULL值的处理。如果集合或范围中包含NULL值，结果可能会与预期不同。特别是在使用NOT IN时，如果集合中包含NULL，那么查询结果可能为空，因为任何与NULL的比较结果都是UNKNOWN。

在实际应用中，BETWEEN和IN是非常常用的运算符。它们不仅让SQL语句更加简洁，而且通常也比等价的AND/OR组合有更好的性能。数据库优化器能够更好地优化这些特殊的运算符。

## [3.4 模糊匹配：LIKE](#_3-4-模糊匹配-like)

有时候我们需要进行模糊匹配，而不是精确匹配。比如，我们可能只记得产品名称的一部分，或者想找到所有符合某种模式的数据。这时候，LIKE运算符就派上用场了。

LIKE运算符使用两个通配符：百分号（%）和下划线（\_）。百分号表示任意数量的字符（包括零个字符），下划线表示单个字符。

让我们看一些实际的例子。假设我们想找到所有名称中包含"iPhone"的产品：

```
SELECT name, category, price
FROM products
WHERE name LIKE '%iPhone%';
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| iPhone 15    | 手机      |  5999.00 |
+--------------+-----------+----------+
1 row in set (0.00 sec)
```

这里的'%iPhone%'表示在产品名称的任意位置包含"iPhone"这个字符串。前面的%表示iPhone前面可以有任意字符，后面的%表示iPhone后面可以有任意字符。

如果我们想找到所有以"小米"开头的产品：

```
SELECT name, category, price
FROM products
WHERE name LIKE '小米%';
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| 小米13       | 手机      |  3999.00 |
| 小米手环     | 智能穿戴  |   299.00 |
+--------------+-----------+----------+
2 rows in set (0.00 sec)
```

这个查询中的'小米%'表示以"小米"开头，后面可以跟任意字符。

同样，我们可以找到所有以"Pro"结尾的产品：

```
SELECT name, category, price
FROM products
WHERE name LIKE '%Pro';
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| MacBook Pro  | 笔记本    | 12999.00 |
| Surface Pro  | 平板      |  6999.00 |
| AirPods Pro  | 耳机      |  1899.00 |
+--------------+-----------+----------+
3 rows in set (0.00 sec)
```

下划线通配符用于匹配单个字符。比如，我们想找到所有"小米"后面跟一个数字的产品：

```
SELECT name, category, price
FROM products
WHERE name LIKE '小米_';
```

执行结果：

```
+-----------+-----------+----------+
| name      | category  | price    |
+-----------+-----------+----------+
| 小米13    | 手机      |  3999.00 |
+-----------+-----------+----------+
1 row in set (0.00 sec)
```

这个查询中的'小米\_'表示"小米"后面跟任意一个字符。注意它不会匹配"小米手环"，因为"手环"不是一个字符。

如果我们需要匹配字面意义上的百分号或下划线，可以使用转义字符。默认情况下，反斜杠（\）是转义字符：

```
-- 假设我们有一个包含百分号的产品名称
SELECT name, category, price
FROM products
WHERE name LIKE '%\%%';
```

这个查询会找到名称中包含百分号的产品。

从性能角度来看，LIKE查询有一个重要的特点：如果通配符在开头（如'%iPhone'），数据库通常无法使用索引，会进行全表扫描。而如果通配符在结尾（如'iPhone%'），数据库则可能使用索引。因此，在设计查询时，应该尽量避免使用前置百分号的模糊匹配，特别是在大数据量的表中。

对于更复杂的文本搜索需求，MySQL提供了全文索引（FULLTEXT）功能，它能够提供更强大的搜索能力和更好的性能。但这超出了我们当前的学习范围。

NOT LIKE用于排除符合某个模式的数据。比如，我们想找到所有不以"小米"开头的产品：

```
SELECT name, category, price
FROM products
WHERE name NOT LIKE '小米%';
```

这个查询会返回除"小米13"和"小米手环"之外的所有产品。

LIKE运算符是SQL中非常强大的工具，它让我们能够进行灵活的模式匹配。但在使用时要注意性能影响，特别是在处理大量数据时。

## [3.5 空值判断：IS NULL](#_3-5-空值判断-is-null)

在数据库中，NULL是一个特殊的值，表示"未知"或"缺失"。NULL不同于空字符串或0，它表示数据的缺失。处理NULL值需要特殊的语法，这也是很多初学者容易混淆的地方。

让我们先在products表中添加一些NULL值来演示：

```
-- 添加一些NULL值用于演示
UPDATE products SET stock = NULL WHERE name = 'ThinkPad X1';
UPDATE products SET category = NULL WHERE name = 'AirPods Pro';
```

现在，如果我们想找到库存为NULL的产品，很多人会尝试这样写：

```
SELECT name, category, stock
FROM products
WHERE stock = NULL;
```

但这个查询不会返回任何结果！这是因为NULL与任何值的比较结果都是NULL，而不是TRUE或FALSE。在WHERE子句中，只有条件为TRUE的记录才会被返回。

正确的做法是使用IS NULL：

```
SELECT name, category, stock
FROM products
WHERE stock IS NULL;
```

执行结果：

```
+--------------+-----------+-------+
| name         | category  | stock |
+--------------+-----------+-------+
| ThinkPad X1  | 笔记本    |  NULL |
+--------------+-----------+-------+
1 row in set (0.00 sec)
```

同样，要找到库存不为NULL的产品，应该使用IS NOT NULL：

```
SELECT name, category, stock
FROM products
WHERE stock IS NOT NULL;
```

这个查询会返回所有库存不为NULL的产品。

NULL参与运算时，结果通常也是NULL。比如：

```
SELECT name, price, stock, price * stock AS total_value
FROM products
WHERE name = 'ThinkPad X1';
```

执行结果：

```
+--------------+----------+-------+-------------+
| name         | price    | stock | total_value |
+--------------+----------+-------+-------------+
| ThinkPad X1  |  8999.00 |  NULL |        NULL |
+--------------+----------+-------+-------------+
1 row in set (0.00 sec)
```

因为stock是NULL，所以price \* stock的结果也是NULL。

在处理NULL值时，COALESCE函数非常有用。它返回参数列表中的第一个非NULL值。比如，我们可以用COALESCE为NULL值提供默认值：

```
SELECT name, category, COALESCE(stock, 0) AS safe_stock
FROM products;
```

执行结果：

```
+--------------+-----------+------------+
| name         | category  | safe_stock |
+--------------+-----------+------------+
| iPhone 15    | 手机      |        100 |
| 小米13       | 手机      |        150 |
| 华为P60      | 手机      |         80 |
| MacBook Pro  | 笔记本    |         50 |
| ThinkPad X1  | 笔记本    |          0 |
| iPad Air     | 平板      |        120 |
| Surface Pro  | 平板      |         40 |
| AirPods Pro  | NULL      |        200 |
| 小米手环     | 智能穿戴  |        300 |
| 华为手表     | 智能穿戴  |         90 |
+--------------+-----------+------------+
10 rows in set (0.00 sec)
```

在这个查询中，如果stock是NULL，COALESCE会返回0，否则返回stock的实际值。

另一个常用的函数是IFNULL，它与COALESCE类似，但只接受两个参数：

```
SELECT name, category, IFNULL(stock, 0) AS safe_stock
FROM products;
```

这个查询与上面的COALESCE查询效果相同。

在ORDER BY中，NULL值的处理也需要注意。默认情况下，NULL值被认为是最小的值，在升序排序时会排在最前面。我们可以使用COALESCE来改变这种行为：

```
SELECT name, stock
FROM products
ORDER BY COALESCE(stock, 0) DESC;
```

这个查询会将NULL值当作0来排序，而不是让它们排在最前面。

理解NULL的处理对于编写正确的SQL查询非常重要。记住，NULL不是空字符串，不是0，它表示值的缺失。在与NULL比较时，必须使用IS NULL或IS NOT NULL，而不能使用=或!=。

## [练习题](#练习题)

### [练习1：多条件筛选](#练习1-多条件筛选)

查询products表中价格大于4000元且库存大于100的产品，显示产品名称、类别、价格和库存。

查看答案

```
SELECT name, category, price, stock
FROM products
WHERE price > 4000 AND stock > 100;
```

### [练习2：范围和集合查询](#练习2-范围和集合查询)

查询products表中价格在3000到8000元之间，且类别为手机或平板的产品。

查看答案

```
SELECT name, category, price
FROM products
WHERE price BETWEEN 3000 AND 8000
AND category IN ('手机', '平板');
```

### [练习3：模糊匹配和空值处理](#练习3-模糊匹配和空值处理)

查询products表中产品名称包含"Pro"或库存为NULL的产品。

查看答案

```
SELECT name, category, price, stock
FROM products
WHERE name LIKE '%Pro%' OR stock IS NULL;
```

## [常见坑](#常见坑)

### [坑1：在WHERE中使用聚合函数](#坑1-在where中使用聚合函数)

很多初学者会尝试在WHERE子句中使用聚合函数，这是错误的。因为聚合函数在WHERE执行时还没有计算。

**错误示例**：

```
SELECT name, price
FROM products
WHERE price > AVG(price);
```

**纠正方法**：使用HAVING子句或子查询：

```
-- 方法1：使用HAVING（需要GROUP BY）
SELECT name, price
FROM products
GROUP BY name, price
HAVING price > (SELECT AVG(price) FROM products);

-- 方法2：使用子查询
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

### [坑2：BETWEEN的边界值问题](#坑2-between的边界值问题)

有些初学者会误以为BETWEEN不包含边界值，但实际上BETWEEN是包含边界值的（闭区间）。

**纠正方法**：如果需要开区间，应该使用大于和小于运算符：

```
-- 不包含边界值
SELECT name, price
FROM products
WHERE price > 3000 AND price < 8000;
```

### [坑3：NULL值的比较](#坑3-null值的比较)

最常见的错误是使用=或!=来比较NULL值，这是不会返回预期结果的。

**错误示例**：

```
SELECT name, stock
FROM products
WHERE stock = NULL;
```

**纠正方法**：使用IS NULL或IS NOT NULL：

```
SELECT name, stock
FROM products
WHERE stock IS NULL;
```

## [速记卡](#速记卡)

- **比较运算符**：=、!=、<>、>、>=、<、<=，用于数值和字符串比较
- **逻辑运算符**：AND（与）、OR（或）、NOT（非），AND优先级高于OR
- **BETWEEN**：用于范围查询，包含边界值，等价于AND组合
- **IN**：用于集合查询，比多个OR更简洁，可配合子查询使用
- **LIKE**：模糊匹配，%表示任意字符，\_表示单个字符
- **NULL处理**：必须使用IS NULL/IS NOT NULL，不能用=比较
- **COALESCE**：返回第一个非NULL值，常用于NULL值的默认处理
- **三值逻辑**：TRUE、FALSE、UNKNOWN，NULL参与运算结果通常为UNKNOWN

## [章节总结](#章节总结)

在这一章中，我们深入学习了WHERE子句的各种筛选条件，这是SQL查询中最重要的部分之一。从最基本的比较运算开始，我们了解了如何使用各种比较运算符来精确筛选数据。

逻辑运算符AND、OR、NOT让我们能够组合多个条件，构建复杂的筛选逻辑。关键是要理解运算符的优先级，适当使用括号来明确逻辑关系，避免因优先级问题导致的错误。

BETWEEN和IN运算符为范围查询和集合查询提供了简洁的语法。它们不仅让SQL语句更加易读，而且通常也比等价的AND/OR组合有更好的性能。

LIKE运算符赋予我们强大的模糊匹配能力，通过通配符%和\_可以灵活地匹配各种模式。但要注意性能影响，特别是前置百分号的模糊匹配可能导致全表扫描。

NULL值的处理是很多初学者的难点。记住NULL不是空字符串或0，它表示值的缺失。在与NULL比较时，必须使用IS NULL或IS NOT NULL，而不能使用普通的比较运算符。

掌握了这些WHERE子句的技巧，你就能够应对各种数据筛选需求，从海量数据中精确地找到需要的信息。下一章，我们将学习如何对查询结果进行排序和分页，进一步完善我们的SQL技能。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [03｜筛选：WHERE 要怎么写？](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_03-筛选-where-要怎么写)
- [3.1 比较运算](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_3-1-比较运算)
- [3.2 逻辑运算：AND / OR / NOT](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_3-2-逻辑运算-and-or-not)
- [3.3 范围与集合：BETWEEN / IN](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_3-3-范围与集合-between-in)
- [3.4 模糊匹配：LIKE](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_3-4-模糊匹配-like)
- [3.5 空值判断：IS NULL](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#_3-5-空值判断-is-null)
- [练习题](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#练习题)
- [练习1：多条件筛选](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#练习1-多条件筛选)
- [练习2：范围和集合查询](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#练习2-范围和集合查询)
- [练习3：模糊匹配和空值处理](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#练习3-模糊匹配和空值处理)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#常见坑)
- [坑1：在WHERE中使用聚合函数](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#坑1-在where中使用聚合函数)
- [坑2：BETWEEN的边界值问题](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#坑2-between的边界值问题)
- [坑3：NULL值的比较](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#坑3-null值的比较)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/03-where-filtering.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
