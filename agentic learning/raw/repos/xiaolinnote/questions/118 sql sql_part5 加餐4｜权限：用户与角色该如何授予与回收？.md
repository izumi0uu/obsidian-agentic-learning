---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html"
source: "https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html"
last_checked: 2026-05-07
freshness: watch
sha256: 5b540e36ce653ae6a14bd7f938bdc7b3d4a8fb138a65c75926713856d2011058
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 加餐4｜权限：用户与角色该如何授予与回收？

原始链接：https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 17 分钟约 5241 字2025/8/31

---


大家好，我是小林。

在前面的学习中，我们主要关注了如何查询和操作数据。但是你有没有想过，在实际的生产环境中，不同的用户应该有不同的操作权限？比如，客服人员只能查看用户信息和订单状态，财务人员可以查看订单金额但不能修改用户数据，而数据库管理员则拥有所有权限。

想象一下，如果一个电商系统的数据库权限设置不当，普通用户竟然能够删除订单数据，或者客服人员能够看到用户的支付密码，这会造成多么严重的安全问题！又或者，一个新入职的员工需要访问数据库，你不知道该给他什么权限，给太多有安全风险，给太少又影响工作效率。

在实际工作中，数据库权限管理是一个非常重要但又容易被忽视的话题。合理的权限管理既能保证数据安全，又能提高工作效率。就像一栋大楼，不同的人有不同的门禁卡，有的只能进入公共区域，有的可以进入办公区域，只有少数人可以进入核心机房。

在这一章中，我们将学习MySQL的用户权限管理，包括账号模型的理解、基本的权限操作命令、如何设计角色模板，以及生产环境中的权限变更最佳实践。准备好了吗？让我们一起学习如何成为数据库的"门禁管理员"吧！

## [账号模型](#账号模型)

MySQL的用户账号模型可能和你想象的不太一样。在其他系统中，我们通常只需要一个用户名，但在MySQL中，一个完整的用户标识是`'用户名'@'主机名'`的格式。

### [user@host 的含义](#user-host-的含义)

这个格式看起来有点奇怪，为什么要包含主机名呢？这其实是MySQL的一个重要安全特性。`'用户名'@'主机名'`表示"从特定主机连接的特定用户"。比如：

```
'admin'@'localhost'        -- 只能从本地连接的admin用户
'admin'@'192.168.1.100'   -- 只能从192.168.1.100这个IP连接的admin用户
'admin'@'%'              -- 可以从任何主机连接的admin用户
```

让我们创建几个用户来理解这个概念：

```
-- 创建只能从本地连接的用户
CREATE USER 'local_admin'@'localhost' IDENTIFIED BY 'LocalPass123!';

-- 创建只能从特定IP连接的用户
CREATE USER 'office_user'@'192.168.1.100' IDENTIFIED BY 'OfficePass123!';

-- 创建可以从任何地方连接的用户（开发环境用）
CREATE USER 'app_user'@'%' IDENTIFIED BY 'AppPass123!';
```

创建后，我们可以查看这些用户：

```
SELECT host, user FROM mysql.user;
```

### [来源限制的价值](#来源限制的价值)

这种设计有什么实际价值呢？让我们看几个实际的例子：

**1. 环境隔离**

```
-- 开发环境用户（只能从开发机连接）
CREATE USER 'dev_readonly'@'192.168.1.50' IDENTIFIED BY 'DevRead123!';

-- 测试环境用户（只能从测试服务器连接）
CREATE USER 'test_readonly'@'192.168.1.60' IDENTIFIED BY 'TestRead123!';

-- 生产环境用户（只能从应用服务器连接）
CREATE USER 'prod_app'@'192.168.1.70' IDENTIFIED BY 'ProdApp123!';
```

**2. 权限精细化控制**

```
-- 数据库管理员（只能从管理机连接）
CREATE USER 'dba'@'10.0.0.100' IDENTIFIED BY 'DbaSecure123!';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'10.0.0.100';

-- 应用用户（只能从应用服务器连接）
CREATE USER 'webapp'@'172.16.0.50' IDENTIFIED BY 'WebApp123!';
GRANT SELECT, INSERT, UPDATE ON webapp_db.* TO 'webapp'@'172.16.0.50';

-- 备份用户（只能从备份服务器连接）
CREATE USER 'backup_user'@'192.168.2.100' IDENTIFIED BY 'Backup123!';
GRANT SELECT, LOCK TABLES, RELOAD ON *.* TO 'backup_user'@'192.168.2.100';
```

**3. 安全防护**

```
-- 限制root用户只能从本地连接（重要安全措施）
UPDATE mysql.user SET host = 'localhost' WHERE user = 'root' AND host = '%';
FLUSH PRIVILEGES;

-- 创建远程管理员（从特定IP连接）
CREATE USER 'remote_admin'@' trusted_company_ip' IDENTIFIED BY 'RemoteSecure123!';
GRANT ALL PRIVILEGES ON *.* TO 'remote_admin'@'trusted_company_ip';
```

### [MySQL 8 角色概念](#mysql-8-角色概念)

MySQL 8.0引入了角色的概念，这让权限管理更加方便。角色可以看作是一组权限的集合，我们可以先创建角色，然后把角色授予用户。

```
-- MySQL 8 角色示例
CREATE ROLE 'readonly_role', 'readwrite_role', 'admin_role';

-- 为角色分配权限
GRANT SELECT ON app_db.* TO 'readonly_role';
GRANT SELECT, INSERT, UPDATE, DELETE ON app_db.* TO 'readwrite_role';
GRANT ALL PRIVILEGES ON *.* TO 'admin_role';

-- 将角色授予用户
CREATE USER 'analyst'@'%' IDENTIFIED BY 'Analyst123!';
GRANT 'readonly_role' TO 'analyst'@'%';

CREATE USER 'developer'@'%' IDENTIFIED BY 'Dev123!';
GRANT 'readwrite_role' TO 'developer'@'%';
```

角色的好处是可以批量管理权限，比如修改角色的权限，所有拥有该角色的用户都会自动获得新的权限。

## [最小命令清单](#最小命令清单)

权限管理涉及几个核心命令，让我们通过实际的例子来学习它们。

### [CREATE USER - 创建用户](#create-user-创建用户)

```
-- 基本语法
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

-- 创建具体用户
CREATE USER 'shop_reader'@'localhost' IDENTIFIED BY 'ShopRead123!';
CREATE USER 'shop_writer'@'192.168.1.100' IDENTIFIED BY 'ShopWrite123!';
CREATE USER 'shop_admin'@'localhost' IDENTIFIED BY 'ShopAdmin123!';
```

**注意事项**：

- 密码要符合MySQL的密码策略要求
- 主机名可以用`%`通配符表示任意主机
- 用户创建后默认没有任何权限

### [GRANT - 授予权限](#grant-授予权限)

```
-- 基本语法
GRANT privileges ON database.table TO 'user'@'host';

-- 授予数据库级别的权限
GRANT SELECT ON shop_db.* TO 'shop_reader'@'localhost';
GRANT SELECT, INSERT, UPDATE ON shop_db.* TO 'shop_writer'@'192.168.1.100';
GRANT ALL PRIVILEGES ON shop_db.* TO 'shop_admin'@'localhost';

-- 授予全局权限（谨慎使用）
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP ON *.* TO 'shop_admin'@'localhost';

-- 授予特定表的权限
GRANT SELECT ON shop_db.users TO 'shop_reader'@'localhost';
GRANT SELECT, UPDATE ON shop_db.orders TO 'shop_writer'@'192.168.1.100';

-- 授予列级别的权限
GRANT SELECT (id, username, email), UPDATE (email) ON shop_db.users TO 'shop_writer'@'192.168.1.100';
```

**权限级别**：

- 全局级别：`*.*` （所有数据库的所有表）
- 数据库级别：`database_name.*` （特定数据库的所有表）
- 表级别：`database_name.table_name` （特定表）
- 列级别：`database_name.table_name(column_name)` （特定列）

### [REVOKE - 回收权限](#revoke-回收权限)

```
-- 基本语法
REVOKE privileges ON database.table FROM 'user'@'host';

-- 回收数据库级别权限
REVOKE INSERT, UPDATE ON shop_db.* FROM 'shop_reader'@'localhost';

-- 回收特定表权限
REVOKE SELECT ON shop_db.users FROM 'shop_writer'@'192.168.1.100';

-- 回收所有权限
REVOKE ALL PRIVILEGES ON shop_db.* FROM 'shop_writer'@'192.168.1.100';
```

**注意事项**：

- 回收权限后要记得刷新权限：`FLUSH PRIVILEGES;`
- 某些权限可能需要 CASCADE 选项来回收衍生权限

### [SHOW GRANTS - 查看权限](#show-grants-查看权限)

```
-- 查看用户权限
SHOW GRANTS FOR 'shop_reader'@'localhost';
SHOW GRANTS FOR 'shop_writer'@'192.168.1.100';
SHOW GRANTS FOR 'shop_admin'@'localhost';

-- 查看当前用户权限
SHOW GRANTS FOR CURRENT_USER();
```

执行结果示例：

```
+--------------------------------------------------+
| Grants for shop_reader@localhost                   |
+--------------------------------------------------+
| GRANT USAGE ON *.* TO `shop_reader`@`localhost`  |
| GRANT SELECT ON `shop_db`.* TO `shop_reader`@`localhost` |
+--------------------------------------------------+
```

### [完整的权限管理示例](#完整的权限管理示例)

让我们通过一个完整的例子来演示权限管理的完整流程：

```
-- 步骤1：创建数据库和表
CREATE DATABASE shop_db;
USE shop_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    status VARCHAR(20),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 步骤2：创建用户
CREATE USER 'data_analyst'@'localhost' IDENTIFIED BY 'Analyst123!';
CREATE USER 'customer_service'@'localhost' IDENTIFIED BY 'Service123!';
CREATE USER 'sales_manager'@'localhost' IDENTIFIED BY 'Sales123!';

-- 步骤3：授予权限
-- 数据分析师：只读权限
GRANT SELECT ON shop_db.* TO 'data_analyst'@'localhost';

-- 客服：查看用户和订单，更新订单状态
GRANT SELECT ON shop_db.users TO 'customer_service'@'localhost';
GRANT SELECT, UPDATE (status) ON shop_db.orders TO 'customer_service'@'localhost';

-- 销售经理：读写权限
GRANT SELECT, INSERT, UPDATE, DELETE ON shop_db.* TO 'sales_manager'@'localhost';

-- 步骤4：验证权限
SHOW GRANTS FOR 'data_analyst'@'localhost';
SHOW GRANTS FOR 'customer_service'@'localhost';
SHOW GRANTS FOR 'sales_manager'@'localhost';

-- 步骤5：测试权限（在实际环境中需要切换用户测试）
```

## [最小权限原则与角色模板](#最小权限原则与角色模板)

最小权限原则是信息安全的基本原则：只给用户完成其工作所需的最小权限。这样可以减少安全风险和误操作的可能性。

### [常用角色模板](#常用角色模板)

在实际工作中，我们可以设计一些标准的角色模板：

#### [只读角色模板](#只读角色模板)

```
-- 创建只读角色
CREATE ROLE 'readonly_role';

-- 授予只读权限
GRANT SELECT ON shop_db.* TO 'readonly_role';

-- 将角色授予用户
CREATE USER 'analyst'@'localhost' IDENTIFIED BY 'Analyst123!';
CREATE USER 'reporter'@'localhost' IDENTIFIED BY 'Reporter123!';
GRANT 'readonly_role' TO 'analyst'@'localhost';
GRANT 'readonly_role' TO 'reporter'@'localhost';

-- 激活角色（MySQL 8.0+）
SET DEFAULT ROLE ALL TO 'analyst'@'localhost';
SET DEFAULT ROLE ALL TO 'reporter'@'localhost';
```

#### [读写角色模板](#读写角色模板)

```
-- 创建读写角色
CREATE ROLE 'readwrite_role';

-- 授予读写权限（不包括删除和结构修改）
GRANT SELECT, INSERT, UPDATE ON shop_db.* TO 'readwrite_role';
GRANT DELETE ON shop_db.orders TO 'readwrite_role'; -- 允许删除订单

-- 授予临时表权限（某些应用需要）
GRANT CREATE TEMPORARY TABLES ON shop_db.* TO 'readwrite_role';

-- 将角色授予用户
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'App123!';
CREATE USER 'data_entry'@'localhost' IDENTIFIED BY 'Entry123!';
GRANT 'readwrite_role' TO 'app_user'@'localhost';
GRANT 'readwrite_role' TO 'data_entry'@'localhost';
```

#### [DDL管理员角色模板](#ddl管理员角色模板)

```
-- 创建DDL管理员角色
CREATE ROLE 'ddl_admin_role';

-- 授予DDL权限（表结构修改）
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, INDEX 
ON shop_db.* TO 'ddl_admin_role';

-- 授予查看所有数据库的权限
GRANT SHOW DATABASES ON *.* TO 'ddl_admin_role';

-- 将角色授予用户
CREATE USER 'developer'@'localhost' IDENTIFIED BY 'Dev123!';
GRANT 'ddl_admin_role' TO 'developer'@'localhost';
```

#### [应用专用角色模板](#应用专用角色模板)

```
-- 创建应用专用角色
CREATE ROLE 'app_backend_role';

-- 应用后端需要的权限
GRANT SELECT, INSERT, UPDATE, DELETE ON shop_db.* TO 'app_backend_role';
GRANT CREATE TEMPORARY TABLES ON shop_db.* TO 'app_backend_role';
GRANT EXECUTE ON PROCEDURE shop_db.* TO 'app_backend_role'; -- 存储过程权限

-- 将角色授予应用用户
CREATE USER 'backend_service'@'192.168.1.100' IDENTIFIED BY 'Backend123!';
GRANT 'app_backend_role' TO 'backend_service'@'192.168.1.100';
```

### [角色权限验证](#角色权限验证)

创建角色后，我们需要验证权限是否正确设置：

```
-- 查看角色权限
SHOW GRANTS FOR 'readonly_role';
SHOW GRANTS FOR 'readwrite_role';

-- 查看用户的角色
SHOW GRANTS FOR 'analyst'@'localhost';

-- 查看角色授予情况
SELECT * FROM mysql.role_edges;
```

### [实际应用场景](#实际应用场景)

让我们通过一个实际的电商系统来演示角色权限的应用：

```
-- 场景：电商系统的权限管理

-- 1. 创建数据库
CREATE DATABASE ecommerce;
USE ecommerce;

-- 2. 创建基本表结构
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    stock INT DEFAULT 0,
    category VARCHAR(50)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled'),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- 3. 创建角色模板
CREATE ROLE 'customer_service_role';
CREATE ROLE 'warehouse_role';
CREATE ROLE 'finance_role';
CREATE ROLE 'admin_role';

-- 4. 为角色分配权限
-- 客服角色：查看客户和订单，更新订单状态
GRANT SELECT ON ecommerce.customers TO 'customer_service_role';
GRANT SELECT, UPDATE (status) ON ecommerce.orders TO 'customer_service_role';

-- 仓库角色：查看产品和订单，更新库存
GRANT SELECT ON ecommerce.products TO 'warehouse_role';
GRANT SELECT ON ecommerce.orders TO 'warehouse_role';
GRANT UPDATE (stock) ON ecommerce.products TO 'warehouse_role';

-- 财务角色：查看所有表的财务信息
GRANT SELECT ON ecommerce.customers TO 'finance_role';
GRANT SELECT ON ecommerce.orders TO 'finance_role';
GRANT SELECT (name, price) ON ecommerce.products TO 'finance_role';

-- 管理员角色：所有权限
GRANT ALL PRIVILEGES ON ecommerce.* TO 'admin_role';

-- 5. 创建用户并分配角色
CREATE USER 'cs_agent1'@'localhost' IDENTIFIED BY 'Cs123!';
CREATE USER 'warehouse_mgr'@'localhost' IDENTIFIED BY 'Warehouse123!';
CREATE USER 'finance_officer'@'localhost' IDENTIFIED BY 'Finance123!';
CREATE USER 'system_admin'@'localhost' IDENTIFIED BY 'Admin123!';

GRANT 'customer_service_role' TO 'cs_agent1'@'localhost';
GRANT 'warehouse_role' TO 'warehouse_mgr'@'localhost';
GRANT 'finance_role' TO 'finance_officer'@'localhost';
GRANT 'admin_role' TO 'system_admin'@'localhost';

-- 6. 激活所有角色
SET DEFAULT ROLE ALL TO 'cs_agent1'@'localhost';
SET DEFAULT ROLE ALL TO 'warehouse_mgr'@'localhost';
SET DEFAULT ROLE ALL TO 'finance_officer'@'localhost';
SET DEFAULT ROLE ALL TO 'system_admin'@'localhost';

-- 7. 验证权限设置
SHOW GRANTS FOR 'cs_agent1'@'localhost';
SHOW GRANTS FOR 'warehouse_mgr'@'localhost';
SHOW GRANTS FOR 'finance_officer'@'localhost';
SHOW GRANTS FOR 'system_admin'@'localhost';
```

## [生产变更注意](#生产变更注意)

在生产环境中进行权限变更需要特别谨慎，任何错误都可能导致系统中断或安全问题。

### [变更前准备](#变更前准备)

**1. 导出当前权限状态**

```
-- 导出所有用户的权限
SELECT 
    CONCAT('SHOW GRANTS FOR \'', user, '\'@\'', host, '\';') AS grant_statements
FROM mysql.user
WHERE user NOT IN ('root', 'mysql.sys', 'mysql.session')
ORDER BY user, host;

-- 将结果保存到文件，以便回滚
-- 或者使用 mysqldump
mysqldump -u root -p mysql mysql > mysql_user_backup.sql
```

**2. 选择合适的变更窗口**

```
-- 在低峰期进行变更
-- 避免在业务高峰期修改权限
-- 建议在维护窗口期进行
```

**3. 准备回滚方案**

```
-- 准备回滚脚本
-- 比如：用户创建失败时的回滚语句
DROP USER IF EXISTS 'new_user'@'host';
REVOKE ALL PRIVILEGES ON *.* FROM 'existing_user'@'host';
```

### [权限变更最佳实践](#权限变更最佳实践)

**1. 避免直接修改用户权限**

```
-- 不好的做法：直接修改用户权限
REVOKE SELECT ON app_db.* FROM 'app_user'@'192.168.1.100';
GRANT SELECT, INSERT ON app_db.* TO 'app_user'@'192.168.1.100';

-- 好的做法：通过角色管理
-- 先修改角色权限
REVOKE DELETE ON app_db.* FROM 'readwrite_role';
GRANT SELECT, INSERT ON app_db.* TO 'readwrite_role';
-- 用户的权限会自动更新
```

**2. 使用事务性操作**

```
-- MySQL的权限操作是自动提交的，但我们可以用脚本确保一致性
-- 示例：添加新用户的完整脚本
START TRANSACTION;

-- 创建用户
CREATE USER 'new_user'@'192.168.1.200' IDENTIFIED BY 'SecurePass123!';

-- 授予权限
GRANT 'readonly_role' TO 'new_user'@'192.168.1.200';

-- 激活角色
SET DEFAULT ROLE ALL TO 'new_user'@'192.168.1.200';

-- 验证用户创建成功
SELECT 'User created successfully' as status;

COMMIT;
```

**3. 避免权限冲突**

```
-- 在授予权限前，先清理可能存在的冲突权限
REVOKE ALL PRIVILEGES ON app_db.* FROM 'user'@'host';
GRANT SELECT, INSERT ON app_db.* TO 'user'@'host';
```

### [避免短暂断权](#避免短暂断权)

在修改用户权限时，要避免"先删后加"的操作，这会导致用户在删除和添加之间短暂失去权限。

```
-- 不好的做法：先回收所有权限再重新授予
-- REVOKE ALL PRIVILEGES ON *.* FROM 'app_user'@'%';
-- GRANT SELECT, INSERT ON app_db.* TO 'app_user'@'%';
-- 这样会导致用户在操作期间断权

-- 好的做法：直接修改需要的权限
-- 如果需要减少权限，直接回收特定权限
REVOKE DELETE ON app_db.* FROM 'app_user'@'%';
-- 如果需要增加权限，直接授予新权限
GRANT UPDATE ON app_db.orders TO 'app_user'@'%';
```

### [权限验证脚本](#权限验证脚本)

创建权限验证脚本来确保变更正确：

```
-- 权限验证存储过程
DELIMITER //
CREATE PROCEDURE verify_user_permissions(IN username VARCHAR(50), IN host VARCHAR(50))
BEGIN
    DECLARE user_exists INT;
    
    -- 检查用户是否存在
    SELECT COUNT(*) INTO user_exists 
    FROM mysql.user 
    WHERE user = username AND host = host;
    
    IF user_exists > 0 THEN
        -- 显示用户权限
        SELECT CONCAT('Permissions for ', username, '@', host) as user_info;
        SHOW GRANTS FOR CONCAT(username, '@', host);
    ELSE
        SELECT CONCAT('User ', username, '@', host, ' does not exist') as error;
    END IF;
END //
DELIMITER ;

-- 使用验证过程
CALL verify_user_permissions('app_user', '192.168.1.100');
```

### [监控和审计](#监控和审计)

```
-- 创建权限变更审计表
CREATE TABLE permission_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    username VARCHAR(50),
    hostname VARCHAR(50),
    action VARCHAR(20),
    object_type VARCHAR(20),
    privileges TEXT,
    changed_by VARCHAR(50),
    change_reason TEXT
);

-- 在权限变更时记录审计信息
INSERT INTO permission_audit (username, hostname, action, object_type, privileges, changed_by, change_reason)
VALUES ('new_user', '192.168.1.200', 'GRANT', 'DATABASE', 'SELECT, INSERT', 'admin', '新用户入职');

-- 定期检查权限异常
SELECT 
    user, host, 
    COUNT(*) as privilege_count
FROM mysql.db 
GROUP BY user, host 
HAVING privilege_count > 10; -- 权限过多的用户
```

## [练习题](#练习题)

### [练习1：创建只读用户](#练习1-创建只读用户)

创建一个只能查询shop\_db数据库的用户，用户名为`shop_analyst`，只能从本地连接。

查看答案

```
-- 创建只读用户
CREATE USER 'shop_analyst'@'localhost' IDENTIFIED BY 'AnalystSecure123!';

-- 授予只读权限
GRANT SELECT ON shop_db.* TO 'shop_analyst'@'localhost';

-- 验证权限
SHOW GRANTS FOR 'shop_analyst'@'localhost';

-- 测试权限（切换到该用户测试）
-- mysql -u shop_analyst -p
-- USE shop_db;
-- SELECT * FROM users; -- 应该成功
-- INSERT INTO users VALUES (NULL, 'test', 'test@test.com'); -- 应该失败
```

### [练习2：创建读写角色并授予用户](#练习2-创建读写角色并授予用户)

创建一个读写角色`shop_data_entry`，包含对shop\_db数据库的增删改查权限，并将此角色授予用户`data_operator`。

查看答案

```
-- 创建读写角色
CREATE ROLE 'shop_data_entry';

-- 为角色分配权限
GRANT SELECT, INSERT, UPDATE, DELETE ON shop_db.* TO 'shop_data_entry';

-- 创建用户
CREATE USER 'data_operator'@'localhost' IDENTIFIED BY 'OperatorSecure123!';

-- 将角色授予用户
GRANT 'shop_data_entry' TO 'data_operator'@'localhost';

-- 激活角色
SET DEFAULT ROLE ALL TO 'data_operator'@'localhost';

-- 验证权限
SHOW GRANTS FOR 'data_operator'@'localhost';
```

### [练习3：修改用户权限](#练习3-修改用户权限)

将用户`shop_analyst`的权限修改为只能查询customers表，不能查询其他表。

查看答案

```
-- 先查看当前权限
SHOW GRANTS FOR 'shop_analyst'@'localhost';

-- 回收原有的数据库级别权限
REVOKE SELECT ON shop_db.* FROM 'shop_analyst'@'localhost';

-- 授予特定表的权限
GRANT SELECT ON shop_db.customers TO 'shop_analyst'@'localhost';

-- 验证新权限
SHOW GRANTS FOR 'shop_analyst'@'localhost';

-- 注意：这里使用了直接修改权限的方式，在实际生产环境中，
-- 如果使用角色，应该修改角色权限而不是直接修改用户权限
```

## [常见坑](#常见坑)

### [坑1：密码策略不符合要求](#坑1-密码策略不符合要求)

MySQL 8.0有严格的密码策略要求，简单的密码会导致创建用户失败。

**错误示例**：

```
-- 错误：密码太简单
CREATE USER 'test'@'localhost' IDENTIFIED BY '123456';
```

**纠正方法**：

```
-- 正确：使用强密码
CREATE USER 'test'@'localhost' IDENTIFIED BY 'SecurePass123!';

-- 或者查看当前密码策略
SHOW VARIABLES LIKE 'validate_password%';

-- 临时降低密码策略（仅开发环境）
SET GLOBAL validate_password.policy=LOW;
```

### [坑2：忘记FLUSH PRIVILEGES](#坑2-忘记flush-privileges)

在直接修改权限表后，忘记刷新权限导致权限不生效。

**错误示例**：

```
-- 直接修改mysql.user表
UPDATE mysql.user SET Grant_priv = 'Y' WHERE user = 'test';
-- 忘记刷新权限，权限不生效
```

**纠正方法**：

```
-- 修改权限表后立即刷新
UPDATE mysql.user SET Grant_priv = 'Y' WHERE user = 'test';
FLUSH PRIVILEGES;

-- 更好的做法：使用GRANT/REVOKE命令
GRANT ALL PRIVILEGES ON *.* TO 'test'@'localhost';
```

### [坑3：主机名配置错误](#坑3-主机名配置错误)

用户创建成功但无法连接，通常是因为主机名配置错误。

**错误示例**：

```
-- 创建用户时主机名不匹配
CREATE USER 'app'@'192.168.1.100' IDENTIFIED BY 'pass';
-- 但应用服务器IP是192.168.1.101，导致连接失败
```

**纠正方法**：

```
-- 使用正确的IP或通配符
CREATE USER 'app'@'192.168.1.%' IDENTIFIED BY 'pass'; -- 子网
CREATE USER 'app'@'%' IDENTIFIED BY 'pass'; -- 任意主机（仅开发环境）

-- 或者创建多个主机条目
CREATE USER 'app'@'192.168.1.101' IDENTIFIED BY 'pass';
CREATE USER 'app'@'192.168.1.102' IDENTIFIED BY 'pass';
```

## [速记卡](#速记卡)

- **账号格式**：`'用户名'@'主机名'`，主机名控制来源限制
- **CREATE USER**：创建用户，`CREATE USER 'name'@'host' IDENTIFIED BY 'password'`
- **GRANT**：授予权限，`GRANT privileges ON db.table TO 'user'@'host'`
- **REVOKE**：回收权限，`REVOKE privileges ON db.table FROM 'user'@'host'`
- **SHOW GRANTS**：查看权限，`SHOW GRANTS FOR 'user'@'host'`
- **权限级别**：全局(`*.*`)、数据库(`db.*`)、表(`db.table`)、列(`db.table(col)`)
- **角色**：MySQL 8.0+支持角色，一组权限的集合，便于批量管理
- **最小权限原则**：只给工作所需的最小权限
- **生产变更**：先备份、选择窗口、准备回滚、避免断权
- **安全建议**：限制root远程访问、使用强密码、定期审计权限

## [章节总结](#章节总结)

在这个加餐中，我们学习了MySQL的用户权限管理，这是数据库安全的重要组成部分。我们了解了MySQL独特的账号模型`'用户名'@'主机名'`，这种设计让我们能够精细控制用户从哪里连接数据库，提供了额外的安全层。

通过几个核心命令`CREATE USER`、`GRANT`、`REVOKE`、`SHOW GRANTS`，我们可以完成用户权限的完整管理。我们学习了如何创建用户、授予权限、回收权限和查看权限，以及这些命令在不同权限级别（全局、数据库、表、列）的应用。

最小权限原则是权限管理的核心原则，我们通过角色模板的设计来实现这一原则。我们创建了只读、读写、DDL管理员、应用专用等标准角色模板，这些模板可以根据实际业务需求进行调整，确保每个用户都只拥有完成其工作所需的最小权限。

在生产环境中进行权限变更需要特别谨慎。我们学习了变更前的准备工作（导出权限、选择窗口、准备回滚），变更中的最佳实践（避免直接修改、使用事务性操作、避免权限冲突），以及变更后的验证和监控。这些措施能够确保权限变更的安全性和可靠性。

权限管理是一个持续的过程，需要定期审计和调整。随着业务的发展和人员的变化，我们需要及时更新用户权限，确保既不影响工作效率，又不危及数据安全。掌握了这些权限管理技能，你就能够构建既安全又高效的数据库访问控制体系。

在实际工作中，建议建立完善的权限管理制度，包括权限申请流程、定期审计机制、紧急响应预案等。同时，要结合公司的具体业务需求，设计合适的角色模板和权限分配策略。记住，好的权限管理既能保护数据安全，又能提高工作效率，是数据库管理中不可忽视的重要环节。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [加餐4｜权限：用户与角色该如何授予与回收？](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#加餐4-权限-用户与角色该如何授予与回收)
- [账号模型](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#账号模型)
- [user@host 的含义](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#user-host-的含义)
- [来源限制的价值](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#来源限制的价值)
- [MySQL 8 角色概念](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#mysql-8-角色概念)
- [最小命令清单](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#最小命令清单)
- [CREATE USER - 创建用户](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#create-user-创建用户)
- [GRANT - 授予权限](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#grant-授予权限)
- [REVOKE - 回收权限](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#revoke-回收权限)
- [SHOW GRANTS - 查看权限](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#show-grants-查看权限)
- [完整的权限管理示例](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#完整的权限管理示例)
- [最小权限原则与角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#最小权限原则与角色模板)
- [常用角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#常用角色模板)
- [只读角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#只读角色模板)
- [读写角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#读写角色模板)
- [DDL管理员角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#ddl管理员角色模板)
- [应用专用角色模板](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#应用专用角色模板)
- [角色权限验证](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#角色权限验证)
- [实际应用场景](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#实际应用场景)
- [生产变更注意](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#生产变更注意)
- [变更前准备](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#变更前准备)
- [权限变更最佳实践](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#权限变更最佳实践)
- [避免短暂断权](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#避免短暂断权)
- [权限验证脚本](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#权限验证脚本)
- [监控和审计](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#监控和审计)
- [练习题](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#练习题)
- [练习1：创建只读用户](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#练习1-创建只读用户)
- [练习2：创建读写角色并授予用户](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#练习2-创建读写角色并授予用户)
- [练习3：修改用户权限](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#练习3-修改用户权限)
- [常见坑](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#常见坑)
- [坑1：密码策略不符合要求](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#坑1-密码策略不符合要求)
- [坑2：忘记FLUSH PRIVILEGES](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#坑2-忘记flush-privileges)
- [坑3：主机名配置错误](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#坑3-主机名配置错误)
- [速记卡](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part5/supplement4-permissions.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
