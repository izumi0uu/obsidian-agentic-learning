---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
  - "linux"
status: inbox
created: 2026-05-07
updated: 2026-05-17
url: "https://xiaolinnote.com/linux/06-pipes-and-composition.html"
source: "https://xiaolinnote.com/linux/06-pipes-and-composition.html"
last_checked: 2026-05-17
freshness: watch
sha256: cdc1d17344381bdddecb7d5c46eb72210845686ce844f259eeecca63262777db
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 第6章 管道与命令组合

原始链接：https://xiaolinnote.com/linux/06-pipes-and-composition.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 第6章 管道与命令组合

[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 23 分钟约 7028 字2025/9/2

---

# [06｜管道与命令组合](#_06-管道与命令组合)

大家好，我是小林。

想象一下这样的场景：你正在分析一个大型日志文件，需要找出包含"error"的行，统计这些行出现的次数，然后按时间排序。如果用传统的做法，你可能需要多次保存中间文件，操作繁琐且容易出错。有没有一种方法，能够像工厂流水线一样，让数据在不同的处理工序之间顺畅流动？

在 Linux 命令行中，管道（|）就是这样一个神奇的"传送带"。它让你能够将多个简单的命令组合起来，形成强大的数据处理流水线。每个命令专注于做一件事，但通过管道的连接，它们能够协同完成复杂的任务。这一章我们要学习的，就是如何利用管道和命令组合，让简单的工具发挥出 1+1>2 的威力。

## [6.1 管道：连接命令的"传送带"](#_6-1-管道-连接命令的-传送带)

让我们先来理解管道的本质。管道就像工厂的流水线，数据从一个工序流向下一个工序，每个工序都对数据进行加工处理。在 Linux 中，这个"工序"就是各种命令，而"流水线"就是管道符号 `|`。

### [理解管道的工作原理](#理解管道的工作原理)

管道的核心思想很简单：将前一个命令的输出作为后一个命令的输入。这听起来似乎很简单，但它的威力在于可以无限组合，创造出复杂的数据处理流程。

让我们从一个简单的例子开始：

```
$ ps aux | grep bash
user      1234  0.0  0.1  12345  6789 pts/0    S+   10:30   0:00 bash
user      1235  0.0  0.0  12346  6790 pts/1    S+   10:31   0:00 grep bash
```

这个命令做了什么？`ps aux` 显示了系统中的所有进程，然后管道将这个输出传递给 `grep bash`，`grep` 就像筛子一样，只保留了包含 "bash" 的行。

你可能会问："这比使用临时文件好在哪里？" 让我们对比一下传统做法：

```
# 传统做法：需要创建临时文件
$ ps aux > temp.txt
$ grep bash temp.txt
$ rm temp.txt
```

传统做法需要创建临时文件，占用磁盘空间，而且操作步骤繁琐。管道则让数据直接在内存中流动，效率更高，代码也更简洁。

### [从简单到复杂：构建数据处理流水线](#从简单到复杂-构建数据处理流水线)

管道真正的威力在于可以将多个简单的命令组合成复杂的数据处理流程。让我们通过一个实际的例子来看看如何构建一个完整的文件类型统计流水线：

```
$ ls -l | grep "^-" | awk '{print $9}' | cut -d. -f2 | sort | uniq -c | sort -nr
  15 txt
   8 log
   3 conf
```

这个看起来复杂的命令其实是一个很直观的处理流程：

1. **数据源**：`ls -l` 获取文件详细信息
2. **过滤**：`grep "^-"` 只保留普通文件（排除目录）
3. **提取**：`awk '{print $9}'` 提取文件名
4. **分离**：`cut -d. -f2` 提取文件扩展名
5. **整理**：`sort` 将相同扩展名排在一起
6. **统计**：`uniq -c` 统计每个扩展名出现的次数
7. **排序**：`sort -nr` 按数量从多到少排序

每一步都很简单，但组合起来就能完成复杂的数据分析任务。

### [实际应用场景解析](#实际应用场景解析)

让我们看看管道在日常工作中的一些典型应用：

**场景1：磁盘空间分析**

```
$ du -sh /* | sort -hr | head -10
4.5G    /home
2.1G    /var
1.8G    /usr
```

这个命令帮助我们快速找到占用空间最大的目录。`du -sh /*` 计算每个目录的大小，`sort -hr` 按大小降序排序，`head -10` 显示前10个最大的目录。

**场景2：网络连接监控**

```
$ netstat -an | grep ESTABLISHED | wc -l
42
```

这个命令实时统计已建立的连接数量。`netstat -an` 显示所有网络连接，`grep ESTABLISHED` 筛选已建立的连接，`wc -l` 统计行数。

**场景3：进程管理**

```
$ ps aux | sort -rk 3 | head -10
```

这个命令找出CPU使用率最高的10个进程。`ps aux` 显示所有进程，`sort -rk 3` 按第三列（CPU使用率）降序排序，`head -10` 显示前10行。

### [管道的限制与解决方案](#管道的限制与解决方案)

管道虽然强大，但也有一些需要注意的限制：

**问题1：错误输出不会被传递**

```
$ command_with_error | next_command
# 错误信息会直接显示在终端，不会传递给下一个命令
```

**解决方案**：

```
$ command_with_error 2>&1 | next_command
# 2>&1 将错误输出重定向到标准输出
```

**问题2：子shell中的命令不会影响当前shell**

```
$ cd /tmp | pwd
# pwd 显示的仍然是当前目录，因为 cd 只在子shell中生效
```

**解决方案**：使用 `&&` 或 `;` 连接命令

```
$ cd /tmp && pwd
# 这样会在当前shell中切换目录
```

理解这些限制能帮助我们更好地使用管道，避免常见的陷阱。

## [6.2 命令替换：将命令结果嵌入其他命令](#_6-2-命令替换-将命令结果嵌入其他命令)

现在让我们来学习另一种重要的命令组合方式：命令替换。如果说管道是连接命令的"传送带"，那么命令替换就像是"插值"，它让你能够将一个命令的输出结果直接嵌入到另一个命令的参数中。

### [理解命令替换的原理](#理解命令替换的原理)

命令替换的核心思想很简单：在执行命令之前，Shell 会先执行括号内的命令，然后用这个命令的输出结果替换整个表达式。这样你就可以动态地构建命令参数。

### [现代语法 vs 传统语法](#现代语法-vs-传统语法)

Linux 提供了两种命令替换的语法，但强烈推荐使用现代语法：

```
# 现代语法：$(command) - 推荐使用
$ echo "当前时间：$(date)"
当前时间：2025-09-02 10:30:15

# 传统语法：`command` - 也可以用，但不推荐
$ echo "当前时间：`date`"
当前时间：2025-09-02 10:30:15
```

为什么推荐 `$(command)` 而不是反引号？主要有三个原因：

1. **可读性更好**：`$(command)` 更清晰，不容易与单引号混淆
2. **支持嵌套**：可以轻松地嵌套多层命令替换
3. **引号处理**：在引号内使用时不会出现问题

### [实际应用场景](#实际应用场景)

**场景1：动态创建目录**

```
$ mkdir "backup_$(date +%Y%m%d)"
$ ls
backup_20250902
```

这个命令很有用：我们创建了一个以当前日期命名的备份目录。`date +%Y%m%d` 会输出格式化的日期，然后这个输出被替换到目录名中。

**场景2：批量文件处理**

```
$ for file in *.txt; do
>   mv "$file" "processed_$(date +%Y%m%d)_$file"
> done
```

这个循环会给所有的 `.txt` 文件重命名，在文件名前面加上处理日期。这在日志文件处理和数据归档中非常实用。

**场景3：进程管理**

```
$ kill $(pgrep firefox)
# 杀死所有 Firefox 进程
```

这个命令很强大：`pgrep firefox` 找到所有 Firefox 进程的 PID，然后 `kill` 命令使用这些 PID 作为参数。

**场景4：嵌套命令替换**

```
$ echo "系统信息：$(uname -a | cut -d' ' -f1,3)"
系统信息：Linux 5.4.0
```

这里我们看到了嵌套的使用：`uname -a` 获取系统信息，然后通过 `cut` 提取需要的字段，最后将结果嵌入到 echo 命令中。

### [命令替换与管道的区别](#命令替换与管道的区别)

很多人容易混淆这两个概念，让我们来澄清一下：

**命令替换**：将命令的输出作为另一个命令的**参数**

```
$ echo "文件有 $(wc -l < file.txt) 行"
文件有 100 行
```

这里 `wc -l < file.txt` 的输出（数字 100）被作为 echo 命令的参数。

**管道**：将命令的输出作为另一个命令的**标准输入**

```
$ wc -l file.txt | echo
# 这样不会工作，因为 echo 不会从标准输入读取
```

管道要求后面的命令能够从标准输入读取数据，而 echo 不能这样做。

### [实际工作中的技巧](#实际工作中的技巧)

**技巧1：使用命令替换避免重复输入**

```
# 不好的做法：重复输入目录名
$ cd /very/long/path/to/directory
$ tar -czf backup.tar.gz /very/long/path/to/directory

# 好的做法：使用命令替换
$ cd /very/long/path/to/directory
$ tar -czf backup.tar.gz $(pwd)
```

**技巧2：结合条件判断**

```
# 如果目录存在，则进入
if [ -d "$(pwd)/backup" ]; then
    cd backup
fi
```

**技巧3：动态生成配置**

```
# 根据当前主机名生成配置文件
$ sed "s/HOSTNAME/$(hostname)/g" template.conf > config.conf
```

## [6.3 xargs：连接管道与命令的桥梁](#_6-3-xargs-连接管道与命令的桥梁)

现在我们来学习一个非常重要的工具：`xargs`。如果说管道是数据流的"传送带"，那么 `xargs` 就像是一个"转换器"，它能够将管道传递的数据流转换成命令可以理解的参数格式。

### [为什么需要 xargs？](#为什么需要-xargs)

想象一下这样的场景：你通过 `find` 命令找到了一批需要删除的临时文件，然后想要用 `rm` 命令删除它们。你可能会这样尝试：

```
$ find . -name "*.tmp" | rm
# 这样不会工作！rm 不知道如何从标准输入读取文件名
```

问题在于 `rm` 命令期望的是参数，而不是标准输入。这时候 `xargs` 就派上用场了：

```
$ find . -name "*.tmp" | xargs rm
# 现在可以工作了！xargs 将文件列表转换为 rm 的参数
```

`xargs` 的工作原理很简单：它读取标准输入，然后将输入的内容作为参数传递给指定的命令。

### [xargs 与 find -exec 的选择](#xargs-与-find-exec-的选择)

你可能会问："为什么不直接用 `find -exec`？" 这确实是个好问题。让我们比较一下：

```
# 使用 xargs
$ find . -name "*.tmp" | xargs rm

# 使用 find -exec
$ find . -name "*.tmp" -exec rm {} \;
```

两者的主要区别：

- **性能**：`xargs` 通常更高效，因为它会批量处理参数
- **兼容性**：`xargs` 更通用，可以与任何命令配合使用
- **灵活性**：`xargs` 提供了更多的控制选项

### [xargs 的实用选项详解](#xargs-的实用选项详解)

**安全第一：测试模式**

```
# 显示将要执行的命令（不会真正执行）
$ find . -name "*.log" | xargs -t rm
rm file1.log file2.log file3.log
```

这个选项在调试复杂命令时非常有用，可以让你看到 `xargs` 实际会执行什么命令。

**逐个处理模式**

```
# 逐个处理文件（适合大量文件或需要单独处理的场景）
$ find . -name "*.jpg" | xargs -n 1 convert -resize 800x600
```

`-n 1` 选项告诉 `xargs` 每次只传递一个参数，这在需要逐个处理文件时很有用。

**交互式确认**

```
# 交互式确认（防止误操作）
$ find . -name "*.tmp" | xargs -p rm
rm file1.tmp ?...y
rm file2.tmp ?...n
```

这个选项在执行危险操作时特别有用，它会逐个询问你是否要执行。

**处理特殊文件名**

```
# 处理包含空格的文件名
$ find . -name "*.txt" | xargs -d '\n' wc -l
```

默认情况下，`xargs` 使用空格作为分隔符，这会导致包含空格的文件名被错误地分割。`-d '\n'` 选项告诉 `xargs` 使用换行符作为分隔符。

### [实际应用场景](#实际应用场景-1)

**场景1：批量修改文件权限**

```
$ find . -type f -name "*.sh" | xargs chmod +x
```

这个命令会找到所有的 shell 脚本文件，并给它们添加执行权限。这在部署脚本时非常实用。

**场景2：日志文件管理**

```
# 压缩 30 天前的日志文件
$ find /var/log -name "*.log" -mtime +30 | xargs gzip
```

这个命令会找到 30 天前的日志文件，并用 gzip 压缩它们，节省磁盘空间。

**场景3：灵活的参数位置**

```
# 使用占位符指定参数位置
$ ls *.txt | xargs -I {} cp {} /backup/
```

`-I {}` 选项指定了一个占位符，这样你就可以将参数放在命令的任意位置，而不只是末尾。

**场景4：复杂的批量操作**

```
# 批量重命名文件
$ find . -name "*.old" | xargs -I {} bash -c 'mv "$1" "${1%.old}.new"' _ {}
```

这个命令展示了 `xargs` 的高级用法：使用 bash 内联脚本进行复杂的文件名转换。

### [xargs 的最佳实践](#xargs-的最佳实践)

**安全建议**：

```
# 在执行删除操作前，先测试
$ find . -name "*.tmp" | xargs -t -p rm
```

**处理大量文件**：

```
# 分批处理，避免参数过长
$ find . -name "*.jpg" | xargs -n 100 jpegoptim
```

**错误处理**：

```
# 遇到错误时继续执行
$ find . -name "*.txt" | xargs -r wc -l
```

`-r` 选项告诉 `xargs` 如果没有输入就不执行命令，避免不必要的错误。

## [6.4 tee：数据流的智能分流器](#_6-4-tee-数据流的智能分流器)

现在我们来学习一个非常实用的工具：`tee`。如果说管道是数据流的"传送带"，那么 `tee` 就像是一个"三通管"，它让数据流可以同时流向多个方向：既继续向下传递，又保存到文件中。

### [tee 的独特价值](#tee-的独特价值)

让我们先理解为什么需要 `tee`。想象一下你在处理一个重要的数据流，既想实时查看处理结果，又想将结果保存到文件中以备后续分析。你可能会这样尝试：

```
# 不好的做法：只能保存到文件
$ command > output.txt
# 这样你就看不到实时输出了

# 也不好的做法：只能看到输出
$ command
# 这样你就无法保存结果了
```

`tee` 命令完美地解决了这个问题：

```
# 好的做法：既能看到输出，又能保存结果
$ command | tee output.txt
```

`tee` 的工作原理很简单：它读取标准输入，然后将内容同时写入标准输出和指定的文件。这样数据流就可以继续向下传递，同时被保存下来。

### [tee 与重定向的区别](#tee-与重定向的区别)

你可能会问："这和重定向有什么区别？" 让我们对比一下：

```
# 重定向：数据流被截断
$ command > output.txt | next_command
# next_command 不会收到任何输入，因为数据已经被重定向到文件了

# tee：数据流继续流动
$ command | tee output.txt | next_command
# next_command 会收到完整的输入，同时数据被保存到文件
```

重定向就像是一个"单向阀"，数据只能流向文件；而 `tee` 像是一个"分流器"，数据可以同时流向多个地方。

### [实际应用场景](#实际应用场景-2)

**场景1：实时监控与记录**

```
# 监控系统日志并保存到文件
$ tail -f /var/log/syslog | tee system.log | grep error
```

这个命令很实用：它实时监控系统日志，将所有日志保存到 `system.log` 文件，同时在终端只显示包含 "error" 的行。这样你既不会错过任何日志信息，又能专注于错误信息。

**场景2：数据分析与记录**

```
# 分析磁盘使用情况并保存结果
$ df -h | tee disk_usage.txt | sort -hr
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   15G  4.5G  77% /
/dev/sdb1       100G   50G   50G  50% /data
```

这个命令分析了磁盘使用情况，将原始数据保存到 `disk_usage.txt`，同时在终端按使用率排序显示。这样你既得到了原始数据，又看到了分析结果。

**场景3：构建处理日志**

```
# 统计 Python 文件数量并记录文件列表
$ find . -name "*.py" | tee python_files.txt | wc -l
25
$ cat python_files.txt | wc -l
25
```

这个命令既统计了 Python 文件的数量，又将文件列表保存到了 `python_files.txt` 中，方便后续处理。

**场景4：编译过程的记录**

```
# 编译项目并记录编译日志
$ make 2>&1 | tee build.log
```

这个命令在编译项目时特别有用：它将编译输出（包括错误信息）保存到 `build.log` 文件，同时在终端实时显示。这样如果编译失败，你可以查看完整的日志来诊断问题。

### [tee 的高级选项](#tee-的高级选项)

**追加模式**

```
# 追加到文件而不是覆盖
$ date | tee -a log.txt
```

`-a` 选项告诉 `tee` 追加内容到文件末尾，而不是覆盖原有内容。这在创建持续更新的日志文件时很有用。

**多文件输出**

```
# 同时保存到多个文件
$ command | tee file1.txt file2.txt | next_command
```

这个功能让你可以将数据同时保存到多个文件，适合需要备份或多用途的场景。

**静默模式**

```
# 只保存到文件，不在终端显示
$ command | tee -a file.txt > /dev/null
```

这个选项让你可以在后台静默地记录数据，而不会干扰终端的输出。

### [实际工作中的应用技巧](#实际工作中的应用技巧)

**技巧1：创建会话记录**

```
# 记录整个操作过程
$ script session.txt
# 开始记录，执行各种命令...
$ exit
# 结束记录
```

`script` 命令实际上使用了类似 `tee` 的机制来记录终端会话。

**技巧2：调试复杂管道**

```
# 在管道中插入 tee 来调试
$ command1 | tee debug1.txt | command2 | tee debug2.txt | command3
```

这样你就可以查看每个步骤的中间结果，帮助调试复杂的管道命令。

**技巧3：实时备份**

```
# 处理数据时同时创建备份
$ cat important_data.txt | tee backup.txt | process_data
```

这在处理重要数据时很有用，可以确保原始数据不会丢失。

**技巧4：多用户协作**

```
# 将重要信息同时显示给多个用户
$ command | tee >(mail -s "Alert" user1@example.com) | >(mail -s "Alert" user2@example.com)
```

这个高级用法可以将数据同时发送给多个用户。

## [6.5 实战案例：构建强大的数据处理流水线](#_6-5-实战案例-构建强大的数据处理流水线)

现在让我们通过一些真实的案例，综合运用我们学到的工具来构建完整的数据处理流水线。这些案例都来自于实际的工作场景，能够帮助你理解如何将这些工具组合起来解决实际问题。

### [案例1：Web 服务器日志分析](#案例1-web-服务器日志分析)

想象一下，你是一个系统管理员，需要分析 Web 服务器的访问日志，找出潜在的安全问题和性能瓶颈。让我们构建一个完整的日志分析流水线。

**分析访问频率最高的 IP 地址**

```
# 分析访问量最大的 10 个 IP
$ cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
   150 192.168.1.100
    89 192.168.1.101
    76 192.168.1.102
```

这个命令的工作流程很清晰：

1. `cat access.log` 读取日志文件
2. `awk '{print $1}'` 提取 IP 地址（第一列）
3. `sort` 将相同 IP 排列在一起
4. `uniq -c` 统计每个 IP 的访问次数
5. `sort -nr` 按访问次数降序排序
6. `head -10` 显示前 10 个最活跃的 IP

**分析最受欢迎的页面**

```
# 找出访问最多的页面
$ cat access.log | awk '{print $7}' | sort | uniq -c | sort -nr | head -10
   200 /index.html
   150 /about.html
   120 /contact.html
```

这个命令帮助我们了解哪些页面最受欢迎，有助于优化网站性能和用户体验。

**检测 404 错误**

```
# 分析 404 错误并记录到文件
$ cat access.log | tee analysis.log | awk '{print $7, $9}' | grep "404" | wc -l
```

这个命令统计了 404 错误的数量，同时将完整的分析过程保存到日志文件中，便于后续详细分析。

### [案例2：批量文件管理流水线](#案例2-批量文件管理流水线)

作为开发人员或系统管理员，我们经常需要批量处理文件。让我们构建一个高效的文件管理流水线。

**批量图片处理**

```
# 批量压缩大尺寸图片
$ find . -name "*.jpg" -size +1M | tee large_images.txt | \
  xargs -n 1 -I {} convert {} -resize 800x600 resized/{}
```

这个命令做了什么：

1. `find . -name "*.jpg" -size +1M` 查找所有大于 1MB 的 JPG 文件
2. `tee large_images.txt` 将找到的文件列表保存到文件
3. `xargs -n 1 -I {} convert {} -resize 800x600 resized/{}` 逐个压缩图片并保存到 resized 目录

**智能文件归档**

```
# 按日期批量重命名文件
$ ls *.txt | while read file; do
    mv "$file" "archive_$(date +%Y%m%d)_$file"
done
```

这个命令会为所有的文本文件添加日期前缀，便于按时间管理和查找文件。

**清理临时文件**

```
# 清理 7 天前的临时文件并记录操作日志
$ find . -name "*.tmp" -mtime +7 | tee deleted_files.txt | xargs rm -v
```

这个命令在清理临时文件的同时，会记录删除了哪些文件，便于审计和追踪。

### [案例3：系统监控与报警流水线](#案例3-系统监控与报警流水线)

系统监控是运维工作的重要组成部分。让我们构建一个自动化的监控和报警系统。

**CPU 使用率监控**

```
# 监控 CPU 使用率并记录趋势
$ top -b -n 1 | grep "Cpu" | tee cpu_usage.log | \
  awk '{print $2}' | cut -d'%' -f1
```

这个命令：

1. `top -b -n 1` 获取一次性的系统快照
2. `grep "Cpu"` 过滤出 CPU 相关的信息
3. `tee cpu_usage.log` 保存到日志文件
4. `awk '{print $2}'` 提取 CPU 使用率数值
5. `cut -d'%' -f1` 去掉百分号，得到纯数字

**磁盘空间预警**

```
# 磁盘空间监控和自动报警
$ df -h | awk '$5 > 80 {print $6 " 使用率: " $5}' | \
  tee disk_warning.log | mail -s "磁盘空间预警" admin@example.com
```

这个命令会监控磁盘使用率，当超过 80% 时自动发送邮件给管理员。这是实际运维中非常实用的功能。

### [一行流模板：常用处理模式](#一行流模板-常用处理模式)

让我们总结一些常用的处理模式，这些模板可以直接应用到你的工作中：

**数据分析模板**

```
# 数据分析的标准流程：过滤→统计→排序→去重
$ cat data.txt | grep pattern | wc -l | sort -nr | uniq
```

**文件处理模板**

```
# 安全的文件处理：查找→备份→处理
$ find . -name "*.conf" -exec cp {} {}.bak \; | \
  xargs sed -i 's/old/new/g'
```

**实时监控模板**

```
# 实时监控和报警：监控→过滤→记录→报警
$ tail -f log.txt | grep --line-buffered ERROR | \
  tee -a errors.log | mail -s "发现错误" admin@example.com
```

**批量重命名模板**

```
# 批量重命名：查找→循环处理
$ ls *.old | while read f; do mv "$f" "${f%.old}.new"; done
```

### [构建复杂流水线的最佳实践](#构建复杂流水线的最佳实践)

**渐进式构建**  
 在构建复杂的管道时，建议采用渐进式的方法：

```
# 第一步：测试数据源
$ cat access.log | head -5

# 第二步：添加过滤
$ cat access.log | awk '{print $1}' | head -5

# 第三步：添加统计
$ cat access.log | awk '{print $1}' | sort | uniq -c | head -5

# 第四步：完成完整流水线
$ cat access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
```

**错误处理和调试**

```
# 在关键节点添加 tee 来调试
$ command1 | tee debug1.txt | command2 | tee debug2.txt | command3
```

**安全操作**

```
# 危险操作前先测试
$ find . -name "*.tmp" | xargs -t -p rm
```

记住，构建复杂流水线时要遵循"由简到繁"的原则，先用少量数据测试，确认每个环节都正常工作后再处理大量数据。

---

## [练习题](#练习题)

1. 如何找出系统中占用 CPU 最多的 5 个进程，并将结果保存到文件同时在终端显示？

查看答案

- 思路与步骤：使用 `ps aux` 获取进程信息，通过管道排序过滤，用 `tee` 同时显示和保存
- 示例命令：

```
# 方法1：基本版本
$ ps aux --sort=-%cpu | head -6 | tee top_cpu_processes.txt

# 方法2：更精确的版本（排除标题行）
$ ps aux --sort=-%cpu | awk 'NR>1 {print $0}' | head -5 | tee top_cpu_processes.txt

# 方法3：格式化输出
$ ps aux --sort=-%cpu | head -6 | \
  awk '{printf "%-10s %-5s %-5s %s\n", $1, $2, $3, $11}' | \
  tee top_cpu_processes.txt
```

第一个命令会显示 CPU 使用率最高的 6 个进程（包括标题行），并将结果保存到文件中。`--sort=-%cpu` 按CPU使用率降序排序，`head -6` 取前6行，`tee` 同时显示和保存。

2. 如何批量查找所有 `.log` 文件中包含 "ERROR" 的行，并将这些行复制到一个汇总文件中？

查看答案

- 思路与步骤：使用 `find` 查找文件，`grep` 过滤内容，`tee` 保存结果
- 示例命令：

```
# 方法1：基本版本
$ find . -name "*.log" -exec grep -H "ERROR" {} \; | tee error_summary.txt

# 方法2：显示行号和文件名
$ find . -name "*.log" -exec grep -Hn "ERROR" {} \; | \
  tee error_summary.txt

# 方法3：更详细的格式
$ find . -name "*.log" -exec grep -Hn "ERROR" {} \; | \
  awk -F: '{printf "文件: %s, 行号: %s, 内容: %s\n", $1, $2, $3}' | \
  tee error_summary.txt

# 方法4：实时监控版本
$ tail -f *.log | grep --line-buffered "ERROR" | \
  tee -a error_summary.txt
```

这些命令会查找所有 `.log` 文件中的 "ERROR" 行，并将结果保存到 `error_summary.txt` 中。`-H` 选项显示文件名，`-n` 选项显示行号，`-a` 选项追加而不是覆盖。

3. 如何统计一个目录下所有文件的扩展名分布情况，并按数量从多到少排序？

查看答案

- 思路与步骤：使用 `find` 查找文件，`awk` 提取扩展名，`sort` 和 `uniq` 统计
- 示例命令：

```
# 方法1：基本版本
$ find . -type f -name "*.*" | awk -F. '{print $NF}' | \
  sort | uniq -c | sort -nr

# 方法2：处理无扩展名文件
$ find . -type f | awk -F. '{if(NF>1)print $NF; else print "无扩展名"}' | \
  sort | uniq -c | sort -nr

# 方法3：更友好的输出格式
$ find . -type f | awk -F. '{if(NF>1)ext=$NF; else ext="无扩展名"; count[ext]++} \
  END {for(e in count) printf "%-15s %d\n", e, count[e]}' | \
  sort -k2 -nr

# 方法4：只显示前10个
$ find . -type f -name "*.*" | awk -F. '{print $NF}' | \
  sort | uniq -c | sort -nr | head -10
```

这些命令会统计文件扩展名的分布情况。`-F.` 设置字段分隔符为点号，`$NF` 获取最后一个字段（扩展名），`uniq -c` 统计频次，`sort -nr` 按数值降序排序。

---

## [速记卡](#速记卡)

- `command1 | command2`：管道连接，将前一个命令的输出作为后一个命令的输入
- `$(command)`：命令替换，将命令结果作为参数
- `find . | xargs rm`：将查找结果转换为删除命令的参数
- `command | tee file.txt`：同时显示输出并保存到文件
- `find . -exec grep {} \;`：对查找结果执行命令
- `command 2>&1`：将错误输出重定向到标准输出
- `sort | uniq -c`：统计重复行的出现次数
- `command | head -10`：只显示前10行结果

## [常见坑](#常见坑)

- 管道中 `cd` 命令失效：管道中的每个命令都在子shell中运行，`cd` 不会影响当前shell
- xargs 处理带空格文件名：默认情况下 xargs 不能正确处理包含空格的文件名，需要用 `-d '\n'` 或 `-0` 选项
- 命令替换嵌套困难：多层嵌套时建议使用 `$(command)` 而不是反引号
- 管道错误输出丢失：管道只传递标准输出，错误输出会直接显示，用 `2>&1` 合并
- xargs 参数过多：某些系统对命令参数数量有限制，用 `-n` 选项分批处理
- tee 覆盖原文件：默认情况下 tee 会覆盖文件，用 `-a` 选项追加内容
- 复杂管道难以调试：构建复杂管道时，建议分段测试每个环节
- 忘记管道的顺序：数据从左向右流动，注意命令的执行顺序

## [章节总结](#章节总结)

管道和命令组合是 Linux 命令行的精髓所在。通过 `|` 管道，你可以将多个简单的命令连接成强大的数据处理流水线，每个命令专注于做一件事，但协同工作时能完成复杂的任务。

命令替换 `$(command)` 让你能够将命令结果嵌入到其他命令中，而 `xargs` 则解决了标准输入与命令参数之间的转换问题。`tee` 命令提供了数据分流的能力，让你能够同时查看和保存数据流。

在实际应用中，这些工具的组合使用能够极大地提高工作效率。无论是日志分析、批量文件处理，还是系统监控，都可以通过构建合适的处理流水线来自动化完成。

记住，构建复杂管道时要遵循"由简到繁"的原则：先用简单的命令测试，确认每个环节都正常工作，再逐步组合成完整的流水线。同时，要特别注意数据的流向和每个命令的输入输出格式，确保管道的各个环节能够正确衔接。

掌握了这些技能，你就能够真正发挥 Linux 命令行的威力，将简单的小工具组合成强大的数据处理系统。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/06-pipes-and-composition.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [06｜管道与命令组合](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_06-管道与命令组合)
- [6.1 管道：连接命令的"传送带"](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_6-1-管道-连接命令的-传送带)
- [理解管道的工作原理](https://xiaolinnote.com/linux/06-pipes-and-composition.html#理解管道的工作原理)
- [从简单到复杂：构建数据处理流水线](https://xiaolinnote.com/linux/06-pipes-and-composition.html#从简单到复杂-构建数据处理流水线)
- [实际应用场景解析](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际应用场景解析)
- [管道的限制与解决方案](https://xiaolinnote.com/linux/06-pipes-and-composition.html#管道的限制与解决方案)
- [6.2 命令替换：将命令结果嵌入其他命令](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_6-2-命令替换-将命令结果嵌入其他命令)
- [理解命令替换的原理](https://xiaolinnote.com/linux/06-pipes-and-composition.html#理解命令替换的原理)
- [现代语法 vs 传统语法](https://xiaolinnote.com/linux/06-pipes-and-composition.html#现代语法-vs-传统语法)
- [实际应用场景](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际应用场景)
- [命令替换与管道的区别](https://xiaolinnote.com/linux/06-pipes-and-composition.html#命令替换与管道的区别)
- [实际工作中的技巧](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际工作中的技巧)
- [6.3 xargs：连接管道与命令的桥梁](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_6-3-xargs-连接管道与命令的桥梁)
- [为什么需要 xargs？](https://xiaolinnote.com/linux/06-pipes-and-composition.html#为什么需要-xargs)
- [xargs 与 find -exec 的选择](https://xiaolinnote.com/linux/06-pipes-and-composition.html#xargs-与-find-exec-的选择)
- [xargs 的实用选项详解](https://xiaolinnote.com/linux/06-pipes-and-composition.html#xargs-的实用选项详解)
- [实际应用场景](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际应用场景-1)
- [xargs 的最佳实践](https://xiaolinnote.com/linux/06-pipes-and-composition.html#xargs-的最佳实践)
- [6.4 tee：数据流的智能分流器](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_6-4-tee-数据流的智能分流器)
- [tee 的独特价值](https://xiaolinnote.com/linux/06-pipes-and-composition.html#tee-的独特价值)
- [tee 与重定向的区别](https://xiaolinnote.com/linux/06-pipes-and-composition.html#tee-与重定向的区别)
- [实际应用场景](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际应用场景-2)
- [tee 的高级选项](https://xiaolinnote.com/linux/06-pipes-and-composition.html#tee-的高级选项)
- [实际工作中的应用技巧](https://xiaolinnote.com/linux/06-pipes-and-composition.html#实际工作中的应用技巧)
- [6.5 实战案例：构建强大的数据处理流水线](https://xiaolinnote.com/linux/06-pipes-and-composition.html#_6-5-实战案例-构建强大的数据处理流水线)
- [案例1：Web 服务器日志分析](https://xiaolinnote.com/linux/06-pipes-and-composition.html#案例1-web-服务器日志分析)
- [案例2：批量文件管理流水线](https://xiaolinnote.com/linux/06-pipes-and-composition.html#案例2-批量文件管理流水线)
- [案例3：系统监控与报警流水线](https://xiaolinnote.com/linux/06-pipes-and-composition.html#案例3-系统监控与报警流水线)
- [一行流模板：常用处理模式](https://xiaolinnote.com/linux/06-pipes-and-composition.html#一行流模板-常用处理模式)
- [构建复杂流水线的最佳实践](https://xiaolinnote.com/linux/06-pipes-and-composition.html#构建复杂流水线的最佳实践)
- [练习题](https://xiaolinnote.com/linux/06-pipes-and-composition.html#练习题)
- [速记卡](https://xiaolinnote.com/linux/06-pipes-and-composition.html#速记卡)
- [常见坑](https://xiaolinnote.com/linux/06-pipes-and-composition.html#常见坑)
- [章节总结](https://xiaolinnote.com/linux/06-pipes-and-composition.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
