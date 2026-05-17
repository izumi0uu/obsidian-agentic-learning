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
url: "https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html"
source: "https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html"
last_checked: 2026-05-17
freshness: watch
sha256: 98215e96b7792dc39accfda4dc2fee40e4d333f03750e3bba6be5765a195e290
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 附录A1：常用命令速查表

原始链接：https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 附录A1：常用命令速查表

[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 16 分钟约 4678 字2025/9/2

---

# [附录A1｜常用命令速查表](#附录a1-常用命令速查表)

大家好，我是小林。

想象一下这样的场景：你已经学习了 Linux 命令行的基本概念，但在实际工作中突然忘记了某个命令的具体用法。或者你需要快速查找某个特定功能的命令，但又不想翻阅整个教程。这时候，一个按主题组织的命令速查表就非常有用了。

这个速查表就像是你 Linux 命令行的"随身词典"，它将本书中介绍的所有核心命令按照功能主题进行了分组。每个命令都包含了最常用的选项和实际示例，让你能够快速找到需要的信息。

## [文件与目录操作](#文件与目录操作)

### [基础文件操作](#基础文件操作)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `ls` | 列出目录内容 | `-l` (详细信息), `-a` (显示隐藏文件), `-h` (人类可读大小) | `ls -lah` |
| `pwd` | 显示当前工作目录 | `-P` (显示真实路径) | `pwd` |
| `cd` | 切换目录 | `~` (家目录), `..` (上级目录), `-` (上一次目录) | `cd /var/www` |
| `mkdir` | 创建目录 | `-p` (创建多级目录) | `mkdir -p project/src/main` |
| `rmdir` | 删除空目录 | (无常用选项) | `rmdir empty_dir` |

### [文件操作](#文件操作)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `touch` | 创建空文件或更新时间戳 | `-a` (只修改访问时间), `-m` (只修改修改时间) | `touch notes.txt` |
| `cp` | 复制文件或目录 | `-r` (递归复制目录), `-p` (保留属性), `-i` (交互式) | `cp -r source/ destination/` |
| `mv` | 移动或重命名文件 | `-i` (交互式), `-u` (只更新较新文件) | `mv old.txt new.txt` |
| `rm` | 删除文件或目录 | `-r` (递归删除目录), `-f` (强制删除), `-i` (交互式) | `rm -rf temp/` |
| `file` | 识别文件类型 | `-i` (显示 MIME 类型), `-b` (简洁模式) | `file unknown_file` |
| `stat` | 显示文件详细信息 | `-c` (自定义格式), `-f` (显示文件系统状态) | `stat file.txt` |

### [文件查找与搜索](#文件查找与搜索)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `find` | 查找文件 | `-name` (按名称), `-type` (按类型), `-size` (按大小) | `find . -name "*.py" -type f` |
| `locate` | 快速查找文件 (数据库索引) | `-i` (忽略大小写), `-r` (正则表达式) | `locate -i "*.conf"` |
| `which` | 查找可执行文件路径 | `-a` (显示所有匹配) | `which python3` |
| `whereis` | 查找命令相关文件 | `-b` (只查找二进制文件), `-m` (只查找手册) | `whereis ls` |

## [权限与所有权管理](#权限与所有权管理)

### [权限查看与修改](#权限查看与修改)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `chmod` | 修改文件权限 | `-R` (递归), `u+rwx` (符号模式), `755` (八进制模式) | `chmod 755 script.sh` |
| `chown` | 修改文件所有者 | `-R` (递归), `user:group` (同时修改组) | `chown www-data:www-data /var/www` |
| `chgrp` | 修改文件所属组 | `-R` (递归) | `chgrp developers file.txt` |
| `umask` | 设置默认权限掩码 | `-S` (符号模式显示), `-p` (可输出格式) | `umask 0022` |

### [用户与组信息](#用户与组信息)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `whoami` | 显示当前用户名 | (无常用选项) | `whoami` |
| `id` | 显示用户身份信息 | `-u` (只显示 UID), `-g` (只显示 GID), `-Gn` (显示所有组名) | `id` |
| `groups` | 显示用户所属组 | (无常用选项) | `groups username` |
| `sudo` | 以超级用户权限执行命令 | `-i` (登录为 root), `-u` (指定用户) | `sudo apt update` |

## [文本查看与编辑](#文本查看与编辑)

### [文本查看](#文本查看)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `cat` | 显示文件内容 | `-n` (显示行号), `-A` (显示所有字符) | `cat -n file.txt` |
| `less` | 分页查看文件 | `-N` (显示行号), `-S` (不换行), `+F` (跟踪模式) | `less -N large_file.log` |
| `head` | 显示文件开头 | `-n` (指定行数), `-c` (指定字节数) | `head -n 20 file.txt` |
| `tail` | 显示文件结尾 | `-n` (指定行数), `-f` (实时跟踪), `-F` (跟踪文件名) | `tail -f /var/log/syslog` |
| `nl` | 显示行号 | `-b a` (为所有行编号), `-s` (分隔符) | `nl file.txt` |

### [文本统计与处理](#文本统计与处理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `wc` | 统计文件信息 | `-l` (行数), `-w` (单词数), `-c` (字节数), `-L` (最长行) | `wc -l *.txt` |
| `split` | 分割文件 | `-l` (按行数), `-b` (按大小), `-d` (数字后缀) | `split -l 1000 large_file.txt part_` |
| `sort` | 排序文本行 | `-n` (数值排序), `-r` (反向), `-k` (指定字段) | `sort -nr numbers.txt` |
| `uniq` | 去除重复行 | `-c` (显示重复次数), `-d` (只显示重复行) | `sort file.txt | uniq -c` |
| `cut` | 提取列 | `-d` (分隔符), `-f` (字段号), `-c` (字符位置) | `cut -d',' -f1,3 data.csv` |

### [文本编辑器](#文本编辑器)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `nano` | 简单文本编辑器 | `-N` (显示行号), `-B` (创建备份), `-Y` (语法高亮) | `nano -N config.py` |
| `vim` | 高级文本编辑器 | `+` (跳转到行), `-R` (只读模式) | `vim +10 file.txt` |

## [压缩与归档](#压缩与归档)

### [压缩与解压](#压缩与解压)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `tar` | 打包/解包文件 | `-c` (创建), `-x` (解包), `-v` (显示过程), `-f` (指定文件) | `tar -czvf archive.tar.gz files/` |
| `gzip` | 压缩文件 | `-d` (解压), `-l` (显示信息), `-r` (递归压缩) | `gzip -r directory/` |
| `gunzip` | 解压 gzip 文件 | `-k` (保留原文件), `-r` (递归解压) | `gunzip file.gz` |
| `zip` | 创建 zip 压缩包 | `-r` (递归), `-e` (加密), `-q` (安静模式) | `zip -r archive.zip folder/` |
| `unzip` | 解压 zip 文件 | `-l` (列出内容), `-d` (指定目录) | `unzip archive.zip -d target/` |

### [文件校验](#文件校验)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `md5sum` | 生成/验证 MD5 校验和 | `-c` (验证文件), `-t` (文本模式) | `md5sum important_file.iso` |
| `sha256sum` | 生成/验证 SHA256 校验和 | `-c` (验证文件), `-b` (二进制模式) | `sha256sum *.iso > checksums.txt` |

## [进程管理](#进程管理)

### [进程查看](#进程查看)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `ps` | 显示进程信息 | `aux` (所有进程), `-ef` (完整格式), `-p` (指定 PID) | `ps aux | grep nginx` |
| `top` | 动态显示进程 | `-d` (刷新间隔), `-p` (指定 PID), `-u` (指定用户) | `top -u username` |
| `htop` | 增强版进程查看器 | `-u` (指定用户), `-p` (指定 PID) | `htop -u www-data` |
| `pgrep` | 查找进程 PID | `-u` (指定用户), `-f` (完整命令名), `-l` (显示进程名) | `pgrep -f "nginx"` |

### [进程控制](#进程控制)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `kill` | 终止进程 | `-9` (强制终止), `-15` (正常终止), `-1` (重新加载) | `kill -9 1234` |
| `pkill` | 按名称终止进程 | `-f` (完整命令名), `-u` (指定用户) | `pkill -f "apache2"` |
| `killall` | 终止所有同名进程 | `-i` (交互式), `-w` (等待进程结束) | `killall chrome` |
| `jobs` | 显示后台任务 | `-l` (显示 PID), `-r` (只显示运行中), `-s` (只显示停止) | `jobs -l` |
| `fg` | 将后台任务调至前台 | (无常用选项) | `fg %1` |
| `bg` | 将任务调至后台 | (无常用选项) | `bg %1` |
| `nohup` | 忽略挂起信号运行命令 | (无常用选项) | `nohup long_command &` |

## [系统监控](#系统监控)

### [系统信息](#系统信息)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `uname` | 显示系统信息 | `-a` (所有信息), `-r` (内核版本), `-m` (机器架构) | `uname -a` |
| `uptime` | 显示系统运行时间 | `-p` (美观格式), `-s` (自启动时间) | `uptime` |
| `date` | 显示/设置日期时间 | `+FORMAT` (自定义格式), `-u` (UTC 时间) | `date "+%Y-%m-%d %H:%M:%S"` |
| `lscpu` | 显示 CPU 信息 | (无常用选项) | `lscpu` |
| `free` | 显示内存使用情况 | `-h` (人类可读), `-m` (MB), `-g` (GB) | `free -h` |

### [磁盘与文件系统](#磁盘与文件系统)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `df` | 显示磁盘空间使用 | `-h` (人类可读), `-T` (显示文件系统类型) | `df -h` |
| `du` | 显示目录大小 | `-h` (人类可读), `-s` (总计), `-d` (深度) | `du -sh /var/log` |
| `lsblk` | 显示块设备信息 | `-f` (显示文件系统), `-m` (权限信息) | `lsblk -f` |
| `mount` | 挂载文件系统 | `-t` (指定类型), `-o` (挂载选项) | `mount /dev/sdb1 /mnt/data` |
| `umount` | 卸载文件系统 | `-l` (懒人卸载), `-f` (强制卸载) | `umount /mnt/data` |

### [网络监控](#网络监控)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `netstat` | 显示网络连接 | `-t` (TCP), `-u` (UDP), `-l` (监听), `-n` (数字格式) | `netstat -tlnp` |
| `ss` | 显示套接字统计 | `-t` (TCP), `-u` (UDP), `-l` (监听), `-n` (数字格式) | `ss -tlnp` |
| `lsof` | 显示打开的文件 | `-i` (网络文件), `-p` (指定 PID), `-u` (指定用户) | `lsof -i :80` |
| `iftop` | 显示网络带宽使用 | `-i` (指定接口), `-n` (数字格式) | `iftop -i eth0` |

## [网络工具](#网络工具)

### [网络配置](#网络配置)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `ip` | 显示/管理网络接口 | `addr` (地址), `link` (链路), `route` (路由) | `ip addr show` |
| `ifconfig` | 配置网络接口 (传统) | `up` (启用), `down` (禁用), `inet` (IP 地址) | `ifconfig eth0 up` |
| `hostname` | 显示/设置主机名 | `-i` (显示 IP 地址), `-d` (显示域名) | `hostnamectl set-hostname newname` |
| `resolvectl` | 管理 DNS 解析 | `status` (状态), `query` (查询) | `resolvectl query example.com` |

### [网络连接与测试](#网络连接与测试)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `ping` | 测试网络连通性 | `-c` (指定次数), `-i` (间隔), `-W` (超时) | `ping -c 4 google.com` |
| `traceroute` | 追踪网络路径 | `-n` (数字格式), `-w` (超时), `-q` (安静模式) | `traceroute google.com` |
| `nslookup` | DNS 查询工具 | `-type=A` (A 记录), `-type=MX` (MX 记录) | `nslookup google.com` |
| `dig` | DNS 查询工具 | `+short` (简洁输出), `+trace` (追踪查询) | `dig google.com` |

### [文件传输](#文件传输)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `scp` | 安全复制文件 | `-r` (递归), `-P` (指定端口), `-i` (指定密钥) | `scp -r file.txt user@host:/path/` |
| `rsync` | 同步文件/目录 | `-a` (归档模式), `-v` (详细), `-z` (压缩) | `rsync -avz source/ destination/` |
| `sftp` | 安全 FTP 客户端 | `-P` (指定端口), `-i` (指定密钥) | `sftp user@host` |
| `wget` | 下载文件 | `-c` (断点续传), `-r` (递归下载), `-O` (指定文件名) | `wget -c https://example.com/file.zip` |
| `curl` | 传输数据 | `-O` (保存文件), `-L` (跟随重定向), `-X` (指定方法) | `curl -O https://example.com/file.txt` |

### [远程连接](#远程连接)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `ssh` | 安全远程连接 | `-p` (指定端口), `-i` (指定密钥), `-X` (X11 转发) | `ssh user@hostname` |
| `ssh-keygen` | 生成 SSH 密钥 | `-t` (密钥类型), `-b` (密钥位数), `-f` (指定文件) | `ssh-keygen -t rsa -b 4096` |
| `ssh-copy-id` | 复制 SSH 公钥 | `-i` (指定密钥文件), `-p` (指定端口) | `ssh-copy-id user@host` |

## [文本处理三剑客](#文本处理三剑客)

### [grep - 文本搜索](#grep-文本搜索)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `grep` | 搜索文本模式 | `-i` (忽略大小写), `-r` (递归), `-n` (显示行号) | `grep -r "error" /var/log/` |
| `egrep` | 扩展正则表达式搜索 | `-i` (忽略大小写), `-v` (反向匹配), `-w` (全词匹配) | `egrep "error|warning" log.txt` |
| `fgrep` | 固定字符串搜索 | `-x` (完全匹配), `-f` (从文件读取模式) | `fgrep "exact phrase" file.txt` |

### [awk - 文本处理](#awk-文本处理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `awk` | 模式扫描和处理 | `-F` (字段分隔符), `-f` (指定脚本文件) | `awk -F: '{print $1}' /etc/passwd` |
| `gawk` | GNU awk | `--posix` (POSIX 模式), `--re-interval` (间隔表达式) | `gawk '{sum+=$1} END {print sum}' numbers.txt` |

### [sed - 流编辑器](#sed-流编辑器)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `sed` | 流编辑器 | `-i` (原地编辑), `-e` (多个命令), `-n` (安静模式) | `sed -i 's/old/new/g' file.txt` |
| `-i` | 原地编辑 | `.bak` (创建备份) | `sed -i.bak 's/foo/bar/g' file.txt` |

## [管道与重定向](#管道与重定向)

### [管道操作](#管道操作)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| ` | ` | 管道 (连接命令) | (无选项) |
| `xargs` | 将标准输入转换为参数 | `-n` (每次处理数量), `-I` (替换字符串) | `find . -name "*.tmp" | xargs rm` |
| `tee` | 分流输出到文件和屏幕 | `-a` (追加模式), `-i` (忽略中断) | `ls -la | tee filelist.txt` |

### [重定向操作](#重定向操作)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `>` | 输出重定向 (覆盖) | (无选项) | `ls > filelist.txt` |
| `>>` | 输出重定向 (追加) | (无选项) | `echo "log entry" >> logfile.txt` |
| `<` | 输入重定向 | (无选项) | `sort < unsorted.txt` |
| `2>` | 错误输出重定向 | (无选项) | `command 2> error.log` |
| `&>` | 标准和错误输出重定向 | (无选项) | `command &> all_output.log` |

### [命令替换](#命令替换)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `$()` | 命令替换 | (无选项) | `echo "Current time: $(date)"` |
| ` | 反引号命令替换 | (无选项) | `echo "Users: \`whoami`"` |

## [系统服务管理](#系统服务管理)

### [systemd 服务管理](#systemd-服务管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `systemctl` | 控制 systemd 服务 | `start`/`stop`/`restart`, `enable`/`disable`, `status` | `systemctl start nginx` |
| `journalctl` | 查看系统日志 | `-u` (指定服务), `-f` (跟踪), `-n` (显示行数) | `journalctl -u nginx -f` |
| `timedatectl` | 时间日期管理 | `set-timezone`, `set-ntp` | `timedatectl set-timezone Asia/Shanghai` |

### [传统服务管理](#传统服务管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `service` | 控制系统服务 | `start`/`stop`/`restart`, `status` | `service apache2 restart` |
| `chkconfig` | 管理服务启动项 | `--list`, `--add`, `--del` | `chkconfig --list` |
| `update-rc.d` | Debian 服务管理 | `defaults`, `remove` | `update-rc.d nginx defaults` |

## [常用系统管理命令](#常用系统管理命令)

### [系统信息](#系统信息-1)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `dmesg` | 显示内核消息 | `-T` (显示时间戳), `-l` (指定级别) | `dmesg | grep -i error` |
| `lspci` | 显示 PCI 设备 | `-v` (详细信息), `-k` (显示驱动) | `lspci | grep VGA` |
| `lsusb` | 显示 USB 设备 | `-v` (详细信息), `-t` (树状结构) | `lsusb` |
| `lsmod` | 显示加载的内核模块 | (无常用选项) | `lsmod | grep drm` |
| `modprobe` | 加载/卸载内核模块 | `-r` (卸载), `-v` (详细信息) | `modprobe -r vboxdrv` |

### [性能监控](#性能监控)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `vmstat` | 显示虚拟内存统计 | `-s` (显示内存统计), `-a` (显示活跃内存) | `vmstat 1 10` |
| `iostat` | 显示 I/O 统计 | `-x` (扩展统计), `-d` (设备统计) | `iostat -xz 1` |
| `sar` | 系统活动报告 | `-u` (CPU), `-r` (内存), `-b` (I/O) | `sar -u 1 5` |
| `nethogs` | 按进程显示网络使用 | `-t` (跟踪模式), `-p` (指定进程) | `nethogs eth0` |
| `iotop` | 按进程显示 I/O 使用 | `-o` (只显示有 I/O 的进程), `-a` (累积) | `iotop -oP` |

### [磁盘管理](#磁盘管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `fdisk` | 磁盘分区工具 | `-l` (列出分区), `-u` (显示扇区) | `fdisk -l` |
| `parted` | 高级分区工具 | `-l` (列出分区), `-s` (脚本模式) | `parted /dev/sdb print` |
| `mkfs` | 创建文件系统 | `-t` (指定类型), `-L` (指定标签) | `mkfs -t ext4 /dev/sdb1` |
| `fsck` | 文件系统检查 | `-y` (自动修复), `-f` (强制检查) | `fsck -y /dev/sda1` |
| `dd` | 转换和复制文件 | `if=` (输入文件), `of=` (输出文件), `bs=` (块大小) | `dd if=/dev/zero of=test.img bs=1M count=100` |

## [安全与权限](#安全与权限)

### [权限管理](#权限管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `setfacl` | 设置访问控制列表 | `-m` (修改), `-x` (删除), `-b` (删除所有) | `setfacl -m u:john:rw file.txt` |
| `getfacl` | 获取访问控制列表 | (无常用选项) | `getfacl file.txt` |
| `attr` | 扩展属性管理 | `-l` (列出), `-s` (设置), `-r` (递归) | `attr -l file.txt` |
| `chattr` | 改变文件属性 | `+i` (不可变), `+a` (只追加), `-i` (可变) | `chattr +i important_file` |

### [网络安全](#网络安全)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `iptables` | 防火墙配置 | `-A` (追加规则), `-D` (删除规则), `-L` (列出规则) | `iptables -L -n` |
| `ufw` | 简化防火墙 | `enable`/`disable`, `allow`/`deny`, `status` | `ufw allow 22/tcp` |
| `firewalld` | 防火墙管理 | `--add-port`, `--remove-port`, `--list-all` | `firewall-cmd --add-port=80/tcp` |
| `nmap` | 网络扫描工具 | `-sS` (TCP SYN 扫描), `-p` (指定端口), `-A` (全面扫描) | `nmap -sS -p 1-1000 target_ip` |

## [开发者工具](#开发者工具)

### [版本控制](#版本控制)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `git` | 分布式版本控制 | `clone`, `add`, `commit`, `push`, `pull` | `git clone https://github.com/user/repo.git` |
| `svn` | Subversion 版本控制 | `checkout`, `update`, `commit`, `add` | `svn checkout svn://server/path` |
| `hg` | Mercurial 版本控制 | `clone`, `add`, `commit`, `push` | `hg clone https://server/repo` |

### [包管理](#包管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `apt` | Debian/Ubuntu 包管理 | `install`, `remove`, `update`, `upgrade` | `apt install nginx` |
| `apt-get` | 传统 APT 工具 | `install`, `remove`, `update`, `upgrade` | `apt-get install nginx` |
| `yum` | RHEL/CentOS 包管理 | `install`, `remove`, `update`, `search` | `yum install nginx` |
| `dnf` | Fedora 包管理 | `install`, `remove`, `update`, `search` | `dnf install nginx` |
| `pacman` | Arch Linux 包管理 | `-S` (安装), `-R` (删除), `-Syu` (系统升级) | `pacman -S nginx` |

### [编译与构建](#编译与构建)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `make` | 构建工具 | `-j` (并行编译), `-f` (指定文件), `-n` (模拟执行) | `make -j4` |
| `gcc` | GNU C 编译器 | `-o` (输出文件), `-c` (只编译), `-g` (调试信息) | `gcc -o program program.c` |
| `g++` | GNU C++ 编译器 | `-o` (输出文件), `-c` (只编译), `-g` (调试信息) | `g++ -o program program.cpp` |
| `cmake` | 跨平台构建系统 | `-B` (构建目录), `-S` (源目录), `-G` (生成器) | `cmake -B build -S .` |

## [实用工具](#实用工具)

### [文本处理](#文本处理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `tr` | 字符转换 | `-d` (删除字符), `-s` (压缩重复字符) | `echo "hello" | tr 'a-z' 'A-Z'` |
| `column` | 格式化列输出 | `-t` (创建表格), `-s` (指定分隔符) | `cat data.csv | column -t -s','` |
| `fold` | 折叠长行 | `-w` (指定宽度), `-s` (按空格分割) | `fold -w 80 longfile.txt` |
| `fmt` | 文本格式化 | `-w` (指定宽度), `-u` (统一间距) | `fmt -w 72 text.txt` |
| `pr` | 准备打印文件 | `-n` (编号), `-h` (标题), `-o` (缩进) | `pr -n -h "Report" file.txt` |

### [系统信息](#系统信息-2)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `cal` | 显示日历 | `-y` (全年), `-m` (指定月份), `-3` (三个月) | `cal -y 2024` |
| `bc` | 计算器 | `-l` (数学库), `-q` (安静模式) | `echo "scale=2; 10/3" | bc` |
| `factor` | 因数分解 | (无常用选项) | `factor 123456` |
| `seq` | 生成序列 | `-f` (格式), `-s` (分隔符), `-w` (等宽) | `seq -f "file%03g.txt" 1 10` |
| `shuf` | 随机排列 | `-n` (输出行数), `-i` (输入范围) | `shuf -n 5 names.txt` |

### [时间管理](#时间管理)

| 命令 | 功能描述 | 常用选项 | 示例 |
| --- | --- | --- | --- |
| `at` | 在指定时间执行命令 | `-f` (指定文件), `-t` (时间戳), `-l` (列出任务) | `at 2:30 PM tomorrow` |
| `cron` | 定时任务调度 | `-e` (编辑), `-l` (列出), `-r` (删除) | `crontab -e` |
| `timeout` | 运行有时间限制的命令 | `-s` (指定信号), `-k` (超时后杀死) | `timeout 10s command` |
| `sleep` | 暂停指定时间 | `s` (秒), `m` (分), `h` (小时) | `sleep 30` |

## [使用建议](#使用建议)

### [快速查找技巧](#快速查找技巧)

1. **按功能分类查找**：根据你要完成的任务类型，找到对应的分类
2. **使用表格搜索**：在表格中使用 `Ctrl+F` 快速搜索特定命令
3. **注意常用选项**：表格中列出了最常用的选项，实际使用时可能需要更多
4. **结合示例理解**：每个命令都提供了实际示例，便于理解用法

### [命令组合技巧](#命令组合技巧)

1. **管道连接**：使用 `|` 将多个命令连接起来，形成处理流水线
2. **命令替换**：使用 `$()` 将命令结果作为参数传递给其他命令
3. **重定向输出**：使用 `>`、`>>` 将命令结果保存到文件
4. **错误处理**：使用 `2>&1` 合并标准输出和错误输出

### [学习建议](#学习建议)

1. **从基础开始**：先掌握文件操作、权限管理等基础命令
2. **实际练习**：每个命令都要亲手操作，加深理解
3. **查阅手册**：使用 `man` 命令查看完整的命令手册
4. **逐步深入**：基础命令熟练后，再学习更高级的功能

### [安全提醒](#安全提醒)

1. **备份重要数据**：在执行危险操作前，先备份重要文件
2. **测试环境验证**：重要命令先在测试环境中验证
3. **理解命令作用**：不要运行不理解的命令，特别是 `rm -rf` 等危险命令
4. **使用交互模式**：删除操作时使用 `-i` 选项，避免误操作

记住，这个速查表只是帮助你快速回顾和查找命令的工具。要真正掌握 Linux 命令行，还需要大量的实际练习和经验积累。建议你在日常工作中经常使用这些命令，逐渐形成自己的工作流程和习惯。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [附录A1｜常用命令速查表](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#附录a1-常用命令速查表)
- [文件与目录操作](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文件与目录操作)
- [基础文件操作](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#基础文件操作)
- [文件操作](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文件操作)
- [文件查找与搜索](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文件查找与搜索)
- [权限与所有权管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#权限与所有权管理)
- [权限查看与修改](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#权限查看与修改)
- [用户与组信息](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#用户与组信息)
- [文本查看与编辑](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本查看与编辑)
- [文本查看](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本查看)
- [文本统计与处理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本统计与处理)
- [文本编辑器](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本编辑器)
- [压缩与归档](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#压缩与归档)
- [压缩与解压](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#压缩与解压)
- [文件校验](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文件校验)
- [进程管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#进程管理)
- [进程查看](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#进程查看)
- [进程控制](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#进程控制)
- [系统监控](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#系统监控)
- [系统信息](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#系统信息)
- [磁盘与文件系统](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#磁盘与文件系统)
- [网络监控](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#网络监控)
- [网络工具](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#网络工具)
- [网络配置](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#网络配置)
- [网络连接与测试](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#网络连接与测试)
- [文件传输](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文件传输)
- [远程连接](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#远程连接)
- [文本处理三剑客](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本处理三剑客)
- [grep - 文本搜索](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#grep-文本搜索)
- [awk - 文本处理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#awk-文本处理)
- [sed - 流编辑器](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#sed-流编辑器)
- [管道与重定向](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#管道与重定向)
- [管道操作](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#管道操作)
- [重定向操作](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#重定向操作)
- [命令替换](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#命令替换)
- [系统服务管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#系统服务管理)
- [systemd 服务管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#systemd-服务管理)
- [传统服务管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#传统服务管理)
- [常用系统管理命令](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#常用系统管理命令)
- [系统信息](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#系统信息-1)
- [性能监控](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#性能监控)
- [磁盘管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#磁盘管理)
- [安全与权限](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#安全与权限)
- [权限管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#权限管理)
- [网络安全](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#网络安全)
- [开发者工具](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#开发者工具)
- [版本控制](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#版本控制)
- [包管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#包管理)
- [编译与构建](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#编译与构建)
- [实用工具](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#实用工具)
- [文本处理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#文本处理)
- [系统信息](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#系统信息-2)
- [时间管理](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#时间管理)
- [使用建议](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#使用建议)
- [快速查找技巧](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#快速查找技巧)
- [命令组合技巧](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#命令组合技巧)
- [学习建议](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#学习建议)
- [安全提醒](https://xiaolinnote.com/linux/appendix-a1-command-cheat-sheet.html#安全提醒)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
