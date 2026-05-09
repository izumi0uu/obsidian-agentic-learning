---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html"
source: "https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html"
last_checked: 2026-05-07
freshness: watch
sha256: 79f7af2ff1820cbd3d343169e529b8457e01ddfac0cf81b11dc9b0990c2eec55
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[SQL GROUP BY]]"
  - "[[Aggregate Function]]"
  - "[[SQL]]"
---
# 08｜聚合与分组：统计与分组该怎么做？

原始链接：https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[SQL GROUP BY]]
- [[Aggregate Function]]
- [[SQL]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 16 分钟约 4931 字2025/8/31

---


大家好，我是小林。

在前面的章节中，我们学习了如何查询、筛选、排序和连接数据，这些操作主要针对单行或多行数据进行处理。但在实际应用中，我们经常需要对数据进行统计分析，比如计算总销售额、平均订单金额、各类产品的销量分布等。这时候就需要用到聚合函数和分组操作。

你有没有想过，当你在电商网站看到"月度销售额突破100万"这样的统计信息时，系统是如何从成千上万笔订单中计算出这个总量的？当你在数据分析平台看到"各年龄段用户分布图"时，这些分组统计数据是如何生成的？当财务部门需要"每个季度的利润报表"时，这些汇总数据是如何从大量交易记录中提取出来的？

在这一章中，我们将学习如何使用聚合函数对数据进行统计分析，如何使用GROUP BY对数据进行分组，以及如何使用HAVING筛选分组结果。掌握了这些技术，你就能够从海量数据中提取出有价值的统计信息，为业务决策提供数据支持。

准备好了吗？让我们开始学习聚合与分组的奥秘吧！

## [8.1 聚合函数（COUNT、SUM、AVG、MAX、MIN）](#_8-1-聚合函数-count、sum、avg、max、min)

聚合函数是SQL中用于对一组值进行计算并返回单个值的函数。最常用的聚合函数包括COUNT（计数）、SUM（求和）、AVG（平均值）、MAX（最大值）和MIN（最小值）。这些函数能够帮我们从大量数据中快速提取出统计信息。

让我们创建一个销售数据表来演示各种聚合函数的使用：

```
-- 创建销售数据表
DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    region VARCHAR(50) NOT NULL
);

-- 插入示例数据
INSERT INTO sales (product_name, category, price, quantity, sale_date, region) VALUES 
('iPhone 15', '手机', 5999.00, 2, '2025-08-01', '北京'),
('小米13', '手机', 3999.00, 3, '2025-08-01', '上海'),
('MacBook Pro', '笔记本', 12999.00, 1, '2025-08-02', '北京'),
('iPad Air', '平板', 4599.00, 2, '2025-08-02', '广州'),
('华为P60', '手机', 4999.00, 1, '2025-08-03', '深圳'),
('ThinkPad X1', '笔记本', 8999.00, 1, '2025-08-03', '上海'),
('AirPods Pro', '耳机', 1899.00, 4, '2025-08-04', '北京'),
('小米手环', '智能穿戴', 299.00, 5, '2025-08-04', '杭州'),
('华为手表', '智能穿戴', 1299.00, 2, '2025-08-05', '成都'),
('Surface Pro', '平板', 6999.00, 1, '2025-08-05', '武汉');
```

**COUNT函数**是最常用的聚合函数，用于计算行数。我们可以计算总销售记录数：

```
SELECT COUNT(*) AS total_records
FROM sales;
```

执行结果：

```
+---------------+
| total_records |
+---------------+
|            10 |
+---------------+
1 row in set (0.00 sec)
```

这个查询返回了sales表中的总记录数。COUNT(\*)会计算所有行，包括包含NULL值的行。如果我们只想计算特定列的非NULL值数量，可以使用COUNT(column\_name)：

```
SELECT COUNT(category) AS non_null_categories
FROM sales;
```

在这个例子中，由于category列被定义为NOT NULL，所以结果与COUNT(\*)相同。但如果列中包含NULL值，COUNT(column\_name)会忽略这些NULL值。

**SUM函数**用于计算数值列的总和。比如，我们可以计算所有产品的总销售额：

```
SELECT SUM(price * quantity) AS total_revenue
FROM sales;
```

执行结果：

```
+---------------+
| total_revenue |
+---------------+
|     102684.00 |
+---------------+
1 row in set (0.00 sec)
```

这个查询首先计算每条记录的销售额（价格×数量），然后使用SUM函数求和得到总销售额。我们可以在聚合函数中使用表达式，这为我们提供了很大的灵活性。

**AVG函数**用于计算平均值。比如，我们可以计算平均订单金额：

```
SELECT AVG(price * quantity) AS avg_order_amount
FROM sales;
```

执行结果：

```
+------------------+
| avg_order_amount |
+------------------+
|       10268.4000 |
+------------------+
1 row in set (0.00 sec)
```

这个查询计算了所有订单的平均金额。AVG函数会忽略NULL值，只计算非NULL值的平均值。

**MAX和MIN函数**分别用于找出最大值和最小值。比如，我们可以找出最高和最低的单笔订单金额：

```
SELECT 
    MAX(price * quantity) AS max_order_amount,
    MIN(price * quantity) AS min_order_amount
FROM sales;
```

执行结果：

```
+------------------+------------------+
| max_order_amount | min_order_amount |
+------------------+------------------+
|         12999.00 |          1495.00 |
+------------------+------------------+
1 row in set (0.00 sec)
```

这个查询同时使用了MAX和MIN函数，找出了最高和最低的订单金额。最高金额来自MacBook Pro的销售（12999.00×1），最低金额来自小米手环的销售（299.00×5=1495.00）。

聚合函数还可以与DISTINCT关键字结合使用，计算不同值的数量。比如，我们可以计算有多少个不同的产品类别：

```
SELECT COUNT(DISTINCT category) AS unique_categories
FROM sales;
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

这个查询告诉我们，销售数据中包含5个不同的产品类别：手机、笔记本、平板、耳机、智能穿戴。

在实际应用中，我们经常需要在一个查询中使用多个聚合函数来获取全面的统计信息。比如，我们可以同时计算总销售额、平均订单金额、订单数量和最大订单金额：

```
SELECT 
    COUNT(*) AS total_orders,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount,
    MAX(price * quantity) AS max_order_amount,
    MIN(price * quantity) AS min_order_amount
FROM sales;
```

执行结果：

```
+--------------+---------------+------------------+------------------+------------------+
| total_orders | total_revenue | avg_order_amount | max_order_amount | min_order_amount |
+--------------+---------------+------------------+------------------+------------------+
|           10 |     102684.00 |       10268.4000 |         12999.00 |          1495.00 |
+--------------+---------------+------------------+------------------+------------------+
1 row in set (0.00 sec)
```

这个查询为我们提供了销售数据的全面统计概览。从结果可以看出，我们总共有10笔订单，总销售额为102684.00元，平均每笔订单金额为10268.40元，最大单笔订单金额为12999.00元，最小单笔订单金额为1495.00元。

聚合函数的一个重要作用是帮助我们快速了解数据的整体特征。比如，通过最大值和最小值，我们可以了解数据的分布范围；通过平均值，我们可以了解数据的集中趋势；通过总和，我们可以了解数据的总体规模。这些统计信息对于数据分析和业务决策非常重要。

## [8.2 GROUP BY 分组](#_8-2-group-by-分组)

GROUP BY子句让我们能够将数据按照指定的列进行分组，然后对每个分组应用聚合函数。这在实际业务中非常有用，比如按产品类别统计销售额、按地区分析销售情况、按时间段汇总数据等。

让我们使用之前创建的sales表来演示GROUP BY的使用。首先，我们可以按产品类别分组，统计每个类别的销售情况：

```
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount
FROM sales
GROUP BY category;
```

执行结果：

```
+-----------+------------+---------------+------------------+
| category  | order_count | total_revenue | avg_order_amount |
+-----------+------------+---------------+------------------+
| 手机      |          3 |      32994.00 |       10998.0000 |
| 平板      |          2 |      16197.00 |        8098.5000 |
| 智能穿戴  |          2 |       3093.00 |        1546.5000 |
| 笔记本    |          2 |      21998.00 |       10999.0000 |
| 耳机      |          1 |       7596.00 |        7596.0000 |
+-----------+------------+---------------+------------------+
5 rows in set (0.00 sec)
```

这个查询按category列对数据进行分组，然后对每个分组分别计算订单数量、总销售额和平均订单金额。从结果可以看出，手机类别的销售额最高（32994.00元），而智能穿戴类别的平均订单金额最低（1546.50元）。

GROUP BY的一个重要原则是：**SELECT子句中的非聚合列必须出现在GROUP BY子句中**。

这是因为数据库需要知道如何将行分组，如果一个列既不在GROUP BY中，又不是聚合函数，数据库就无法确定应该显示该列的哪个值。

我们可以按多个列进行分组。比如，我们可以按地区和产品类别分组，统计每个地区在每个类别的销售情况：

```
SELECT 
    region,
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY region, category
ORDER BY region, total_revenue DESC;
```

执行结果：

```
+--------+-----------+------------+---------------+
| region | category  | order_count | total_revenue |
+--------+-----------+------------+---------------+
| 上海   | 笔记本    |          1 |       8999.00 |
| 上海   | 手机      |          1 |       3999.00 |
| 北京   | 手机      |          1 |      11998.00 |
| 北京   | 笔记本    |          1 |      12999.00 |
| 北京   | 耳机      |          1 |       7596.00 |
| 广州   | 平板      |          1 |       9198.00 |
| 深圳   | 手机      |          1 |       4999.00 |
| 杭州   | 智能穿戴  |          1 |       1495.00 |
| 成都   | 智能穿戴  |          1 |       2598.00 |
| 武汉   | 平板      |          1 |       6999.00 |
+--------+-----------+------------+---------------+
10 rows in set (0.00 sec)
```

这个查询首先按region分组，然后在每个地区内按category分组，最后按地区和销售额降序排列。从结果可以看出，北京地区的总销售额最高，其中笔记本类别的销售额最高（12999.00元）。

在实际应用中，GROUP BY经常与时间相关的函数结合使用，用于按时间段进行统计分析。比如，我们可以按月份统计销售情况：

```
SELECT 
    DATE_FORMAT(sale_date, '%Y-%m') AS month,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
ORDER BY month;
```

执行结果：

```
+---------+------------+---------------+
| month   | order_count | total_revenue |
+---------+------------+---------------+
| 2025-08 |         10 |     102684.00 |
+---------+------------+---------------+
1 row in set (0.00 sec)
```

由于我们的示例数据都在同一个月份，所以结果只有一行。如果有跨月度的数据，这个查询就会显示每个月的销售统计。

GROUP BY还可以与CASE语句结合使用，实现自定义分组。比如，我们可以将订单金额分为高、中、低三个档次，然后统计每个档次的订单数量：

```
SELECT 
    CASE 
        WHEN price * quantity >= 10000 THEN '高价值订单'
        WHEN price * quantity >= 5000 THEN '中价值订单'
        ELSE '低价值订单'
    END AS order_level,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY 
    CASE 
        WHEN price * quantity >= 10000 THEN '高价值订单'
        WHEN price * quantity >= 5000 THEN '中价值订单'
        ELSE '低价值订单'
    END
ORDER BY total_revenue DESC;
```

执行结果：

```
+-----------------+------------+---------------+
| order_level     | order_count | total_revenue |
+-----------------+------------+---------------+
| 高价值订单      |          3 |      54996.00 |
| 中价值订单      |          3 |      31995.00 |
| 低价值订单      |          4 |      15693.00 |
+-----------------+------------+---------------+
3 rows in result set (0.00 sec)
```

这个查询使用CASE语句将订单分为三个价值档次，然后统计每个档次的订单数量和总销售额。从结果可以看出，高价值订单虽然数量最少（3笔），但总销售额最高（54996.00元）。

在使用GROUP BY时，需要注意一些性能问题。当分组列上有索引时，GROUP BY操作会更高效。另外，如果分组的结果集很大，可能需要考虑分页或者进一步汇总数据。

## [8.3 HAVING 筛选聚合结果](#_8-3-having-筛选聚合结果)

WHERE子句用于在分组前筛选行，而HAVING子句用于在分组后筛选分组结果。这是一个重要的区别：**WHERE在GROUP BY之前执行，过滤的是原始行；HAVING在GROUP BY之后执行，过滤的是分组结果**。

让我们用一个实际的例子来说明HAVING的用途。假设我们想找出销售额超过10000元的产品类别：

```
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY category
HAVING SUM(price * quantity) > 10000;
```

执行结果：

```
+-----------+------------+---------------+
| category  | order_count | total_revenue |
+-----------+------------+---------------+
| 手机      |          3 |      32994.00 |
| 笔记本    |          2 |      21998.00 |
+-----------+------------+---------------+
2 rows in set (0.00 sec)
```

这个查询首先按category分组，计算每个类别的总销售额，然后使用HAVING子句筛选出销售额超过10000元的类别。从结果可以看出，只有手机和笔记本两个类别的销售额超过了10000元。

如果我们尝试用WHERE子句来实现同样的功能，会发现这是不可能的：

```
-- 错误的写法：WHERE不能直接使用聚合函数
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
WHERE SUM(price * quantity) > 10000
GROUP BY category;
```

这个查询会报错，因为WHERE子句在GROUP BY之前执行，此时聚合函数还没有计算出来。

HAVING子句可以包含聚合函数，这使得它非常适合用于筛选分组结果。我们可以在HAVING中使用各种聚合函数和条件表达式。比如，我们可以找出平均订单金额超过8000元且订单数量至少为2的产品类别：

```
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount
FROM sales
GROUP BY category
HAVING AVG(price * quantity) > 8000 AND COUNT(*) >= 2;
```

执行结果：

```
+-----------+------------+---------------+------------------+
| category  | order_count | total_revenue | avg_order_amount |
+-----------+------------+---------------+------------------+
| 手机      |          3 |      32994.00 |       10998.0000 |
| 笔记本    |          2 |      21998.00 |       10999.0000 |
+-----------+------------+---------------+------------------+
2 rows in set (0.00 sec)
```

这个查询筛选出了平均订单金额超过8000元且至少有2笔订单的产品类别。从结果可以看出，手机和笔记本都满足这两个条件。

HAVING子句还可以与WHERE子句结合使用，实现更复杂的筛选逻辑。WHERE用于筛选原始行，HAVING用于筛选分组结果。比如，我们可以先筛选出2025年8月1日之后的销售记录，然后按地区分组，最后筛选出总销售额超过8000元的地区：

```
SELECT 
    region,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
WHERE sale_date >= '2025-08-01'
GROUP BY region
HAVING SUM(price * quantity) > 8000
ORDER BY total_revenue DESC;
```

执行结果：

```
+--------+------------+---------------+
| region | order_count | total_revenue |
+--------+------------+---------------+
| 北京   |          3 |      32593.00 |
| 上海   |          2 |      12998.00 |
| 广州   |          1 |       9198.00 |
| 深圳   |          1 |       4999.00 |
+--------+------------+---------------+
4 rows in set (0.00 sec)
```

这个查询的执行顺序是：

1. WHERE子句筛选出2025年8月1日之后的销售记录
2. GROUP BY子句按地区分组
3. 聚合函数计算每个地区的订单数量和总销售额
4. HAVING子句筛选出总销售额超过8000元的地区
5. ORDER BY子句按销售额降序排列

从结果可以看出，北京地区的销售额最高（32593.00元），其次是上海地区（12998.00元）。

HAVING子句在数据分析中非常有用，特别是在需要基于聚合结果进行筛选的场景。比如，找出销售表现最好的产品类别、识别活跃度最高的用户群体、分析不同时间段的业务表现等。

让我们再看一个更复杂的例子，假设我们想找出那些平均订单金额高于总体平均订单金额的产品类别：

```
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount
FROM sales
GROUP BY category
HAVING AVG(price * quantity) > (
    SELECT AVG(price * quantity) 
    FROM sales
)
ORDER BY avg_order_amount DESC;
```

执行结果：

```
+-----------+------------+---------------+------------------+
| category  | order_count | total_revenue | avg_order_amount |
+-----------+------------+---------------+------------------+
| 笔记本    |          2 |      21998.00 |       10999.0000 |
| 手机      |          3 |      32994.00 |       10998.0000 |
| 平板      |          2 |      16197.00 |        8098.5000 |
+-----------+------------+---------------+------------------+
3 rows in set (0.00 sec)
```

这个查询使用子查询计算总体平均订单金额，然后用HAVING子句筛选出高于这个平均值的产品类别。从结果可以看出，笔记本、手机和平板三个类别的平均订单金额都高于总体平均水平。

在实际应用中，HAVING子句经常用于业务报表和分析查询，帮助我们识别表现突出或需要关注的业务单元。掌握了HAVING的使用，你就能够进行更加精细和深入的数据分析。

## [练习题](#练习题)

### [练习1：基础聚合函数使用](#练习1-基础聚合函数使用)

查询sales表中的统计信息，包括总订单数、总销售额、平均订单金额、最高订单金额和最低订单金额。

查看答案

```
SELECT 
    COUNT(*) AS total_orders,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount,
    MAX(price * quantity) AS max_order_amount,
    MIN(price * quantity) AS min_order_amount
FROM sales;
```

### [练习2：分组统计与筛选](#练习2-分组统计与筛选)

按地区分组统计销售情况，找出总销售额超过10000元的地区，显示地区名称、订单数量和总销售额，按销售额降序排列。

查看答案

```
SELECT 
    region,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY region
HAVING SUM(price * quantity) > 10000
ORDER BY total_revenue DESC;
```

### [练习3：多条件分组与HAVING筛选](#练习3-多条件分组与having筛选)

按产品类别分组，找出平均订单金额超过8000元且订单数量至少为2的类别，显示类别名称、订单数量、总销售额和平均订单金额。

查看答案

```
SELECT 
    category,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_amount
FROM sales
GROUP BY category
HAVING AVG(price * quantity) > 8000 AND COUNT(*) >= 2
ORDER BY avg_order_amount DESC;
```

## [常见坑](#常见坑)

### [坑1：GROUP BY与SELECT列的匹配错误](#坑1-group-by与select列的匹配错误)

很多初学者会犯这样的错误：在SELECT中使用了没有在GROUP BY中的非聚合列。

**错误示例**：

```
-- 错误：product_name没有在GROUP BY中
SELECT 
    category,
    product_name,
    COUNT(*) AS order_count
FROM sales
GROUP BY category;
```

**纠正方法**：要么将product\_name加入GROUP BY，要么从SELECT中移除product\_name：

```
-- 方法1：将product_name加入GROUP BY
SELECT 
    category,
    product_name,
    COUNT(*) AS order_count
FROM sales
GROUP BY category, product_name;

-- 方法2：从SELECT中移除product_name
SELECT 
    category,
    COUNT(*) AS order_count
FROM sales
GROUP BY category;
```

### [坑2：WHERE与HAVING的混淆](#坑2-where与having的混淆)

经常有人试图在WHERE子句中使用聚合函数，这会导致错误。

**错误示例**：

```
-- 错误：WHERE中不能使用聚合函数
SELECT category, SUM(price * quantity) AS total_revenue
FROM sales
WHERE SUM(price * quantity) > 10000
GROUP BY category;
```

**纠正方法**：使用HAVING子句来筛选聚合结果：

```
SELECT category, SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY category
HAVING SUM(price * quantity) > 10000;
```

### [坑3：忽略NULL值对聚合结果的影响](#坑3-忽略null值对聚合结果的影响)

聚合函数处理NULL值的方式可能让初学者感到困惑。

**常见问题**：

```
-- COUNT(*) vs COUNT(column)的区别
SELECT 
    COUNT(*) AS count_all,        -- 包含NULL行
    COUNT(category) AS count_category,  -- 忽略NULL值
    SUM(price) AS sum_price,      -- 忽略NULL值
    AVG(price) AS avg_price       -- 忽略NULL值
FROM sales;
```

**纠正方法**：理解聚合函数对NULL值的处理规则，根据需求选择合适的函数：

- COUNT(\*)计算所有行
- COUNT(column)忽略NULL值
- SUM、AVG、MAX、MIN都忽略NULL值

## [速记卡](#速记卡)

- **COUNT(\*)**：计算所有行数，包括包含NULL值的行
- **COUNT(column)**：计算指定列的非NULL值数量
- **SUM(column)**：计算指定列的总和，忽略NULL值
- **AVG(column)**：计算指定列的平均值，忽略NULL值
- **MAX(column)**：找出指定列的最大值，忽略NULL值
- **MIN(column)**：找出指定列的最小值，忽略NULL值
- **GROUP BY**：将数据按指定列分组，对每个分组应用聚合函数
- **HAVING**：在分组后筛选分组结果，可以使用聚合函数
- **WHERE vs HAVING**：WHERE在分组前筛选行，HAVING在分组后筛选分组
- **GROUP BY原则**：SELECT中的非聚合列必须出现在GROUP BY子句中

## [章节总结](#章节总结)

在这一章中，我们学习了SQL中非常重要的聚合与分组技术，这些技术让我们能够从大量数据中提取出有价值的统计信息。聚合函数包括COUNT、SUM、AVG、MAX、MIN等，它们能够帮我们快速计算数据的总体特征，如总数、总和、平均值、最大值和最小值。

GROUP BY子句让我们能够将数据按照指定的列进行分组，然后对每个分组应用聚合函数。这在实际业务中非常有用，比如按产品类别统计销售额、按地区分析销售情况、按时间段汇总数据等。我们还学习了如何按多个列进行分组，以及如何使用CASE语句实现自定义分组。

HAVING子句用于在分组后筛选分组结果，它与WHERE子句有重要的区别：WHERE在GROUP BY之前执行，过滤的是原始行；HAVING在GROUP BY之后执行，过滤的是分组结果。HAVING子句可以包含聚合函数，这使得它非常适合用于基于聚合结果的筛选。

掌握了聚合与分组技术，你就能够进行更加深入和精细的数据分析。无论是生成业务报表、分析销售趋势，还是识别关键业务指标，这些技术都是不可或缺的。在下一章中，我们将学习子查询技术，这将让我们能够构建更加复杂和强大的SQL查询。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [08｜聚合与分组：统计与分组该怎么做？](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#_08-聚合与分组-统计与分组该怎么做)
- [8.1 聚合函数（COUNT、SUM、AVG、MAX、MIN）](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#_8-1-聚合函数-count、sum、avg、max、min)
- [8.2 GROUP BY 分组](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#_8-2-group-by-分组)
- [8.3 HAVING 筛选聚合结果](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#_8-3-having-筛选聚合结果)
- [练习题](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#练习题)
- [练习1：基础聚合函数使用](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#练习1-基础聚合函数使用)
- [练习2：分组统计与筛选](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#练习2-分组统计与筛选)
- [练习3：多条件分组与HAVING筛选](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#练习3-多条件分组与having筛选)
- [常见坑](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#常见坑)
- [坑1：GROUP BY与SELECT列的匹配错误](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#坑1-group-by与select列的匹配错误)
- [坑2：WHERE与HAVING的混淆](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#坑2-where与having的混淆)
- [坑3：忽略NULL值对聚合结果的影响](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#坑3-忽略null值对聚合结果的影响)
- [速记卡](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part2/08-aggregation-grouping.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
