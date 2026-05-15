---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html"
source: "https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html"
last_checked: 2026-05-07
freshness: watch
sha256: 65a16e21f57387136da5bb0df02d75ae8173cf965a8ca7a66b48323406216840
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 01｜入门：数据库与 SQL 到底是什么？

原始链接：https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)SQL大约 24 分钟约 7178 字2025/8/31

---


大家好，我是小林。

欢迎来到SQL学习之旅！在开始之前，我想问你一个问题：你有没有想过，我们每天使用的微信、淘宝、抖音这些APP，它们的海量数据都存在哪里？当你刷朋友圈时，系统是如何快速找到你的好友动态的？当你在淘宝下单时，订单信息是如何被保存和管理的？

答案就是数据库。数据库就像是这些应用程序的"超级记忆管家"，负责存储、管理和检索海量的数据。而SQL，就是我们和这个"记忆管家"对话的语言。想象一下，如果你想让数据库帮你找到某个用户的信息，或者添加一条新的订单记录，你总不能直接对电脑喊话吧？这时候就需要SQL这种标准化的语言来和数据库沟通。

在这一章里，我们会一起探索数据库的奥秘，学习SQL的基本概念，并且亲自动手安装MySQL，完成你的第一个数据库查询。准备好了吗？让我们开始这段SQL学习之旅吧！

## [1.1 什么是数据库与 SQL](#_1-1-什么是数据库与-sql)

数据库本质上就是一个专门用来存储和管理数据的系统。你可以把它想象成一个超级智能的文件柜，这个文件柜不是简单地堆放文件，而是有着严密的组织和结构。

传统的文件存储方式就像把所有文件都扔在一个大箱子里，想要找某个文件时就得翻箱倒柜。而数据库则像是一个专业的图书管理员，它会把相关的数据放在一起，比如用户信息放在一个地方，订单信息放在另一个地方，能够迅速找到你想要的数据，即使数据量很大，确保数据的准确性和完整性，不会出现数据混乱的情况，还允许多个用户同时访问和修改数据而不会互相干扰。

我们学习的是关系型数据库，这是最常用的一种数据库类型。关系型数据库把数据存储在表格中，就像Excel表格一样，但是功能强大得多。

想象一下，在一个典型的电商应用中，数据库会如何组织数据呢？它可能会创建用户表来存储所有用户的基本信息，商品表来存储各种商品的详细信息，还有订单表来记录每一笔交易。每个表都有自己特定的用途，就像不同的文件夹存放不同类型的文件一样。

每个表都由行和列组成。行代表一条具体的记录，比如用户表中的每一行就代表一个真实的用户。列则代表记录的属性，比如用户的姓名、年龄、地址等特征。这种表格化的组织方式让数据变得井井有条，便于管理和查询。

### [表、行、列和主键](#表、行、列和主键)

让我们以一个用户表为例来看看这些概念。

我们需要创建一个简单的用户表来存储用户的基本信息。这个表设计了5个列来存储用户信息。id列作为用户的唯一标识，每个用户都会有一个不同的id，这样就能确保我们能够准确地区分每个用户。name列用来存储用户的名字，email列存储用户的邮箱地址，age列记录用户的年龄，而created\_at列则记录用户信息创建的时间。这种设计既简单又实用，能够满足基本的用户信息管理需求。

```
-- 创建一个简单的用户表
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    age INT,
    created_at TIMESTAMP
);
```

现在让我们向表中插入一些示例数据，看看实际的表格是什么样子：

```
INSERT INTO users VALUES 
(1, '张三', 'zhangsan@example.com', 25, '2025-01-01 10:00:00'),
(2, '李四', 'lisi@example.com', 30, '2025-01-02 11:00:00'),
(3, '王五', 'wangwu@example.com', 28, '2025-01-03 12:00:00');
```

查询表中的所有数据：

```
SELECT * FROM users;
```

执行结果如下：

```
+----+--------+---------------------+------+---------------------+
| id | name   | email               | age  | created_at          |
+----+--------+---------------------+------+---------------------+
|  1 | 张三   | zhangsan@example.com |   25 | 2025-01-01 10:00:00 |
|  2 | 李四   | lisi@example.com    |   30 | 2025-01-02 11:00:00 |
|  3 | 王五   | wangwu@example.com  |   28 | 2025-01-03 12:00:00 |
+----+--------+---------------------+------+---------------------+
```

在这个例子中，每一行代表一个用户，每一列代表用户的一个属性。主键是一个特殊的概念，它是表中每一行的唯一标识。就像身份证号码一样，主键的值在整个表中必须是唯一的，不能重复。在上面的例子中，id列就是主键。

主键的作用非常重要，它确保每条记录都能被唯一识别，就像每个人的身份证号码都是独一无二的。数据库可以通过主键快速定位到特定的记录，大大提高了查询效率。此外，主键还在不同的表之间建立关联关系，让数据能够有机地联系在一起。比如，我们可以在订单表中存储用户的主键，这样就能轻松地找到每个订单对应的用户信息。

### [什么是SQL？](#什么是sql)

SQL（Structured Query Language，结构化查询语言）是用来操作关系型数据库的标准语言。通过SQL，我们可以告诉数据库要做什么，比如从数据库中查询需要的信息，向数据库中添加新的记录，修改现有的数据，删除不需要的记录，创建新的数据表，或者修改表的结构。SQL就像是我们与数据库沟通的桥梁，让我们能够用标准化的方式来管理数据。

SQL的优势在于它的简洁性和标准化。不管你使用MySQL、PostgreSQL、SQL Server还是Oracle，基本的SQL语法都是相通的。学会了SQL，你就可以操作各种不同的关系型数据库，这种"一次学习，多处使用"的特性让SQL成为了数据库领域的通用语言。

### [SQL与NoSQL的区别](#sql与nosql的区别)

虽然我们主要学习关系型数据库和SQL，但了解一下NoSQL也是有益的。NoSQL（Not Only SQL）是非关系型数据库的总称，它们与关系型数据库有着不同的设计理念。

关系型数据库就像一个有着严格规则的图书馆，所有书籍都必须按照统一的分类标准摆放，每本书都有固定的位置。这种结构化的存储方式确保了数据的一致性和完整性，特别适合需要复杂查询和事务处理的场景，比如银行系统中的转账操作。

而非关系型数据库则像一个更加灵活的仓库，你可以用不同的方式存放物品，有的按类别堆放，有的按时间顺序排列，还有的按物品之间的关系摆放。这种灵活性让NoSQL特别适合大数据量、高并发、结构多变的场景，比如社交媒体应用中用户发帖、点赞等非结构化数据的存储。

那么如何选择呢？如果你的应用需要严格的数据一致性和复杂的事务处理，比如财务系统、企业ERP等，关系型数据库是更好的选择。如果你的应用需要处理大量非结构化数据，对扩展性要求很高，比如大数据分析、物联网应用等，那么NoSQL可能更适合。

对于初学者来说，我建议先掌握SQL和关系型数据库，因为它们有着更成熟的理论基础和更广泛的应用场景。等你掌握了SQL之后，再学习NoSQL会更容易理解，因为你已经有了数据库思维的基础。

## [1.2 安装 MySQL 与客户端工具](#_1-2-安装-mysql-与客户端工具)

现在我们知道了数据库和SQL的基本概念，接下来让我们动手安装MySQL。MySQL是最流行的开源关系型数据库之一，功能强大且易于使用，是学习SQL的理想选择。

安装MySQL有几种方式，你可以根据自己的情况选择最适合的一种。

### [Mac 安装 MySQL](#mac-安装-mysql)

如果你使用的是Mac电脑，Homebrew是最简单的安装方式。Homebrew是Mac的包管理器，可以帮你轻松安装各种软件。首先检查是否已经安装了Homebrew：

```
brew --version
```

如果已经安装，你会看到Homebrew的版本信息。如果没有安装，可以使用以下命令安装：

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装完Homebrew后，就可以一键安装MySQL了：

```
brew install mysql
```

安装完成后，启动MySQL服务：

```
brew services start mysql
```

检查MySQL是否运行正常：

```
mysql --version
```

你会看到类似这样的输出：

```
mysql  Ver 8.0.33 for macos13.0 on x86_64 (Homebrew)
```

MySQL官方提供了各种操作系统的安装包，这是最传统的安装方式。对于Mac用户，可以访问MySQL官网下载macOS版本的DMG安装包，双击安装包，按照提示完成安装，安装过程中会要求设置root密码，请务必记住这个密码。

### [Windows 安装 MySQL](#windows-安装-mysql)

对于Windows用户来说，安装MySQL最简单的方式就是使用官方提供的MSI安装包。这种图形化的安装方式就像安装普通的Windows软件一样，只需要按照向导一步步操作就能完成安装。让我来详细介绍整个安装过程。

首先，我们需要打开[MySQL官方网站的下载页面](https://dev.mysql.com/downloads/installer/)。在浏览器中访问：[dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)，你会看到两个版本的MySQL Installer：web版本和完整版本。web版本体积较小，但在安装过程中需要联网下载组件；完整版本体积较大，但包含了所有需要的组件，可以离线安装。我建议选择完整版本，这样可以避免网络问题导致的安装失败。

下载完成后，双击运行MSI安装包。这时你会看到MySQL安装向导的欢迎界面，点击"Next"继续。接下来，安装程序会显示几种安装类型供你选择：

- Developer Default（开发者默认）：包含MySQL服务器、客户端工具以及开发所需的库和头文件
- Server only（仅服务器）：只安装MySQL服务器
- Client only（仅客户端）：只安装客户端工具
- Full（完整）：安装所有MySQL产品和功能
- Custom（自定义）：自己选择要安装的组件

对于初学者来说，我建议选择"Developer Default"，这样既能学习MySQL服务器，又能使用图形化管理工具。选择后点击"Next"，安装程序会检查依赖项，如果缺少某些组件会提示你安装。

接下来是最重要的配置环节。安装程序会显示"Products and Features"界面，这里列出了将要安装的组件。你可以保持默认设置，点击"Execute"开始安装。安装过程可能需要几分钟时间，具体取决于你的电脑性能。

安装完成后，会进入"Product Configuration"阶段。首先是MySQL Server的配置：

1. **Type and Networking**：选择配置类型。对于学习环境，选择"Development Computer"即可，这样MySQL会使用较少的系统资源。网络配置保持默认的TCP/IP端口3306。
2. **Accounts and Roles**：这是最关键的一步，需要设置root用户的密码。root是MySQL的超级管理员账户，拥有所有权限。请务必设置一个强密码，包含大小写字母、数字和特殊字符，并且要牢记这个密码。你还可以添加其他用户账户，但对于初学者，设置好root密码就足够了。
3. **Windows Service**：配置MySQL作为Windows服务运行。保持默认设置，将MySQL配置为在系统启动时自动运行，这样每次开机后MySQL就会自动启动，无需手动启动。

配置完成后，点击"Execute"应用配置。完成后点击"Finish"结束配置过程。

安装程序还会安装其他组件，比如MySQL Shell和MySQL Workbench。MySQL Shell是一个命令行工具，MySQL Workbench则是图形化管理工具，对于初学者来说非常友好。

安装完成后，我们需要验证MySQL是否安装成功。打开命令提示符（按Win+R，输入cmd，回车），输入以下命令：

```
mysql --version
```

如果显示MySQL的版本信息，说明安装成功。接下来测试连接：

```
mysql -u root -p
```

系统会提示你输入密码，输入你之前设置的root密码。如果看到"mysql>"提示符，恭喜你，MySQL安装成功了！

如果你更喜欢图形化界面，可以启动MySQL Workbench。点击"Database"菜单，选择"Connect to Database"，输入连接信息：

- Hostname：localhost
- Port：3306
- Username：root
- Password：你设置的root密码

点击"Test Connection"测试连接，如果显示"Successfully made the MySQL connection"，说明配置正确。

有时候你可能会遇到一些问题。比如，如果在连接时出现"Access denied"错误，可能是密码输入错误；如果出现"Can't connect to MySQL server"错误，可能是MySQL服务没有启动。这时你可以打开Windows的服务管理器（services.msc），找到MySQL服务，确保它处于"正在运行"状态。

对于Windows 10用户，如果遇到安装失败的问题，可能需要以管理员身份运行安装程序。右键点击MSI安装包，选择"以管理员身份运行"。

安装完成后，建议你设置环境变量，这样就可以在任何目录下使用mysql命令。右键点击"此电脑"选择"属性"，然后点击"高级系统设置"，在"环境变量"中找到"Path"变量，添加MySQL的bin目录路径（通常是`C:\Program Files\MySQL\MySQL Server 8.0\bin`）。

现在你已经成功在Windows上安装了MySQL，可以开始你的SQL学习之旅了！建议同时安装MySQL Workbench，它提供了直观的图形界面，特别适合初学者学习使用。

### [Linux 安装 MySQL](#linux-安装-mysql)

Linux用户（以Ubuntu为例）可以使用系统的包管理器安装：

```
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
```

如果你已经熟悉Docker，这是最干净的安装方式，不会污染你的系统环境。首先确保你已经安装了Docker，然后运行以下命令：

```
docker run --name mysql8 -e MYSQL_ROOT_PASSWORD=your_password -p 3306:3306 -d mysql:8.0
```

这个命令会创建一个名为mysql8的容器，设置root密码为your\_password（记得替换成你自己的密码），将容器的3306端口映射到主机的3306端口，使用MySQL 8.0版本。这样你就可以在容器中运行MySQL，同时通过主机的3306端口访问它。

### [验证安装](#验证安装)

无论你选择哪种安装方式，都可以通过以下方式验证MySQL是否安装成功：

```
mysql -u root -p
```

系统会提示你输入密码，输入你设置的root密码后，如果看到类似下面的欢迎信息，说明安装成功：

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.33 MySQL Community Server - GPL

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

输入`\q`或`exit`可以退出MySQL命令行。

### [客户端工具选择](#客户端工具选择)

虽然MySQL命令行工具功能完整，但对于初学者来说，图形化界面工具更加友好。让我为你介绍几个常用的MySQL客户端工具，你可以根据自己的需求选择合适的工具。

[MySQL Workbench](https://dev.mysql.com/downloads/workbench/)是MySQL官方提供的图形化管理工具，功能强大且完全免费。作为官方出品的产品，它的兼容性是最好的，几乎支持MySQL的所有功能。不过正因为它功能太全面，界面相对复杂，初学者可能需要一些时间来适应。而且它的资源占用也比较大，如果你的电脑配置不高，可能会感觉有些卡顿。

[DBeaver](https://dbeaver.io/download/)是一个免费开源的数据库管理工具，我个人特别推荐给初学者。它最大的优势是完全免费且没有功能限制，同时支持多种数据库，包括MySQL、PostgreSQL、Oracle等。界面设计简洁直观，对于新手来说很容易上手。不过它是基于Java开发的，启动速度相对较慢，某些高级功能可能不如专业的商业工具。

对于Mac用户，[Sequel Ace](https://sequel-ace.com/)是一个很好的选择。这是一个轻量级的免费MySQL客户端，启动快速，界面简洁，完全免费。不过它只支持Mac系统，功能也相对简单，但对于学习SQL来说已经足够了。

对于初学者，我推荐什么配置呢？我个人建议使用MySQL 8.0+作为数据库，可以通过官方安装包安装。客户端工具方面，我推荐DBeaver，它免费且功能完整，特别适合新手。如果你是Mac用户，Sequel Ace也是一个很好的选择，更加轻量级。这样的配置既简单易用，又足够应对学习过程中的各种需求。等你熟悉了基本操作后，可以根据需要尝试其他工具。

无论你选择哪种客户端工具，都需要配置连接信息。通常需要设置Host为localhost（如果数据库安装在本地），Port为3306（MySQL默认端口），User为root（管理员账号），Password为你设置的root密码，Database可以留空，连接后再选择。

配置完成后，记得测试连接，如果成功，你就可以开始使用MySQL了！

## [1.3 连接数据库与首个查询](#_1-3-连接数据库与首个查询)

现在我们已经安装好了MySQL和客户端工具，是时候连接数据库并执行我们的第一个SQL查询了。这一步非常重要，它标志着你正式踏入了SQL的世界！

### [连接数据库的基本方法](#连接数据库的基本方法)

首先让我们学习最基本的连接方式——使用命令行工具。打开你的终端（Mac/Linux）或命令提示符（Windows），输入以下命令：

```
mysql -u root -p
```

这里的参数含义是：`-u root`指定用户名为root，`-p`提示输入密码。

输入你之前设置的root密码后，如果一切正常，你会看到MySQL的欢迎界面：

```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.33 MySQL Community Server - GPL

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

看到`mysql>`提示符，恭喜你！你已经成功连接到MySQL服务器了。

如果你使用的是图形化客户端工具（如DBeaver、MySQL Workbench等），连接步骤如下：打开客户端工具，点击"新建连接"或"New Connection"，选择MySQL作为数据库类型，填写连接信息：Host设置为localhost，Port设置为3306，User设置为root，Password设置为你设置的root密码，Database可以留空。点击"测试连接"或"Test Connection"，如果测试成功，点击"保存"并连接。

### [你的第一个SQL查询](#你的第一个sql查询)

现在我们已经连接到数据库了，让我们执行一个最简单的SQL查询。在MySQL命令行或图形化工具的查询编辑器中输入：

```
SELECT 1;
```

然后按回车键执行。你会看到类似这样的结果：

```
+---+
| 1 |
+---+
| 1 |
+---+
1 row in set (0.00 sec)
```

恭喜你！这是你的第一个SQL查询！虽然它很简单，但它证明了你的SQL环境工作正常。这个查询的作用就是返回数字1，通常用来测试数据库连接是否正常。

### [理解数据库和表的概念](#理解数据库和表的概念)

在实际工作中，我们通常需要操作具体的数据表。但在开始之前，我们需要理解一个重要概念：数据库服务器可以包含多个数据库，每个数据库可以包含多个表。

让我们先查看当前有哪些数据库：

```
SHOW DATABASES;
```

执行结果如下：

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)
```

这些是MySQL系统自带的数据库，用于存储系统信息。现在让我们创建一个自己的数据库：

```
CREATE DATABASE my_first_db;
```

执行成功后，再次查看数据库列表：

```
SHOW DATABASES;
```

你会看到新创建的数据库：

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| my_first_db        |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)
```

要操作某个数据库中的表，首先需要"使用"这个数据库：

```
USE my_first_db;
```

执行成功后，你会看到提示：

```
Database changed
```

现在我们就在`my_first_db`数据库中了，接下来的所有操作都会在这个数据库中进行。

### [创建第一个表](#创建第一个表)

让我们创建一个简单的用户表：

```
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

这个创建语句定义了一个包含5个列的表：id是整数类型，主键，自动增长；name是字符串类型，最大长度50，不能为空；email是字符串类型，最大长度100，值必须唯一；age是整数类型；created\_at是时间戳类型，默认值为当前时间。

让我们验证表是否创建成功：

```
SHOW TABLES;
```

你会看到：

```
+----------------------+
| Tables_in_my_first_db |
+----------------------+
| users                |
+----------------------+
1 row in set (0.00 sec)
```

查看表的结构：

```
DESCRIBE users;
```

输出结果：

```
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| name       | varchar(50)  | NO   |     | NULL              |                   |
| email      | varchar(100) | YES  | UNI | NULL              |                   |
| age        | int          | YES  |     | NULL              |                   |
| created_at | timestamp    | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)
```

### [插入和查询数据](#插入和查询数据)

现在让我们向表中插入一些数据：

```
INSERT INTO users (name, email, age) VALUES 
('张三', 'zhangsan@example.com', 25),
('李四', 'lisi@example.com', 30),
('王五', 'wangwu@example.com', 28);
```

执行成功后，你会看到：

```
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

现在让我们查询刚刚插入的数据：

```
SELECT * FROM users;
```

执行结果：

```
+----+--------+---------------------+------+---------------------+
| id | name   | email               | age  | created_at          |
+----+--------+---------------------+------+---------------------+
|  1 | 张三   | zhangsan@example.com |   25 | 2025-08-31 10:30:00 |
|  2 | 李四   | lisi@example.com    |   30 | 2025-08-31 10:30:00 |
|  3 | 王五   | wangwu@example.com  |   28 | 2025-08-31 10:30:00 |
+----+--------+---------------------+------+---------------------+
3 rows in set (0.00 sec)
```

这就是你的第一个真正的数据查询！这个查询使用了`SELECT * FROM users`，其中`SELECT *`选择所有列，`FROM users`从users表中查询。

### [常见连接问题及解决方法](#常见连接问题及解决方法)

在连接数据库时，你可能会遇到一些问题。以下是最常见的几个问题及其解决方法：

如果你看到类似"`Access denied for user 'root'@'localhost`'"的错误，说明密码输入错误。仔细检查密码是否正确，如果忘记密码，需要重置MySQL的root密码。

如果看到"`Can't connect to MySQL server on 'localhost'`"错误，可能是MySQL服务没有启动。

- 对于Mac用户，可以运行`brew services start mysql`；
- Windows用户可以在服务管理器中启动MySQL服务；
- Linux用户可以运行`sudo systemctl start mysql`。

如果MySQL无法在默认端口3306上启动，可能是因为端口被其他程序占用。查看端口占用情况：`lsof -i :3306`，关闭占用端口的程序，或者修改MySQL的配置文件使用其他端口。

有时候即使密码正确，也可能因为权限问题无法连接。确保root用户有从localhost连接的权限，如果需要，可以重新授权：`GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';`。

当你无法连接数据库时，可以按照以下步骤快速排查问题：检查账号密码是否正确，确认用户名和密码是否正确；检查服务状态，确认MySQL服务是否正在运行；检查网络连接，确认端口是否正确，网络是否通畅。

完成操作后，你可以使用`EXIT;`或`QUIT;`命令退出MySQL，也可以使用快捷键`Ctrl+D`。

## [练习题](#练习题)

### [练习1：创建数据库和表](#练习1-创建数据库和表)

创建一个名为`shop_db`的数据库，并在其中创建一个`products`表，包含以下字段：id（整数，主键，自增）、name（字符串，最大长度100，不能为空）、price（十进制数，10位数字，2位小数）、stock（整数，默认值为0）、created\_at（时间戳，默认当前时间）。

查看答案

```
-- 创建数据库
CREATE DATABASE shop_db;

-- 使用数据库
USE shop_db;

-- 创建products表
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2),
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 验证表是否创建成功
SHOW TABLES;
DESCRIBE products;
```

### [练习2：插入数据并查询](#练习2-插入数据并查询)

向`products`表中插入3条商品数据，然后查询所有商品信息。

查看答案

```
-- 插入商品数据
INSERT INTO products (name, price, stock) VALUES 
('iPhone 15', 5999.00, 100),
('小米13', 3999.00, 50),
('华为P60', 4999.00, 80);

-- 查询所有商品
SELECT * FROM products;
```

### [练习3：查询特定商品](#练习3-查询特定商品)

查询价格大于4000元的商品名称和价格。

查看答案

```
SELECT name, price 
FROM products 
WHERE price > 4000;
```

## [常见坑](#常见坑)

### [坑1：忘记分号结束SQL语句](#坑1-忘记分号结束sql语句)

很多初学者在写SQL语句时会忘记在语句末尾加分号，这会导致语句无法执行。记住，在MySQL命令行中，每个SQL语句都需要以分号结尾。

**纠正方法**：养成在每条SQL语句末尾加分号的好习惯。

### [坑2：使用关键字作为表名或列名](#坑2-使用关键字作为表名或列名)

SQL有很多保留关键字（如`order`、`group`、`table`等），如果用这些词作为表名或列名，会导致语法错误。

**纠正方法**：避免使用SQL关键字作为命名，如果必须使用，需要用反引号括起来，如`order`。

### [坑3：连接时密码输入错误](#坑3-连接时密码输入错误)

在命令行连接MySQL时，密码输入是隐藏的（不会显示星号），很多用户会以为自己没有输入成功而重复输入。

**纠正方法**：相信你的输入，密码虽然不可见，但实际上已经输入了。直接按回车即可。

## [速记卡](#速记卡)

- **数据库**：专门存储和管理数据的系统，像智能文件柜
- **关系型数据库**：使用表格存储数据，通过行和列组织信息
- **主键**：表中每行的唯一标识符，确保数据的唯一性
- **SQL**：结构化查询语言，用于与数据库对话的标准语言
- **MySQL**：最流行的开源关系型数据库之一
- **客户端工具**：图形化界面工具，让数据库操作更直观

## [章节总结](#章节总结)

在这一章中，我们开启了SQL学习之旅。我们从最基本的概念开始，了解了什么是数据库，什么是关系型数据库，以及SQL的作用。数据库就像是应用程序的超级记忆管家，而SQL就是我们与这个管家对话的语言。

接着，我们学习了如何安装MySQL，提供了三种安装方式供不同需求的用户选择。无论是通过Homebrew、官方安装包还是Docker，都能让你快速搭建好学习环境。我们还介绍了几种常用的客户端工具，从免费的DBeaver到功能强大的MySQL Workbench，你可以根据自己的需求选择合适的工具。

最重要的部分是连接数据库并执行第一个查询。我们学习了如何连接到MySQL服务器，如何创建数据库和表，如何插入数据以及如何查询数据。当你成功执行`SELECT * FROM users;`并看到查询结果时，你已经正式迈入了SQL的世界！

最后，我们通过练习题巩固了所学知识，从创建表到增删改查的基本操作，为后续章节的学习打下了坚实的基础。

记住，学习SQL最重要的是多练习。建议你多创建几个表，尝试不同的查询语句，遇到问题不要害怕，这正是学习的过程。下一章，我们将深入学习SELECT查询的各种用法，敬请期待！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [01｜入门：数据库与 SQL 到底是什么？](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#_01-入门-数据库与-sql-到底是什么)
- [1.1 什么是数据库与 SQL](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#_1-1-什么是数据库与-sql)
- [表、行、列和主键](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#表、行、列和主键)
- [什么是SQL？](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#什么是sql)
- [SQL与NoSQL的区别](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#sql与nosql的区别)
- [1.2 安装 MySQL 与客户端工具](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#_1-2-安装-mysql-与客户端工具)
- [Mac 安装 MySQL](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#mac-安装-mysql)
- [Windows 安装 MySQL](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#windows-安装-mysql)
- [MySQL官方网站的下载页面](https://dev.mysql.com/downloads/installer/)
- [dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
- [Linux 安装 MySQL](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#linux-安装-mysql)
- [验证安装](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#验证安装)
- [客户端工具选择](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#客户端工具选择)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [DBeaver](https://dbeaver.io/download/)
- [Sequel Ace](https://sequel-ace.com/)
- [1.3 连接数据库与首个查询](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#_1-3-连接数据库与首个查询)
- [连接数据库的基本方法](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#连接数据库的基本方法)
- [你的第一个SQL查询](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#你的第一个sql查询)
- [理解数据库和表的概念](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#理解数据库和表的概念)
- [创建第一个表](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#创建第一个表)
- [插入和查询数据](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#插入和查询数据)
- [常见连接问题及解决方法](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#常见连接问题及解决方法)
- [练习题](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#练习题)
- [练习1：创建数据库和表](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#练习1-创建数据库和表)
- [练习2：插入数据并查询](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#练习2-插入数据并查询)
- [练习3：查询特定商品](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#练习3-查询特定商品)
- [常见坑](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#常见坑)
- [坑1：忘记分号结束SQL语句](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#坑1-忘记分号结束sql语句)
- [坑2：使用关键字作为表名或列名](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#坑2-使用关键字作为表名或列名)
- [坑3：连接时密码输入错误](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#坑3-连接时密码输入错误)
- [速记卡](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#速记卡)
- [章节总结](https://xiaolinnote.com/sql/sql_part1/01-introduction-and-setup.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
