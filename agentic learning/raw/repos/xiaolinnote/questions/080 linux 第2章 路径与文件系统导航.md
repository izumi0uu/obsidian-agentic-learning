---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html"
source: "https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html"
last_checked: 2026-05-07
freshness: watch
sha256: 60dfb2b37617476e515df7dd13020baf1ac473a152379cc54319dab88142f864
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Linux Filesystem]]"
  - "[[Path]]"
  - "[[Command Line]]"
---
# 第2章 路径与文件系统导航

原始链接：https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[Linux Filesystem]]
- [[Path]]
- [[Command Line]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 17 分钟约 5023 字2025/9/2

---

# [02｜路径与文件系统导航](#_02-路径与文件系统导航)

大家好，我是小林。

想象一下这样的场景：你刚刚下载了一个重要的文件，系统提示保存在 `~/Downloads` 目录下。你兴冲冲地打开终端，输入 `ls` 查看文件，却发现文件不在当前目录。这时候你该怎么办？是反复尝试 `cd` 进入各种目录，还是直接放弃使用命令行？

很多新手在命令行里最容易犯的"迷路"问题，本质上都是因为没有理解 Linux 的路径系统。就像我们在现实生活中需要地址才能找到目的地一样，在 Linux 世界里，路径就是文件的"地址"。这一章我们要解决的，就是让你在命令行的"城市"中不再迷路。

## [2.1 理解路径：Linux 文件系统的"地址系统"](#_2-1-理解路径-linux-文件系统的-地址系统)

Linux 中的路径到底是怎么回事？为什么有些路径以 `/` 开头，有些不是？

实际上，路径系统的存在是为了解决一个基本问题：如何在浩瀚的文件系统中准确定位一个文件。如果没有统一的地址系统，我们就无法告诉计算机具体要操作哪个文件。

### [什么是绝对路径？—— 从"首都"开始的完整地址](#什么是绝对路径-——-从-首都-开始的完整地址)

绝对路径就像是从国家首都开始的完整地址，它总是从根目录 `/` 开始。不管你现在在哪里，绝对路径都能准确指向同一个位置。

让我们来体验一下：

```
# 先看看我们现在在哪里
$ pwd
/home/user

# 使用绝对路径查看文档目录，不管我们在哪都能找到
$ ls /home/user/Documents
notes.txt  report.docx  photos/
```

看到了吗？即使我们在 `/home/user` 目录下，`/home/user/Documents` 这个路径依然能准确地指向文档目录。这就是绝对路径的特点——**可靠且明确**。

你可能会问："为什么需要这种从根目录开始的完整路径？" 想象一下，如果你告诉快递员你的地址，你会说"北京市朝阳区某某街道123号"，而不是"往前走100米然后右转"。绝对路径就是这个完整地址，确保任何人都能准确找到目标位置。

### [什么是相对路径？—— 从"当前位置"开始的导航](#什么是相对路径-——-从-当前位置-开始的导航)

相对路径就像是你给别人指路时会说"往前走100米然后右转"，它的起点是你当前所在的位置。

```
# 确认我们在家目录
$ pwd
/home/user

# 用相对路径进入文档目录（从当前位置出发）
$ ls Documents
notes.txt  report.docx  photos/

# 如果我们在其他地方，同样的相对路径可能就无效了
$ cd /
$ ls Documents
ls: cannot access 'Documents': No such file or directory
```

这就是为什么新手经常遇到"文件找不到"的问题——他们用的相对路径在当前位置下并不存在。就像你在北京告诉朋友"往前走100米"，和你朋友在上海听到同样的指令，结果会完全不同。

### [那些特殊的"快捷符号"](#那些特殊的-快捷符号)

Linux 为了方便我们导航，提供了几个特殊的符号，就像城市的地标建筑：

```
# ~ 符号代表你的"家"（家目录）
$ cd ~
$ pwd
/home/user
# 不管你在哪，cd ~ 都能带你回家

# . 符号代表"这里"（当前目录）
$ ls .           # 查看当前目录
# 等同于
$ ls             # 通常我们省略这个 .

# .. 符号代表"上一级"（父目录）
$ pwd
/home/user/Documents
$ cd ..          # 回到上一级目录
$ pwd
/home/user

# - 符号代表"刚才来的地方"（上一个工作目录）
$ cd /tmp        # 先去临时目录
$ cd -           # 再回到刚才的地方
# 输出：
/home/user
```

### [Linux 城市的"地图布局"](#linux-城市的-地图布局)

Linux 的文件系统就像一座规划良好的城市，根目录 `/` 是市中心，各个目录有不同的功能：

```
# 让我们看看这座"城市"的主要区域
$ ls /
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
```

- `/home`：居民区，每个用户都有自己的房子
- `/bin` 和 `/usr/bin`：工具店，存放各种命令工具
- `/etc`：市政厅，存放系统配置
- `/tmp`：临时停车场，存放临时文件

## [2.2 定位自己：别迷路了，看看你在哪里](#_2-2-定位自己-别迷路了-看看你在哪里)

你有没有过这样的经历：在命令行里操作了一会儿，突然忘记自己现在在哪个目录了？或者想要查看某个目录里有什么文件，却不知道该用什么命令？

这种"迷路"的感觉很正常，就像你在一个陌生的城市里走着走着就不知道自己在哪条街了。好消息是，Linux 提供了简单的方法让你随时"定位"自己。

### [pwd：你的"GPS定位"工具](#pwd-你的-gps定位-工具)

`pwd` 命令就像你手机上的 GPS，随时告诉你"你现在在这里"。这个简单的命令能帮你避免迷路。

```
# 让我们看看现在在哪里
$ pwd
/home/user/Documents

# 这就像GPS显示：你现在在"家目录的文档文件夹"
```

有时候你可能会遇到一些"假路径"——看起来是一个目录，实际上是其他地方的快捷方式。这时可以用 `pwd -P` 来查看真实地址：

```
# 比如有些系统的 /usr/local/bin 实际上是 /usr/bin 的链接
$ cd /usr/local/bin
$ pwd
/usr/local/bin
$ pwd -P
/usr/bin
# pwd -P 显示了真实的物理路径
```

养成一个好习惯：每次不确定当前位置时，先 `pwd` 一下，就像迷路时先查看地图一样。

### [ls：打开目录的"门"，看看里面有什么](#ls-打开目录的-门-看看里面有什么)

`ls` 就像是打开房间的门，让你看到里面有什么。它是你使用频率最高的命令之一。

#### [最基本的用法：看看房间里有什么](#最基本的用法-看看房间里有什么)

```
# 基本用法：列出当前目录的内容
$ ls
Documents  Downloads  Music  Pictures  Videos
# 这就像打开了你的"家目录"这扇门，看到里面有5个房间
```

#### [想知道更多细节？加上 `-l` 选项](#想知道更多细节-加上-l-选项)

有时候你不仅想知道"有什么"，还想了解"它们是什么时候创建的"、"有多大"等信息：

```
# 用 -l 选项查看详细信息
$ ls -l
# 输出：
total 16
drwxr-xr-x 2 user user 4096 Sep  1 14:30 Documents
drwxr-xr-x 2 user user 4096 Sep  1 14:30 Downloads
-rw-r--r-- 1 user user  512 Sep  1 15:20 notes.txt
```

这个输出告诉我们：

- `drwxr-xr-x`：这是目录（d开头）的权限信息
- `user user`：文件的所有者和所属组
- `4096`：文件大小（字节）
- `Sep 1 14:30`：创建时间
- `Documents`：文件/目录名

你可能会问："为什么需要这么多详细信息？" 想象一下，如果你在整理房间，你不仅想知道"有什么物品"，还想知道"每个物品多重、什么时候放的、是谁放的"。`ls -l` 就提供了这些详细信息。

#### [隐藏文件在哪里？用 `-a` 选项](#隐藏文件在哪里-用-a-选项)

有些文件像"隐形"的一样，普通的 `ls` 看不到它们。这些以点开头的文件通常是配置文件：

```
# 显示所有文件，包括隐藏文件
$ ls -a
.   .bashrc  .profile  Documents  Downloads  Music
..  .cache   .ssh      Pictures   Videos
```

看到了吗？`.bashrc`、`.profile` 这些就是隐藏的配置文件。它们很重要，但平时不需要看到。

为什么要隐藏这些文件呢？就像你家里的电线和管道，它们很重要，但你平时不想看到它们，避免视觉混乱。

#### [文件大小看不懂？用 `-h` 选项让数字更友好](#文件大小看不懂-用-h-选项让数字更友好)

```
# 普通方式显示文件大小
$ ls -l
-rw-r--r-- 1 user user 12288 Sep  1 15:20 large_file.txt
# 12288 字节是多少KB？得计算一下...

# 用 -h 选项人性化显示
$ ls -lh
-rw-r--r-- 1 user user 12K Sep  1 15:20 large_file.txt
# 12K，这样一下子就明白了！
```

### [最实用的组合：`ls -la`](#最实用的组合-ls-la)

经过上面的学习，你可能已经猜到了：最常用的组合就是把最有用的选项合在一起：

```
# 显示所有文件的详细信息，文件大小用友好单位
$ ls -lah
# 输出示例：
total 64K
drwxr-xr-x 8 user user 4.0K Sep  1 15:30 .
drwxr-xr-x 3 user user 4.0K Sep  1 14:00 ..
-rw------- 1 user user  220 Sep  1 14:00 .bash_logout
-rw-r--r-- 1 user user 3.7K Sep  1 14:00 .bashrc
-rw-r--r-- 1 user user  12K Sep  1 15:20 large_file.txt
```

这个组合能让你看到一个目录的"全貌"，是排查问题和了解目录结构的首选。

## [2.3 目录切换：cd 命令的灵活用法](#_2-3-目录切换-cd-命令的灵活用法)

学会了如何"看路"，现在我们来学习如何"走路"。`cd` 命令就像你的"双腿"，让你在 Linux 的"城市"中自由移动。

### [基本移动：从当前位置到目标位置](#基本移动-从当前位置到目标位置)

```
# 先确认我们在家目录
$ pwd
/home/user

# 进入 Documents 子目录（就像走进家里的书房）
$ cd Documents
$ pwd
/home/user/Documents

# 回到上级目录（就像从书房回到客厅）
$ cd ..
$ pwd
/home/user
```

这些是最基本的移动方式，就像你在家里从客厅走到卧室一样简单。

### [快速回家的技巧](#快速回家的技巧)

无论你在哪里，想要回家都有几种方法：

```
# 先去一个远的地方
$ cd /tmp
$ pwd
/tmp

# 方法1：用 ~ 符号回家
$ cd ~
$ pwd
/home/user

# 方法2：直接 cd 不加参数也能回家
$ cd /tmp
$ cd
$ pwd
/home/user
```

就像无论你在城市的哪个角落，都能通过打车直接回家一样。

你可能会问："为什么 `cd` 不加参数就能回家？" 这是 Linux 的一个便民设计，因为回到家目录是最常用的操作之一，所以系统给了这个"快捷方式"。

### [最实用的技巧：在"刚才"和"现在"之间切换](#最实用的技巧-在-刚才-和-现在-之间切换)

这是一个很多新手都不知道但非常实用的功能：

```
# 假设你在工作目录
$ pwd
/home/user/Documents/projects

# 临时去一下临时目录处理某个文件
$ cd /tmp
$ pwd
/tmp

# 处理完后，如何快速回到刚才的工作目录？
$ cd -
# 输出：
/home/user/Documents/projects
$ pwd
/home/user/Documents/projects
```

`cd -` 就像一个"传送门"，让你在两个目录之间快速切换。当你需要在两个目录之间频繁操作时，这个功能特别有用。

### [多级路径导航：像搭积木一样组合路径](#多级路径导航-像搭积木一样组合路径)

有时候你需要一次移动多个层级，就像从三楼直接到一楼，不用一层一层地走：

```
# 假设你在很深的目录里
$ pwd
/home/user/Documents/projects/website/css

# 一次回到三级上级目录
$ cd ../../..
$ pwd
/home/user/Documents

# 或者直接进入深层的子目录
$ cd Documents/projects/website
$ pwd
/home/user/Documents/projects/website
```

### [Tab 补全：你的"自动导航助手"](#tab-补全-你的-自动导航助手)

这是提高效率最重要的技巧之一！想象一下，你要进入一个很长的目录名，比如 `VeryLongDirectoryName`，手动输入很容易出错：

```
# 输入部分路径后按 Tab 补全
$ cd Doc(按 Tab)
# 自动补全为：
$ cd Documents/

# 如果有多个匹配，按两次 Tab 显示选项
$ cd D(按两次 Tab)
Documents/  Downloads/
```

**Tab 键的神奇之处到底在哪里？**

- 如果只有一个匹配，它会直接补全，就像智能输入法自动完成你的词语
- 如果有多个匹配，按两次 Tab 会显示所有选项，就像给你一个选择列表
- 如果没有匹配，说明你输入错了，这就像实时的拼写检查，帮你避免浪费时间在错误的命令上

你可能会问："为什么不用鼠标点击？"因为在命令行环境下，键盘操作通常比鼠标更快，特别是当你需要输入长路径或复杂命令时。

> ⚠️高危操作：`cd ~; rm -rf *` 会删除家目录下所有文件！在执行删除操作前，务必用 `pwd` 确认当前位置，并用 `ls` 查看要删除的内容。养成好习惯：重要操作前先确认位置！

## [2.4 链接：文件的"替身"和"分身"](#_2-4-链接-文件的-替身-和-分身)

想象一下这样的场景：你有一个重要的配置文件，需要在多个地方都能访问到，但又不想复制多份（因为复制后修改其中一个，其他的不会同步更新）。这时候就需要用到链接了。

链接就像是为文件创建了"替身"或"分身"，让你能够在不同位置访问同一个文件。

### [软链接：文件的"替身"](#软链接-文件的-替身)

软链接就像是为原文件创建了一个"替身"，这个替身指向原文件。就像你给朋友一个你家的地址，朋友通过这个地址就能找到你家。

```
# 假设你有一个重要的笔记文件
$ ls /home/user/Documents/notes.txt
notes.txt

# 创建一个软链接，让它出现在家目录下方便访问
$ ln -s /home/user/Documents/notes.txt ~/quick_notes

# 查看这个链接（注意开头的 l 表示链接）
$ ls -l ~/quick_notes
# 输出：
lrwxrwxrwx 1 user user 32 Sep  1 16:00 /home/user/quick_notes -> /home/user/Documents/notes.txt
# 箭头表示它指向哪里

# 通过链接访问文件
$ cat ~/quick_notes
# 这和你直接访问原文件是完全一样的
```

软链接的特点：

- 它是一个独立的文件，只是指向原文件
- 如果删除原文件，链接就会失效（就像你搬家了，朋友拿着旧地址就找不到了）
- 可以跨文件系统创建（就像可以给外地朋友地址一样）

### [硬链接：文件的"分身"](#硬链接-文件的-分身)

硬链接更像是文件的"分身"，它不是指向文件，而是文件的另一个名字。就像一个人可以有多个名字，但都是同一个人。

```
# 创建一个测试文件
$ echo "重要数据" > important_data.txt

# 创建硬链接
$ ln important_data.txt backup_data.txt

# 查看它们的关系（注意相同的 inode 号）
$ ls -li important_data.txt backup_data.txt
# 输出：
1234567 -rw-r--r-- 2 user user 10 Sep  1 16:05 important_data.txt
1234567 -rw-r--r-- 2 user user 10 Sep  1 16:05 backup_data.txt
# 注意：inode 号完全相同，链接计数为 2

# 修改其中一个文件
$ echo "追加内容" >> important_data.txt

# 查看另一个文件，内容也同步更新了
$ cat backup_data.txt
重要数据
追加内容
```

硬链接的特点：

- 与原文件共享相同的 inode 和数据
- 删除原文件，硬链接仍然有效（就像一个人改了名字，但人还是那个人）
- 只能在同一个文件系统内创建

你可能会问："为什么需要硬链接？" 想象一下，你有一个重要的文件，想做个备份，但又不希望占用双倍的空间。硬链接就是完美的解决方案——它不复制文件内容，只是给文件起个别名。

### [实际对比：软链接 vs 硬链接](#实际对比-软链接-vs-硬链接)

让我们通过一个实验来理解它们的区别：

```
# 准备测试环境
$ echo "测试内容" > test_original.txt

# 创建软链接和硬链接
$ ln -s test_original.txt soft_link.txt
$ ln test_original.txt hard_link.txt

# 查看初始状态
$ ls -li *.txt
# 输出：
1234567 -rw-r--r-- 2 user user 10 Sep  1 16:10 test_original.txt
1234567 -rw-r--r-- 2 user user 10 Sep  1 16:10 hard_link.txt
1234568 lrwxrwxrwx 1 user user 15 Sep  1 16:10 soft_link.txt -> test_original.txt

# 删除原文件
$ rm test_original.txt

# 测试软链接
$ cat soft_link.txt
cat: soft_link.txt: No such file or directory
# 软链接失效了，就像地址对应的房子被拆除了

# 测试硬链接
$ cat hard_link.txt
测试内容
# 硬链接仍然有效，就像改了名字但人还在
```

> 💡注意：硬链接只能在同一个文件系统内创建，而软链接可以跨文件系统。这就像你只能在同一个城市里给同一个地点起多个名字，但可以把地址告诉其他城市的朋友。

---

## [练习题](#练习题)

1. 如何快速回到上一次所在的目录，而不是家目录或上级目录？

查看答案

- 思路与步骤：使用 `cd -` 命令回到上一个工作目录，这是很多人不知道但非常实用的技巧
- 示例命令：

```
$ pwd
/home/user/Documents
$ cd /tmp
$ pwd
/tmp
$ cd -
# 输出：
/home/user/Documents
$ pwd
/home/user/Documents
```

`cd -` 会在输出目标目录的同时完成切换。这个技巧在需要在两个目录之间频繁工作时特别有用，比如在一个目录编辑文件，在另一个目录测试运行。

2. 如何找到当前目录下所有以点开头的隐藏文件，并按大小排序？

查看答案

- 思路与步骤：使用 `ls` 命令结合 `-a` 选项显示隐藏文件，`-l` 显示详细信息，`-h` 人性化显示大小，然后用 `sort` 排序
- 示例命令：

```
# 方法1：显示所有文件并按大小排序
$ ls -lah | grep "^\\." | sort -k5 -h

# 方法2：更简单的方法，直接显示隐藏文件
$ ls -lah .*
```

输出会显示所有隐藏文件的详细信息，并按文件大小排序。这在查找占用空间过大的配置文件时特别有用。

3. 如何创建一个软链接，使得在任何目录下都可以通过 `~/config` 访问 `/etc/nginx/nginx.conf`？

查看答案

- 思路与步骤：使用 `ln -s` 创建软链接，目标使用绝对路径确保链接的可靠性
- 示例命令：

```
$ ln -s /etc/nginx/nginx.conf ~/config
$ ls -l ~/config
# 输出：
lrwxrwxrwx 1 user user 22 Sep  1 16:30 /home/user/config -> /etc/nginx/nginx.conf

# 测试链接
$ cat ~/config
# 会显示 nginx.conf 的内容
```

使用绝对路径创建软链接可以确保即使移动链接文件，指向关系仍然正确。这是创建软链接的最佳实践。

---

## [速记卡](#速记卡)

- `pwd`：显示当前工作目录的完整路径（GPS定位）
- `ls -la`：显示所有文件（包括隐藏文件）的详细信息（查看房间全貌）
- `cd ~`：快速回到家目录（一键回家）
- `cd ..`：回到上级目录（回到客厅）
- `cd -`：回到上一个工作目录（传送门）
- `ln -s 源文件 链接文件`：创建软链接（创建替身）
- `ln 源文件 链接文件`：创建硬链接（创建分身）

## [常见坑](#常见坑)

- 混淆相对路径和绝对路径：在脚本中尽量使用绝对路径避免歧义，就像寄信要用完整地址
- 删除原文件后软链接失效：硬链接更适合需要备份的场景，软链接适合临时引用
- 在错误目录执行操作：养成用 `pwd` 确认位置的习惯，就像出门前先看地图
- 忘记 Tab 键补全：手动输入路径容易出错，效率低下，拒绝使用效率工具就像拒绝用计算器
- 随意删除 `..` 或 `.`：这些是系统特殊目录，不能删除，就像不能拆掉楼道的楼梯
- 在文件系统间创建硬链接：硬链接只能在同一文件系统内使用，软链接没有这个限制
- 不看 `ls -l` 的链接计数：链接计数显示文件有多少个硬链接，这是判断文件状态的重要信息

## [章节总结](#章节总结)

路径导航是 Linux 命令行的基础技能。通过理解绝对路径和相对路径的区别，你可以在文件系统中精确定位。`pwd` 让你时刻知道"我在哪里"，`ls` 让你看到"这里有什么"，而 `cd` 则让你能够"去任何地方"。

特殊目录符号（`~`、`.`、`..`、`-`）的使用大大提高了导航效率，特别是 `cd -` 这个经常被忽视的实用功能。Tab 补全不仅是防错工具，更是提高输入效率的利器。

软链接和硬链接的理解让你能够更灵活地管理文件。软链接适合跨文件系统的引用和临时链接，而硬链接则是文件备份的轻量级解决方案。掌握这些导航技能，你就可以在 Linux 文件系统中游刃有余地移动和操作文件了。

记住，在 Linux 的世界里，不会迷路的关键是理解路径系统和善用导航工具。就像在现实生活中，只要你会看地图、会问路，就永远不会迷路一样。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [02｜路径与文件系统导航](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#_02-路径与文件系统导航)
- [2.1 理解路径：Linux 文件系统的"地址系统"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#_2-1-理解路径-linux-文件系统的-地址系统)
- [什么是绝对路径？—— 从"首都"开始的完整地址](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#什么是绝对路径-——-从-首都-开始的完整地址)
- [什么是相对路径？—— 从"当前位置"开始的导航](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#什么是相对路径-——-从-当前位置-开始的导航)
- [那些特殊的"快捷符号"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#那些特殊的-快捷符号)
- [Linux 城市的"地图布局"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#linux-城市的-地图布局)
- [2.2 定位自己：别迷路了，看看你在哪里](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#_2-2-定位自己-别迷路了-看看你在哪里)
- [pwd：你的"GPS定位"工具](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#pwd-你的-gps定位-工具)
- [ls：打开目录的"门"，看看里面有什么](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#ls-打开目录的-门-看看里面有什么)
- [最基本的用法：看看房间里有什么](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#最基本的用法-看看房间里有什么)
- [想知道更多细节？加上 -l 选项](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#想知道更多细节-加上-l-选项)
- [隐藏文件在哪里？用 -a 选项](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#隐藏文件在哪里-用-a-选项)
- [文件大小看不懂？用 -h 选项让数字更友好](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#文件大小看不懂-用-h-选项让数字更友好)
- [最实用的组合： ls -la](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#最实用的组合-ls-la)
- [2.3 目录切换：cd 命令的灵活用法](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#_2-3-目录切换-cd-命令的灵活用法)
- [基本移动：从当前位置到目标位置](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#基本移动-从当前位置到目标位置)
- [快速回家的技巧](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#快速回家的技巧)
- [最实用的技巧：在"刚才"和"现在"之间切换](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#最实用的技巧-在-刚才-和-现在-之间切换)
- [多级路径导航：像搭积木一样组合路径](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#多级路径导航-像搭积木一样组合路径)
- [Tab 补全：你的"自动导航助手"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#tab-补全-你的-自动导航助手)
- [2.4 链接：文件的"替身"和"分身"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#_2-4-链接-文件的-替身-和-分身)
- [软链接：文件的"替身"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#软链接-文件的-替身)
- [硬链接：文件的"分身"](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#硬链接-文件的-分身)
- [实际对比：软链接 vs 硬链接](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#实际对比-软链接-vs-硬链接)
- [练习题](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#练习题)
- [速记卡](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#速记卡)
- [常见坑](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#常见坑)
- [章节总结](https://xiaolinnote.com/linux/02-path-and-filesystem-navigation.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
