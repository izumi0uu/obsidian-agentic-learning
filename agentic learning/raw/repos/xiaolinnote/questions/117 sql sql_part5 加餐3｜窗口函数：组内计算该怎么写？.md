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
url: https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html
source: https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html
last_checked: 2026-05-17
freshness: watch
sha256: a2f528236826bea2466b06c9700ebe547d816a73ee8101dcc5fda35e50e75957
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 加餐3｜窗口函数：组内计算该怎么写？

原始链接：https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 加餐3｜窗口函数：组内计算该怎么写？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 16 分钟约 4921 字2025/8/31

---

# [加餐3｜窗口函数：组内计算该怎么写？](#加餐3-窗口函数-组内计算该怎么写)

大家好，我是小林。

在前面的学习中，我们学习了GROUP BY分组统计，它能帮我们计算每个分组的汇总信息。但是你有没有遇到过这样的需求：既要看到每个员工的详细信息，又要知道他们在各自部门的工资排名？或者既要列出每天的销售额，又要计算累计销售额和环比增长？

如果使用GROUP BY，我们会得到每个部门的一行汇总数据，丢失了员工的具体信息。比如，用GROUP BY统计各部门工资情况，我们只能看到"技术部平均工资8000元"，但看不到技术部每个员工的具体工资和排名。

这时候，窗口函数就派上用场了。窗口函数能够在保留每一行明细数据的同时，在相关行集上执行计算。简单来说，**窗口函数 = 保留明细 + 组内计算**。

想象一下，你有一张班级成绩单，GROUP BY就像按学科分组算平均分，你只能看到"数学平均分85分"；而窗口函数就像在成绩单上增加几列，既能看到每个学生的具体成绩，又能看到他们在班级的排名、与平均分的差距等。

在这一章中，我们将学习窗口函数的核心概念、基本语法，以及如何在实际业务中应用窗口函数来解决复杂的分析需求。准备好了吗？让我们一起探索窗口函数的强大功能吧！

## [为什么需要窗口函数？](#为什么需要窗口函数)

让我们通过一个具体的例子来理解为什么需要窗口函数。假设我们有一个员工工资表，想要分析每个部门员工的工资情况：

```
-- 创建员工工资表
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

-- 插入测试数据
INSERT INTO employees (name, department, position, salary, hire_date) VALUES 
('张三', '技术部', '工程师', 12000, '2023-01-15'),
('李四', '技术部', '高级工程师', 18000, '2022-03-10'),
('王五', '技术部', '架构师', 25000, '2021-06-20'),
('赵六', '市场部', '专员', 8000, '2023-02-01'),
('钱七', '市场部', '经理', 15000, '2022-08-15'),
('孙八', '市场部', '总监', 20000, '2021-12-01'),
('周九', '财务部', '会计', 10000, '2023-03-10'),
('吴十', '财务部', '财务经理', 16000, '2022-05-20');
```

### [传统GROUP BY的局限](#传统group-by的局限)

如果我们想统计每个部门的平均工资，使用GROUP BY：

```
SELECT 
    department,
    COUNT(*) as employee_count,
    AVG(salary) as avg_salary,
    MAX(salary) as max_salary
FROM employees
GROUP BY department;
```

执行结果：

```
+------------+----------------+-------------+------------+
| department | employee_count | avg_salary  | max_salary |
+------------+----------------+-------------+------------+
| 技术部     |              3 | 18333.33333 |   25000.00 |
| 市场部     |              3 | 14333.33333 |   20000.00 |
| 财务部     |              2 | 13000.00000 |   16000.00 |
+------------+----------------+-------------+------------+
```

这个结果的问题是：我们丢失了每个员工的具体信息。如果我们想知道"张三在技术部的工资排名如何"，这个查询结果无法告诉我们。

### [窗口函数的解决方案](#窗口函数的解决方案)

使用窗口函数，我们可以既保留每个员工的详细信息，又添加部门内的统计分析：

```
SELECT 
    name,
    department,
    position,
    salary,
    COUNT(*) OVER (PARTITION BY department) as dept_employee_count,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_salary_rank
FROM employees;
```

执行结果：

```
+--------+------------+--------------+--------+-------------------+-----------------+------------------+
| name   | department | position     | salary | dept_employee_count | dept_avg_salary | dept_salary_rank |
+--------+------------+--------------+--------+-------------------+-----------------+------------------+
| 王五   | 技术部     | 架构师      | 25000 |                 3 |     18333.33333 |                1 |
| 李四   | 技术部     | 高级工程师  | 18000 |                 3 |     18333.33333 |                2 |
| 张三   | 技术部     | 工程师      | 12000 |                 3 |     18333.33333 |                3 |
| 孙八   | 市场部     | 总监        | 20000 |                 3 |     14333.33333 |                1 |
| 钱七   | 市场部     | 经理        | 15000 |                 3 |     14333.33333 |                2 |
| 赵六   | 市场部     | 专员        |  8000 |                 3 |     14333.33333 |                3 |
| 吴十   | 财务部     | 财务经理    | 16000 |                 2 |     13000.00000 |                1 |
| 周九   | 财务部     | 会计        | 10000 |                 2 |     13000.00000 |                2 |
+--------+------------+--------------+--------+-------------------+-----------------+------------------+
```

看到了吗？窗口函数让我们既保留了每个员工的详细信息，又增加了部门内的统计数据。现在我们可以清楚地看到：

- 张三的工资是12000元，在技术部排名第3
- 技术部有3个员工，平均工资18333元
- 张三的工资低于部门平均水平

这就是窗口函数的核心价值：**保留明细数据的同时，进行组内计算**。

## [核心概念 vs GROUP BY](#核心概念-vs-group-by)

窗口函数和GROUP BY有什么本质区别呢？让我们通过一个具体的对比来理解。

### [GROUP BY的工作方式](#group-by的工作方式)

GROUP BY会将多行数据压缩成一行，只能返回分组列和聚合函数的结果：

```
-- GROUP BY：多行变一行
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

结果：

```
+------------+-------------+
| department | avg_salary  |
+------------+-------------+
| 技术部     | 18333.33333 |
| 市场部     | 14333.33333 |
| 财务部     | 13000.00000 |
+------------+-------------+
```

### [窗口函数的工作方式](#窗口函数的工作方式)

窗口函数保持行数不变，为每一行添加计算结果：

```
-- 窗口函数：行数不变，添加计算列
SELECT 
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees;
```

结果：

```
+--------+------------+--------+-----------------+
| name   | department | salary | dept_avg_salary |
+--------+------------+--------+-----------------+
| 张三   | 技术部     | 12000 |     18333.33333 |
| 李四   | 技术部     | 18000 |     18333.33333 |
| 王五   | 技术部     | 25000 |     18333.33333 |
| 赵六   | 市场部     |  8000 |     14333.33333 |
| 钱七   | 市场部     | 15000 |     14333.33333 |
| 孙八   | 市场部     | 20000 |     14333.33333 |
| 周九   | 财务部     | 10000 |     13000.00000 |
| 吴十   | 财务部     | 16000 |     13000.00000 |
+--------+------------+--------+-----------------+
```

### [典型应用场景](#典型应用场景)

窗口函数在以下场景特别有用：

**1. 分组内排名**

```
-- 各部门工资排名
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
FROM employees;
```

**2. 累计计算**

```
-- 按入职时间累计计算各部门人数
SELECT 
    name,
    department,
    hire_date,
    COUNT(*) OVER (PARTITION BY department ORDER BY hire_date) as cumulative_hires
FROM employees
ORDER BY department, hire_date;
```

**3. 同比/环比分析**

```
-- 与上一行数据的比较
SELECT 
    name,
    salary,
    LAG(salary, 1) OVER (ORDER BY salary) as prev_salary,
    salary - LAG(salary, 1) OVER (ORDER BY salary) as salary_diff
FROM employees
ORDER BY salary;
```

**4. 移动平均**

```
-- 计算3行移动平均
SELECT 
    name,
    salary,
    AVG(salary) OVER (
        ORDER BY salary 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as moving_avg
FROM employees
ORDER BY salary;
```

## [基本语法](#基本语法)

窗口函数的基本语法结构如下：

```
函数名(表达式) OVER (
    [PARTITION BY 分组列1, 分组列2, ...]
    [ORDER BY 排序列1, 排序列2, ...]
    [ROWS/RANGE 窗口框架]
)
```

让我们分解这个语法：

### [PARTITION BY - 分组子句](#partition-by-分组子句)

`PARTITION BY`类似于GROUP BY，用于将数据分成不同的组。与GROUP BY不同的是，它不会压缩行数，只是为计算定义了窗口范围。

```
-- 按部门分组，计算每个部门的统计信息
SELECT 
    name,
    department,
    salary,
    COUNT(*) OVER (PARTITION BY department) as dept_count,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees;
```

可以按多个列分组：

```
-- 按部门和职位分组
SELECT 
    name,
    department,
    position,
    salary,
    AVG(salary) OVER (PARTITION BY department, position) as dept_pos_avg_salary
FROM employees;
```

### [ORDER BY - 排序子句](#order-by-排序子句)

`ORDER BY`在窗口函数中有两个作用：

1. 为排名函数（如RANK、ROW\_NUMBER）确定排序顺序
2. 为累计函数定义计算方向

```
-- 排名函数需要ORDER BY
SELECT 
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) as overall_rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;
```

```
-- 累计函数使用ORDER BY定义计算方向
SELECT 
    name,
    department,
    salary,
    SUM(salary) OVER (PARTITION BY department ORDER BY salary) as cumulative_salary
FROM employees
ORDER BY department, salary;
```

### [窗口框架 - ROWS/RANGE](#窗口框架-rows-range)

窗口框架定义了在当前行的"窗口"范围内包含哪些行。这是窗口函数最复杂但也最强大的部分。

```
-- 默认窗口框架：RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
SELECT 
    name,
    salary,
    SUM(salary) OVER (ORDER BY salary) as running_total_default
FROM employees
ORDER BY salary;

-- 明确指定窗口框架：从第一行到当前行
SELECT 
    name,
    salary,
    SUM(salary) OVER (
        ORDER BY salary 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_total_rows
FROM employees
ORDER BY salary;

-- 移动平均：前后各一行
SELECT 
    name,
    salary,
    AVG(salary) OVER (
        ORDER BY salary 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as moving_avg_3rows
FROM employees
ORDER BY salary;
```

## [两个最小例子](#两个最小例子)

让我们通过两个实际的例子来深入理解窗口函数的应用。

### [例1：分组排名 - ROW\_NUMBER()](#例1-分组排名-row-number)

假设我们要找出每个部门工资最高的前两名员工：

```
-- 使用窗口函数找出各部门工资前两名的员工
WITH dept_rank AS (
    SELECT 
        name,
        department,
        position,
        salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
    FROM employees
)
SELECT name, department, position, salary
FROM dept_rank
WHERE salary_rank <= 2
ORDER BY department, salary_rank;
```

执行结果：

```
+--------+------------+--------------+--------+
| name   | department | position     | salary |
+--------+------------+--------------+--------+
| 王五   | 技术部     | 架构师      | 25000 |
| 李四   | 技术部     | 高级工程师  | 18000 |
| 孙八   | 市场部     | 总监        | 20000 |
| 钱七   | 市场部     | 经理        | 15000 |
| 吴十   | 财务部     | 财务经理    | 16000 |
| 周九   | 财务部     | 会计        | 10000 |
+--------+------------+--------------+--------+
```

如果没有窗口函数，我们需要用复杂的自连接或子查询来实现这个需求：

```
-- 传统方法：复杂且效率低
SELECT e1.name, e1.department, e1.position, e1.salary
FROM employees e1
WHERE (
    SELECT COUNT(*) 
    FROM employees e2 
    WHERE e2.department = e1.department 
    AND e2.salary >= e1.salary
) <= 2
ORDER BY e1.department, e1.salary DESC;
```

可以看到，窗口函数的写法更加简洁易懂，而且通常性能更好。

### [例2：累计计算与环比 - LAG() + SUM() OVER](#例2-累计计算与环比-lag-sum-over)

假设我们有一个销售数据表，想要分析每日销售的累计情况和环比增长：

```
-- 创建销售数据表
DROP TABLE IF EXISTS daily_sales;
CREATE TABLE daily_sales (
    sale_date DATE,
    product_name VARCHAR(50),
    sales_amount DECIMAL(10,2),
    region VARCHAR(20)
);

-- 插入测试数据
INSERT INTO daily_sales (sale_date, product_name, sales_amount, region) VALUES 
('2025-08-01', 'iPhone 15', 50000, '北京'),
('2025-08-01', '小米13', 30000, '北京'),
('2025-08-02', 'iPhone 15', 45000, '北京'),
('2025-08-02', '小米13', 35000, '北京'),
('2025-08-03', 'iPhone 15', 60000, '北京'),
('2025-08-03', '小米13', 40000, '北京'),
('2025-08-01', 'iPhone 15', 40000, '上海'),
('2025-08-01', '小米13', 25000, '上海'),
('2025-08-02', 'iPhone 15', 55000, '上海'),
('2025-08-02', '小米13', 30000, '上海');
```

现在我们使用窗口函数进行销售分析：

```
SELECT 
    sale_date,
    region,
    product_name,
    sales_amount,
    -- 累计销售额
    SUM(sales_amount) OVER (
        PARTITION BY region, product_name 
        ORDER BY sale_date 
        ROWS UNBOUNDED PRECEDING
    ) as cumulative_sales,
    -- 前一天的销售额
    LAG(sales_amount, 1) OVER (
        PARTITION BY region, product_name 
        ORDER BY sale_date
    ) as prev_day_sales,
    -- 环比增长
    CASE 
        WHEN LAG(sales_amount, 1) OVER (
            PARTITION BY region, product_name 
            ORDER BY sale_date
        ) = 0 THEN NULL
        ELSE (sales_amount - LAG(sales_amount, 1) OVER (
            PARTITION BY region, product_name 
            ORDER BY sale_date
        )) / LAG(sales_amount, 1) OVER (
            PARTITION BY region, product_name 
            ORDER BY sale_date
        ) * 100
    END as growth_rate_percent
FROM daily_sales
ORDER BY region, product_name, sale_date;
```

执行结果：

```
+------------+--------+-------------+--------------+------------------+----------------+---------------------+
| sale_date  | region | product_name | sales_amount | cumulative_sales | prev_day_sales | growth_rate_percent |
+------------+--------+-------------+--------------+------------------+----------------+---------------------+
| 2025-08-01 | 北京   | iPhone 15    |     50000.00 |         50000.00 |           NULL |                NULL |
| 2025-08-02 | 北京   | iPhone 15    |     45000.00 |         95000.00 |       50000.00 |              -10.00 |
| 2025-08-03 | 北京   | iPhone 15    |     60000.00 |        155000.00 |       45000.00 |               33.33 |
| 2025-08-01 | 北京   | 小米13      |     30000.00 |         30000.00 |           NULL |                NULL |
| 2025-08-02 | 北京   | 小米13      |     35000.00 |         65000.00 |       30000.00 |               16.67 |
| 2025-08-03 | 北京   | 小米13      |     40000.00 |        105000.00 |       35000.00 |               14.29 |
| 2025-08-01 | 上海   | iPhone 15    |     40000.00 |         40000.00 |           NULL |                NULL |
| 2025-08-02 | 上海   | iPhone 15    |     55000.00 |         95000.00 |       40000.00 |               37.50 |
| 2025-08-01 | 上海   | 小米13      |     25000.00 |         25000.00 |           NULL |                NULL |
| 2025-08-02 | 上海   | 小米13      |     30000.00 |         55000.00 |       25000.00 |               20.00 |
+------------+--------+-------------+--------------+------------------+----------------+---------------------+
```

这个查询一下子就给我们提供了丰富的分析信息：

- 每个地区每个产品的累计销售额
- 与前一天的销售对比
- 环比增长率

如果用传统方法实现同样的分析，需要多个复杂的子查询，性能会很差。

## [使用建议](#使用建议)

窗口函数虽然强大，但也要合理使用。以下是一些使用建议：

### [何时使用窗口函数](#何时使用窗口函数)

**1. 需要保留明细数据的统计分析**  
 当你既需要看到每一行的详细信息，又需要进行统计分析时，窗口函数是最佳选择。比如：

- 员工详细信息 + 部门排名
- 每日销售数据 + 累计销售额
- 学生成绩 + 班级排名

**2. 复杂的排名需求**  
 当需要进行分组排名、密集排名、百分比排名时，窗口函数提供了丰富的排名函数：

- `ROW_NUMBER()`: 连续排名（1,2,3,4）
- `RANK()`: 跳跃排名（1,2,2,4）
- `DENSE_RANK()`: 密集排名（1,2,2,3）
- `PERCENT_RANK()`: 百分比排名

**3. 时间序列分析**  
 当需要进行累计计算、移动平均、同比环比等时间序列分析时，窗口函数非常高效：

- 累计销售、累计用户增长
- 7日移动平均、30日移动平均
- 同比增长、环比增长

**4. 简化复杂查询**  
 当需要用子查询或自连接才能实现的需求，考虑是否可以用窗口函数简化。通常窗口函数的写法更简洁，性能也更好。

### [使用注意事项](#使用注意事项)

**1. 性能考虑**  
 窗口函数会消耗较多资源，特别是在大数据集上。要注意：

- 避免在WHERE子句中使用窗口函数
- 考虑在分区列和排序列上创建索引
- 复杂的窗口框架可能影响性能

**2. MySQL版本支持**  
 确保你的MySQL版本支持窗口函数。MySQL从8.0版本开始支持窗口函数，如果你使用的是更早的版本，需要升级或使用其他方法。

**3. 与传统方法的权衡**  
 虽然窗口函数很强大，但并不是所有场景都适合：

- 简单的汇总统计，GROUP BY可能更直观
- 需要实际压缩行数的场景，必须用GROUP BY
- 某些复杂的业务逻辑，可能需要应用层处理

### [实际应用示例](#实际应用示例)

让我们看一个更实际的综合应用：员工绩效分析

```
-- 员工绩效综合分析
SELECT 
    name,
    department,
    position,
    salary,
    hire_date,
    -- 基本统计信息
    COUNT(*) OVER (PARTITION BY department) as dept_size,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary,
    -- 工资排名
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank,
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) as salary_percentile,
    -- 入职时间分析
    DATEDIFF(CURRENT_DATE, hire_date) as days_employed,
    AVG(DATEDIFF(CURRENT_DATE, hire_date)) OVER (PARTITION BY department) as dept_avg_tenure,
    -- 绩效评级（基于工资排名和工作年限）
    CASE 
        WHEN RANK() OVER (PARTITION BY department ORDER BY salary DESC) <= 1 
             AND DATEDIFF(CURRENT_DATE, hire_date) > 365 THEN '优秀'
        WHEN RANK() OVER (PARTITION BY department ORDER BY salary DESC) <= 2 THEN '良好'
        ELSE '待改进'
    END as performance_level
FROM employees
ORDER BY department, salary_rank;
```

这个综合分析提供了丰富的员工信息，从基本统计到绩效评级，全部在一个查询中完成，无需多个子查询或应用层计算。

## [练习题](#练习题)

### [练习1：销售业绩排名](#练习1-销售业绩排名)

创建一个查询，找出每个地区销售额排名前2的产品，包括产品名称、地区、销售额和排名信息。

查看答案

```
WITH product_rank AS (
    SELECT 
        product_name,
        region,
        SUM(sales_amount) as total_sales,
        RANK() OVER (PARTITION BY region ORDER BY SUM(sales_amount) DESC) as sales_rank
    FROM daily_sales
    GROUP BY product_name, region
)
SELECT 
    product_name,
    region,
    total_sales,
    sales_rank
FROM product_rank
WHERE sales_rank <= 2
ORDER BY region, sales_rank;
```

### [练习2：累计移动平均](#练习2-累计移动平均)

计算每个产品按日期的累计销售额和3日移动平均销售额。

查看答案

```
SELECT 
    sale_date,
    product_name,
    sales_amount,
    -- 累计销售额
    SUM(sales_amount) OVER (
        PARTITION BY product_name 
        ORDER BY sale_date 
        ROWS UNBOUNDED PRECEDING
    ) as cumulative_sales,
    -- 3日移动平均
    AVG(sales_amount) OVER (
        PARTITION BY product_name 
        ORDER BY sale_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3day
FROM daily_sales
ORDER BY product_name, sale_date;
```

### [练习3：同比增长分析](#练习3-同比增长分析)

分析每个产品的同比增长情况，计算与去年同期相比的增长率（提示：使用LAG函数按年偏移）。

查看答案

```
-- 先创建包含去年同期数据的测试数据
INSERT INTO daily_sales (sale_date, product_name, sales_amount, region) VALUES 
('2024-08-01', 'iPhone 15', 45000, '北京'),
('2024-08-02', 'iPhone 15', 48000, '北京'),
('2024-08-01', '小米13', 28000, '北京'),
('2024-08-02', '小米13', 32000, '北京');

-- 同比增长分析
SELECT 
    sale_date,
    product_name,
    sales_amount,
    -- 去年同期的销售额
    LAG(sales_amount, 365) OVER (
        PARTITION BY product_name 
        ORDER BY sale_date
    ) as prev_year_sales,
    -- 同比增长率
    CASE 
        WHEN LAG(sales_amount, 365) OVER (
            PARTITION BY product_name 
            ORDER BY sale_date
        ) = 0 THEN NULL
        ELSE (sales_amount - LAG(sales_amount, 365) OVER (
            PARTITION BY product_name 
            ORDER BY sale_date
        )) / LAG(sales_amount, 365) OVER (
            PARTITION BY product_name 
            ORDER BY sale_date
        ) * 100
    END as year_over_year_growth
FROM daily_sales
WHERE sale_date IN ('2025-08-01', '2025-08-02')
ORDER BY product_name, sale_date;
```

## [常见坑](#常见坑)

### [坑1：在WHERE子句中使用窗口函数](#坑1-在where子句中使用窗口函数)

很多初学者试图在WHERE子句中直接使用窗口函数，这是不允许的。

**错误示例**：

```
-- 错误：WHERE子句中不能使用窗口函数
SELECT name, salary
FROM employees
WHERE RANK() OVER (ORDER BY salary DESC) <= 3;
```

**纠正方法**：

```
-- 正确：使用子查询或CTE
WITH ranked_employees AS (
    SELECT 
        name,
        salary,
        RANK() OVER (ORDER BY salary DESC) as salary_rank
    FROM employees
)
SELECT name, salary
FROM ranked_employees
WHERE salary_rank <= 3;
```

### [坑2：忽略窗口函数的性能影响](#坑2-忽略窗口函数的性能影响)

窗口函数虽然强大，但在大数据集上可能消耗大量资源。

**纠正方法**：

- 在分区列和排序列上创建合适的索引
- 避免在频繁执行的查询中使用复杂的窗口函数
- 考虑物化或预计算的方式处理复杂的分析需求

### [坛3：过度使用窗口函数](#坛3-过度使用窗口函数)

有些初学者学会了窗口函数后，试图用窗口函数解决所有问题，包括简单的GROUP BY场景。

**纠正方法**：

- 简单的汇总统计用GROUP BY更直观高效
- 只在需要保留明细数据时使用窗口函数
- 权衡代码复杂度和性能，选择最合适的方案

## [速记卡](#速记卡)

- **窗口函数核心**：保留明细数据的同时进行组内计算
- **基本语法**：`函数名() OVER (PARTITION BY 分组 ORDER BY 排序)`
- **PARTITION BY**：类似GROUP BY，但不压缩行数，定义计算窗口
- **ORDER BY**：为排名和累计函数定义顺序
- **ROW\_NUMBER()**：连续排名（1,2,3,4）
- **RANK()**：跳跃排名（1,2,2,4）
- **LAG()**：获取前面第N行的数据
- **LEAD()**：获取后面第N行的数据
- **SUM() OVER**：累计计算
- **窗口框架**：ROWS BETWEEN定义计算范围
- **适用场景**：排名分析、累计计算、同比环比、移动平均
- **性能注意**：大数据集上要谨慎使用，考虑索引优化

## [章节总结](#章节总结)

在这个加餐中，我们学习了MySQL窗口函数这一强大的分析工具。窗口函数的核心特点是能够在保留每一行明细数据的同时，在相关的行集上执行计算，这解决了传统GROUP BY方法无法满足的分析需求。

我们通过员工工资分析的例子，理解了为什么需要窗口函数。GROUP BY会将多行压缩成一行，丢失明细信息；而窗口函数保持行数不变，为每一行添加计算结果，让我们既能看到具体数据，又能进行统计分析。

窗口函数的基本语法包括PARTITION BY分组子句、ORDER BY排序子句和窗口框架定义。PARTITION BY类似于GROUP BY，但不会压缩行数；ORDER BY不仅为排名函数确定顺序，还为累计函数定义计算方向；窗口框架则精确控制计算的范围。

通过两个实际例子，我们看到了窗口函数的强大应用。分组排名让我们能够轻松找出各部门工资最高的员工，而累计计算与环比分析则帮助我们进行深入的业务分析。这些功能如果用传统方法实现，会非常复杂且低效。

在使用窗口函数时，我们需要知道何时使用它：当需要保留明细数据的统计分析、进行复杂的排名操作、执行时间序列分析，或者简化复杂查询时，窗口函数是很好的选择。但同时也要注意性能考虑，确保MySQL版本支持，并在适当的时候选择传统方法。

掌握了窗口函数，你就能够进行更丰富的数据分析，从简单的数据查询提升到深入的业务分析。窗口函数是现代SQL分析的重要工具，能够帮助你从数据中发现更多有价值的洞察。在数据分析、报表生成、业务监控等场景中，窗口函数都将成为你的得力助手。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [加餐3｜窗口函数：组内计算该怎么写？](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#加餐3-窗口函数-组内计算该怎么写)
- [为什么需要窗口函数？](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#为什么需要窗口函数)
- [传统GROUP BY的局限](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#传统group-by的局限)
- [窗口函数的解决方案](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#窗口函数的解决方案)
- [核心概念 vs GROUP BY](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#核心概念-vs-group-by)
- [GROUP BY的工作方式](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#group-by的工作方式)
- [窗口函数的工作方式](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#窗口函数的工作方式)
- [典型应用场景](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#典型应用场景)
- [基本语法](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#基本语法)
- [PARTITION BY - 分组子句](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#partition-by-分组子句)
- [ORDER BY - 排序子句](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#order-by-排序子句)
- [窗口框架 - ROWS/RANGE](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#窗口框架-rows-range)
- [两个最小例子](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#两个最小例子)
- [例1：分组排名 - ROW_NUMBER()](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#例1-分组排名-row-number)
- [例2：累计计算与环比 - LAG() + SUM() OVER](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#例2-累计计算与环比-lag-sum-over)
- [使用建议](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#使用建议)
- [何时使用窗口函数](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#何时使用窗口函数)
- [使用注意事项](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#使用注意事项)
- [实际应用示例](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#实际应用示例)
- [练习题](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#练习题)
- [练习1：销售业绩排名](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#练习1-销售业绩排名)
- [练习2：累计移动平均](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#练习2-累计移动平均)
- [练习3：同比增长分析](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#练习3-同比增长分析)
- [常见坑](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#常见坑)
- [坑1：在WHERE子句中使用窗口函数](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#坑1-在where子句中使用窗口函数)
- [坑2：忽略窗口函数的性能影响](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#坑2-忽略窗口函数的性能影响)
- [坛3：过度使用窗口函数](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#坛3-过度使用窗口函数)
- [速记卡](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part5/supplement3-window-functions.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
