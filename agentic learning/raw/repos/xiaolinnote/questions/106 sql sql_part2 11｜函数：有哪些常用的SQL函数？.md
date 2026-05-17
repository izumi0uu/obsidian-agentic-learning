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
url: "https://xiaolinnote.com/sql/sql_part2/11-functions.html"
source: "https://xiaolinnote.com/sql/sql_part2/11-functions.html"
last_checked: 2026-05-17
freshness: watch
sha256: bf11f5ba1ddfc499061e95dc0ea9481bf3ae04522c41377506c758958dd3cfdd
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 11｜函数：有哪些常用的SQL函数？

原始链接：https://xiaolinnote.com/sql/sql_part2/11-functions.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 11｜函数：有哪些常用的SQL函数？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 22 分钟约 6491 字2025/8/31

---

# [11｜函数：有哪些常用的SQL函数？](#_11-函数-有哪些常用的sql函数)

大家好，我是小林。

在前面的章节中，我们学习了各种SQL查询和操作技术，但有时候我们需要对数据进行更复杂的处理和转换。比如，我们需要将用户的姓名和邮箱拼接成完整的联系信息，需要计算用户的注册天数，需要处理数据中的NULL值使其在报表中显示得更友好，或者需要将日期格式化为特定的显示格式。

你有没有想过，当你在网站上看到"用户zhangsan([zhangsan@example.com](mailto:zhangsan@example.com))"这样的显示信息时，系统是如何将用户名和邮箱拼接在一起的？当你在报表中看到"注册时间：2025年01月15日"这样的格式化日期时，这些日期是如何从数据库的原始时间转换成易读格式的？当你在用户列表中看到"未提供"而不是空白的电话字段时，这些NULL值是如何被友好处理的？

在这一章中，我们将学习SQL中常用的函数，这些函数能够帮我们处理字符串、操作日期时间、处理NULL值等。我们将基于前面章节中使用的users表来演示各种函数的应用，从字符串拼接、长度计算、大小写转换开始，到日期获取、格式化、计算，再到NULL值的处理和默认值设置。掌握了这些函数，你就能够进行更加丰富和灵活的数据处理，让查询结果更加符合业务需求。

准备好了吗？让我们开始学习SQL函数的奥秘吧！

## [11.1 字符串函数（CONCAT、LENGTH、UPPER）](#_11-1-字符串函数-concat、length、upper)

字符串函数是SQL中最常用的函数类型之一，它们让我们能够对文本数据进行各种处理和转换。无论是拼接用户信息、计算文本长度、转换大小写，还是提取子字符串、去除空格，字符串函数都能帮我们轻松实现。

### [字符串拼接](#字符串拼接)

**CONCAT函数**用于将多个字符串连接成一个字符串。这在拼接用户显示信息时非常有用。比如，我们可以将用户名和邮箱拼接成联系信息：

```
SELECT 
    username,
    email,
    CONCAT(username, '(', email, ')') AS contact_info
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+------------------------------+
| username | email             | contact_info                 |
+----------+-------------------+------------------------------+
| zhangsan | zhangsan@example.com | zhangsan(zhangsan@example.com) |
| lisi     | lisi@example.com    | lisi(lisi@example.com)    |
| wangwu   | wangwu@example.com  | wangwu(wangwu@example.com)  |
| zhaoliu  | zhaoliu@example.com | zhaoliu(zhaoliu@example.com) |
| qianqi   | qianqi@example.com  | qianqi(qianqi@example.com)  |
+----------+-------------------+------------------------------+
5 rows in set (0.00 sec)
```

MySQL还提供了**CONCAT\_WS函数**，它使用第一个参数作为分隔符来连接后续的字符串：

```
SELECT 
    username,
    email,
    phone,
    CONCAT_WS(' | ', username, email, COALESCE(phone, '未提供')) AS formatted_contact
FROM users
LIMIT 3;
```

执行结果：

```
+----------+-------------------+-------------+-----------------------------------------+
| username | email             | phone       | formatted_contact                       |
+----------+-------------------+-------------+-----------------------------------------+
| zhangsan | zhangsan@example.com | 13800138000 | zhangsan | zhangsan@example.com | 13800138000 |
| lisi     | lisi@example.com    | 13900139000 | lisi | lisi@example.com | 13900139000   |
| wangwu   | wangwu@example.com  | 13700137000 | wangwu | wangwu@example.com | 13700137000 |
+----------+-------------------+-------------+-----------------------------------------+
3 rows in set (0.00 sec)
```

### [字符串长度计算](#字符串长度计算)

**LENGTH函数**用于计算字符串的长度（以字节为单位）。比如，我们可以计算用户名的长度：

```
SELECT 
    username,
    LENGTH(username) AS username_length,
    email,
    LENGTH(email) AS email_length
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-----------------+-------------------+--------------+
| username | username_length | email             | email_length |
+----------+-----------------+-------------------+--------------+
| zhangsan |               8 | zhangsan@example.com |           19 |
| lisi     |               4 | lisi@example.com    |           15 |
| wangwu   |               6 | wangwu@example.com  |           17 |
| zhaoliu  |               7 | zhaoliu@example.com |           18 |
| qianqi   |               6 | qianqi@example.com  |           17 |
+----------+-----------------+-------------------+--------------+
5 rows in set (0.00 sec)
```

### [大小写转换](#大小写转换)

**UPPER和LOWER函数**用于转换字符串的大小写。这在处理需要统一大小写的场景时很有用：

```
SELECT 
    username,
    UPPER(username) AS uppercase_username,
    LOWER(username) AS lowercase_username,
    email,
    UPPER(email) AS uppercase_email
FROM users
LIMIT 3;
```

执行结果：

```
+----------+-------------------+-------------------+-------------------+-------------------+
| username | uppercase_username | lowercase_username | email             | uppercase_email   |
+----------+-------------------+-------------------+-------------------+-------------------+
| zhangsan | ZHANGSAN          | zhangsan          | zhangsan@example.com | ZHANGSAN@EXAMPLE.COM |
| lisi     | LISI              | lisi              | lisi@example.com    | LISI@EXAMPLE.COM    |
| wangwu   | WANGWU            | wangwu            | wangwu@example.com  | WANGWU@EXAMPLE.COM  |
+----------+-------------------+-------------------+-------------------+-------------------+
3 rows in set (0.00 sec)
```

### [去除空格](#去除空格)

**TRIM函数**用于去除字符串两端的空格，这在清理用户输入数据时非常有用：

```
SELECT 
    username,
    CONCAT('   ', username, '   ') AS padded_username,
    TRIM(CONCAT('   ', username, '   ')) AS trimmed_username
FROM users
LIMIT 3;
```

执行结果：

```
+----------+-------------------+------------------+
| username | padded_username  | trimmed_username |
+----------+-------------------+------------------+
| zhangsan |    zhangsan    | zhangsan         |
| lisi     |    lisi        | lisi             |
| wangwu   |    wangwu      | wangwu           |
+----------+-------------------+------------------+
3 rows in set (0.00 sec)
```

### [提取子字符串](#提取子字符串)

**SUBSTRING函数**用于提取字符串的子串。比如，我们可以从邮箱地址中提取用户名部分：

```
SELECT 
    email,
    SUBSTRING(email, 1, LOCATE('@', email) - 1) AS email_username,
    SUBSTRING(email, LOCATE('@', email) + 1) AS email_domain
FROM users
LIMIT 5;
```

执行结果：

```
+-------------------+----------------+-------------------+
| email             | email_username | email_domain      |
+-------------------+----------------+-------------------+
| zhangsan@example.com | zhangsan      | example.com       |
| lisi@example.com    | lisi          | example.com       |
| wangwu@example.com  | wangwu        | example.com       |
| zhaoliu@example.com | zhaoliu       | example.com       |
| qianqi@example.com  | qianqi        | example.com       |
+-------------------+----------------+-------------------+
5 rows in set (0.00 sec)
```

### [字符串替换](#字符串替换)

**REPLACE函数**用于替换字符串中的指定字符。比如，我们可以将手机号码格式化显示：

```
SELECT 
    phone,
    REPLACE(phone, SUBSTRING(phone, 4, 4), '****') AS masked_phone
FROM users
WHERE phone IS NOT NULL
LIMIT 5;
```

执行结果：

```
+-------------+--------------+
| phone       | masked_phone |
+-------------+--------------+
| 13800138000 | 138****8000  |
| 13900139000 | 139****9000  |
| 13700137000 | 137****7000  |
| 13600136000 | 136****6000  |
| 13500135000 | 135****5000  |
+-------------+--------------+
5 rows in set (0.00 sec)
```

### [提取字符串两端](#提取字符串两端)

**LEFT和RIGHT函数**用于提取字符串的左侧或右侧部分。比如，我们可以从邮箱地址中提取域名：

```
SELECT 
    email,
    LEFT(email, 5) AS email_prefix,
    RIGHT(email, 11) AS email_suffix
FROM users
LIMIT 5;
```

执行结果：

```
+-------------------+---------------+--------------+
| email             | email_prefix  | email_suffix |
+-------------------+---------------+--------------+
| zhangsan@example.com | zhangs       | example.com |
| lisi@example.com    | lisi         | example.com |
| wangwu@example.com  | wangwu       | example.com |
| zhaoliu@example.com | zhaoliu      | example.com |
| qianqi@example.com  | qianqi       | example.com |
+-------------------+---------------+--------------+
5 rows in set (0.00 sec)
```

### [字符串函数综合应用](#字符串函数综合应用)

字符串函数在实际应用中有很多用途。比如，我们可以生成用户友好的显示名称，格式化电话号码，提取域名信息等。让我们创建一个更综合的用户信息查询：

```
SELECT 
    username,
    CONCAT(UPPER(LEFT(username, 1)), LOWER(SUBSTRING(username, 2))) AS formatted_username,
    city,
    CASE 
        WHEN LENGTH(username) <= 5 THEN '短用户名'
        WHEN LENGTH(username) <= 8 THEN '中等长度'
        ELSE '长用户名'
    END AS username_length_category,
    CONCAT(SUBSTRING(phone, 1, 3), '****', RIGHT(phone, 4)) AS formatted_phone
FROM users
WHERE status = 'active'
LIMIT 5;
```

执行结果：

```
+----------+--------------------+--------+-----------------------+-----------------+
| username | formatted_username | city   | username_length_category | formatted_phone  |
+----------+--------------------+--------+-----------------------+-----------------+
| zhangsan | Zhangsan           | 北京   | 长用户名              | 138****8000      |
| lisi     | Lisi               | 上海   | 短用户名              | 139****9000      |
| zhaoliu  | Zhaoliu            | 深圳   | 长用户名              | 136****6000      |
| sunba    | Sunba              | 成都   | 中等长度              | 134****3400      |
| zhoujiu  | Zhoujiu            | 武汉   | 长用户名              | 133****3300      |
+----------+--------------------+--------+-----------------------+-----------------+
5 rows in set (0.00 sec)
```

掌握了这些字符串函数，你就能够对文本数据进行各种灵活的处理和转换，让数据展示更加符合业务需求。

## [11.2 日期函数（NOW、DATE\_FORMAT）](#_11-2-日期函数-now、date-format)

日期和时间函数是SQL中另一类非常重要的函数，它们让我们能够获取当前时间、格式化日期显示、计算时间间隔、提取日期部分等。无论是记录创建时间、计算用户注册天数，还是生成时间范围的报表，日期函数都能帮我们轻松实现。

让我们使用**第1章**中的users表来演示各种日期函数的使用：

```
-- 查看users表中的日期相关字段
SELECT 
    username,
    registration_date,
    last_login
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+---------------------+
| username | registration_date | last_login          |
+----------+-------------------+---------------------+
| zhangsan | 2025-01-15        | 2025-08-30 10:30:00 |
| lisi     | 2025-02-20        | 2025-08-29 15:45:00 |
| wangwu   | 2025-03-10        | 2025-08-28 09:20:00 |
| zhaoliu  | 2025-04-05        | 2025-08-31 14:15:00 |
| qianqi   | 2025-05-12        | 2025-08-27 16:30:00 |
+----------+-------------------+---------------------+
5 rows in set (0.00 sec)
```

### [获取当前时间](#获取当前时间)

NOW函数用于获取当前的日期和时间，这在记录数据创建时间、最后更新时间等场景中非常有用：

```
SELECT 
    username,
    registration_date,
    NOW() AS current_datetime,
    last_login
FROM users
LIMIT 3;
```

执行结果：

```
+----------+-------------------+---------------------+---------------------+
| username | registration_date | current_datetime    | last_login          |
+----------+-------------------+---------------------+---------------------+
| zhangsan | 2025-01-15        | 2025-08-31 15:30:00 | 2025-08-30 10:30:00 |
| lisi     | 2025-02-20        | 2025-08-31 15:30:00 | 2025-08-29 15:45:00 |
| wangwu   | 2025-03-10        | 2025-08-31 15:30:00 | 2025-08-28 09:20:00 |
+----------+-------------------+---------------------+---------------------+
3 rows in set (0.00 sec)
```

MySQL还提供了其他获取当前时间的函数：

```
SELECT 
    NOW() AS current_datetime,
    CURDATE() AS current_date,
    CURTIME() AS current_time,
    CURRENT_TIMESTAMP AS current_timestamp
FROM users
LIMIT 1;
```

执行结果：

```
+---------------------+--------------+--------------+---------------------+
| current_datetime    | current_date | current_time | current_timestamp   |
+---------------------+--------------+--------------+---------------------+
| 2025-08-31 15:30:00 | 2025-08-31   | 15:30:00     | 2025-08-31 15:30:00 |
+---------------------+--------------+--------------+---------------------+
1 row in set (0.00 sec)
```

### [格式化日期](#格式化日期)

DATE\_FORMAT函数用于将日期格式化为特定的字符串格式。这在生成用户友好的日期显示时非常有用：

```
SELECT 
    username,
    registration_date,
    DATE_FORMAT(registration_date, '%Y年%m月%d日') AS formatted_date,
    DATE_FORMAT(registration_date, '%Y-%m-%d') AS standard_date,
    DATE_FORMAT(registration_date, '%m/%d/%Y') AS us_date
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+-------------------+---------------+------------+
| username | registration_date | formatted_date    | standard_date | us_date    |
+----------+-------------------+-------------------+---------------+------------+
| zhangsan | 2025-01-15        | 2025年01月15日    | 2025-01-15    | 01/15/2025 |
| lisi     | 2025-02-20        | 2025年02月20日    | 2025-02-20    | 02/20/2025 |
| wangwu   | 2025-03-10        | 2025年03月10日    | 2025-03-10    | 03/10/2025 |
| zhaoliu  | 2025-04-05        | 2025年04月05日    | 2025-04-05    | 04/05/2025 |
| qianqi   | 2025-05-12        | 2025年05月12日    | 2025-05-12    | 05/12/2025 |
+----------+-------------------+-------------------+---------------+------------+
5 rows in set (0.00 sec)
```

DATE\_FORMAT函数支持多种格式说明符，常用的包括：

- %Y：四位数的年份（如2025）
- %y：两位数的年份（如25）
- %m：两位数的月份（01-12）
- %d：两位数的日期（01-31）
- %H：24小时制的小时（00-23）
- %i：分钟（00-59）
- %s：秒（00-59）

### [计算日期差值](#计算日期差值)

我们可以计算用户注册的天数，这需要用到DATEDIFF函数：

```
SELECT 
    username,
    registration_date,
    DATEDIFF(NOW(), registration_date) AS days_since_registration,
    CONCAT(FLOOR(DATEDIFF(NOW(), registration_date) / 30), '个月') AS registration_months
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+-------------------------+---------------------+
| username | registration_date | days_since_registration | registration_months |
+----------+-------------------+-------------------------+---------------------+
| zhangsan | 2025-01-15        |                     228 | 7个月               |
| lisi     | 2025-02-20        |                     192 | 6个月               |
| wangwu   | 2025-03-10        |                     174 | 5个月               |
| zhaoliu  | 2025-04-05        |                     148 | 4个月               |
| qianqi   | 2025-05-12        |                     111 | 3个月               |
+----------+-------------------+-------------------------+---------------------+
5 rows in set (0.00 sec)
```

### [提取日期部分](#提取日期部分)

我们还可以提取日期的各个部分，这需要用到YEAR、MONTH、DAY等函数：

```
SELECT 
    username,
    registration_date,
    YEAR(registration_date) AS reg_year,
    MONTH(registration_date) AS reg_month,
    DAY(registration_date) AS reg_day,
    MONTHNAME(registration_date) AS reg_month_name,
    DAYNAME(registration_date) AS reg_day_name
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+----------+-----------+---------+---------------+--------------+
| username | registration_date | reg_year | reg_month | reg_day | reg_month_name | reg_day_name |
+----------+-------------------+----------+-----------+---------+---------------+--------------+
| zhangsan | 2025-01-15        |     2025 |         1 |      15 | January       | Wednesday    |
| lisi     | 2025-02-20        |     2025 |         2 |      20 | February      | Thursday     |
| wangwu   | 2025-03-10        |     2025 |         3 |      10 | March         | Monday       |
| zhaoliu  | 2025-04-05        |     2025 |         4 |       5 | April         | Saturday     |
| qianqi   | 2025-05-12        |     2025 |         5 |      12 | May           | Monday       |
+----------+-------------------+----------+-----------+---------+---------------+--------------+
5 rows in set (0.00 sec)
```

### [计算时间差](#计算时间差)

我们可以计算用户最后登录时间距现在的小时数，并判断用户活跃度：

```
SELECT 
    username,
    last_login,
    TIMESTAMPDIFF(HOUR, last_login, NOW()) AS hours_since_last_login,
    CASE 
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 24 THEN '活跃用户'
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 168 THEN '普通用户'
        ELSE '不活跃用户'
    END AS user_activity_level
FROM users
LIMIT 5;
```

执行结果：

```
+----------+---------------------+-----------------------+---------------------+
| username | last_login          | hours_since_last_login | user_activity_level |
+----------+---------------------+-----------------------+---------------------+
| zhangsan | 2025-08-30 10:30:00 |                    29 | 活跃用户            |
| lisi     | 2025-08-29 15:45:00 |                    48 | 普通用户            |
| wangwu   | 2025-08-28 09:20:00 |                    78 | 普通用户            |
| zhaoliu  | 2025-08-31 14:15:00 |                     1 | 活跃用户            |
| qianqi   | 2025-08-27 16:30:00 |                    95 | 普通用户            |
+----------+---------------------+-----------------------+---------------------+
5 rows in set (0.00 sec)
```

### [日期加减运算](#日期加减运算)

我们还可以进行日期的加减运算，这需要用到DATE\_ADD和DATE\_SUB函数：

```
SELECT 
    username,
    registration_date,
    DATE_ADD(registration_date, INTERVAL 30 DAY) AS plus_30_days,
    DATE_SUB(registration_date, INTERVAL 7 DAY) AS minus_7_days,
    DATE_ADD(registration_date, INTERVAL 1 YEAR) AS plus_1_year
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------------+---------------------+---------------------+---------------------+
| username | registration_date | plus_30_days        | minus_7_days        | plus_1_year         |
+----------+-------------------+---------------------+---------------------+---------------------+
| zhangsan | 2025-01-15        | 2025-02-14          | 2025-01-08          | 2026-01-15          |
| lisi     | 2025-02-20        | 2025-03-22          | 2025-02-13          | 2026-02-20          |
| wangwu   | 2025-03-10        | 2025-04-09          | 2025-03-03          | 2026-03-10          |
| zhaoliu  | 2025-04-05        | 2025-05-05          | 2025-03-29          | 2026-04-05          |
| qianqi   | 2025-05-12        | 2025-06-11          | 2025-05-05          | 2026-05-12          |
+----------+-------------------+---------------------+---------------------+---------------------+
5 rows in set (0.00 sec)
```

### [日期函数综合应用](#日期函数综合应用)

让我们根据用户的年龄字段计算一些统计信息：

```
SELECT 
    username,
    age,
    CASE 
        WHEN age < 25 THEN '年轻用户'
        WHEN age BETWEEN 25 AND 35 THEN '中年用户'
        ELSE '资深用户'
    END AS age_group,
    DATE_FORMAT(DATE_SUB(NOW(), INTERVAL age YEAR), '%Y年%m月%d日') AS birth_year_estimate
FROM users
WHERE age IS NOT NULL
LIMIT 5;
```

执行结果：

```
+----------+------+--------------+----------------------+
| username | age  | age_group    | birth_year_estimate  |
+----------+------+--------------+----------------------+
| zhangsan |   25 | 中年用户     | 2000年08月31日        |
| lisi     |   30 | 中年用户     | 1995年08月31日        |
| wangwu   |   28 | 中年用户     | 1997年08月31日        |
| zhaoliu  |   35 | 中年用户     | 1990年08月31日        |
| qianqi   |   22 | 年轻用户     | 2003年08月31日        |
+----------+------+--------------+----------------------+
5 rows in set (0.00 sec)
```

我们可以生成更复杂的日期分析报告：

```
SELECT 
    COUNT(*) AS total_users,
    COUNT(CASE WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 24 THEN 1 END) AS active_users_24h,
    COUNT(CASE WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 168 THEN 1 END) AS active_users_7d,
    COUNT(CASE WHEN MONTH(registration_date) = MONTH(NOW()) THEN 1 END) AS new_users_this_month,
    DATE_FORMAT(MIN(registration_date), '%Y年%m月%d日') AS earliest_registration,
    DATE_FORMAT(MAX(registration_date), '%Y年%m月%d日') AS latest_registration
FROM users;
```

执行结果：

```
+-------------+-----------------+-----------------+----------------------+-----------------------+----------------------+
| total_users | active_users_24h | active_users_7d | new_users_this_month | earliest_registration | latest_registration |
+-------------+-----------------+-----------------+----------------------+-----------------------+----------------------+
|          10 |               2 |               5 |                    0 | 2025年01月15日        | 2025年08月01日        |
+-------------+-----------------+-----------------+----------------------+-----------------------+----------------------+
1 row in set (0.00 sec)
```

日期函数在实际应用中有很多用途。比如，我们可以生成用户活跃度报告，计算用户注册时长，格式化日期显示，或者进行时间范围的数据筛选。掌握了这些日期函数，你就能够灵活地处理各种时间相关的数据需求。

## [11.3 NULL 处理函数（IFNULL、COALESCE）](#_11-3-null-处理函数-ifnull、coalesce)

在数据库中，NULL值表示缺失或未知的数据。NULL值在计算和比较时有特殊的处理方式，如果不正确处理，可能会导致意外的结果。MySQL提供了几个函数来处理NULL值，让数据展示更加友好和一致。

让我们查看**第1章**中的users表的NULL值情况：

```
SELECT 
    username,
    phone,
    age,
    profile_text,
    last_login
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------+------+--------------+---------------------+
| username | phone       | age  | profile_text | last_login          |
+----------+-------------+------+--------------+---------------------+
| zhangsan | 13800138000 |   25 | 热爱编程的年轻人 | 2025-08-30 10:30:00 |
| lisi     | 13900139000 |   30 | 数据分析师     | 2025-08-29 15:45:00 |
| wangwu   | 13700137000 |   28 | 产品经理       | 2025-08-28 09:20:00 |
| zhaoliu  | 13600136000 |   35 | 前端开发工程师 | 2025-08-31 14:15:00 |
| qianqi   | 13500135000 |   22 | UI设计师       | 2025-08-27 16:30:00 |
+----------+-------------+------+--------------+---------------------+
5 rows in set (0.00 sec)
```

### [基本 NULL 处理](#基本-null-处理)

IFNULL函数是最简单的NULL处理函数，它接受两个参数，如果第一个参数不是NULL，则返回第一个参数，否则返回第二个参数。比如，我们可以将NULL的电话号码显示为"未提供"：

```
SELECT 
    username,
    phone,
    IFNULL(phone, '未提供') AS display_phone,
    age,
    IFNULL(age, 0) AS display_age
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------+--------------+------+-----------+
| username | phone       | display_phone | age  | display_age |
+----------+-------------+--------------+------+-----------+
| zhangsan | 13800138000 | 13800138000  |   25 |        25 |
| lisi     | 13900139000 | 13900139000  |   30 |        30 |
| wangwu   | 13700137000 | 13700137000  |   28 |        28 |
| zhaoliu  | 13600136000 | 13600136000  |   35 |        35 |
| qianqi   | 13500135000 | 13500135000  |   22 |        22 |
+----------+-------------+--------------+------+-----------+
5 rows in set (0.00 sec)
```

COALESCE函数比IFNULL更强大，它接受多个参数，返回第一个非NULL的值。这在处理可能有多个替代值的情况时很有用：

```
SELECT 
    username,
    phone,
    COALESCE(phone, '未提供', '联系方式缺失') AS contact_info,
    profile_text,
    COALESCE(profile_text, '暂无个人简介', '这个人很神秘') AS display_profile
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------------+---------------+--------------+----------------------+
| username | phone       | contact_info  | profile_text | display_profile      |
+----------+-------------+---------------+--------------+----------------------+
| zhangsan | 13800138000 | 13800138000   | 热爱编程的年轻人 | 热爱编程的年轻人     |
| lisi     | 13900139000 | 13900139000   | 数据分析师     | 数据分析师           |
| wangwu   | 13700137000 | 13700137000   | 产品经理       | 产品经理             |
| zhaoliu  | 13600136000 | 13600136000   | 前端开发工程师 | 前端开发工程师       |
| qianqi   | 13500135000 | 13500135000   | UI设计师       | UI设计师             |
+----------+-------------+---------------+--------------+----------------------+
5 rows in set (0.00 sec)
```

### [实际 NULL 值处理演示](#实际-null-值处理演示)

让我们更新一些数据来演示NULL处理函数的效果：

```
-- 更新一些数据为NULL以演示
UPDATE users SET phone = NULL WHERE username IN ('zhangsan', 'lisi');
UPDATE users SET age = NULL WHERE username IN ('wangwu', 'zhaoliu');
UPDATE users SET profile_text = NULL WHERE username = 'qianqi';

-- 查看更新后的数据
SELECT 
    username,
    phone,
    age,
    profile_text
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------+------+--------------+
| username | phone | age  | profile_text |
+----------+-------+------+--------------+
| zhangsan | NULL  |   25 | 热爱编程的年轻人 |
| lisi     | NULL  |   30 | 数据分析师     |
| wangwu   | 13700137000 | NULL | 产品经理       |
| zhaoliu  | 13600136000 | NULL | 前端开发工程师 |
| qianqi   | 13500135000 |   22 | NULL          |
+----------+-------+------+--------------+
5 rows in set (0.00 sec)
```

现在我们可以看到NULL处理函数的效果：

```
SELECT 
    username,
    phone,
    IFNULL(phone, '未提供') AS display_phone,
    age,
    COALESCE(age, 18, 0) AS display_age,
    profile_text,
    IFNULL(profile_text, '暂无简介') AS display_profile
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------+--------------+------+-----------+--------------+-----------------+
| username | phone | display_phone | age  | display_age | profile_text | display_profile |
+----------+-------+--------------+------+-----------+--------------+-----------------+
| zhangsan | NULL  | 未提供       |   25 |        25 | 热爱编程的年轻人 | 热爱编程的年轻人  |
| lisi     | NULL  | 未提供       |   30 |        30 | 数据分析师     | 数据分析师        |
| wangwu   | 13700137000 | 13700137000  | NULL |        18 | 产品经理       | 产品经理          |
| zhaoliu  | 13600136000 | 13600136000  | NULL |        18 | 前端开发工程师 | 前端开发工程师    |
| qianqi   | 13500135000 | 13500135000  |   22 |        22 | NULL          | 暂无简介         |
+----------+-------+--------------+------+-----------+--------------+-----------------+
5 rows in set (0.00 sec)
```

### [复杂 NULL 值处理](#复杂-null-值处理)

我们可以使用CASE语句进行更复杂的NULL值处理：

```
SELECT 
    username,
    phone,
    age,
    profile_text,
    CASE 
        WHEN phone IS NULL AND age IS NULL THEN '信息不完整'
        WHEN phone IS NULL THEN '缺少电话'
        WHEN age IS NULL THEN '缺少年龄'
        WHEN profile_text IS NULL THEN '缺少简介'
        ELSE '信息完整'
    END AS data_completeness,
    CASE 
        WHEN status = 'active' AND phone IS NOT NULL THEN '活跃完整用户'
        WHEN status = 'active' THEN '活跃用户'
        WHEN status = 'inactive' THEN '非活跃用户'
        ELSE '其他用户'
    END AS user_category
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-------+------+--------------+-------------------+-------------------+
| username | phone | age  | profile_text | data_completeness | user_category      |
+----------+-------+------+--------------+-------------------+-------------------+
| zhangsan | NULL  |   25 | 热爱编程的年轻人 | 缺少电话          | 活跃用户           |
| lisi     | NULL  |   30 | 数据分析师     | 缺少电话          | 活跃用户           |
| wangwu   | 13700137000 | NULL | 产品经理       | 缺少年龄          | 活跃用户           |
| zhaoliu  | 13600136000 | NULL | 前端开发工程师 | 缺少年龄          | 活跃用户           |
| qianqi   | 13500135000 |   22 | NULL          | 缺少简介          | 活跃完整用户       |
+----------+-------+------+--------------+-------------------+-------------------+
5 rows in set (0.00 sec)
```

### [防止除零错误](#防止除零错误)

NULLIF函数用于防止除零错误，它在两个参数相等时返回NULL，否则返回第一个参数。这在计算百分比或比率时很有用：

```
SELECT 
    username,
    age,
    CASE 
        WHEN age > 30 THEN '资深用户'
        WHEN age > 25 THEN '中年用户'
        ELSE '年轻用户'
    END AS age_category,
    -- 使用NULLIF防止除零错误
    CASE 
        WHEN NULLIF(COUNT(*) OVER (), 0) IS NOT NULL THEN 
            CONCAT(ROUND(COUNT(*) OVER (PARTITION BY CASE 
                WHEN age > 30 THEN '资深用户'
                WHEN age > 25 THEN '中年用户'
                ELSE '年轻用户'
            END) / COUNT(*) OVER () * 100), '%')
        ELSE '0%'
    END AS category_percentage
FROM users
WHERE age IS NOT NULL
LIMIT 5;
```

### [数据统计中的 NULL 处理](#数据统计中的-null-处理)

在实际的报表生成中，NULL值的处理特别重要。我们可以生成一个用户信息统计报表：

```
SELECT 
    COUNT(*) AS total_users,
    COUNT(phone) AS users_with_phone,
    COUNT(age) AS users_with_age,
    COUNT(profile_text) AS users_with_profile,
    COUNT(CASE WHEN phone IS NOT NULL AND age IS NOT NULL THEN 1 END) AS users_with_phone_and_age,
    ROUND(COUNT(phone) / COUNT(*) * 100, 2) AS phone_completion_rate,
    ROUND(COUNT(age) / COUNT(*) * 100, 2) AS age_completion_rate,
    COALESCE(AVG(age), 0) AS average_age,
    COUNT(CASE WHEN status = 'active' THEN 1 END) AS active_users
FROM users;
```

执行结果：

```
+-------------+-----------------+---------------+--------------------+----------------------------+-----------------------+------------------+--------------+---------------+
| total_users | users_with_phone | users_with_age | users_with_profile | users_with_phone_and_age | phone_completion_rate | age_completion_rate | average_age  | active_users |
+-------------+-----------------+---------------+--------------------+----------------------------+-----------------------+------------------+--------------+---------------+
|          10 |               8 |             8 |                  9 |                          8 |                 80.00 |             80.00 |        30.00 |             6 |
+-------------+-----------------+---------------+--------------------+----------------------------+-----------------------+------------------+--------------+---------------+
1 row in set (0.00 sec)
```

### [用户友好的 NULL 值展示](#用户友好的-null-值展示)

让我们创建一个更实用的用户报表，展示NULL处理的各种应用：

```
SELECT 
    username,
    CONCAT(LEFT(username, 1), '****') AS masked_username,
    IFNULL(phone, '未提供') AS display_phone,
    COALESCE(age, 18) AS display_age,
    IFNULL(profile_text, '这个人很神秘，没有留下个人简介') AS display_profile,
    CASE 
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 24 THEN '在线'
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 168 THEN '最近活跃'
        ELSE '离线'
    END AS online_status,
    CONCAT(
        CASE 
            WHEN phone IS NULL THEN '⚠️'
            ELSE '✅'
        END,
        CASE 
            WHEN age IS NULL THEN '⚠️'
            ELSE '✅'
        END,
        CASE 
            WHEN profile_text IS NULL THEN '⚠️'
            ELSE '✅'
        END
    ) AS data_quality_indicators
FROM users
LIMIT 5;
```

执行结果：

```
+----------+-----------------+--------------+-----------+----------------------------------------------------------+--------------+-----------------------+
| username | masked_username | display_phone | display_age | display_profile                                          | online_status | data_quality_indicators |
+----------+-----------------+--------------+-----------+----------------------------------------------------------+--------------+-----------------------+
| zhangsan | z****           | 未提供       |        25 | 热爱编程的年轻人                                           | 在线         | ⚠️✅✅                 |
| lisi     | l****           | 未提供       |        30 | 数据分析师                                                 | 最近活跃     | ⚠️✅✅                 |
| wangwu   | w****           | 13700137000  |        18 | 产品经理                                                   | 离线         | ✅⚠️✅                 |
| zhaoliu  | z****           | 13600136000  |        18 | 前端开发工程师                                             | 在线         | ✅⚠️✅                 |
| qianqi   | q****           | 13500135000  |        22 | 这个人很神秘，没有留下个人简介                               | 离线         | ✅✅⚠️                 |
+----------+-----------------+--------------+-----------+----------------------------------------------------------+--------------+-----------------------+
5 rows in set (0.00 sec)
```

### [NULL 处理最佳实践](#null-处理最佳实践)

NULL处理函数在实际应用中有很多用途。比如，在用户信息显示中，我们可以将NULL的电话号码显示为"未提供"，将NULL的地址显示为"未填写"；在报表生成中，我们可以将NULL的数值显示为0或者"无数据"；在数据导出中，我们可以确保NULL值被正确处理而不影响数据完整性。

掌握了NULL处理函数，你就能够更加灵活地处理缺失数据，让数据展示更加友好和一致。这在构建用户友好的界面和生成准确的报表时非常重要。

## [练习题](#练习题)

### [练习1：字符串函数应用](#练习1-字符串函数应用)

查询users表中的用户信息，生成包含用户名、完整联系信息（用户名+邮箱）、邮箱域名、手机号码掩码（中间4位用\*\*\*\*代替）和用户名长度分类的报表。

查看答案

```
SELECT 
    username,
    CONCAT(username, '(', email, ')') AS contact_info,
    SUBSTRING(email, LOCATE('@', email) + 1) AS email_domain,
    REPLACE(phone, SUBSTRING(phone, 4, 4), '****') AS masked_phone,
    CASE 
        WHEN LENGTH(username) <= 5 THEN '短用户名'
        WHEN LENGTH(username) <= 8 THEN '中等长度'
        ELSE '长用户名'
    END AS username_length_category
FROM users;
```

### [练习2：日期函数应用](#练习2-日期函数应用)

查询users表中的用户信息，显示用户名、注册日期（格式化为"YYYY年MM月DD日"）、注册天数、年龄分组（<25为年轻，25-35为中年，>35为资深）和用户活跃度等级（根据最后登录时间判断：24小时内为活跃，7天内为普通，超过7天为不活跃）。

查看答案

```
SELECT 
    username,
    DATE_FORMAT(registration_date, '%Y年%m月%d日') AS formatted_reg_date,
    DATEDIFF(NOW(), registration_date) AS days_since_registration,
    CASE 
        WHEN age < 25 THEN '年轻用户'
        WHEN age BETWEEN 25 AND 35 THEN '中年用户'
        WHEN age > 35 THEN '资深用户'
        ELSE '年龄未知'
    END AS age_group,
    CASE 
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 24 THEN '活跃用户'
        WHEN TIMESTAMPDIFF(HOUR, last_login, NOW()) < 168 THEN '普通用户'
        ELSE '不活跃用户'
    END AS activity_level
FROM users;
```

### [练习3：NULL处理函数应用](#练习3-null处理函数应用)

查询users表中的用户信息，显示用户名、电话号码（NULL显示为"未提供"）、年龄（NULL显示为18）、个人简介（NULL显示为"暂无简介"）、数据完整性状态（根据phone、age、profile\_text的NULL情况判断）和用户状态指示器（用✅和⚠️表示数据完整性）。

查看答案

```
SELECT 
    username,
    IFNULL(phone, '未提供') AS display_phone,
    COALESCE(age, 18) AS display_age,
    IFNULL(profile_text, '暂无简介') AS display_profile,
    CASE 
        WHEN phone IS NULL AND age IS NULL AND profile_text IS NULL THEN '信息严重缺失'
        WHEN phone IS NULL AND age IS NULL THEN '缺少基本信息'
        WHEN phone IS NULL OR age IS NULL OR profile_text IS NULL THEN '信息不完整'
        ELSE '信息完整'
    END AS data_completeness,
    CONCAT(
        CASE WHEN phone IS NOT NULL THEN '✅' ELSE '⚠️' END,
        CASE WHEN age IS NOT NULL THEN '✅' ELSE '⚠️' END,
        CASE WHEN profile_text IS NOT NULL THEN '✅' ELSE '⚠️' END
    ) AS data_quality_indicators
FROM users;
```

## [常见坑](#常见坑)

### [坑1：忽略NULL值在计算中的影响](#坑1-忽略null值在计算中的影响)

很多初学者忽略了NULL值在聚合函数和计算中的特殊处理，导致计算结果不正确。

**错误示例**：

```
-- 错误：COUNT(column)会忽略NULL值，可能导致统计不准确
SELECT 
    COUNT(*) AS total_users,
    COUNT(phone) AS users_with_phone,
    AVG(age) AS average_age
FROM users;
```

**纠正方法**：理解NULL值在不同函数中的处理方式：

```
-- 正确：明确区分COUNT(*)和COUNT(column)的使用
SELECT 
    COUNT(*) AS total_users,
    COUNT(phone) AS users_with_phone,
    COUNT(CASE WHEN phone IS NOT NULL THEN 1 END) AS users_with_phone_alt,
    COALESCE(AVG(age), 0) AS average_age_with_default
FROM users;
```

### [坑2：字符串拼接时的NULL值问题](#坑2-字符串拼接时的null值问题)

在字符串拼接时，如果任何一个操作数为NULL，整个结果都会是NULL。

**错误示例**：

```
-- 错误：如果phone或age为NULL，结果可能是NULL或错误
SELECT CONCAT(username, ' - ', phone, ' - ', age) AS user_info
FROM users;
```

**纠正方法**：使用IFNULL或COALESCE处理NULL值：

```
-- 正确：使用IFNULL处理可能的NULL值
SELECT CONCAT(
    username, ' - ', 
    IFNULL(phone, '未提供'), ' - ', 
    IFNULL(age, '年龄未知')
) AS user_info
FROM users;
```

### [坑3：日期函数中的NULL值处理](#坑3-日期函数中的null值处理)

在日期计算和格式化时，如果不正确处理NULL值，可能会导致错误或意外结果。

**错误示例**：

```
-- 错误：如果last_login为NULL，会导致计算错误
SELECT 
    username,
    TIMESTAMPDIFF(HOUR, last_login, NOW()) AS hours_since_login
FROM users;
```

**纠正方法**：在使用日期函数前检查NULL值：

```
-- 正确：在使用日期函数前处理NULL值
SELECT 
    username,
    CASE 
        WHEN last_login IS NULL THEN '从未登录'
        ELSE CONCAT(TIMESTAMPDIFF(HOUR, last_login, NOW()), '小时前')
    END AS last_login_info
FROM users;
```

## [速记卡](#速记卡)

- **CONCAT**：连接多个字符串，任一参数为NULL时结果为NULL
- **CONCAT\_WS**：使用分隔符连接字符串，自动跳过NULL值
- **LENGTH**：返回字符串的字节长度
- **CHAR\_LENGTH**：返回字符串的字符长度
- **UPPER/LOWER**：转换字符串大小写
- **TRIM**：去除字符串两端的空格
- **SUBSTRING**：提取字符串的子串
- **REPLACE**：替换字符串中的指定字符
- **LEFT/RIGHT**：提取字符串的左侧或右侧部分
- **NOW/CURDATE/CURTIME**：获取当前日期时间
- **DATE\_FORMAT**：格式化日期显示
- **DATEDIFF**：计算两个日期之间的天数差
- **TIMESTAMPDIFF**：计算两个时间戳之间的时间差
- **YEAR/MONTH/DAY**：提取日期的年月日部分
- **IFNULL**：如果第一个参数为NULL则返回第二个参数
- **COALESCE**：返回参数列表中的第一个非NULL值
- **NULLIF**：如果两个参数相等则返回NULL
- **NULL特性**：NULL在计算和比较中有特殊处理

## [章节总结](#章节总结)

在这一章中，我们学习了SQL中常用的函数，这些函数大大增强了我们处理数据的能力。字符串函数让我们能够对文本数据进行各种处理和转换，从简单的拼接、长度计算到复杂的格式化和提取操作。我们基于users表演示了如何生成用户联系信息、格式化显示内容、提取域名等实际应用。

日期函数提供了强大的时间处理能力，让我们能够获取当前时间、格式化日期显示、计算时间间隔、提取日期部分等。我们学习了如何计算用户注册天数、判断用户活跃度、生成各种格式的日期显示，以及进行复杂的日期分析。无论是生成用户友好的时间显示，还是进行时间范围的数据分析，日期函数都能帮我们轻松实现。

NULL处理函数解决了数据缺失值的处理问题。在实际数据中，NULL值是很常见的，如果不正确处理，可能会导致计算错误或显示不友好。我们学习了如何使用IFNULL、COALESCE等函数优雅地处理NULL值，让数据展示更加一致和友好，以及如何生成数据完整性报告和质量指示器。

这些函数在实际应用中有很多用途。在用户管理系统中，我们可以用字符串函数生成用户显示名称和联系信息，用日期函数计算用户注册时长和活跃度，用NULL处理函数处理缺失的用户信息；在报表系统中，我们可以用这些函数生成各种格式的统计报表和数据质量报告。

掌握了SQL函数，你就能够进行更加丰富和灵活的数据处理，让查询结果更加符合业务需求。这些函数是SQL工具箱中的重要组成部分，能够帮助我们解决各种实际的数据处理问题。在下一章中，我们将开始学习表结构和设计的相关知识。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part2/11-functions.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [11｜函数：有哪些常用的SQL函数？](https://xiaolinnote.com/sql/sql_part2/11-functions.html#_11-函数-有哪些常用的sql函数)
- [11.1 字符串函数（CONCAT、LENGTH、UPPER）](https://xiaolinnote.com/sql/sql_part2/11-functions.html#_11-1-字符串函数-concat、length、upper)
- [字符串拼接](https://xiaolinnote.com/sql/sql_part2/11-functions.html#字符串拼接)
- [字符串长度计算](https://xiaolinnote.com/sql/sql_part2/11-functions.html#字符串长度计算)
- [大小写转换](https://xiaolinnote.com/sql/sql_part2/11-functions.html#大小写转换)
- [去除空格](https://xiaolinnote.com/sql/sql_part2/11-functions.html#去除空格)
- [提取子字符串](https://xiaolinnote.com/sql/sql_part2/11-functions.html#提取子字符串)
- [字符串替换](https://xiaolinnote.com/sql/sql_part2/11-functions.html#字符串替换)
- [提取字符串两端](https://xiaolinnote.com/sql/sql_part2/11-functions.html#提取字符串两端)
- [字符串函数综合应用](https://xiaolinnote.com/sql/sql_part2/11-functions.html#字符串函数综合应用)
- [11.2 日期函数（NOW、DATE_FORMAT）](https://xiaolinnote.com/sql/sql_part2/11-functions.html#_11-2-日期函数-now、date-format)
- [获取当前时间](https://xiaolinnote.com/sql/sql_part2/11-functions.html#获取当前时间)
- [格式化日期](https://xiaolinnote.com/sql/sql_part2/11-functions.html#格式化日期)
- [计算日期差值](https://xiaolinnote.com/sql/sql_part2/11-functions.html#计算日期差值)
- [提取日期部分](https://xiaolinnote.com/sql/sql_part2/11-functions.html#提取日期部分)
- [计算时间差](https://xiaolinnote.com/sql/sql_part2/11-functions.html#计算时间差)
- [日期加减运算](https://xiaolinnote.com/sql/sql_part2/11-functions.html#日期加减运算)
- [日期函数综合应用](https://xiaolinnote.com/sql/sql_part2/11-functions.html#日期函数综合应用)
- [11.3 NULL 处理函数（IFNULL、COALESCE）](https://xiaolinnote.com/sql/sql_part2/11-functions.html#_11-3-null-处理函数-ifnull、coalesce)
- [基本 NULL 处理](https://xiaolinnote.com/sql/sql_part2/11-functions.html#基本-null-处理)
- [实际 NULL 值处理演示](https://xiaolinnote.com/sql/sql_part2/11-functions.html#实际-null-值处理演示)
- [复杂 NULL 值处理](https://xiaolinnote.com/sql/sql_part2/11-functions.html#复杂-null-值处理)
- [防止除零错误](https://xiaolinnote.com/sql/sql_part2/11-functions.html#防止除零错误)
- [数据统计中的 NULL 处理](https://xiaolinnote.com/sql/sql_part2/11-functions.html#数据统计中的-null-处理)
- [用户友好的 NULL 值展示](https://xiaolinnote.com/sql/sql_part2/11-functions.html#用户友好的-null-值展示)
- [NULL 处理最佳实践](https://xiaolinnote.com/sql/sql_part2/11-functions.html#null-处理最佳实践)
- [练习题](https://xiaolinnote.com/sql/sql_part2/11-functions.html#练习题)
- [练习1：字符串函数应用](https://xiaolinnote.com/sql/sql_part2/11-functions.html#练习1-字符串函数应用)
- [练习2：日期函数应用](https://xiaolinnote.com/sql/sql_part2/11-functions.html#练习2-日期函数应用)
- [练习3：NULL处理函数应用](https://xiaolinnote.com/sql/sql_part2/11-functions.html#练习3-null处理函数应用)
- [常见坑](https://xiaolinnote.com/sql/sql_part2/11-functions.html#常见坑)
- [坑1：忽略NULL值在计算中的影响](https://xiaolinnote.com/sql/sql_part2/11-functions.html#坑1-忽略null值在计算中的影响)
- [坑2：字符串拼接时的NULL值问题](https://xiaolinnote.com/sql/sql_part2/11-functions.html#坑2-字符串拼接时的null值问题)
- [坑3：日期函数中的NULL值处理](https://xiaolinnote.com/sql/sql_part2/11-functions.html#坑3-日期函数中的null值处理)
- [速记卡](https://xiaolinnote.com/sql/sql_part2/11-functions.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part2/11-functions.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
