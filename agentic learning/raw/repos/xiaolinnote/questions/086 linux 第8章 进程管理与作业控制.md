---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/linux/08-process-and-job-control.html"
source: "https://xiaolinnote.com/linux/08-process-and-job-control.html"
last_checked: 2026-05-07
freshness: watch
sha256: 629a0d9d058cb875f4ed3039d22d6f0efef7cbae644a1af4ca7ede06e507df09
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---
# 第8章 进程管理与作业控制

原始链接：https://xiaolinnote.com/linux/08-process-and-job-control.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 34 分钟约 10339 字2025/9/2

---

# [08｜进程管理与作业控制](#_08-进程管理与作业控制)

大家好，我是小林。

想象一下这样的场景：你正在运行一个需要很长时间的程序，突然发现它占用了太多的系统资源，导致其他程序都无法正常运行。或者你启动了一个程序，但需要关闭终端，却发现程序也随之终止了。这时候，你该如何有效地管理系统中的进程呢？

在 Linux 系统中，进程是程序的执行实例。就像我们日常生活中的各种任务一样，进程也需要被管理和控制。有些进程需要优先处理，有些需要暂时搁置，有些需要完全停止。这一章我们要学习的，就是如何成为 Linux 系统的"任务调度员"，能够有效地管理和控制系统中的各种进程。

## [8.1 查看进程：ps、pgrep 和 top](#_8-1-查看进程-ps、pgrep-和-top)

如何了解系统中正在运行的进程？有哪些工具可以帮助我们监控进程状态？

在 Linux 系统中，进程管理的基础是能够查看和了解当前运行的进程。不同的工具提供了不同的视角和详细信息。

### [ps：静态进程快照](#ps-静态进程快照)

`ps` 命令就像是给系统中的进程拍了一张照片，显示某个时刻的进程状态。

```
# 基本用法：显示当前用户的进程
$ ps
  PID TTY          TIME CMD
 1234 pts/0    00:00:01 bash
 1235 pts/0    00:00:00 ps

# 显示所有用户的详细进程信息
$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1 168000 12000 ?        Ss   10:00   0:02 /sbin/init
user        1234  0.0  0.1  12000  8000 pts/0    Ss   10:30   0:01 bash
user        1236  0.2  0.5 500000 40000 pts/0    R+   10:35   0:00 python script.py
```

你可能会问："`ps aux` 中的这些列代表什么意思？"

- `USER`：进程所有者
- `PID`：进程 ID（唯一标识）
- `%CPU`：CPU 使用率
- `%MEM`：内存使用率
- `VSZ`：虚拟内存大小
- `RSS`：实际使用的物理内存
- `TTY`：控制终端
- `STAT`：进程状态（S=睡眠，R=运行，Z=僵尸等）
- `START`：启动时间
- `TIME`：累计 CPU 时间
- `COMMAND`：命令名称

### [灵活运用 ps 命令](#灵活运用-ps-命令)

在实际工作中，你经常需要用不同的方式来查看进程信息。`ps` 命令提供了丰富的选项来满足各种需求。

有时候你需要了解进程之间的父子关系，比如你想知道某个进程启动了哪些子进程：

```
# 显示进程树结构
$ ps auxf
```

这个命令会以树形结构显示进程，让你能够清楚地看到进程之间的父子关系。这在排查进程启动问题时特别有用。比如，你可能发现一个Web服务器启动了多个工作进程，通过进程树就能清楚地看到它们的关系。

当你只想查看特定用户的进程时，可以使用 `-u` 选项：

```
# 查看特定用户的进程
$ ps -u username
```

这在多用户系统中特别有用。比如，系统管理员想要查看某个用户正在运行哪些进程，或者你想要查看自己的进程有哪些。

如果你已经知道某个进程的 PID，想要查看它的详细信息：

```
# 查看指定进程的详细信息
$ ps -p 1234 -l
```

这里的 `-l` 选项会显示更详细的信息，包括进程的优先级、调度策略等。这对于调试特定进程的问题很有帮助。

在实际的系统监控中，你经常需要找出占用资源最多的进程。`ps` 命令的排序功能就能派上用场：

```
# 按CPU使用率排序，显示前10个进程
$ ps aux --sort=-%cpu | head -10

# 按内存使用率排序，显示前10个进程
$ ps aux --sort=-%mem | head -10
```

你可能会问："为什么用 `head -10` 而不是 `head -11`？" 因为 `ps aux` 的输出包含一行标题，所以我们取前10行实际上得到了9个进程的信息。这在系统变慢时特别有用，你能快速找到是哪个进程在消耗大量资源。

### [pgrep：进程查找的"快捷方式"](#pgrep-进程查找的-快捷方式)

想象一下这样的场景：你需要快速找到一个正在运行的进程，但不想在大量的进程输出中费力地搜索。或者你需要编写一个脚本来自动处理某些进程，但需要一个可靠的方式来定位它们。这时候，`pgrep` 就是你的得力助手。

`pgrep` 就像是一个专门查找进程的"搜索引擎"，它比传统的 `ps | grep` 方法更高效、更精确。

**基本用法：快速定位进程**

当你需要根据进程名查找进程时，`pgrep` 的用法非常直观：

```
# 查找所有bash进程
$ pgrep bash
1234
1256
2345
```

这个输出显示了所有 bash 进程的 PID。你可能会问："这和 `ps | grep bash` 有什么区别？" 让我们对比一下：

```
# 传统方法
$ ps aux | grep bash
user      1234  0.0  0.1  12000  8000 pts/0    Ss   10:00   0:01 bash
user      1256  0.0  0.1  12000  8000 pts/1    Ss   10:05   0:01 bash
user      5678  0.0  0.0   8000  4000 pts/0    S+   10:30   0:00 grep bash
```

注意到了吗？`ps | grep` 会把 grep 进程本身也显示出来，而 `pgrep` 不会。这在编写脚本时特别重要，因为你不想误杀 grep 进程。

**增强功能：不止是查找PID**

`pgrep` 的真正威力在于它的各种选项，让你能够精确地查找进程：

```
# 查找进程并显示进程名（更直观）
$ pgrep -l bash
1234 bash
1256 bash

# 查找特定用户的进程（多用户环境很有用）
$ pgrep -u username bash
# 这会显示指定用户的所有bash进程

# 查找完整的命令行（区分同名进程）
$ pgrep -f "python backup_script.py"
# 这会匹配完整的命令行，而不是只匹配进程名
```

你可能会问："什么时候需要 `-f` 选项？" 想象一下，你运行了多个 Python 脚本，它们都显示为 "python" 进程。如果你想终止特定的备份脚本，就需要用 `-f` 来精确匹配。

**实际应用场景**

`pgrep` 在系统管理和脚本编写中有很多实用场景：

```
# 场景1：检查某个服务是否运行
$ if pgrep nginx > /dev/null; then
    echo "nginx is running"
else
    echo "nginx is not running"
fi

# 场景2：优雅地重启服务
$ pgrep nginx | xargs kill -HUP
# 向所有nginx进程发送重载配置信号

# 场景3：查找并终止僵死进程
$ pgrep -f "defunct" | xargs kill -9
```

**与其它工具的对比**

你可能会问："为什么还要学习 `pgrep`，`ps` 不是已经够用了吗？" 这就像问："为什么需要计算器，纸笔不是可以计算吗？"

- `ps aux | grep`：适合人工查看，详细信息丰富
- `pgrep`：适合脚本编程，输出简洁精确
- `pgrep` 不会匹配自己的进程，避免了误操作
- `pgrep` 语法更简洁，减少了出错的可能性

在实际工作中，建议将这两个工具结合使用：用 `ps` 查看详细信息，用 `pgrep` 进行精确的进程操作。

### [top 和 htop：系统的"实时监控仪表板"](#top-和-htop-系统的-实时监控仪表板)

想象一下这样的场景：你的服务器突然变得很慢，用户抱怨网站响应迟钝。你需要快速找出是哪个进程在捣乱，但静态的 `ps` 命令只能显示某一时刻的快照。这时候，你就需要一个能够实时监控系统状态的工具。

`top` 就像是汽车的仪表板，让你能够实时看到系统的"运行状态"，包括 CPU 使用率、内存使用情况、以及哪些进程正在消耗资源。

**top：经典的过程监控器**

当你启动 `top` 时，会看到一个持续更新的界面：

```
$ top
```

你会看到类似这样的界面（持续更新）：

```
top - 10:30:15 up 10 days,  2:30,  2 users,  load average: 0.10, 0.20, 0.15
Tasks: 123 total,   1 running, 122 sleeping,   0 stopped,   0 zombie
%Cpu(s): 10.0 us,  5.0 sy,  0.0 ni, 85.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  8175468 total,  2345678 used,  4567890 free,  123456 buffers
KiB Swap:  2097148 total,        0 used,  2097148 free,  567890 cached

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 1234 mysql     20   0  1234567 890123  56789 S  15.2 10.9   0:45.67 mysqld
 5678 apache    20   0   567890 456789  34567 S   8.5  5.6   0:12.34 apache2
```

这个界面告诉我们什么？

**系统概览区**（前5行）：

- 第一行：系统时间、运行时间、用户数、系统负载
- 第二行：进程总数和状态统计
- 第三行：CPU 使用情况（用户态、系统态、空闲等）
- 第四行：内存使用情况
- 第五行：交换空间使用情况

**进程列表区**（下方）：

- 按CPU使用率排序的进程列表
- 显示每个进程的PID、用户、CPU和内存使用率等信息

你可能会问："什么是系统负载？" 负载平均值表示在单位时间内，等待运行的进程数量。一般来说，负载值不超过CPU核心数是正常的。如果负载持续很高，说明系统很忙。

**top 的交互式操作**

`top` 不仅仅是用来看的，它还提供了丰富的交互功能：

```
# 在 top 运行时，可以按以下键：
P       # 按 CPU 使用率排序（默认）
M       # 按内存使用率排序
k       # 杀死进程（会提示输入PID）
r       # 重新设置进程优先级
z       # 彩色/黑白显示切换
c       # 显示完整命令行
q       # 退出 top
```

这些操作让你能够在不退出 `top` 的情况下进行各种进程管理操作。比如，当你发现某个进程占用过多CPU时，可以直接按 `k` 键终止它。

**htop：现代化的监控工具**

虽然 `top` 功能强大，但它的界面相对简陋，操作也不够直观。`htop` 就是 `top` 的现代化改进版本。

首先需要安装 `htop`：

```
$ sudo apt install htop  # Ubuntu/Debian
$ sudo yum install htop  # CentOS/RHEL
```

启动 `htop`：

```
$ htop
```

你会看到一个彩色的、更直观的界面。`htop` 的优势体现在：

**视觉体验的改进**：

- 彩色显示，不同类型的进程用不同颜色
- 进度条显示CPU和内存使用率，更直观
- 支持鼠标操作（在支持的终端中）

**功能的增强**：

- 可以垂直和水平滚动，查看更多信息
- 支持进程树显示，清楚展示进程间的父子关系
- 可以直接点击进程进行操作，无需输入PID

**操作更便捷**：

- F1-F10 功能键提供常用操作
- 支持标记多个进程进行批量操作
- 支持自定义显示列和排序方式

你可能会问："为什么还要用 `top`，直接用 `htop` 不是更好吗？" 这就像问："为什么还有用老式手机的人？"

- `top` 在所有系统上都预装，无需额外安装
- `top` 资源占用更少，适合在资源紧张的系统上使用
- `htop` 功能更丰富，但需要额外安装
- 在某些嵌入式系统或服务器上，可能只有 `top` 可用

**实际应用场景**

```
# 场景1：监控系统负载
$ top -d 5  # 每5秒刷新一次

# 场景2：监控特定用户进程
$ top -u username

# 场景3：批量监控模式（适合脚本）
$ top -b -n 1 > top_snapshot.txt
```

在实际的系统管理中，建议：

- 日常监控使用 `htop`，界面友好，信息丰富
- 脚本编程使用 `top -b` 批处理模式
- 紧急情况下使用 `top`，因为它总是可用的

掌握了 `top` 和 `htop` 的使用，你就能够实时监控系统的健康状况，及时发现和解决性能问题。

**综合应用案例**

在实际的系统管理中，你需要根据不同的情况选择合适的工具。让我们通过一些具体的场景来展示如何灵活运用这些进程查看工具。

**场景1：系统突然变慢的快速排查**

当用户抱怨系统变慢时，你需要快速定位问题：

```
# 第一步：快速查看系统负载和最耗CPU的进程
$ top -b -n 1 | head -15
# 或者更简洁的：
$ ps aux --sort=-%cpu | head -5

# 第二步：如果发现某个进程异常，持续监控它
$ top -p 1234  # 专门监控可疑进程

# 第三步：检查内存使用情况
$ ps aux --sort=-%mem | head -5
```

**场景2：服务器性能监控**

对于长期运行的服务器，你需要定期检查进程状态：

```
# 检查Web服务进程
$ pgrep nginx || echo "nginx is not running"
$ ps -fC nginx  # 查看nginx进程详细信息

# 检查数据库进程
$ ps -o pid,ppid,%cpu,%mem,cmd -C mysql
# 只显示关键字段，避免信息过载

# 检查所有用户的进程数量
$ ps hax -o user | sort | uniq -c | sort -nr
```

**场景3：开发环境调试**

在开发和测试环境中，经常需要查找和控制进程：

```
# 查找自己的Python进程
$ ps aux | grep python | grep $(whoami)

# 查找僵尸进程
$ ps aux | awk '$8 ~ /^Z/ {print $2, $11}'

# 监控特定应用的进程
$ watch -n 2 'pgrep -f "myapp" | wc -l'
```

你可能会问："为什么需要这么多不同的方法？" 因为不同的场景需要不同的粒度和信息量。就像医生检查病人，有时候需要快速体温测量，有时候需要详细的血液检查。

**工具选择的决策树**

在实际工作中，可以按照这个思路选择工具：

1. **需要快速查看系统概况** → 用 `top` 或 `htop`
2. **需要查看某个时间点的快照** → 用 `ps aux`
3. **需要编写脚本处理进程** → 用 `pgrep`
4. **需要持续监控单个进程** → 用 `top -p PID`
5. **需要查看进程树结构** → 用 `ps auxf` 或 `htop`

记住，这些工具不是相互替代的关系，而是相互补充的。熟练掌握它们的使用场景，你就能在系统管理中游刃有余。

## [8.2 终止进程：kill、pkill 和 killall](#_8-2-终止进程-kill、pkill-和-killall)

想象一下这样的场景：你发现某个进程占用了过多的系统资源，导致其他程序无法正常运行。或者某个程序卡住了，没有任何响应。这时候，你需要"终止"这个进程，让它停止运行。

但是，"终止进程"这件事并不像表面上看起来那么简单。就像让一个人离开房间，你可以礼貌地请他离开，也可以直接把他赶出去。不同的方式会有不同的结果和影响。

### [kill：进程通信的"信号语言"](#kill-进程通信的-信号语言)

`kill` 命令的本质并不是"杀死"进程，而是向进程发送信号。在 Linux 中，信号是一种进程间通信的方式，不同的信号代表不同的含义。

**最基本的进程终止**

当你需要终止一个进程时，最简单的方法是：

```
# 基本用法：向进程发送终止信号
$ kill 1234  # 1234是进程的PID
```

这个命令实际上向进程发送了 SIGTERM 信号（信号编号15）。这是一种"礼貌的"终止方式，它会请求进程自行终止，给进程一个清理的机会。

你可能会问："为什么要给进程清理的机会？" 想象一下，如果一个进程正在写入重要的数据，突然被强制终止可能会导致数据损坏。给它一个清理的机会，就像让一个人离开前收拾好自己的物品。

**信号的艺术：不同的终止方式**

Linux 提供了多种信号，让你能够以不同的方式与进程通信：

```
# 发送不同的信号，效果完全不同
$ kill -TERM 1234    # 终止信号（默认），相当于请他离开
$ kill -INT 1234     # 中断信号，类似按Ctrl+C
$ kill -KILL 1234    # 强制终止信号，相当于直接赶出去
$ kill -HUP 1234     # 挂起信号，通常用于重新加载配置
```

这些信号有什么区别？

- **SIGTERM（15）**：礼貌地请求进程终止。进程可以捕获这个信号，保存数据后优雅退出。
- **SIGKILL（9）**：强制终止进程。进程无法捕获或忽略这个信号，会被立即终止。
- **SIGHUP（1）**：挂起信号。很多服务会重新加载配置文件，而不是真正退出。

**信号的完整清单**

Linux 系统中定义了很多信号，每种都有其特定用途：

```
# 查看所有可用信号
$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

虽然信号很多，但作为系统管理员，你最需要记住的是：

```
# 最常用的信号
# 1 (SIGHUP)：重新加载配置 - 让服务重新读取配置文件
# 2 (SIGINT)：中断 - 像Ctrl+C一样中断进程
# 9 (SIGKILL)：强制终止 - 无条件终止进程，最后手段
# 15 (SIGTERM)：正常终止 - 优雅地请求进程退出
# 18 (SIGCONT)：继续运行 - 恢复被暂停的进程
# 19 (SIGSTOP)：暂停运行 - 暂停进程的执行
```

**实际应用场景**

让我们看看在实际工作中如何使用这些信号：

```
# 场景1：优雅地重启Web服务
$ kill -HUP $(pgrep nginx)
# 这会让nginx重新加载配置，而不是完全重启

# 场景2：处理无响应的进程
$ kill -TERM 1234   # 先尝试礼貌地终止
sleep 2              # 等待2秒
$ kill -KILL 1234   # 如果还活着，就强制终止

# 场景3：暂停和恢复进程
$ kill -STOP 1234   # 暂停进程
$ kill -CONT 1234   # 恢复进程运行
```

你可能会问："为什么不直接用 SIGKILL？" 因为强制终止可能会带来问题：

- 可能导致数据丢失或文件损坏
- 可能会导致临时文件没有被清理
- 可能会破坏正在进行的数据库事务

**信号处理的最佳实践**

在实际的系统管理中，建议遵循这个终止进程的流程：

```
# 1. 首先尝试优雅终止
$ kill 1234

# 2. 等待几秒钟，给进程清理的时间
$ sleep 3

# 3. 检查进程是否还在运行
$ ps -p 1234

# 4. 如果还在运行，再尝试强制终止
$ kill -9 1234
```

这个流程既给了进程优雅退出的机会，又确保了最终能够终止进程。就像处理一个不愿离开的人，先礼貌地请他离开，给他时间收拾，如果实在不行再采取强制措施。

理解信号的工作原理，让你能够更精细地控制进程的行为，而不是简单地"杀死"它们。这是 Linux 系统管理的重要技能。

### [pkill 和 killall：批量进程管理的利器](#pkill-和-killall-批量进程管理的利器)

想象一下这样的场景：你需要终止所有属于某个用户的进程，或者需要关闭某个程序的所有实例。如果使用 `kill` 命令，你需要先用 `ps` 或 `pgrep` 找到所有相关的 PID，然后再一个个地终止它们。这显然很繁琐。

这时候，`pkill` 和 `killall` 就派上用场了。它们能够根据进程名或其他属性直接终止进程，无需手动查找 PID。

**pkill：灵活的进程终止工具**

`pkill` 就像是一个"智能猎手"，它能够根据多种条件找到并终止进程。

```
# 基本用法：根据进程名终止
$ pkill firefox
# 这会终止所有名为firefox的进程
```

这个命令会找到所有进程名为 "firefox" 的进程，并向它们发送 SIGTERM 信号。你不需要先查找 PID，`pkill` 会自动完成这个工作。

**按条件精确终止**

`pkill` 的真正威力在于它支持多种匹配条件：

```
# 终止特定用户的所有进程
$ pkill -u username
# 这在清理用户会话时很有用

# 根据完整的命令行终止进程
$ pkill -f "python backup_script.py"
# 这会匹配包含"python backup_script.py"的完整命令行

# 终止特定终端的进程
$ pkill -t pts/0
# 终止在pts/0终端上运行的所有进程

# 终止特定用户组的进程
$ pkill -G groupname
```

你可能会问："什么时候需要 `-f` 选项？" 想象一下，你运行了多个 Python 脚本，它们都显示为 "python" 进程。如果你想终止特定的备份脚本，就需要用 `-f` 来精确匹配完整的命令行。

**发送不同的信号**

和 `kill` 一样，`pkill` 也可以发送不同的信号：

```
# 优雅地重启服务
$ pkill -HUP nginx
# 这会让nginx重新加载配置文件

# 强制终止所有Java进程
$ pkill -KILL -f java
# 向所有Java进程发送SIGKILL信号
```

**killall：传统的批量终止工具**

`killall` 是另一个批量终止进程的工具，但它的行为与 `pkill` 略有不同：

```
# 基本用法
$ killall firefox

# 按信号终止
$ killall -HUP nginx

# 交互式确认（安全选项）
$ killall -i firefox
# 终止前会询问确认

# 测试模式（只显示会做什么）
$ killall -e firefox
```

**pkill vs killall：选择哪个？**

你可能会问："这两个工具功能相似，应该用哪个？" 让我们比较一下：

```
# pkill 的优势：
$ pkill -f "python.*backup"  # 支持正则表达式
$ pkill -u username -f java  # 可以组合多个条件
$ pkill --oldest firefox     # 终止最老的进程
$ pkill --newest firefox     # 终止最新的进程

# killall 的特点：
$ killall -i firefox          # 有交互确认选项
$ killall -r "firefox.*"     # 也支持正则表达式
$ killall -w firefox          # 等待进程真正终止
```

主要区别：

- **匹配精度**：`pkill` 默认只匹配进程名，更精确；`killall` 匹配进程名的任何部分，可能误杀
- **功能丰富度**：`pkill` 选项更多，支持更复杂的匹配条件
- **安全性**：`killall` 有交互确认选项，更安全
- **兼容性**：`killall` 在某些系统上可能行为不同（如Solaris系统）

**实际应用场景**

让我们通过一些实际场景来展示这些工具的威力：

```
# 场景1：系统维护时清理用户进程
$ pkill -u username
# 在用户注销后清理其残留进程

# 场景2：重启Web服务
$ pkill -HUP nginx
# 优雅地重新加载nginx配置

# 场景3：处理失控的脚本
$ pkill -f "runaway_script.py"
# 终止所有运行特定脚本的进程

# 场景4：批量终止僵尸进程
$ pkill -f "defunct|<defunct>"
# 清理系统中的僵尸进程

# 场景5：开发环境重置
$ pkill -u $(whoami) -f "python|node|java"
# 终止当前用户的所有开发相关进程
```

**安全使用的最佳实践**

使用这些强大的工具时，需要格外小心：

```
# 测试模式：先看看会终止什么
$ pkill -echo -f "python"
# 这会显示会终止哪些进程，但不实际执行

# 交互模式：逐个确认
$ killall -i firefox
# 终止每个进程前都会询问

# 精确匹配：避免误杀
$ pkill -f "/usr/bin/python3 /path/to/script.py"
# 使用完整路径，避免误杀其他python进程
```

**高级技巧**

```
# 终止除最老进程外的所有进程
$ pkill --older 3600 -f "myapp"
# 终止运行时间超过1小时的进程

# 终止特定终端的所有进程
$ pkill -t pts/0
# 在用户退出后清理其终端进程

# 组合条件：终止特定用户的特定进程
$ pkill -u username -f "nginx"
```

> ⚠️高危操作：批量终止进程是危险的操作！在生产环境中使用前，务必：
>
> 1. 先用 `pgrep -f` 或 `pkill -echo` 测试，确认会终止哪些进程
> 2. 考虑使用 `killall -i` 进行交互确认
> 3. 避免使用过于宽泛的模式，可能误杀重要进程
> 4. 记住 `kill -9` 是最后手段，优先使用 SIGTERM

掌握了 `pkill` 和 `killall` 的使用，你就能够高效地管理批量进程，而不是一个个地手动处理。这在系统维护和故障排除时特别有用。

## [8.3 作业控制：后台运行与进程切换](#_8-3-作业控制-后台运行与进程切换)

想象一下这样的场景：你正在运行一个需要很长时间的备份任务，但突然需要紧急处理其他工作。或者你启动了一个程序，但需要关闭终端回家，却发现程序也随之终止了。这时候，你该如何有效地管理这些任务呢？

作业控制是 Linux 提供的一个强大功能，它让你能够在单个终端中管理多个进程，就像一个任务调度员，能够决定哪个任务在前台运行，哪个任务在后台运行，哪个任务需要暂停。

### [后台运行：& 符号的魔法](#后台运行-符号的魔法)

在默认情况下，当你在终端中运行一个命令时，终端会被"占用"，直到命令执行完成。这在运行长时间任务时很不方便，因为你无法同时做其他事情。

**基本的后台运行**

```
# 将命令放到后台运行
$ long_running_command &
[1] 1234
```

这个命令会立即返回，显示两行信息：

- `[1]`：这是作业号，用于标识这个后台任务
- `1234`：这是进程ID（PID），是系统用来标识进程的数字

**实际应用示例**

让我们看一个实际的例子：

```
# 后台压缩大文件
$ tar -czvf backup.tar.gz large_directory/ &
[1] 1234

# 立即可以执行其他命令
$ ls -la
total 12345
drwxr-xr-x 2 user user 4096 Sep 1 10:00 large_directory
-rw-r--r-- 1 user user  512 Sep 1 10:05 backup.tar.gz

# 查看后台作业的状态
$ jobs
[1]+  Running                 tar -czvf backup.tar.gz large_directory/ &
```

你可能会问："后台运行和在前台运行有什么区别？"

- **前台运行**：终端被占用，无法输入其他命令，直到命令完成
- **后台运行**：终端立即释放，可以继续输入其他命令，程序在"幕后"运行

**后台任务的输出管理**

后台任务的一个特殊之处是它们的输出处理：

```
# 后台任务的输出仍然会显示在终端上
$ sleep 10 & echo "立即执行"
[1] 1234
立即执行
# 10秒后，可能看到：
# [1]+  Done                    sleep 10
```

为了避免输出干扰，通常建议将后台任务的输出重定向：

```
# 将输出重定向到文件
$ long_running_command > output.log 2>&1 &
```

### [暂停和恢复：Ctrl+Z 的力量](#暂停和恢复-ctrl-z-的力量)

有时候你启动了一个程序，后来才发现它需要很长时间运行。这时候你不想重新启动它，而是希望让它暂时"暂停"，等处理完其他事情后再恢复。

**暂停前台进程**

```
# 启动一个长时间运行的命令
$ ping google.com
PING google.com (142.250.196.78) 56(84) bytes of data.
64 bytes from google.com (142.250.196.78): icmp_seq=1 ttl=117 time=15.2 ms
^Z
[1]+  Stopped                 ping google.com
```

按 `Ctrl+Z` 会立即暂停当前进程，并显示作业信息。注意，进程只是暂停了，并没有终止，它还在内存中，只是不再运行。

**恢复进程的运行**

暂停后的进程有两个选择：

```
# 将暂停的进程转到后台运行
$ bg 1
[1]+ ping google.com &

# 或者将暂停的进程调回前台
$ fg 1
ping google.com
64 bytes from google.com (142.250.196.78): icmp_seq=2 ttl=117 time=16.1 ms
```

你可能会问："为什么需要暂停进程？"

1. **临时处理其他任务**：当需要立即处理其他工作，但又不想终止当前任务时
2. **调整进程优先级**：暂停后可以用其他工具调整进程的优先级
3. **检查系统状态**：暂停进程后可以检查系统资源使用情况

### [nohup：让进程"无视"终端关闭](#nohup-让进程-无视-终端关闭)

想象一下这样的场景：你在服务器上启动了一个重要的数据处理任务，需要运行几个小时。但你不能一直保持终端连接，需要关闭电脑回家。这时候，`nohup` 就派上用场了。

**nohup 的工作原理**

`nohup` 的全称是 "no hang up"，意思是"不挂断"。它的作用是让进程忽略 SIGHUP 信号（挂断信号）。

```
# 基本用法
$ nohup long_running_command &
nohup: ignoring input and appending output to 'nohup.out'
```

这个命令会：

1. 让进程忽略 SIGHUP 信号
2. 自动将输出重定向到 `nohup.out` 文件
3. 立即返回提示，进程在后台运行

**更完整的用法**

在实际工作中，通常会这样使用 `nohup`：

```
# 指定输出文件
$ nohup python data_processing.py > processing.log 2>&1 &

# 查看任务进度
$ tail -f processing.log
Processing file 1 of 100...
Processing file 2 of 100...
```

你可能会问："为什么需要 `> output.log 2>&1`？"

- `> output.log`：将标准输出重定向到文件
- `2>&1`：将标准错误也重定向到同一个文件
- `&`：在后台运行

**nohup 的局限性**

虽然 `nohup` 很有用，但它也有一些局限性：

1. **无法交互**：一旦启动，就无法与进程交互
2. **输出管理**：需要手动管理输出文件
3. **无法重新连接**：无法重新连接到已经运行的进程

### [disown：完全脱离终端](#disown-完全脱离终端)

有时候你忘记使用 `nohup` 启动了一个长期任务，但又不想终止它。这时候 `disown` 就能帮到你。

```
# 启动一个进程（忘记用nohup）
$ long_running_command &
[1] 1234

# 将作业从shell的作业列表中移除
$ disown %1

# 现在关闭终端，进程会继续运行
```

`disown` 的作用是将作业从当前 shell 的作业列表中移除，这样当 shell 关闭时，就不会向该作业发送 SIGHUP 信号。

### [screen 和 tmux：终端复用器](#screen-和-tmux-终端复用器)

对于需要长期运行多个任务的场景，`screen` 和 `tmux` 是更好的解决方案。它们就像是"虚拟终端管理器"，让你能够创建多个终端会话，并在它们之间切换。

**screen：经典终端复用器**

首先安装 `screen`：

```
$ sudo apt install screen  # Ubuntu/Debian
$ sudo yum install screen  # CentOS/RHEL
```

基本使用方法：

```
# 创建新的screen会话
$ screen -S myproject

# 在screen中运行命令
$ python data_analysis.py

# 暂时离开screen（按Ctrl+A，然后按D）
[detached from 1234.myproject]

# 查看所有screen会话
$ screen -ls
There is a screen on:
    1234.myproject   (09/01/2025 10:30:15 AM)    (Detached)

# 重新连接到screen
$ screen -r myproject
```

**tmux：现代化的终端复用器**

`tmux` 是 `screen` 的现代化替代品，功能更强大：

```
# 安装tmux
$ sudo apt install tmux

# 创建新会话
$ tmux new -s myproject

# 在tmux中运行命令
$ python data_analysis.py

# 暂时离开（按Ctrl+B，然后按D）
[detached]

# 查看会话
$ tmux ls
myproject: 1 windows (created Tue Sep  1 10:30:15 2025) [80x24]

# 重新连接
$ tmux attach -t myproject
```

**screen/tmux 的优势**

相比于 `nohup` 和 `disown`，终端复用器有很多优势：

1. **多窗口管理**：可以创建多个终端窗口
2. **会话持久化**：可以随时断开和重新连接
3. **实时交互**：可以实时查看和控制进程
4. **会话共享**：可以与其他用户共享终端会话

### [实际应用场景](#实际应用场景)

让我们通过一些具体的场景来展示作业控制的实际应用：

```
# 场景1：数据分析任务
$ nohup python analyze_data.py > analysis.log 2>&1 &
$ tail -f analysis.log  # 实时查看进度

# 场景2：Web服务器启动
$ python -m http.server 8000 &
$ jobs
[1]+  Running    python -m http.server 8000 &
$ fg %1  # 需要停止时调回前台，按Ctrl+C

# 场景3：批量文件处理
$ for i in {1..10}; do
    process_file_$i &
  done
$ jobs  # 查看所有后台任务
$ wait   # 等待所有后台任务完成

# 场景4：远程服务器维护
$ screen -S maintenance
# 在screen中执行维护任务
# 断开连接：Ctrl+A D
# 重新连接：screen -r maintenance
```

**作业控制的最佳实践**

在实际使用中，建议遵循这些原则：

1. **短期任务**：使用 `&` 后台运行
2. **长期任务**：使用 `nohup` 或 `screen/tmux`
3. **需要交互的任务**：使用 `screen/tmux`
4. **多任务管理**：使用 `screen/tmux` 的多窗口功能
5. **忘记nohup的补救**：使用 `disown`

掌握了作业控制，你就能够高效地管理多个任务，无论是在本地开发还是在远程服务器上，都能游刃有余地处理各种复杂的任务场景。

## [8.4 进程优先级：nice 和 renice](#_8-4-进程优先级-nice-和-renice)

如何控制进程的优先级？如何让重要进程获得更多系统资源？

Linux 系统中，进程的优先级决定了它们获得 CPU 时间的多少。`nice` 值范围从 -20（最高优先级）到 19（最低优先级）。

### [nice：启动进程时设置优先级](#nice-启动进程时设置优先级)

```
# 基本语法：nice [-n 优先级] 命令
$ nice -n 10 some_command
# 以较低的优先级运行（10表示nice值）

# 高优先级运行（需要管理员权限）
$ sudo nice -n -5 important_command

# 默认nice值为0
$ some_command  # 等同于 nice -n 0 some_command
```

你可能会问："为什么叫 nice？" 因为这个命令让进程"友好地"与其他进程分享 CPU 时间。较高的 nice 值表示进程更"友好"，会主动让出 CPU 时间。

### [renice：修改运行中进程的优先级](#renice-修改运行中进程的优先级)

```
# 修改指定PID的优先级
$ renice 10 1234

# 修改用户所有进程的优先级
$ renice 10 -u username

# 修改进程组所有进程的优先级
$ renice 10 -g groupname

# 查看进程的当前nice值
$ ps -p 1234 -o pid,ni,nice,cmd
```

### [实际应用场景](#实际应用场景-1)

```
# 场景1：降低备份进程的优先级
$ nice -n 19 tar -czvf backup.tar.gz large_dir/

# 场景2：提高数据库进程的优先级
$ sudo renice -10 $(pgrep mysql)

# 场景3：批量设置用户进程优先级
$ renice 10 -u regularuser

# 场景4：查看系统中的优先级分布
$ ps -eo pid,ni,comm | sort -k2
```

### [time 命令：测量进程执行时间](#time-命令-测量进程执行时间)

```
# 测量命令执行时间
$ time ls -la
real    0m0.002s
user    0m0.001s
sys     0m0.001s

# time输出的含义：
# real：实际经过的时间
# user：用户态CPU时间
# sys：内核态CPU时间
```

## [8.5 实战案例：进程管理最佳实践](#_8-5-实战案例-进程管理最佳实践)

让我们通过一些实际案例，综合运用进程管理工具解决常见问题。

### [案例1：处理僵尸进程](#案例1-处理僵尸进程)

```
# 查找僵尸进程
$ ps aux | grep 'Z'
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
user        5678  0.0  0.0      0     0 ?        Z    10:30   0:00 [defunct]

# 查找僵尸进程的父进程
$ ps -o ppid= -p 5678
1234

# 终止父进程（通常会导致僵尸进程被init进程回收）
$ kill 1234
```

### [案例2：批量管理进程](#案例2-批量管理进程)

```
# 批量终止特定用户的进程
$ pkill -u username

# 批量终止Python脚本
$ pkill -f "python.*\.py"

# 批量调整进程优先级
$ ps aux | grep 'backup' | awk '{print $2}' | xargs renice 10
```

### [案例3：监控系统资源](#案例3-监控系统资源)

```
# 监控CPU使用率
$ top -b -n 1 | head -20

# 持续监控特定进程
$ watch -n 5 'ps -p 1234 -o pid,%cpu,%mem,cmd'

# 监控内存使用情况
$ free -h && ps aux --sort=-%mem | head -10
```

### [案例4：服务管理最佳实践](#案例4-服务管理最佳实践)

```
# 启动服务（推荐方式）
$ sudo systemctl start nginx

# 传统方式启动服务
$ sudo /etc/init.d/nginx start

# 检查服务状态
$ systemctl status nginx

# 重启服务
$ sudo systemctl restart nginx
```

### [一行流模板：常用进程管理模式](#一行流模板-常用进程管理模式)

```
# 查找并终止无响应的进程
$ ps aux | grep 'unresponsive' | awk '{print $2}' | xargs kill -9

# 监控并终止高CPU使用率进程
$ top -b -n 1 | awk '$9 > 80 {print $2}' | xargs renice 10

# 批量启动后台任务
$ for i in {1..5}; do long_task_$i & done

# 清理僵尸进程
$ ps aux | awk '$8 ~ /^Z/ {print $2}' | xargs kill -9
```

> 💡注意：在生产环境中管理进程时，建议使用系统的服务管理工具（如 systemctl），而不是直接操作进程。

> ⚠️高危操作：强制终止系统进程或关键服务进程可能导致系统不稳定。在执行 `kill -9` 前，请确认进程的身份和作用。

---

## [练习题](#练习题)

1. 如何找出系统中占用 CPU 最多的 5 个进程，并将它们的信息保存到文件中？

查看答案

- 思路与步骤：使用 `ps` 或 `top` 获取进程信息，按 CPU 使用率排序，提取前5个进程
- 示例命令：

```
# 方法1：使用 ps 命令
$ ps aux --sort=-%cpu | head -6 | tee top_cpu_processes.txt

# 方法2：更详细的版本（排除标题行）
$ ps aux --sort=-%cpu | awk 'NR>1 {print $0}' | head -5 | \
  tee top_cpu_processes.txt

# 方法3：格式化输出
$ ps aux --sort=-%cpu | head -6 | \
  awk '{printf "%-10s %-5s %-5s %-10s %s\n", $1, $2, $3, $4, $11}' | \
  tee top_cpu_processes.txt

# 方法4：持续监控版本
$ watch -n 5 'ps aux --sort=-%cpu | head -6 > top_cpu_processes.txt'
```

这些命令会显示 CPU 使用率最高的进程信息，并将结果保存到文件中。`--sort=-%cpu` 按CPU使用率降序排序，`head -6` 取前6行（包括标题行），`tee` 同时显示和保存。

2. 如何启动一个长时间运行的脚本，并确保在关闭终端后脚本继续运行？

查看答案

- 思路与步骤：使用 `nohup` 命令让进程忽略挂断信号，并结合后台运行和输出重定向
- 示例命令：

```
# 方法1：基本 nohup 用法
$ nohup long_running_script.sh &

# 方法2：带输出重定向的完整版本
$ nohup ./long_running_script.sh > script.log 2>&1 &

# 方法3：使用 screen（推荐）
$ screen -S myscript
$ ./long_running_script.sh
# 按 Ctrl+A D 暂时离开
$ screen -r myscript  # 重新连接

# 方法4：使用 disown
$ ./long_running_script.sh &
$ disown %1

# 方法5：systemd 方式（生产环境推荐）
$ sudo systemctl start myscript.service
```

`nohup` 让进程忽略 SIGHUP 信号，`&` 让进程在后台运行，`> script.log 2>&1` 将标准输出和错误输出都重定向到日志文件。对于生产环境，推荐使用 systemd 服务管理。

3. 如何查找并终止所有属于特定用户且占用内存超过 100MB 的进程？

查看答案

- 思路与步骤：使用 `ps` 查找用户进程，过滤内存使用量，然后终止符合条件的进程
- 示例命令：

```
# 方法1：基本版本
$ ps -u username -o pid,rss,comm | awk '$2 > 102400 {print $1}' | xargs kill

# 方法2：更安全的版本（先显示再终止）
$ ps -u username -o pid,rss,comm | awk '$2 > 102400 {printf "PID: %s, RSS: %sKB, CMD: %s\n", $1, $2, $3}'
$ ps -u username -o pid,rss,comm | awk '$2 > 102400 {print $1}' | xargs kill

# 方法3：交互式确认
$ ps -u username -o pid,rss,comm | awk '$2 > 102400 {print $1}' | \
  xargs -p kill

# 方法4：详细日志版本
$ ps -u username -o pid,rss,comm | awk '$2 > 102400 {print $1}' | \
  tee terminated_pids.log | xargs kill

# 方法5：使用 pkill（如果符合条件）
$ pkill -u username -f ".*" --signal TERM
```

这些命令会查找指定用户占用内存超过 100MB（102400KB）的进程并终止它们。建议先用显示版本确认要终止的进程，避免误杀重要进程。

---

## [速记卡](#速记卡)

- `ps aux`：显示所有进程的详细信息
- `ps aux --sort=-%cpu`：按CPU使用率排序进程
- `top`：动态监控进程状态
- `kill PID`：终止指定进程
- `pkill name`：按进程名终止进程
- `command &`：后台运行命令
- `nohup command &`：终端关闭后继续运行
- `jobs`：查看当前作业列表
- `nice -n 10 command`：以较低优先级运行
- `renice 10 PID`：修改运行中进程的优先级

## [常见坑](#常见坑)

- 随意使用 `kill -9`：可能导致数据丢失，应该优先使用 `kill`（SIGTERM）
- 忽略僵尸进程：僵尸进程占用系统资源，需要终止其父进程
- 后台进程输出混乱：后台进程的输出会显示在终端，建议重定向到文件
- 关闭终端导致进程终止：使用 `nohup` 或 `screen` 让进程持久运行
- nice 值理解错误：nice 值越高，优先级越低（-20最高，19最低）
- 批量操作不测试：直接运行批量终止命令可能误杀重要进程
- 忽略进程依赖关系：终止父进程可能影响子进程，要考虑进程树
- 混淆前台和后台作业：使用 `fg` 和 `bg` 管理作业状态

## [章节总结](#章节总结)

进程管理是 Linux 系统管理的核心技能之一。通过 `ps`、`top`、`htop` 等工具，你能够全面了解系统中运行的进程状态，及时发现资源占用异常的进程。`kill`、`pkill`、`killall` 等命令提供了灵活的进程终止方式，从温和的 SIGTERM 到强制的 SIGKILL。

作业控制让你能够在单个终端中管理多个任务，通过 `&`、`Ctrl+Z`、`bg`、`fg` 等操作，你可以灵活地切换前台和后台作业。`nohup` 和 `disown` 让进程能够脱离终端独立运行，而 `screen` 和 `tmux` 则提供了更强大的终端复用功能。

进程优先级管理（`nice` 和 `renice`）让你能够合理分配系统资源，确保重要进程获得足够的 CPU 时间。在实际应用中，要根据进程的重要性和资源需求来设置合适的优先级。

记住，进程管理不仅仅是技术操作，更体现了对系统资源的合理规划和对服务稳定性的考虑。在生产环境中，推荐使用系统的服务管理工具（如 `systemd`）来管理长期运行的服务，而不是直接操作进程。掌握了这些技能，你就能够有效地管理和控制 Linux 系统中的各种进程。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/08-process-and-job-control.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [08｜进程管理与作业控制](https://xiaolinnote.com/linux/08-process-and-job-control.html#_08-进程管理与作业控制)
- [8.1 查看进程：ps、pgrep 和 top](https://xiaolinnote.com/linux/08-process-and-job-control.html#_8-1-查看进程-ps、pgrep-和-top)
- [ps：静态进程快照](https://xiaolinnote.com/linux/08-process-and-job-control.html#ps-静态进程快照)
- [灵活运用 ps 命令](https://xiaolinnote.com/linux/08-process-and-job-control.html#灵活运用-ps-命令)
- [pgrep：进程查找的"快捷方式"](https://xiaolinnote.com/linux/08-process-and-job-control.html#pgrep-进程查找的-快捷方式)
- [top 和 htop：系统的"实时监控仪表板"](https://xiaolinnote.com/linux/08-process-and-job-control.html#top-和-htop-系统的-实时监控仪表板)
- [8.2 终止进程：kill、pkill 和 killall](https://xiaolinnote.com/linux/08-process-and-job-control.html#_8-2-终止进程-kill、pkill-和-killall)
- [kill：进程通信的"信号语言"](https://xiaolinnote.com/linux/08-process-and-job-control.html#kill-进程通信的-信号语言)
- [pkill 和 killall：批量进程管理的利器](https://xiaolinnote.com/linux/08-process-and-job-control.html#pkill-和-killall-批量进程管理的利器)
- [8.3 作业控制：后台运行与进程切换](https://xiaolinnote.com/linux/08-process-and-job-control.html#_8-3-作业控制-后台运行与进程切换)
- [后台运行：& 符号的魔法](https://xiaolinnote.com/linux/08-process-and-job-control.html#后台运行-符号的魔法)
- [暂停和恢复：Ctrl+Z 的力量](https://xiaolinnote.com/linux/08-process-and-job-control.html#暂停和恢复-ctrl-z-的力量)
- [nohup：让进程"无视"终端关闭](https://xiaolinnote.com/linux/08-process-and-job-control.html#nohup-让进程-无视-终端关闭)
- [disown：完全脱离终端](https://xiaolinnote.com/linux/08-process-and-job-control.html#disown-完全脱离终端)
- [screen 和 tmux：终端复用器](https://xiaolinnote.com/linux/08-process-and-job-control.html#screen-和-tmux-终端复用器)
- [实际应用场景](https://xiaolinnote.com/linux/08-process-and-job-control.html#实际应用场景)
- [8.4 进程优先级：nice 和 renice](https://xiaolinnote.com/linux/08-process-and-job-control.html#_8-4-进程优先级-nice-和-renice)
- [nice：启动进程时设置优先级](https://xiaolinnote.com/linux/08-process-and-job-control.html#nice-启动进程时设置优先级)
- [renice：修改运行中进程的优先级](https://xiaolinnote.com/linux/08-process-and-job-control.html#renice-修改运行中进程的优先级)
- [实际应用场景](https://xiaolinnote.com/linux/08-process-and-job-control.html#实际应用场景-1)
- [time 命令：测量进程执行时间](https://xiaolinnote.com/linux/08-process-and-job-control.html#time-命令-测量进程执行时间)
- [8.5 实战案例：进程管理最佳实践](https://xiaolinnote.com/linux/08-process-and-job-control.html#_8-5-实战案例-进程管理最佳实践)
- [案例1：处理僵尸进程](https://xiaolinnote.com/linux/08-process-and-job-control.html#案例1-处理僵尸进程)
- [案例2：批量管理进程](https://xiaolinnote.com/linux/08-process-and-job-control.html#案例2-批量管理进程)
- [案例3：监控系统资源](https://xiaolinnote.com/linux/08-process-and-job-control.html#案例3-监控系统资源)
- [案例4：服务管理最佳实践](https://xiaolinnote.com/linux/08-process-and-job-control.html#案例4-服务管理最佳实践)
- [一行流模板：常用进程管理模式](https://xiaolinnote.com/linux/08-process-and-job-control.html#一行流模板-常用进程管理模式)
- [练习题](https://xiaolinnote.com/linux/08-process-and-job-control.html#练习题)
- [速记卡](https://xiaolinnote.com/linux/08-process-and-job-control.html#速记卡)
- [常见坑](https://xiaolinnote.com/linux/08-process-and-job-control.html#常见坑)
- [章节总结](https://xiaolinnote.com/linux/08-process-and-job-control.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
