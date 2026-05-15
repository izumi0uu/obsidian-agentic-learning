---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html"
source: "https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html"
last_checked: 2026-05-07
freshness: watch
sha256: c41e0980e124e0b9f94d4ae7c23a60d09226ab8089808f1a942dda1f587bd8aa
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 04｜排序与分页：结果怎么排序与分页？

原始链接：https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 12 分钟约 3706 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了如何使用WHERE子句筛选数据，但有时候我们不仅需要找到符合条件的数据，还需要按照特定的顺序来展示这些数据。比如，在电商网站上，我们可能想按照价格从低到高查看商品，或者按照销量排序查看热门商品。另外，当数据量很大时，我们通常不会一次性显示所有数据，而是分页展示，就像翻书一样一页一页地查看。

你有没有想过，为什么你在浏览商品列表时，商品总是按照某种顺序排列？为什么有些网站能够快速加载第100页的内容而不会很慢？这背后就是ORDER BY和分页技术在发挥作用。ORDER BY让数据变得有序，而分页技术则让大数据量的展示变得高效和用户友好。

在这一章中，我们将学习如何使用ORDER BY对查询结果进行排序，包括单列排序、多列排序、升降序控制等。然后我们还会学习如何使用LIMIT和OFFSET实现分页功能，以及在大数据量情况下如何优化分页性能。

准备好了吗？让我们开始学习排序与分页的奥秘吧！

## [4.1 ORDER BY 基础与多列排序](#_4-1-order-by-基础与多列排序)

ORDER BY子句用于对查询结果进行排序，它可以让原本无序的数据变得井井有条。最基本的用法是按照单个列进行排序，我们可以指定升序（ASC）或降序（DESC）。

让我们继续使用熟悉的products表来演示排序功能。为了确保数据完整，我们重新创建一下这个表并添加一些数据：

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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入示例数据
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

最基本的排序是按照价格从低到高排列。默认情况下，ORDER BY使用升序排列，我们可以省略ASC关键字：

```
SELECT name, category, price
FROM products
ORDER BY price;
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| 小米手环     | 智能穿戴  |   299.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
| AirPods Pro  | 耳机      |  1899.00 |
| 小米13       | 手机      |  3999.00 |
| 华为P60      | 手机      |  4999.00 |
| iPad Air     | 平板      |  4599.00 |
| iPhone 15    | 手机      |  5999.00 |
| Surface Pro  | 平板      |  6999.00 |
| ThinkPad X1  | 笔记本    |  8999.00 |
| MacBook Pro  | 笔记本    | 12999.00 |
+--------------+-----------+----------+
10 rows in set (0.00 sec)
```

如果我们想按照价格从高到低排列，需要明确指定DESC关键字：

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
| iPad Air     | 平板      |  4599.00 |
| 华为P60      | 手机      |  4999.00 |
| 小米13       | 手机      |  3999.00 |
| AirPods Pro  | 耳机      |  1899.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
| 小米手环     | 智能穿戴  |   299.00 |
+--------------+-----------+----------+
10 rows in set (0.00 sec)
```

在实际业务中，我们经常需要按照多个列进行排序。比如，我们想先按照类别排序，然后在同一类别内按照价格从高到低排序：

```
SELECT name, category, price
FROM products
ORDER BY category, price DESC;
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| iPhone 15    | 手机      |  5999.00 |
| 华为P60      | 手机      |  4999.00 |
| 小米13       | 手机      |  3999.00 |
| ThinkPad X1  | 笔记本    |  8999.00 |
| MacBook Pro  | 笔记本    | 12999.00 |
| iPad Air     | 平板      |  4599.00 |
| Surface Pro  | 平板      |  6999.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
| 小米手环     | 智能穿戴  |   299.00 |
| AirPods Pro  | 耳机      |  1899.00 |
+--------------+-----------+----------+
10 rows in set (0.00 sec)
```

在这个查询中，数据首先按照类别升序排列（默认），然后在每个类别内部按照价格降序排列。你可以看到手机类别中iPhone 15价格最高排在前面，笔记本类别中MacBook Pro价格最高排在前面。

多列排序在实际业务中有很多应用场景。比如，在电商网站中，我们可能想按照销量排序，销量相同的按照价格排序，价格再相同的按照上架时间排序。这样的多级排序能够让数据展示更加合理和用户友好。

在排序时，NULL值的处理是一个需要注意的问题。在MySQL中，NULL值被认为是最小的值，在升序排序时会排在最前面，在降序排序时会排在最后面。让我们添加一些NULL值来演示：

```
-- 添加一些NULL值用于演示
UPDATE products SET price = NULL WHERE name = 'ThinkPad X1';
UPDATE products SET sales_count = NULL WHERE name = 'iPad Air';
```

现在我们按照价格排序：

```
SELECT name, price
FROM products
ORDER BY price;
```

执行结果：

```
+--------------+----------+
| name         | price    |
+--------------+----------+
| ThinkPad X1  |     NULL |
| 小米手环     |   299.00 |
| 华为手表     |  1299.00 |
| AirPods Pro  |  1899.00 |
| 小米13       |  3999.00 |
| 华为P60      |  4999.00 |
| iPad Air     |  4599.00 |
| iPhone 15    |  5999.00 |
| Surface Pro  |  6999.00 |
| MacBook Pro  | 12999.00 |
+--------------+----------+
10 rows in set (0.00 sec)
```

可以看到，ThinkPad X1的价格为NULL，排在最前面。如果我们想让NULL值排在最后面，可以使用COALESCE函数：

```
SELECT name, price
FROM products
ORDER BY COALESCE(price, 999999);
```

这个查询会将NULL值当作一个很大的数来处理，从而排在最后面。

ORDER BY还可以与表达式一起使用。比如，我们可以按照产品的总价值（价格×库存）来排序：

```
SELECT name, price, stock, price * stock AS total_value
FROM products
ORDER BY total_value DESC;
```

执行结果：

```
+--------------+----------+-------+-------------+
| name         | price    | stock | total_value |
+--------------+----------+-------+-------------+
| iPhone 15    |  5999.00 |   100 |   599900.00 |
| 小米13       |  3999.00 |   150 |   599850.00 |
| MacBook Pro  | 12999.00 |    50 |   649950.00 |
| 小米手环     |   299.00 |   300 |    89700.00 |
| iPad Air     |  4599.00 |   120 |   551880.00 |
| 华为P60      |  4999.00 |    80 |   399920.00 |
| Surface Pro  |  6999.00 |    40 |   279960.00 |
| 华为手表     |  1299.00 |    90 |   116910.00 |
| AirPods Pro  |  1899.00 |   200 |   379800.00 |
| ThinkPad X1  |     NULL |    30 |        NULL |
+--------------+----------+-------+-------------+
10 rows in set (0.00 sec)
```

注意这里ThinkPad X1的总价值为NULL，因为它的价格是NULL。如果我们想避免这种情况，可以使用COALESCE：

```
SELECT name, price, stock, COALESCE(price, 0) * stock AS total_value
FROM products
ORDER BY total_value DESC;
```

这样NULL值就会被当作0来处理。

## [4.2 LIMIT / OFFSET 分页](#_4-2-limit-offset-分页)

当数据量很大时，我们通常不会一次性显示所有数据，而是分页展示。这就是分页技术的用武之地。在MySQL中，我们可以使用LIMIT和OFFSET来实现分页功能。

LIMIT用于限制返回的记录数，OFFSET用于指定从哪条记录开始返回。最简单的用法是只使用LIMIT，比如我们想查看价格最高的前5个产品：

```
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5;
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| MacBook Pro  | 笔记本    | 12999.00 |
| Surface Pro  | 平板      |  6999.00 |
| iPhone 15    | 手机      |  5999.00 |
| 华为P60      | 手机      |  4999.00 |
| iPad Air     | 平板      |  4599.00 |
+--------------+-----------+----------+
5 rows in set (0.00 sec)
```

这个查询返回了价格最高的5个产品。

如果我们想查看价格排名第6到第10的产品，就需要使用OFFSET：

```
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5 OFFSET 5;
```

执行结果：

```
+--------------+-----------+----------+
| name         | category  | price    |
+--------------+-----------+----------+
| 小米13       | 手机      |  3999.00 |
| AirPods Pro  | 耳机      |  1899.00 |
| 华为手表     | 智能穿戴  |  1299.00 |
| 小米手环     | 智能穿戴  |   299.00 |
| ThinkPad X1  | 笔记本    |     NULL |
+--------------+-----------+----------+
5 rows in set (0.00 sec)
```

这个查询跳过了前5条记录，返回了接下来的5条记录。

分页的通用公式是：LIMIT 每页记录数 OFFSET (页码-1)×每页记录数。比如，每页显示3条记录，要查看第2页：

```
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 3 OFFSET 3;
```

执行结果：

```
+------------+-----------+----------+
| name       | category  | price    |
+------------+-----------+----------+
| iPhone 15  | 手机      |  5999.00 |
| 华为P60     | 手机      |  4999.00 |
| iPad Air   | 平板      |  4599.00 |
+------------+-----------+----------+
3 rows in set (0.00 sec)
```

MySQL还提供了一种更简洁的写法：LIMIT offset, count。上面的查询可以写成：

```
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 3, 3;
```

两种写法的效果完全相同，选择哪种主要看个人偏好。

分页技术在Web应用中非常常见。想象一下，当你在电商网站浏览商品时，通常不会一次性显示所有商品，而是每页显示20个或50个商品，你可以通过点击页码来查看不同页的商品。这就是分页的典型应用场景。

然而，传统的LIMIT OFFSET分页在数据量很大时会有性能问题。当OFFSET值很大时，比如LIMIT 20 OFFSET 100000，数据库仍然需要扫描前100020条记录，然后丢弃前100000条，只返回最后20条。这会导致查询性能随着页码的增加而下降。

对于大数据量的分页，有几种优化思路。一种是基于游标的分页，即记住上一页最后一条记录的某个值（比如ID或时间戳），然后从该值开始查询下一页：

```
-- 假设上一页最后一条记录的ID是50
SELECT name, category, price
FROM products
WHERE id > 50
ORDER BY id
LIMIT 20;
```

这种分页方式性能很好，因为它不需要扫描和丢弃大量记录。缺点是不能跳页访问，只能一页一页地翻。

另一种优化方法是使用子查询，先找到要显示页的ID范围，然后再查询详细数据：

```
SELECT name, category, price
FROM products
WHERE id IN (
    SELECT id
    FROM products
    ORDER BY id
    LIMIT 20 OFFSET 100000
);
```

这种方法在某些情况下性能更好，但具体效果取决于数据库的优化器。

在实际应用中，我们需要根据具体场景选择合适的分页策略。对于小数据量（几万条记录），传统的LIMIT OFFSET分页就足够了。对于大数据量（几百万条记录），则需要考虑使用基于游标的分页或其他优化方法。

分页时通常还需要获取总记录数，用于计算总页数。这可以通过单独的查询来实现：

```
SELECT COUNT(*) FROM products;
```

然后在应用层计算总页数：总页数 = CEILING(总记录数 / 每页记录数)。

## [练习题](#练习题)

### [练习1：多列排序](#练习1-多列排序)

查询products表中的产品信息，先按照类别升序排列，同一类别内按照销量降序排列，显示产品名称、类别和销量。

查看答案

```
SELECT name, category, sales_count
FROM products
ORDER BY category, sales_count DESC;
```

### [练习2：分页查询](#练习2-分页查询)

查询products表中价格最高的第3到第7个产品，显示产品名称、类别和价格。

查看答案

```
SELECT name, category, price
FROM products
ORDER BY price DESC
LIMIT 5 OFFSET 2;
```

### [练习3：带条件的排序分页](#练习3-带条件的排序分页)

查询products表中所有手机和笔记本类别产品，按照价格升序排列，每页显示4条记录，获取第2页的数据。

查看答案

```
SELECT name, category, price
FROM products
WHERE category IN ('手机', '笔记本')
ORDER BY price
LIMIT 4 OFFSET 4;
```

## [常见坑](#常见坑)

### [坑1：在ORDER BY中使用列别名](#坑1-在order-by中使用列别名)

很多人会尝试在ORDER BY中使用列别名，但实际上这是允许的，与WHERE子句不同。ORDER BY是在SELECT之后执行的，所以可以使用别名。

**正确用法**：

```
SELECT name, price * stock AS total_value
FROM products
ORDER BY total_value DESC;
```

这个查询能够正常工作，因为ORDER BY在SELECT之后执行。

### [坑2：大数据量分页的性能问题](#坑2-大数据量分页的性能问题)

当使用LIMIT OFFSET进行分页时，如果OFFSET值很大，会导致性能问题。数据库需要扫描并丢弃前面的所有记录。

**优化方法**：

```
-- 使用基于游标的分页
SELECT name, category, price
FROM products
WHERE id > last_seen_id
ORDER BY id
LIMIT 20;
```

或者限制最大页码，不允许用户跳转到很远的页码。

### [坑3：分页数据不一致](#坑3-分页数据不一致)

如果在两次查询之间有数据被插入或删除，可能导致分页数据不一致或重复显示。比如，用户查看第1页时，某条记录被删除，然后查看第2页时，可能会看到与第1页重复的数据。

**解决方法**：

- 在事务中执行分页查询
- 使用基于游标的分页
- 对于实时性要求不高的场景，可以接受一定程度的数据不一致

## [速记卡](#速记卡)

- **ORDER BY**：用于对查询结果进行排序，默认升序（ASC）
- **DESC**：指定降序排列，必须显式指定
- **多列排序**：按照列的优先级依次排序，先按第一列排，相同再按第二列排
- **NULL值排序**：NULL被认为是最小值，升序时在前，降序时在后
- **LIMIT**：限制返回的记录数
- **OFFSET**：指定跳过的记录数，从0开始计数
- **分页公式**：LIMIT page\_size OFFSET (page-1)\*page\_size
- **大数据量分页**：基于游标的分页性能更好，但不能跳页访问
- **稳定性**：相同值的相对顺序在排序中保持不变

## [章节总结](#章节总结)

在这一章中，我们学习了如何对查询结果进行排序和分页，这是数据展示中非常重要的技术。ORDER BY子句让原本无序的数据变得井井有条，我们可以按照单个列或多个列进行排序，控制升序或降序，还可以处理NULL值的排序问题。

多列排序在实际业务中有很多应用场景，比如先按类别排序，再按价格或销量排序。理解多列排序的优先级对于构建合理的排序逻辑非常重要。同时，我们也学习了如何使用表达式进行排序，比如按照计算出的总价值排序。

分页技术让大数据量的展示变得可行和用户友好。通过LIMIT和OFFSET，我们可以实现基本的分页功能，让用户能够逐页浏览数据。然而，我们也认识到传统分页方式在大数据量时的性能问题，以及基于游标的分页等优化思路。

掌握了排序和分页技术，你就能够构建更加用户友好的数据展示界面。无论是在Web应用、报表系统还是数据分析工具中，这些技术都是不可或缺的。下一章，我们将学习如何向数据库中插入数据，进一步完善我们的SQL技能。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [04｜排序与分页：结果怎么排序与分页？](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#_04-排序与分页-结果怎么排序与分页)
- [4.1 ORDER BY 基础与多列排序](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#_4-1-order-by-基础与多列排序)
- [4.2 LIMIT / OFFSET 分页](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#_4-2-limit-offset-分页)
- [练习题](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#练习题)
- [练习1：多列排序](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#练习1-多列排序)
- [练习2：分页查询](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#练习2-分页查询)
- [练习3：带条件的排序分页](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#练习3-带条件的排序分页)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#常见坑)
- [坑1：在ORDER BY中使用列别名](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#坑1-在order-by中使用列别名)
- [坑2：大数据量分页的性能问题](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#坑2-大数据量分页的性能问题)
- [坑3：分页数据不一致](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#坑3-分页数据不一致)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/04-order-by-pagination.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
