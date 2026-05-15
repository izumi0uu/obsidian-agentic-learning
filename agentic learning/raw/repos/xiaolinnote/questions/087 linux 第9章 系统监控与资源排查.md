---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/linux/09-system-monitoring.html"
source: "https://xiaolinnote.com/linux/09-system-monitoring.html"
last_checked: 2026-05-07
freshness: watch
sha256: 05082b7a9617370ae80f45c70183d92d2fb0545b2f556a1884e04e0787e8255f
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 第9章 系统监控与资源排查

原始链接：https://xiaolinnote.com/linux/09-system-monitoring.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 23 分钟约 6763 字2025/9/2

---

# [09｜系统监控与资源排查](#_09-系统监控与资源排查)

大家好，我是小林。

想象一下这样的场景：你的服务器突然变得很慢，用户抱怨网站无法访问，或者你收到警报说磁盘空间即将用完。这时候，你该如何快速定位问题所在？是磁盘满了？内存不足？还是某个进程失控了？

在 Linux 系统管理中，监控和排查问题是必备技能。就像医生需要通过各种检查来了解病人的健康状况一样，系统管理员也需要通过各种工具来监控系统的"健康状态"。这一章我们要学习的，就是如何成为 Linux 系统的"健康检查师"，能够快速定位和解决系统资源问题。

## [9.1 磁盘空间监控：df 和 du](#_9-1-磁盘空间监控-df-和-du)

如何快速了解磁盘空间使用情况？哪些目录占用了最多的空间？

磁盘空间不足是常见的问题，及时发现和处理能够避免系统故障。

### [df：查看文件系统磁盘空间](#df-查看文件系统磁盘空间)

`df` 命令就像是磁盘空间的"仪表盘"，显示各个文件系统的使用情况。

```
# 基本用法：显示磁盘使用情况
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
/dev/sda1       20642476 10245632   9356844  53% /
/dev/sdb1      103212320  5123456  98088864   6% /data

# 人性化显示（推荐）
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       20G   9.8G  9.0G  53% /
/dev/sdb1       99G   4.9G   94G   6% /data

# 显示特定文件系统
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       20G   9.8G  9.0G  53% /

# 显示inode使用情况
$ df -i
Filesystem      Inodes IUsed   IFree IUse% Mounted on
/dev/sda1     1310720 45678 1265042    4% /
```

你可能会问："为什么要关心 inode 使用情况？" 因为即使磁盘空间还有剩余，如果 inode 用完了，也无法创建新文件。这在存储大量小文件的系统中特别常见。

### [du：目录空间使用分析](#du-目录空间使用分析)

`du` 命令就像是目录的"体重秤"，告诉你每个目录占用了多少空间。

```
# 显示当前目录的总空间使用
$ du -sh
2.3G    .

# 显示各子目录的空间使用
$ du -sh */
1.2G    Documents/
856M    Downloads/
234M    Pictures/

# 按大小排序显示最大的目录
$ du -sh */ | sort -hr
1.2G    Documents/
856M    Downloads/
234M    Pictures/

# 查看指定目录的详细使用情况
$ du -h --max-depth=2 /var
```

### [实际应用场景](#实际应用场景)

```
# 场景1：快速查找占用空间最大的目录
$ du -sh /* 2>/dev/null | sort -hr
4.5G    /home
2.1G    /var
1.8G    /usr

# 场景2：查找大文件
$ find /home -type f -size +100M -exec ls -lh {} \;

# 场景3：监控磁盘使用率
$ df -h | awk '$5 > 80 {print $6 " 使用率: " $5}'
/ 使用率: 85%
/var 使用率: 92%
```

你可能会问："为什么需要同时使用 df 和 du？" `df` 查看整个文件系统的使用情况，而 `du` 查看特定目录的使用情况。两者结合使用能够更全面地了解磁盘空间使用状况。

## [9.2 内存使用监控：free 和其他工具](#_9-2-内存使用监控-free-和其他工具)

如何监控系统的内存使用情况？如何判断系统是否内存不足？

内存是系统性能的关键因素，及时监控内存使用状况能够预防系统性能问题。

### [free：查看内存使用情况](#free-查看内存使用情况)

`free` 命令显示系统的内存使用情况，包括物理内存和交换空间。

```
# 基本用法
$ free
              total        used        free      shared  buff/cache   available
Mem:        8175468     2345678     1234567      123456     4567890     5678901
Swap:       2097148           0     2097148

# 人性化显示（推荐）
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           7.8G        2.2G        1.2G        119M        4.4G        5.4G
Swap:          2.0G          0B        2.0G

# 显示总计
$ free -ht
              total        used        free      shared  buff/cache   available
Mem:           7.8G        2.2G        1.2G        119M        4.4G        5.4G
Swap:          2.0G          0B        2.0G
Total:         9.8G        2.2G        3.2G
```

你可能会问："`available` 和 `free` 有什么区别？" `free` 是完全空闲的内存，而 `available` 是可用于分配的内存（包括一些缓存）。`available` 更准确地反映了系统还能分配多少内存给新程序。

### [深入理解内存使用情况](#深入理解内存使用情况)

有时候，你需要持续监控内存使用的变化趋势，或者查看更详细的内存信息。这时候就需要一些更高级的工具。

`watch` 命令就像是你的"自动刷新助手"，能够定期执行命令并显示结果。当你想要观察内存使用的变化趋势时，这个工具特别有用：

```
# 每2秒刷新一次内存使用情况
$ watch -n 2 free -h
```

你会看到屏幕每2秒更新一次，这样就能清楚地看到内存使用的变化趋势。比如，当你启动一个大型程序时，就能实时看到内存是如何被分配和释放的。

如果你需要查看更详细的内存信息，可以直接查看系统的内存信息文件：

```
# 查看详细的内存信息
$ cat /proc/meminfo
MemTotal:        8175468 kB
MemFree:         1234567 kB
MemAvailable:    5678901 kB
Buffers:          123456 kB
Cached:          4567890 kB
...
```

这个文件提供了比 `free` 命令更详细的信息，比如页面缓存、 slab 缓存等。对于高级的系统调优，这些信息很有价值。

当你发现内存使用率过高时，自然想知道是哪些进程在占用内存。这时候可以结合 `ps` 命令来查看：

```
# 查看内存使用率最高的10个进程
$ ps aux --sort=-%mem | head -10
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
mysql       1234  2.5 15.2 1234567 890123 ?      Sl   10:00   0:45 /usr/sbin/mysqld
apache      5678  1.2  8.5  567890 456789 ?      S    10:01   0:12 /usr/sbin/apache2
```

这样你就能快速定位到内存占用大户，比如上面的 MySQL 服务占用了 15.2% 的内存。

### [vmstat：虚拟内存的"透视镜"](#vmstat-虚拟内存的-透视镜)

`vmstat` 命令就像是一个透视镜，让你能够看到系统虚拟内存的内部工作情况。它不仅显示内存使用，还显示进程、CPU、I/O等系统信息。

当你执行 `vmstat` 时，会看到这样的输出：

```
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1234567 123456 4567890    0    0     2     3   10   15 10  5 85  0  0
```

这些数字看起来很复杂，但每一列都有其重要意义：

- **进程部分**：`r` 列显示有多少进程正在等待运行，`b` 列显示有多少进程处于不可中断的睡眠状态
- **内存部分**：显示内存的详细分配情况
- **交换部分**：`si` 和 `so` 显示系统是否在使用交换空间（这是内存不足的重要信号）
- **I/O部分**：显示磁盘 I/O 的活动情况
- **CPU部分**：显示 CPU 时间是如何分配的

你可能会问："为什么要关注这些指标？" 因为它们能够帮你发现系统性能问题的根源。比如，如果 `wa`（等待 I/O）的值很高，说明系统在等待磁盘 I/O，这时候应该检查磁盘性能而不是 CPU。

如果你想要监控系统状态的变化趋势，可以让 `vmstat` 持续运行：

```
# 每2秒更新一次，共显示5次
$ vmstat 2 5
```

这样你就能看到系统状态是如何随时间变化的，这对于发现间歇性的性能问题特别有用。比如，你可能发现某个程序运行时，交换空间的使用突然增加，这说明该程序可能导致内存不足。

## [9.3 系统运行状态：uptime 和其他信息](#_9-3-系统运行状态-uptime-和其他信息)

如何了解系统的整体运行状态？系统运行了多长时间？负载情况如何？

系统运行状态反映了系统的整体健康状况，包括运行时间、负载情况等。

### [uptime：系统运行时间和负载](#uptime-系统运行时间和负载)

```
# 基本用法
$ uptime
 10:30:15 up 10 days,  2:30,  2 users,  load average: 0.10, 0.20, 0.15
```

`uptime` 输出的含义：

- `10:30:15`：当前时间
- `up 10 days, 2:30`：系统运行了10天2小时30分钟
- `2 users`：当前有2个用户登录
- `load average: 0.10, 0.20, 0.15`：1分钟、5分钟、15分钟的平均负载

你可能会问："什么是负载平均值？" 负载平均值表示在单位时间内，等待运行的进程数量。一般来说，负载值不超过CPU核心数是正常的。

### [系统信息查看](#系统信息查看)

```
# 查看内核信息
$ uname -a
Linux server 5.4.0-80-generic #90-Ubuntu SMP Fri Jul 9 22:49:44 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

# 查看发行版信息
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.2 LTS
Release:        20.04
Codename:       focal

# 查看当前时间和日期
$ date
Tue Sep  2 10:30:15 CST 2025
```

### [watch：你的"自动监控助手"](#watch-你的-自动监控助手)

想象一下这样的场景：你正在排查一个间歇性的系统问题，需要持续观察内存使用的变化。这时候，手动重复输入命令会很烦琐。`watch` 命令就像是你的"自动监控助手"，能够定期执行命令并显示结果。

`watch` 的基本用法很简单：

```
# 每2秒刷新一次内存使用情况
$ watch -n 2 free -h
```

执行这个命令后，你会看到屏幕每2秒自动更新一次，显示最新的内存使用情况。这对于观察内存使用趋势特别有用。比如，当你启动一个大型程序时，就能实时看到内存是如何被分配的。

你可能会问："为什么要用 `watch` 而不是手动重复执行命令？" 因为 `watch` 不仅节省了重复输入的工作，更重要的是它会在同一个位置更新输出，让你能够很容易地看出数值的变化。这就像看电影一样，你能看到动态的变化过程，而不是一张张静态的图片。

不同的监控指标需要不同的刷新频率：

```
# 系统负载变化较慢，可以5秒刷新一次
$ watch -n 5 uptime

# 磁盘使用变化更慢，可以10秒刷新一次
$ watch -n 10 df -h
```

这样你就能根据不同指标的变化特点，设置合适的刷新频率，既能及时发现问题，又不会过于频繁地刷新影响系统性能。

## [9.4 文件和进程监控：lsof](#_9-4-文件和进程监控-lsof)

如何查看哪些进程在使用某个文件？如何找到打开某个端口的进程？

`lsof`（list open files）是一个强大的工具，能够列出系统中所有打开的文件和进程。

### [lsof 的基本用法](#lsof-的基本用法)

`lsof` 命令的功能非常强大，它能够显示系统中所有打开的文件和对应的进程。在 Linux 中，"一切皆文件"，这包括普通文件、目录、设备、网络连接等。

最基本的用法是查看所有打开的文件：

```
# 查看所有打开的文件
$ lsof
```

但通常这个输出会很长，包含大量信息。在实际使用中，我们更经常使用 `lsof` 的过滤功能来查找特定的信息。

比如，当你想知道某个用户正在使用哪些文件时：

```
# 查看特定用户打开的文件
$ lsof -u username
```

这在排查用户权限问题时特别有用。比如，某个用户报告无法删除某个文件，你可以用这个命令查看是否有其他进程正在使用该文件。

有时候你需要查看某个特定进程正在访问哪些文件：

```
# 查看特定进程打开的文件
$ lsof -p 1234
```

这对于调试程序很有帮助。比如，你可以看到一个程序正在读取哪些配置文件、写入哪些日志文件等。

你还可以查看某个目录下的文件访问情况：

```
# 查看特定目录下的打开文件
$ lsof +D /var/log
```

这在排查日志文件被占用的问题时特别有用。比如，当你无法轮转日志文件时，可以用这个命令查看是哪个进程在使用日志文件。

### [实际应用场景：解决真实问题](#实际应用场景-解决真实问题)

`lsof` 的真正价值在于解决实际工作中的各种问题。让我们通过几个典型场景来看看它的威力。

**场景1：端口占用问题 - 最常见的故障排查**

你有没有遇到过这样的情况：启动 Web 服务器时，系统提示"端口已被占用"。这时候如何找到是哪个进程在占用端口？

```
# 查找占用80端口的进程
$ lsof -i :80
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1234 root    6u  IPv4  12345      0t0  TCP *:http
```

这个输出清楚地告诉我们：nginx 进程（PID 1234）正在占用 80 端口。现在你就可以决定是停止 nginx 服务，还是让新的服务使用其他端口。

**场景2：文件被占用 - 为什么无法删除文件**

有时候你想删除某个文件，系统却提示"文件正在使用"。这时候就需要找出是哪个进程在使用这个文件：

```
# 查看谁在使用特定的日志文件
$ lsof /var/log/syslog
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
rsyslog  5678 root    1w   REG    8,1 1234567 123456 /var/log/syslog
```

原来 rsyslog 进程正在写入这个日志文件。这就是为什么你无法删除它的原因。你可以选择停止 rsyslog 服务，或者使用其他方法来处理这个文件。

**场景3：网络连接监控 - 查看系统的网络活动**

有时候你怀疑系统中有异常的网络连接，想要查看所有的网络连接：

```
# 查看所有的TCP连接
$ lsof -i TCP
# 查看所有的UDP连接
$ lsof -i UDP
```

这对于发现异常的网络活动特别有用，比如是否有未经授权的程序在连接外部服务器。

**场景4：已删除文件仍被占用 - 磁盘空间之谜**

这是一个很有趣的问题：有时候你删除了一个大文件，但磁盘空间却没有释放。这可能是因为某个进程仍然在打开这个文件：

```
# 查找已删除但仍被占用的文件
$ lsof +L1
```

这些文件虽然在文件系统中已经"删除"，但因为仍有进程在使用它们，所以磁盘空间不会被释放。你需要重启对应的进程才能真正释放空间。

你可能会问："为什么需要 `lsof`？" 因为有时候文件无法删除、目录无法卸载，或者端口被占用，这时候就需要用 `lsof` 来找到是哪个进程在作怪。

## [9.5 系统日志分析：dmesg 和 journalctl](#_9-5-系统日志分析-dmesg-和-journalctl)

如何查看系统启动信息和错误日志？如何分析系统问题？

系统日志是排查问题的重要线索来源，包含了系统运行过程中的各种信息。

### [dmesg：倾听内核的"声音"](#dmesg-倾听内核的-声音)

`dmesg` 命令就像是内核的"日记本"，记录了系统启动和运行过程中的重要信息。当你遇到硬件问题或者系统启动异常时，`dmesg` 往往能提供重要的线索。

最基本的用法是查看所有的内核消息：

```
# 查看内核消息
$ dmesg
```

但这样会输出大量信息，通常我们需要过滤和查找特定的内容。比如，当你怀疑系统有硬件问题时，可以查找错误信息：

```
# 查找内核错误信息
$ dmesg | grep -i error
```

这里的 `-i` 选项让搜索不区分大小写，这样能找到更多相关信息。你可能会看到类似 "memory error" 或 "disk error" 的信息，这些对于硬件故障诊断很有价值。

有时候你只想看最近的内核消息，比如系统在某个操作后出现了问题：

```
# 查看最近的内核消息
$ dmesg | tail
```

这对于排查刚刚发生的问题特别有用。比如，你插入了一个 USB 设备但系统没有识别，可以用这个命令查看内核是否有相关的错误信息。

如果你想要实时监控内核消息，可以使用 `-w` 选项：

```
# 实时监控内核消息
$ dmesg -w
```

这就像在听内核的"实时播报"，当你插入设备、连接网络或者系统出现问题时，能立即看到相关信息。

默认情况下，`dmesg` 显示的时间戳是从系统启动开始的秒数，不太直观。你可以让它显示人类可读的时间：

```
# 显示人类可读的时间戳
$ dmesg -T
```

这样你就能看到具体的时间点，比如 "Tue Sep 2 10:30:15 2025"，这对于和其他日志文件进行时间对比很有帮助。

### [journalctl：现代系统的"日志管家"](#journalctl-现代系统的-日志管家)

在现代的 Linux 系统中，`journalctl` 是一个功能极其强大的日志管理工具。相比于传统的日志文件，`journalctl` 提供了更统一的日志管理接口和更强大的查询功能。

最基本的用法是查看所有系统日志：

```
# 查看所有日志
$ journalctl
```

但通常我们不需要看所有日志。最常见的场景是查看系统启动以来的日志：

```
# 查看本次启动以来的日志
$ journalctl -b
```

这在排查启动问题时特别有用。比如，系统启动后某个服务没有正常启动，你可以用这个命令查看启动过程中的错误信息。

在实际工作中，我们经常需要查看特定服务的日志：

```
# 查看特定服务的日志
$ journalctl -u nginx
```

这比去 `/var/log/nginx/` 目录下找日志文件要方便得多。特别是当你不记得某个服务的日志文件存放在哪里时，这个命令能帮你快速定位。

你可能会问："如何实时查看日志？" 比如你在调试一个服务，想要实时看到日志输出：

```
# 实时跟踪日志输出
$ journalctl -f -u nginx
```

这就像在"直播"日志内容，每当有新的日志产生，你会立即在屏幕上看到。这对于调试正在运行的服务特别有用。

有时候你只关心错误信息，不希望被正常的日志信息干扰：

```
# 只查看错误级别的日志
$ journalctl -p err
```

这里 `-p err` 表示只显示错误（error）级别及以上的日志。这对于快速定位问题很有帮助。

`journalctl` 的另一个强大功能是时间范围查询：

```
# 查看特定时间范围内的日志
$ journalctl --since "2025-09-02 10:00" --until "2025-09-02 10:30"
```

这在排查特定时间段发生的问题时特别有用。比如用户报告上午10:15分出现了问题，你就可以查看这个时间段的日志。

你可能会问："`dmesg` 和 `journalctl` 有什么区别？" `dmesg` 主要显示内核相关的消息，而 `journalctl` 包含了系统所有服务的日志，信息更全面。

## [9.6 实战案例：系统问题排查流程](#_9-6-实战案例-系统问题排查流程)

让我们通过一些实际案例，综合运用监控工具来排查系统问题。

### [案例1：系统变慢的排查流程](#案例1-系统变慢的排查流程)

```
# 第一步：检查系统负载
$ uptime
$ top

# 第二步：检查内存使用
$ free -h
$ vmstat 2

# 第三步：检查磁盘使用
$ df -h
$ iostat 2

# 第四步：检查是否有I/O瓶颈
$ iostat -dx 2

# 第五步：检查系统日志
$ dmesg | tail
$ journalctl -p err --since "1 hour ago"
```

### [案例2：磁盘空间不足的处理](#案例2-磁盘空间不足的处理)

```
# 查找大文件
$ find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null

# 查找大目录
$ du -sh /* 2>/dev/null | sort -hr

# 清理日志文件
$ find /var/log -name "*.log.*" -mtime +30 -delete

# 清理临时文件
$ find /tmp -type f -mtime +7 -delete

# 清理软件包缓存
$ sudo apt-get clean
```

### [案例3：内存泄漏的排查](#案例3-内存泄漏的排查)

```
# 监控内存使用趋势
$ watch -n 5 'free -h && ps aux --sort=-%mem | head -10'

# 查找内存使用异常的进程
$ ps aux --sort=-%mem | head -20

# 检查是否有僵尸进程
$ ps aux | grep 'Z'

# 查看详细的内存使用信息
$ cat /proc/meminfo
```

### [案例4：网络问题排查](#案例4-网络问题排查)

```
# 检查网络连接
$ netstat -tulnp
$ ss -tulnp

# 检查端口占用
$ lsof -i :80

# 监控网络流量
$ iftop
$ nethogs
```

### [一行流模板：常用监控命令](#一行流模板-常用监控命令)

```
# 系统健康检查
$ echo "=== 系统负载 ===" && uptime && echo "=== 内存使用 ===" && free -h && echo "=== 磁盘使用 ===" && df -h

# 查找占用空间最大的文件
$ find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5 -hr | head -10

# 监控高CPU使用率进程
$ top -b -n 1 | awk '$9 > 80 {print $0}'

# 清理系统垃圾文件
$ find /tmp -type f -mtime +7 -delete && find /var/log -name "*.log.*" -mtime +30 -delete
```

> 💡注意：系统监控应该是持续的，建议设置监控脚本和警报机制，而不是等问题发生后再排查。

> ⚠️高危操作：删除系统文件或停止关键服务可能导致系统不稳定。在清理文件或终止进程前，请确认其作用和影响。

---

## [练习题](#练习题)

1. 如何编写一个脚本，当磁盘使用率超过 80% 时发送警报？

查看答案

- 思路与步骤：使用 `df` 获取磁盘使用率，用 `awk` 处理数据，当超过阈值时发送警报
- 示例命令：

```
# 方法1：简单的监控脚本
#!/bin/bash
THRESHOLD=80
df -h | awk -v threshold=$THRESHOLD '$5+0 > threshold {print $6 " 使用率: " $5 "%"}'

# 方法2：完整的监控脚本
#!/bin/bash
THRESHOLD=80
ALERT_FILE="/tmp/disk_alert.log"

check_disk_usage() {
    df -h | grep -vE '^Filesystem|tmpfs|cdrom' | while read line; do
        usage=$(echo $line | awk '{print $5}' | sed 's/%//')
        partition=$(echo $line | awk '{print $6}')
        
        if [ $usage -gt $THRESHOLD ]; then
            echo "$(date): 警报 - 分区 $partition 使用率: ${usage}%" >> $ALERT_FILE
            echo "警报: 分区 $partition 使用率超过 ${THRESHOLD}%"
        fi
    done
}

check_disk_usage

# 方法3：定期执行版本（添加到crontab）
# */5 * * * * /path/to/disk_monitor.sh
```

这个脚本会检查所有分区的磁盘使用率，当超过阈值时记录到日志文件并显示警报。可以设置为定时任务定期执行。

2. 如何找出系统中最近 1 小时内修改过的日志文件，并筛选出包含 "ERROR" 的行？

查看答案

- 思路与步骤：使用 `find` 查找最近修改的文件，用 `grep` 筛选错误信息
- 示例命令：

```
# 方法1：基本版本
$ find /var/log -name "*.log" -mmin -60 -exec grep -H "ERROR" {} \;

# 方法2：显示时间戳和行号
$ find /var/log -name "*.log" -mmin -60 -exec grep -Hn "ERROR" {} \;

# 方法3：使用 journalctl（如果使用systemd）
$ journalctl --since "1 hour ago" | grep -i "error"

# 方法4：更详细的格式
$ find /var/log -name "*.log" -mmin -60 -exec grep -Hn "ERROR" {} \; | \
  awk -F: '{printf "文件: %s, 行号: %s, 内容: %s\n", $1, $2, $3}'

# 方法5：压缩日志文件也检查
$ find /var/log -name "*.log*" -mmin -60 -exec zgrep -H "ERROR" {} \;
```

这些命令会查找最近1小时内修改过的日志文件，并提取包含 "ERROR" 的行。`-mmin -60` 表示60分钟内修改过，`-H` 显示文件名，`-n` 显示行号。

3. 如何持续监控系统的 CPU、内存、磁盘使用情况，并将结果记录到日志文件中？

查看答案

- 思路与步骤：创建一个监控脚本，定期收集系统信息并记录到日志文件
- 示例命令：

```
# 方法1：简单的监控脚本
#!/bin/bash
LOG_FILE="/tmp/system_monitor.log"
INTERVAL=60  # 监控间隔（秒）

while true; do
    echo "=== $(date) ===" >> $LOG_FILE
    echo "--- 系统负载 ---" >> $LOG_FILE
    uptime >> $LOG_FILE
    echo "--- 内存使用 ---" >> $LOG_FILE
    free -h >> $LOG_FILE
    echo "--- 磁盘使用 ---" >> $LOG_FILE
    df -h >> $LOG_FILE
    echo "--- CPU 使用率最高的进程 ---" >> $LOG_FILE
    ps aux --sort=-%cpu | head -6 >> $LOG_FILE
    echo "" >> $LOG_FILE
    sleep $INTERVAL
done

# 方法2：更完整的版本（带日志轮转）
#!/bin/bash
LOG_DIR="/var/log/system_monitor"
LOG_FILE="$LOG_DIR/monitor_$(date +%Y%m%d).log"
MAX_SIZE=$((100 * 1024 * 1024))  # 100MB

# 创建日志目录
mkdir -p $LOG_DIR

# 检查日志文件大小，超过则轮转
if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -gt $MAX_SIZE ]; then
    mv "$LOG_FILE" "${LOG_FILE}.old"
fi

# 监控函数
monitor_system() {
    {
        echo "=== $(date) ==="
        echo "系统信息: $(uname -a)"
        echo "运行时间: $(uptime)"
        echo "内存使用:"
        free -h
        echo "磁盘使用:"
        df -h
        echo "高CPU使用率进程:"
        ps aux --sort=-%cpu | head -6
        echo "高内存使用率进程:"
        ps aux --sort=-%mem | head -6
        echo ""
    } >> "$LOG_FILE"
}

# 主循环
while true; do
    monitor_system
    sleep 60
done

# 方法3：使用 systemd 服务（生产环境推荐）
# 创建 /etc/systemd/system/system-monitor.service 文件
```

这个脚本会持续监控系统状态并记录到日志文件中，包含日志轮转功能防止文件过大。建议在生产环境中使用 systemd 服务来管理监控脚本。

---

## [速记卡](#速记卡)

- `df -h`：人性化显示磁盘使用情况
- `du -sh *`：显示各目录的空间使用
- `free -h`：人性化显示内存使用情况
- `uptime`：查看系统运行时间和负载
- `top`：动态监控进程和资源使用
- `lsof -i :80`：查看占用80端口的进程
- `dmesg | tail`：查看最近的内核消息
- `journalctl -u service`：查看特定服务的日志
- `watch -n 5 command`：定期执行命令并显示结果

## [常见坑](#常见坑)

- 忽略 inode 使用情况：磁盘空间充足但 inode 用完也会导致无法创建文件
- 误解 available 内存：available 才是真正可用的内存，不是 free
- 过度依赖单一指标：系统性能问题需要综合分析 CPU、内存、I/O 等多个指标
- 频繁执行监控命令：过于频繁的监控会影响系统性能
- 忽略日志轮转：日志文件可能无限增长，占用大量磁盘空间
- 清理文件时误删重要数据：删除前确认文件作用，重要文件先备份
- 监控脚本死循环：确保监控脚本有退出机制，避免资源耗尽
- 忽略权限问题：某些监控命令需要管理员权限才能获取完整信息

## [章节总结](#章节总结)

系统监控是 Linux 系统管理的核心技能。通过 `df` 和 `du` 工具，你能够全面了解磁盘空间使用情况，及时发现空间不足的问题。`free` 和 `vmstat` 让你能够监控内存使用状况，预防内存不足导致的性能问题。

系统运行状态监控（`uptime`、`uname`、`date`）提供了系统的整体健康状况，而 `lsof` 则帮助你诊断文件和端口占用问题。`dmesg` 和 `journalctl` 提供了丰富的日志信息，是排查系统问题的重要线索。

在实际应用中，系统监控应该是主动的而不是被动的。建议设置自动化的监控脚本和警报机制，定期检查系统状态，而不是等到问题发生后再排查。同时，要建立完整的日志记录，便于后续的问题分析和趋势预测。

记住，系统监控不仅仅是技术操作，更是对系统健康的管理。通过持续的监控和分析，你能够及时发现潜在问题，优化系统性能，确保系统的稳定运行。掌握了这些监控技能，你就能够成为一个合格的 Linux 系统管理员。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/09-system-monitoring.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [09｜系统监控与资源排查](https://xiaolinnote.com/linux/09-system-monitoring.html#_09-系统监控与资源排查)
- [9.1 磁盘空间监控：df 和 du](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-1-磁盘空间监控-df-和-du)
- [df：查看文件系统磁盘空间](https://xiaolinnote.com/linux/09-system-monitoring.html#df-查看文件系统磁盘空间)
- [du：目录空间使用分析](https://xiaolinnote.com/linux/09-system-monitoring.html#du-目录空间使用分析)
- [实际应用场景](https://xiaolinnote.com/linux/09-system-monitoring.html#实际应用场景)
- [9.2 内存使用监控：free 和其他工具](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-2-内存使用监控-free-和其他工具)
- [free：查看内存使用情况](https://xiaolinnote.com/linux/09-system-monitoring.html#free-查看内存使用情况)
- [深入理解内存使用情况](https://xiaolinnote.com/linux/09-system-monitoring.html#深入理解内存使用情况)
- [vmstat：虚拟内存的"透视镜"](https://xiaolinnote.com/linux/09-system-monitoring.html#vmstat-虚拟内存的-透视镜)
- [9.3 系统运行状态：uptime 和其他信息](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-3-系统运行状态-uptime-和其他信息)
- [uptime：系统运行时间和负载](https://xiaolinnote.com/linux/09-system-monitoring.html#uptime-系统运行时间和负载)
- [系统信息查看](https://xiaolinnote.com/linux/09-system-monitoring.html#系统信息查看)
- [watch：你的"自动监控助手"](https://xiaolinnote.com/linux/09-system-monitoring.html#watch-你的-自动监控助手)
- [9.4 文件和进程监控：lsof](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-4-文件和进程监控-lsof)
- [lsof 的基本用法](https://xiaolinnote.com/linux/09-system-monitoring.html#lsof-的基本用法)
- [实际应用场景：解决真实问题](https://xiaolinnote.com/linux/09-system-monitoring.html#实际应用场景-解决真实问题)
- [9.5 系统日志分析：dmesg 和 journalctl](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-5-系统日志分析-dmesg-和-journalctl)
- [dmesg：倾听内核的"声音"](https://xiaolinnote.com/linux/09-system-monitoring.html#dmesg-倾听内核的-声音)
- [journalctl：现代系统的"日志管家"](https://xiaolinnote.com/linux/09-system-monitoring.html#journalctl-现代系统的-日志管家)
- [9.6 实战案例：系统问题排查流程](https://xiaolinnote.com/linux/09-system-monitoring.html#_9-6-实战案例-系统问题排查流程)
- [案例1：系统变慢的排查流程](https://xiaolinnote.com/linux/09-system-monitoring.html#案例1-系统变慢的排查流程)
- [案例2：磁盘空间不足的处理](https://xiaolinnote.com/linux/09-system-monitoring.html#案例2-磁盘空间不足的处理)
- [案例3：内存泄漏的排查](https://xiaolinnote.com/linux/09-system-monitoring.html#案例3-内存泄漏的排查)
- [案例4：网络问题排查](https://xiaolinnote.com/linux/09-system-monitoring.html#案例4-网络问题排查)
- [一行流模板：常用监控命令](https://xiaolinnote.com/linux/09-system-monitoring.html#一行流模板-常用监控命令)
- [练习题](https://xiaolinnote.com/linux/09-system-monitoring.html#练习题)
- [速记卡](https://xiaolinnote.com/linux/09-system-monitoring.html#速记卡)
- [常见坑](https://xiaolinnote.com/linux/09-system-monitoring.html#常见坑)
- [章节总结](https://xiaolinnote.com/linux/09-system-monitoring.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
