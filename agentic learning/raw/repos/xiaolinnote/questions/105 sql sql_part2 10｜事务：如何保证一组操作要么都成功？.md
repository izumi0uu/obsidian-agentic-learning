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
url: https://xiaolinnote.com/sql/sql_part2/10-transactions.html
source: https://xiaolinnote.com/sql/sql_part2/10-transactions.html
last_checked: 2026-05-17
freshness: watch
sha256: a689e744d363bcc1126dabe268a5c7a8de8373246cd705c894a1a39322afe4b0
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 10｜事务：如何保证一组操作要么都成功？

原始链接：https://xiaolinnote.com/sql/sql_part2/10-transactions.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 10｜事务：如何保证一组操作要么都成功？

[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 15 分钟约 4424 字2025/8/31

---

# [10｜事务：如何保证一组操作要么都成功？](#_10-事务-如何保证一组操作要么都成功)

大家好，我是小林。

在前面的章节中，我们学习了各种SQL操作，包括查询、插入、更新和删除数据。这些操作都是单个执行的，但在实际应用中，很多业务操作需要多个SQL语句一起完成。比如，银行转账需要从一个账户扣款同时向另一个账户存款，电商下单需要减少库存同时创建订单，用户状态变更需要更新用户信息同时记录变更历史。

你有没有想过，当你在银行转账时，如果系统从你的账户扣款成功，但在向对方账户存款时失败了，会发生什么？你的钱会凭空消失吗？当你在电商网站下单时，如果系统成功创建了订单但库存没有相应减少，会不会出现超卖问题？当你在用户管理系统中修改用户状态时，如果状态更新成功了但变更记录失败了，会不会导致数据不一致？

在这一章中，我们将学习数据库事务技术，它能够确保一组相关的操作要么全部成功，要么全部失败，从而保证数据的一致性和完整性。从事务的基本概念和ACID特性开始，到COMMIT和ROLLBACK的使用方法，再到实际业务场景中的事务应用。

准备好了吗？让我们开始学习事务的奥秘吧！

## [10.1 为什么需要事务？](#_10-1-为什么需要事务)

让我们先来看两个生活中"没做好会出乱子"的例子，这样你就能明白为什么事务如此重要。

**例子一：银行转账的麻烦**

想象一下，你要给朋友转账100元。这个过程实际上包含两个步骤：

1. 从你的账户扣除100元
2. 给朋友的账户增加100元

现在想想，如果第一步成功了（钱从你的账户扣走了），但第二步失败了（朋友没有收到钱），会发生什么？你的钱就这样凭空消失了！这显然是不能接受的。

**例子二：网购下单的混乱**

再比如你在网上买一件衣服，这个过程也需要两个步骤：

1. 系统生成一个订单（显示你购买成功）
2. 仓库减少一件库存（衣服被你买走了）

如果订单生成了，但库存没有减少，会出现什么问题？可能其他顾客也会买到同一件衣服，导致仓库里明明只有一件衣服，却卖给了好几个人，这就是所谓的"超卖"问题。

从这些例子可以看出，**当一件事需要分两步或多步完成时，只要有一步没成，之前的步骤也得作废**。而事务就是帮我们实现"要么全成、要么全不算"的工具，避免出现混乱数据。

## [10.2 什么是事务？](#_10-2-什么是事务)

用最简单的话来说，**事务就是把多个SQL操作"打包"，让它们变成一个不可分割的整体**。

让我用"去超市买东西"来类比：  
 你去超市买东西，整个过程包括"选商品→扫码付款"这两个步骤。这就像一个完整的事务——你不能只选商品不付款，也不能只付款不选商品。这两个步骤要么都完成（成功购物），要么都不完成（放弃购买），不会出现中间状态。

在数据库中，事务就是把多个相关的SQL操作（比如"生成订单"和"减库存"、"扣钱"和"到账"）打包，让它们变成一个整体。这个整体里的所有操作，要么都做完并生效，要么一个都不做，绝对不会出现"做了一半"的尴尬情况。

## [10.3 事务的 ACID 特性](#_10-3-事务的-acid-特性)

ACID是事务的四个重要特性，每个特性都有重要作用。我们还是用"你给朋友转100元"的例子来逐个说明：

### [原子性（Atomicity）](#原子性-atomicity)

**原子性就像是原子一样不可分割**。在转账的例子中：

- 要么100元成功从你账户扣走，并成功到朋友账户（整个过程完成）
- 要么钱还在你账户里（整个过程没开始）

绝对不会出现"扣了你的钱，但朋友没收到"的中间状态。这就是原子性——事务中的所有操作要么全部成功，要么全部失败。

### [一致性（Consistency）](#一致性-consistency)

**一致性确保数据前后"算得通"**。在转账前：

- 你有500元，朋友有300元，总钱数是800元

转账成功后：

- 你剩下400元，朋友有400元，总钱数还是800元

数据的总量在事务前后保持一致，不会多也不会少。这就是一致性——事务执行前后，数据库始终处于一致的状态。

### [隔离性（Isolation）](#隔离性-isolation)

**隔离性让多个事务互不干扰**。想象一下：

- 你给朋友转账的同时
- 另一个人也给你转账

这两个"转账操作"不会互相干扰。不会因为你这边还没转完，导致另一边算错你的余额。每个事务都感觉不到其他事务的存在，就像独立操作一样。

### [持久性（Durability）](#持久性-durability)

**持久性确保成功的结果永久保存**。只要转账成功（显示"转账完成"），就算银行系统突然断电，再次开机后，你和朋友的余额还是"扣完、到账后"的数字，不会回到转账前的状态。

一旦事务提交，其结果就会永久保存，即使系统发生故障也不会丢失。

## [10.4 如何开启事务？](#_10-4-如何开启事务)

开启事务就像是"开会前说'现在开始开会'"，告诉数据库"接下来的操作要打包算一个整体"。

在MySQL中，开启事务有两种常用方式：

```
-- 方式一：通用语句
BEGIN TRANSACTION;

-- 方式二：简化语句（更常用）
START TRANSACTION;
```

这两种方式功能完全一样，`START TRANSACTION`更常用一些，因为少写几个字母。

开启事务后，接下来写的SQL操作（比如"扣钱""到账"）**不会立刻生效**，要等后续"提交"才会真正保存。这就给"出问题时回滚"留了机会。

## [10.5 COMMIT / ROLLBACK 怎么用](#_10-5-commit-rollback-怎么用)

开启事务后，我们需要根据操作的结果来决定是"确认"还是"取消"。这就像是做事要留后路一样。

### [COMMIT —— 没问题就提交](#commit-——-没问题就提交)

如果所有操作都成功执行了，就用`COMMIT`来让所有操作正式生效：

```
COMMIT;
```

这相当于在会议结束时说"今天内容确认，大家执行"，让所有操作正式生效，数据永久保存。

### [ROLLBACK —— 出问题就回滚](#rollback-——-出问题就回滚)

如果在执行过程中发现任何问题，就用`ROLLBACK`来撤销所有操作：

```
ROLLBACK;
```

这相当于在会议中发现错误时说"刚才内容不算，重新来"，让所有操作回到"开启事务前"的状态，数据不会乱。

### [什么时候需要手动包事务？](#什么时候需要手动包事务)

**当你需要执行多个关联操作时**，必须先开启事务，再写操作语句，最后根据结果提交或回滚。比如：

- 转账操作（扣钱+到账）
- 下单操作（生成订单+减库存）
- 用户注册（创建用户+分配权限）

## [10.6 简单事务场景示例：下单扣库存](#_10-6-简单事务场景示例-下单扣库存)

让我们通过一个完整的电商下单例子来理解事务的实际应用。

### [场景描述](#场景描述)

用户买1件衣服，需要完成两个步骤：

1. 生成订单（记录谁买了什么）
2. 减少1件库存（衣服被买走了）

这两个步骤少一步都不行，必须打包在事务中执行。

### [准备数据](#准备数据)

首先，我们需要创建相关的表：

```
-- 创建商品表
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建订单表
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- 插入测试数据
INSERT INTO products (name, price, stock) VALUES 
('时尚T恤', 99.00, 10),
('牛仔裤', 199.00, 5);

-- 查看初始数据
SELECT '商品初始库存:' AS info;
SELECT * FROM products;
```

### [完整的事务操作](#完整的事务操作)

现在让我们看看完整的事务操作过程：

```
-- 步骤1：开启事务
START TRANSACTION;

-- 步骤2：执行操作（生成订单）
INSERT INTO orders (product_id, quantity, total_amount, status) 
VALUES (1, 1, 99.00, 'completed');

-- 步骤3：执行操作（减库存）
UPDATE products SET stock = stock - 1 WHERE id = 1;

-- 步骤4：检查结果
-- 如果上面两步都没报错（比如库存足够），就提交
COMMIT;

-- 如果第二步报错（比如库存只剩0了），就回滚
-- ROLLBACK;
```

### [验证结果](#验证结果)

让我们看看事务执行后的结果：

```
-- 查看订单是否生成
SELECT '生成的订单:' AS info;
SELECT * FROM orders WHERE product_id = 1;

-- 查看库存是否减少
SELECT '更新后的库存:' AS info;
SELECT * FROM products WHERE id = 1;
```

### [异常情况演示](#异常情况演示)

现在让我们模拟一下库存不足的情况，看看事务如何回滚：

```
-- 先重置库存为0
UPDATE products SET stock = 0 WHERE id = 1;

-- 开启事务
START TRANSACTION;

-- 生成订单（这一步会成功）
INSERT INTO orders (product_id, quantity, total_amount, status) 
VALUES (1, 1, 99.00, 'completed');

-- 尝试减库存（这一步会失败，因为库存已经是0）
UPDATE products SET stock = stock - 1 WHERE id = 1;

-- 检查受影响的行数
SELECT ROW_COUNT() AS affected_rows;

-- 如果减库存失败，回滚整个事务
ROLLBACK;

-- 验证订单是否被取消
SELECT '回滚后的订单:' AS info;
SELECT * FROM orders WHERE product_id = 1;

-- 验证库存是否保持不变
SELECT '回滚后的库存:' AS info;
SELECT * FROM products WHERE id = 1;
```

你会发现，即使订单生成成功了，但因为库存减失败，整个事务被回滚了，订单也被取消了，库存保持不变。这就避免了"有订单没库存"的混乱情况。

## [练习题](#练习题)

### [练习1：银行转账事务](#练习1-银行转账事务)

创建一个银行转账事务，从账户"A001"向账户"B001"转账500元。要求在应用代码中检查余额是否充足，如果余额不足则回滚事务，转账成功后显示两个账户的余额。

查看答案

```
-- 应用代码逻辑：先检查余额是否充足
SELECT balance FROM accounts WHERE account_number = "A001";

-- 如果余额充足（>= 500），则执行转账事务
START TRANSACTION;

-- 从转出账户扣除金额
UPDATE accounts SET balance = balance - 500.00 
WHERE account_number = "A001" AND balance >= 500.00;

-- 检查扣除是否成功（在应用代码中检查 ROW_COUNT()）
-- 如果 ROW_COUNT() > 0，说明扣除成功，继续执行转入操作
UPDATE accounts SET balance = balance + 500.00 
WHERE account_number = "B001";

-- 检查转入是否成功（在应用代码中检查 ROW_COUNT()）
-- 如果 ROW_COUNT() > 0，说明转入成功，提交事务
COMMIT;

-- 如果任何一步失败，回滚事务
-- ROLLBACK;

-- 验证转账结果
SELECT account_number, owner_name, balance 
FROM accounts 
WHERE account_number IN ("A001", "B001");
```

### [练习2：商品下单事务](#练习2-商品下单事务)

创建一个商品下单事务，用户购买2件商品ID为1的商品。要求在应用代码中检查库存是否充足，如果库存不足则回滚事务，下单成功后更新库存并显示订单信息。

查看答案

```
-- 应用代码逻辑：先检查库存是否充足
SELECT stock FROM products WHERE id = 1;

-- 如果库存充足（>= 2），则执行下单事务
START TRANSACTION;

-- 生成订单
INSERT INTO orders (product_id, quantity, total_amount, status)
VALUES (1, 2, (SELECT price * 2 FROM products WHERE id = 1), "completed");

-- 检查订单是否生成成功（在应用代码中检查 ROW_COUNT()）
-- 如果 ROW_COUNT() > 0，说明订单生成成功，继续更新库存
UPDATE products SET stock = stock - 2 WHERE id = 1;

-- 检查库存是否更新成功（在应用代码中检查 ROW_COUNT()）
-- 如果 ROW_COUNT() > 0，说明库存更新成功，提交事务
COMMIT;

-- 如果任何一步失败，回滚事务
-- ROLLBACK;

-- 显示下单结果
SELECT "最新订单:" AS info;
SELECT * FROM orders ORDER BY id DESC LIMIT 1;

SELECT "商品库存:" AS info;
SELECT * FROM products WHERE id = 1;
```

### [练习3：批量更新事务](#练习3-批量更新事务)

创建一个批量更新商品价格的事务，将所有"手机"分类的商品价格上调10%。要求在应用代码中记录更新前的商品信息，更新后显示价格变化情况，如果过程中出现错误则全部回滚。

查看答案

```
-- 应用代码逻辑：先查询要更新的商品信息
SELECT id, name, price, category FROM products WHERE category = "手机";

-- 如果找到手机分类商品，则执行批量更新事务
START TRANSACTION;

-- 更新手机价格
UPDATE products 
SET price = price * 1.10 
WHERE category = "手机";

-- 检查更新是否成功（在应用代码中检查 ROW_COUNT()）
-- 如果 ROW_COUNT() > 0，说明更新成功，提交事务
COMMIT;

-- 如果更新失败，回滚事务
-- ROLLBACK;

-- 显示价格变化情况（对比更新前后的数据）
-- 这里需要应用代码保存更新前的数据进行对比
SELECT id, name, category, price AS new_price
FROM products 
WHERE category = "手机"
ORDER BY name;
```

## [常见坑](#常见坑)

### [坑1：忘记开启事务或提交/回滚](#坑1-忘记开启事务或提交-回滚)

最常见的错误是执行多个相关操作时没有使用事务，或者开启了事务但忘记提交或回滚。

**错误示例**：

```
-- 错误：没有使用事务，可能导致数据不一致
UPDATE accounts SET balance = balance - 100 WHERE account_number = 'A001';
UPDATE accounts SET balance = balance + 100 WHERE account_number = 'B001';
```

**纠正方法**：

```
-- 正确：使用事务确保数据一致性
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_number = 'A001';
UPDATE accounts SET balance = balance + 100 WHERE account_number = 'B001';
COMMIT;
```

### [坑2：事务过长影响性能](#坑2-事务过长影响性能)

事务包含太多操作或运行时间过长，会占用系统资源并影响并发性能。

**性能问题示例**：

```
-- 事务过长，影响性能
START TRANSACTION;
-- 批量更新大量数据
UPDATE products SET price = price * 1.05;
-- 批量插入大量数据
INSERT INTO order_items SELECT * FROM temp_order_items;
COMMIT;
```

**纠正方法**：

```
-- 分批处理，减少事务粒度
START TRANSACTION;
UPDATE products SET price = price * 1.05 WHERE id BETWEEN 1 AND 1000;
COMMIT;

START TRANSACTION;
UPDATE products SET price = price * 1.05 WHERE id BETWEEN 1001 AND 2000;
COMMIT;
```

### [坑3：忽略事务隔离级别](#坑3-忽略事务隔离级别)

不了解事务隔离级别，可能导致并发操作时出现脏读、不可重复读等问题。

**问题示例**：

```
-- 会话1：开始事务但未提交
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_number = 'A001';
-- 还未提交

-- 会话2：可能读取到未提交的数据（脏读）
SELECT balance FROM accounts WHERE account_number = 'A001';
```

**纠正方法**：

```
-- 设置合适的隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT balance FROM accounts WHERE account_number = 'A001';
COMMIT;
```

## [速记卡](#速记卡)

- **事务**：多个SQL操作的"打包"，要么全成功，要么全失败
- **原子性**：事务不可分割，不会出现中间状态
- **一致性**：事务前后数据始终保持一致和正确
- **隔离性**：多个事务互不干扰，并发执行时各自独立
- **持久性**：事务提交后，结果永久保存，不会丢失
- **START TRANSACTION**：开启事务，告诉数据库要打包操作
- **COMMIT**：提交事务，让所有操作正式生效
- **ROLLBACK**：回滚事务，撤销所有操作
- **适用场景**：转账、下单、注册等需要多步操作的业务
- **核心价值**：避免数据混乱，保证业务逻辑的正确性

## [章节总结](#章节总结)

在这一章中，我们学习了数据库事务这一重要的概念和技术。事务通过ACID特性确保了数据操作的可靠性和一致性，是构建可靠业务系统的基础。

我们从事务的必要性开始，通过生活中的例子理解了为什么需要事务——当多个操作需要作为一个整体执行时，事务能够确保要么全部成功，要么全部失败，避免出现数据混乱的情况。

通过"转账"和"下单"的具体例子，我们深入理解了ACID四个特性的含义和重要性。原子性确保操作的不可分割性，一致性保证数据的正确性，隔离性让并发事务互不干扰，持久性确保结果的永久保存。

我们学习了如何开启事务、使用COMMIT提交事务、使用ROLLBACK回滚事务，以及在实际业务中如何应用事务技术。通过银行转账、用户注册、批量更新等实际例子，我们看到了事务在真实业务场景中的重要作用。

事务的正确使用对于构建可靠的业务系统至关重要。在实际开发中，需要根据业务需求合理设计事务边界，平衡数据一致性和系统性能，避免常见的事务错误和性能问题。

掌握了事务技术，你就能够构建更加可靠和安全的数据操作，为业务系统提供坚实的数据基础。在下一章中，我们将学习SQL函数的使用，这将让我们能够进行更加丰富的数据处理和计算。敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [10｜事务：如何保证一组操作要么都成功？](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-事务-如何保证一组操作要么都成功)
- [10.1 为什么需要事务？](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-1-为什么需要事务)
- [10.2 什么是事务？](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-2-什么是事务)
- [10.3 事务的 ACID 特性](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-3-事务的-acid-特性)
- [原子性（Atomicity）](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#原子性-atomicity)
- [一致性（Consistency）](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#一致性-consistency)
- [隔离性（Isolation）](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#隔离性-isolation)
- [持久性（Durability）](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#持久性-durability)
- [10.4 如何开启事务？](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-4-如何开启事务)
- [10.5 COMMIT / ROLLBACK 怎么用](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-5-commit-rollback-怎么用)
- [COMMIT —— 没问题就提交](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#commit-——-没问题就提交)
- [ROLLBACK —— 出问题就回滚](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#rollback-——-出问题就回滚)
- [什么时候需要手动包事务？](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#什么时候需要手动包事务)
- [10.6 简单事务场景示例：下单扣库存](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#_10-6-简单事务场景示例-下单扣库存)
- [场景描述](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#场景描述)
- [准备数据](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#准备数据)
- [完整的事务操作](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#完整的事务操作)
- [验证结果](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#验证结果)
- [异常情况演示](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#异常情况演示)
- [练习题](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#练习题)
- [练习1：银行转账事务](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#练习1-银行转账事务)
- [练习2：商品下单事务](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#练习2-商品下单事务)
- [练习3：批量更新事务](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#练习3-批量更新事务)
- [常见坑](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#常见坑)
- [坑1：忘记开启事务或提交/回滚](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#坑1-忘记开启事务或提交-回滚)
- [坑2：事务过长影响性能](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#坑2-事务过长影响性能)
- [坑3：忽略事务隔离级别](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#坑3-忽略事务隔离级别)
- [速记卡](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part2/10-transactions.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
