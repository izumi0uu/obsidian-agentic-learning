---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - "interview"
status: inbox
created: 2026-05-07
updated: 2026-05-09
url: "https://xiaolinnote.com/linux/03-file-operations.html"
source: "https://xiaolinnote.com/linux/03-file-operations.html"
last_checked: 2026-05-07
freshness: watch
sha256: 716e34097de17f07b88ab0d646a70421c6020e22289cd194ae1652538213df62
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Linux Filesystem]]"
  - "[[File Operations]]"
---
# 第3章 文件与目录的日常操作

原始链接：https://xiaolinnote.com/linux/03-file-operations.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[Linux Filesystem]]
- [[File Operations]]

## 页面正文


[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 17 分钟约 5061 字2025/9/2

---

# [03｜文件与目录的日常操作](#_03-文件与目录的日常操作)

大家好，我是小林。

想象一下这样的场景：你刚刚从同事那里收到了一些项目文件，需要整理到自己的工作目录中。有些文件要复制，有些要移动，有些要删除，还有一大堆文件需要按类型分类存放。面对这些杂乱的文件，你该如何高效地组织它们？

在日常生活中，我们经常需要处理各种文件和目录。就像整理房间需要把物品放到正确的位置一样，在 Linux 系统中，我们也需要掌握文件和目录的基本操作。这一章我们要学习的，就是这些日常操作中的核心技能。掌握了这些，你就能像整理自己的房间一样，轻松管理 Linux 系统中的文件。

## [3.1 基础操作：创建、复制、移动和删除](#_3-1-基础操作-创建、复制、移动和删除)

在 Linux 系统中，文件和目录操作是我们日常工作中最频繁的任务之一。想象一下你正在整理一个混乱的办公室：需要创建新的文件夹来分类文件，复制重要文档作为备份，移动文件到合适的位置，以及清理不再需要的文件。Linux 提供了一套完整的工具来帮助我们高效地完成这些任务。

这些基本操作命令不仅仅是简单的工具，它们背后体现了 Linux 文件系统的设计哲学。每个命令都有其特定的用途和使用场景，理解这些场景背后的逻辑，能够帮助我们更好地掌握文件管理的精髓。

### [创建文件和目录：touch 和 mkdir](#创建文件和目录-touch-和-mkdir)

创建文件和目录是组织工作的第一步。就像我们在开始新项目时会先准备好文件夹和文档模板一样，Linux 提供了 `touch` 和 `mkdir` 命令来帮助我们建立工作环境的基础结构。

`touch` 命令看似简单，实则蕴含着 Linux 文件系统的重要概念。在 Linux 中，文件的内容和文件的元数据（如时间戳）是分开管理的。`touch` 命令的核心功能不仅仅是创建空文件，更重要的是管理文件的时间戳。这种设计反映了 Linux 系统的模块化思想——每个工具专注于做一件事，并且把它做好。

让我们通过实际的场景来理解这些命令的应用：

```
# 创建一个新的空文件（比如创建一个笔记文件）
$ touch notes.txt
$ ls -l notes.txt
-rw-r--r-- 1 user user 0 Sep  1 17:00 notes.txt

# 创建目录（创建一个项目目录）
$ mkdir myproject
$ ls -ld myproject
drwxr-xr-x 2 user user 4096 Sep  1 17:01 myproject/
```

在实际工作中，创建空文件有很多用途：作为标记文件、创建配置文件模板、或者在脚本中用作锁文件。而 `mkdir` 则是建立项目结构的基础工具，它帮助我们按照逻辑层次组织文件。

**创建多级目录**：有时候你需要一次创建多级目录结构：

```
# 创建嵌套的目录结构
$ mkdir -p myproject/src/main/java
$ tree myproject/
myproject/
└── src
    └── main
        └── java
```

如果没有 `-p` 选项，你就需要一级一级地创建目录，就像盖房子必须先建一楼再建二楼一样。

### [复制文件和目录：cp](#复制文件和目录-cp)

复制操作是数据管理中的重要环节。无论是创建重要文件的备份，还是分享文件给团队成员，`cp` 命令都是我们不可或缺的工具。复制操作的本质是创建数据的独立副本，这意味着原文件和副本可以独立修改，互不影响。

`cp` 命令的设计体现了 Linux 系统对数据完整性的重视。当我们复制文件时，系统会确保新文件具有与原文件相同的内容和权限属性（除非特别指定）。这种设计哲学贯穿于整个 Linux 系统——保护用户数据的完整性和安全性。

让我们深入了解 `cp` 命令的工作原理：

```
# 复制文件
$ cp notes.txt backup_notes.txt
$ ls -l *.txt
-rw-r--r-- 1 user user 0 Sep  1 17:00 backup_notes.txt
-rw-r--r-- 1 user user 0 Sep  1 17:00 notes.txt

# 复制目录（需要 -r 选项，recursive 递归）
$ cp -r myproject myproject_backup
$ ls -ld myproject*/
drwxr-xr-x 3 user user 4096 Sep  1 17:02 myproject/
drwxr-xr-x 3 user user 4096 Sep  1 17:02 myproject_backup/
```

为什么复制目录需要 `-r` 选项？这涉及到 Linux 文件系统的层次结构特性。目录不仅仅是一个容器，它还包含了指向其他文件和目录的引用。递归复制意味着命令会遍历整个目录树，复制所有的文件、子目录以及它们的内容。这就像搬家时，你不仅要搬箱子，还要把箱子里的所有物品都一起搬走。

**实用的 cp 选项**：

```
# 保留文件属性复制（保持权限、时间戳等）
$ cp -p important_file.txt backup/

# 交互式复制（覆盖前询问）
$ cp -i file1.txt file2.txt
cp: overwrite 'file2.txt'? y

# 显示复制过程
$ cp -v *.txt backup/
'file1.txt' -> 'backup/file1.txt'
'file2.txt' -> 'backup/file2.txt'
```

### [移动和重命名：mv](#移动和重命名-mv)

移动文件就像把物品从一个房间搬到另一个房间，重命名就像给物品换个标签。

```
# 移动文件到目录
$ mv notes.txt myproject/
$ ls myproject/
notes.txt  src

# 重命名文件
$ mv myproject/notes.txt myproject/README.md
$ ls myproject/
README.md  src

# 移动目录（也可以用来重命名目录）
$ mv myproject_backup old_project
$ ls -ld old_project/
drwxr-xr-x 3 user user 4096 Sep  1 17:02 old_project/
```

你可能会问："为什么同一个命令既能移动又能重命名？" 这是因为在 Linux 系统中，移动和重命名在底层是同一个操作。重命名只是把文件在同一个目录下"移动"并改个名字而已。

**注意**：`mv` 操作是直接"剪切"，不像 `cp` 会保留原文件。就像你把书从书架搬到桌子上，书架上的书就消失了。

### [删除文件和目录：rm 和 rmdir](#删除文件和目录-rm-和-rmdir)

删除操作就像扔垃圾，一旦删除就很难恢复（虽然有回收站，但 Linux 默认没有这个概念）。

```
# 删除文件
$ rm backup_notes.txt

# 交互式删除（删除前询问，更安全）
$ rm -i some_file.txt
rm: remove regular empty file 'some_file.txt'? y

# 删除目录及其所有内容（危险操作！）
$ rm -r old_project/
```

**⚠️高危操作警告**：`rm -rf /` 会删除整个文件系统！在执行删除操作前，请务必确认：

1. 你在正确的目录下（`pwd` 确认）
2. 你知道要删除什么（`ls` 查看）
3. 必要时使用 `-i` 选项进行确认

```
# 安全的做法：先查看，再删除
$ ls
file1.txt  file2.txt  important/
$ rm -i file1.txt
rm: remove regular file 'file1.txt'? y
```

**rmdir 命令**：只能删除空目录

```
# 创建空目录
$ mkdir empty_dir

# 删除空目录
$ rmdir empty_dir

# 如果目录不为空，会失败
$ rmdir myproject/
rmdir: failed to remove 'myproject/': Directory not empty
```

## [3.2 查看文件信息：file 和 stat](#_3-2-查看文件信息-file-和-stat)

如何快速了解文件的类型和详细信息？有时候你看到一个文件，却不知道它是什么类型的，或者想查看文件的详细元信息。

### [file 命令：识别文件类型](#file-命令-识别文件类型)

`file` 命令就像是一个"文件鉴定专家"，它能告诉你一个文件到底是什么类型。

```
# 创建不同类型的文件来测试
$ echo "Hello World" > text.txt
$ touch empty.txt
$ ln -s text.txt link_to_text

# 使用 file 命令查看文件类型
$ file text.txt
text.txt: ASCII text

$ file empty.txt
empty.txt: empty

$ file link_to_text
link_to_text: symbolic link to text.txt

$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=..., stripped
```

你可能会问："为什么需要 file 命令？看文件扩展名不行吗？" 不行！因为 Linux 系统中，文件扩展名只是给人看的，系统并不依赖它。一个文件即使没有扩展名或者扩展名错误，`file` 命令也能正确识别它的类型。

这在很多场景下都很有用：

- 下载了一个没有扩展名的文件，想知道它是什么类型
- 收到一个可疑文件，想确认它真的是文本文件而不是可执行文件
- 查看编译后的二进制文件的信息

### [stat 命令：查看文件详细信息](#stat-命令-查看文件详细信息)

`stat` 命令就像是文件的"身份证"，它显示了文件的所有元信息。

```
# 查看文件的详细状态
$ stat text.txt
  File: text.txt
  Size: 12        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 1234567     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/   user)   Gid: ( 1000/   user)
Access: 2025-09-01 17:10:00.000000000 +0800
Modify: 2025-09-01 17:10:00.000000000 +0800
Change: 2025-09-01 17:10:00.000000000 +0800
 Birth: 2025-09-01 17:10:00.000000000 +0800
```

这些信息告诉你：

- **Size**：文件大小（12字节）
- **Inode**：文件的唯一标识号
- **Access**：文件权限
- **Access time**：最后访问时间
- **Modify time**：最后修改时间
- **Change time**：元数据最后修改时间

你可能会问："为什么有三个时间戳？" 想象一下你的一本书：

- Access time：你最后一次翻阅这本书的时间
- Modify time：你最后一次修改这本书内容的时间
- Change time：你最后一次给这本书换封面或贴标签的时间

**实用场景**：

```
# 查看目录的 stat 信息
$ stat myproject/
  File: myproject/
  Size: 4096       	Blocks: 8          IO Block: 4096   directory
Device: 801h/2049d	Inode: 1234568     Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   user)   Gid: ( 1000/   user)
Access: 2025-09-01 17:15:00.000000000 +0800
Modify: 2025-09-01 17:02:00.000000000 +0800
Change: 2025-09-01 17:02:00.000000000 +0800
 Birth: 2025-09-01 17:02:00.000000000 +0800
```

## [3.3 通配符和花括号扩展：批量操作的利器](#_3-3-通配符和花括号扩展-批量操作的利器)

如何一次性操作多个文件？如果一个一个地操作，效率太低了。

Linux 提供了强大的通配符和花括号扩展功能，让你能够批量操作文件。这就像是有一个"魔法选择器"，可以一次性选择符合特定模式的多个文件。

### [基础通配符：\*、?、[]](#基础通配符-、-、)

```
# 准备一些测试文件
$ touch file1.txt file2.txt file3.txt file1.log file2.log data.csv config.json

# * 匹配任意数量的任意字符
$ ls *.txt
file1.txt file2.txt file3.txt

# ? 匹配单个任意字符
$ ls file?.txt
file1.txt file2.txt file3.txt

# [] 匹配指定范围内的单个字符
$ ls file[12].txt
file1.txt file2.txt

# 组合使用
$ ls file[1-3].*
file1.log  file1.txt  file2.log  file2.txt  file3.log  file3.txt
```

你可能会问："这些通配符有什么实际用途？" 想象一下，你要处理一个有上千个文件的目录，手动一个个操作会疯掉的。通配符让你能够：

```
# 批量复制所有日志文件
$ cp *.log logs/

# 批量删除临时文件
$ rm *.tmp

# 查看所有配置文件
$ ls *.conf *.config
```

### [花括号扩展：{}](#花括号扩展)

花括号扩展比通配符更强大，它可以生成组合。

```
# 生成多个文件
$ touch {report,summary}_{2024,2025}.txt
$ ls *.txt
report_2024.txt  report_2025.txt  summary_2024.txt  summary_2025.txt

# 创建目录结构
$ mkdir -p project/{src,doc,test}/{main,util}
$ tree project/
project/
├── doc
│   ├── main
│   └── util
├── src
│   ├── main
│   └── util
└── test
    ├── main
    └── util
```

**通配符 vs 花括号扩展的区别**：

```
# 通配符匹配已存在的文件
$ ls file[12].txt  # 只会显示已存在的 file1.txt 和 file2.txt

# 花括号扩展生成组合，不管文件是否存在
$ echo file{1,5}.txt
file1.txt file5.txt  # 即使 file5.txt 不存在也会生成这个文本
```

### [实际应用场景](#实际应用场景)

```
# 批量重命名（结合通配符和其他命令）
$ for f in *.txt; do mv "$f" "backup_$f"; done

# 批量处理图片
$ convert *.jpg -resize 800x600 resized/

# 创建测试数据
$ touch test_{1..100}.log  # 创建 test_1.log 到 test_100.log
```

## [3.4 查找文件：find 命令的强大功能](#_3-4-查找文件-find-命令的强大功能)

如何在浩瀚的文件系统中快速找到需要的文件？如果你记得文件名但忘记放在哪里了，或者想找到符合特定条件的文件，`find` 命令就是你的得力助手。

### [按名称查找](#按名称查找)

```
# 在当前目录及子目录中查找名为 notes.txt 的文件
$ find . -name "notes.txt"
./myproject/notes.txt

# 不区分大小写查找
$ find . -iname "NOTES.TXT"
./myproject/notes.txt

# 查找所有 .txt 文件
$ find . -name "*.txt"
./file1.txt
./myproject/notes.txt
```

### [按类型查找](#按类型查找)

```
# 只查找文件
$ find . -type f

# 只查找目录
$ find . -type d

# 查找符号链接
$ find . -type l
```

### [按大小查找](#按大小查找)

```
# 查找大于 10MB 的文件
$ find . -type f -size +10M

# 查找小于 1KB 的文件
$ find . -type f -size -1k

# 查找正好 1MB 的文件
$ find . -type f -size 1M
```

### [按时间查找](#按时间查找)

```
# 查找最近 7 天内修改过的文件
$ find . -type f -mtime -7

# 查找超过 30 天未访问的文件
$ find . -type f -atime +30

# 查找最近 1 小时内修改过的文件
$ find . -type f -mmin -60
```

### [组合条件查找](#组合条件查找)

```
# 查找大于 1MB 的 .log 文件
$ find . -name "*.log" -type f -size +1M

# 查找 .txt 文件但排除某个目录
$ find . -name "*.txt" -not -path "./tmp/*"

# 使用 OR 条件
$ find . \( -name "*.txt" -o -name "*.md" \)
```

### [对找到的文件执行操作](#对找到的文件执行操作)

```
# 查找并删除 .tmp 文件
$ find . -name "*.tmp" -delete

# 查找并显示详细信息
$ find . -name "*.txt" -ls

# 查找并复制到指定目录
$ find . -name "*.jpg" -exec cp {} ~/Pictures/ \;
```

你可能会问："find 命令为什么这么复杂？" 因为它需要处理各种各样的查找需求。就像一个好的搜索引擎，你需要能够按名称、类型、大小、时间等多种条件来筛选。

## [3.5 压缩和解压：tar、gzip、zip](#_3-5-压缩和解压-tar、gzip、zip)

如何节省磁盘空间？如何方便地传输多个文件？压缩和解压是日常管理中必不可少的技能。

### [tar：打包文件（不压缩）](#tar-打包文件-不压缩)

`tar` 命令就像打包箱，它可以把多个文件和目录打包成一个文件，但不压缩。

```
# 打包目录
$ tar -cvf myproject.tar myproject/
myproject/
myproject/README.md
myproject/src/

# 查看打包内容
$ tar -tvf myproject.tar
drwxr-xr-x user/user 0 2025-09-01 17:02 myproject/
-rw-r--r-- user/user 0 2025-09-01 17:01 myproject/README.md
drwxr-xr-x user/user 0 2025-09-01 17:01 myproject/src/

# 解包
$ tar -xvf myproject.tar
```

**tar 常用选项**：

- `-c`：create（创建）
- `-x`：extract（解包）
- `-v`：verbose（显示过程）
- `-f`：file（指定文件名）

### [gzip 和 gunzip：压缩和解压](#gzip-和-gunzip-压缩和解压)

`gzip` 就像是真空压缩袋，它能有效减小文件大小。

```
# 压缩文件
$ gzip large_file.txt
$ ls -l large_file.txt*
-rw-r--r-- 1 user user 1024 Sep  1 17:20 large_file.txt.gz

# 解压文件
$ gunzip large_file.txt.gz

# 查看压缩文件内容（不解压）
$ gzip -l large_file.txt.gz
         compressed        uncompressed  ratio uncompressed_name
                1024               4096  75.0% large_file.txt
```

### [tar + gzip：打包并压缩](#tar-gzip-打包并压缩)

这是最常用的组合，就像先打包再真空压缩。

```
# 打包并压缩（.tar.gz 或 .tgz）
$ tar -czvf myproject.tar.gz myproject/

# 解压并解包
$ tar -xzvf myproject.tar.gz

# 查看压缩包内容
$ tar -tzvf myproject.tar.gz
```

### [zip 和 unzip：跨平台压缩格式](#zip-和-unzip-跨平台压缩格式)

`zip` 格式在 Windows 和 Linux 上都通用，适合跨平台传输。

```
# 创建 zip 压缩包
$ zip -r myproject.zip myproject/

# 解压 zip 文件
$ unzip myproject.zip

# 查看 zip 内容
$ unzip -l myproject.zip
```

### [文件校验：md5sum 和 sha256sum](#文件校验-md5sum-和-sha256sum)

如何确保文件在传输过程中没有损坏？使用校验和工具可以验证文件的完整性。

```
# 生成 MD5 校验和
$ md5sum important_file.txt
d41d8cd98f00b204e9800998ecf8427e  important_file.txt

# 生成 SHA256 校验和（更安全）
$ sha256sum important_file.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  important_file.txt

# 批量生成校验和文件
$ md5sum *.txt > checksums.md5

# 验证文件完整性
$ md5sum -c checksums.md5
important_file.txt: OK
another_file.txt: OK
```

你可能会问："什么时候需要校验和？" 这就像你在收到重要文件后，需要确认文件在传输过程中没有被损坏或篡改。常见的场景包括：

- 下载大型软件后验证完整性
- 备份重要数据后验证备份是否完整
- 在网络上传输文件后确认文件未被篡改

---

## [练习题](#练习题)

1. 如何安全地批量删除所有 .log 文件，但删除前要确认每个文件？

查看答案

- 思路与步骤：使用 `rm -i` 选项进行交互式删除，结合通配符批量操作
- 示例命令：

```
# 方法1：使用 rm -i 交互式删除
$ rm -i *.log
rm: remove regular file 'access.log'? y
rm: remove regular file 'error.log'? y
rm: remove regular file 'system.log'? n

# 方法2：先查看要删除的文件，再确认删除
$ ls *.log
access.log  error.log  system.log
$ rm -i *.log
```

交互式删除（`-i` 选项）是批量删除的安全保障，特别是当你不确定是否要删除所有匹配的文件时。

2. 如何找到 /var/log 目录下大于 100MB 且最近 30 天内修改过的日志文件？

查看答案

- 思路与步骤：使用 `find` 命令组合大小和时间条件进行查找
- 示例命令：

```
# 查找大于 100MB 且最近 30 天内修改过的文件
$ find /var/log -type f -size +100M -mtime -30

# 如果需要查看详细信息，可以加上 -ls 选项
$ find /var/log -type f -size +100M -mtime -30 -ls

# 如果需要进一步处理，比如移动到其他位置
$ find /var/log -type f -size +100M -mtime -30 -exec mv {} /backup/old_logs/ \;
```

这个命令组合了三个条件：文件类型（`-type f`）、大小（`-size +100M`）、修改时间（`-mtime -30`），是系统维护中常用的清理大文件的命令。

3. 如何创建一个包含项目源代码的压缩包，但排除 node\_modules 和 .git 目录？

查看答案

- 思路与步骤：使用 `tar` 命令的 `--exclude` 选项排除不需要的目录
- 示例命令：

```
# 创建压缩包，排除指定目录
$ tar -czvf project_backup.tar.gz --exclude='node_modules' --exclude='.git' myproject/

# 或者使用更复杂的排除模式
$ tar -czvf project_backup.tar.gz --exclude='*.log' --exclude='tmp/*' --exclude='.git' myproject/

# 查看压缩包内容确认排除成功
$ tar -tzvf project_backup.tar.gz | grep -E '(node_modules|\.git)'
# 应该没有输出，说明成功排除了这些目录
```

在备份项目时排除不必要的目录（如 node\_modules、.git、缓存文件等）可以大大减少压缩包大小，提高备份效率。

---

## [速记卡](#速记卡)

- `mkdir -p`：创建多级目录（一次性建好楼层结构）
- `cp -r`：递归复制目录（搬家时打包所有物品）
- `mv`：移动/重命名文件（物品换个位置或换个标签）
- `rm -rf`：强制删除目录（清空房间，⚠️小心使用）
- `find . -name "*.txt"`：查找所有txt文件（在房间里找特定物品）
- `tar -czvf`：打包并压缩（装箱并抽真空）
- `md5sum file`：生成文件校验和（给文件做个"指纹"）

## [常见坑](#常见坑)

- `rm -rf /`：会删除整个系统，永远不要运行这个命令！
- `cp` 时忘记 `-r` 选项：无法复制目录，就像搬家时只拿了箱子标签没拿箱子
- `mv` 操作后原文件消失：记住 mv 是剪切不是复制，重要文件最好先备份
- 通配符误匹配：比如 `rm *.txt` 可能误删重要文件，先用 `ls *.txt` 确认
- tar 时忘记 `-f` 选项：命令会等待输入，不知道发生了什么
- 解压到错误目录：污染当前目录，最好先创建目标目录再解压
- 忽略校验和：下载大文件后不验证完整性，可能下载了损坏的文件

## [章节总结](#章节总结)

文件和目录的日常操作是 Linux 命令行的基础技能。通过掌握 `touch`、`mkdir`、`cp`、`mv`、`rm` 这些基本命令，你可以像整理自己的房间一样管理 Linux 系统中的文件。

`file` 和 `stat` 命令让你能够深入了解文件的类型和属性，就像了解物品的特性和历史一样。通配符和花括号扩展则大大提高了批量操作的效率，让你能够一次性处理多个文件。

`find` 命令是文件查找的瑞士军刀，它能够根据各种条件精确地定位文件。而 `tar`、`gzip`、`zip` 等压缩工具则帮助你节省空间和方便传输。

最重要的是，在执行删除等危险操作时一定要小心谨慎。养成先查看再操作的习惯，必要时使用交互式选项进行确认。记住，在 Linux 系统中，删除操作通常是不可逆的，就像打碎的玻璃很难恢复一样。

掌握了这些核心技能，你就能高效地管理 Linux 系统中的文件，为后续更复杂的操作打下坚实的基础。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/03-file-operations.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [03｜文件与目录的日常操作](https://xiaolinnote.com/linux/03-file-operations.html#_03-文件与目录的日常操作)
- [3.1 基础操作：创建、复制、移动和删除](https://xiaolinnote.com/linux/03-file-operations.html#_3-1-基础操作-创建、复制、移动和删除)
- [创建文件和目录：touch 和 mkdir](https://xiaolinnote.com/linux/03-file-operations.html#创建文件和目录-touch-和-mkdir)
- [复制文件和目录：cp](https://xiaolinnote.com/linux/03-file-operations.html#复制文件和目录-cp)
- [移动和重命名：mv](https://xiaolinnote.com/linux/03-file-operations.html#移动和重命名-mv)
- [删除文件和目录：rm 和 rmdir](https://xiaolinnote.com/linux/03-file-operations.html#删除文件和目录-rm-和-rmdir)
- [3.2 查看文件信息：file 和 stat](https://xiaolinnote.com/linux/03-file-operations.html#_3-2-查看文件信息-file-和-stat)
- [file 命令：识别文件类型](https://xiaolinnote.com/linux/03-file-operations.html#file-命令-识别文件类型)
- [stat 命令：查看文件详细信息](https://xiaolinnote.com/linux/03-file-operations.html#stat-命令-查看文件详细信息)
- [3.3 通配符和花括号扩展：批量操作的利器](https://xiaolinnote.com/linux/03-file-operations.html#_3-3-通配符和花括号扩展-批量操作的利器)
- [基础通配符：*、?、[]](https://xiaolinnote.com/linux/03-file-operations.html#基础通配符-、-、)
- [花括号扩展：{}](https://xiaolinnote.com/linux/03-file-operations.html#花括号扩展)
- [实际应用场景](https://xiaolinnote.com/linux/03-file-operations.html#实际应用场景)
- [3.4 查找文件：find 命令的强大功能](https://xiaolinnote.com/linux/03-file-operations.html#_3-4-查找文件-find-命令的强大功能)
- [按名称查找](https://xiaolinnote.com/linux/03-file-operations.html#按名称查找)
- [按类型查找](https://xiaolinnote.com/linux/03-file-operations.html#按类型查找)
- [按大小查找](https://xiaolinnote.com/linux/03-file-operations.html#按大小查找)
- [按时间查找](https://xiaolinnote.com/linux/03-file-operations.html#按时间查找)
- [组合条件查找](https://xiaolinnote.com/linux/03-file-operations.html#组合条件查找)
- [对找到的文件执行操作](https://xiaolinnote.com/linux/03-file-operations.html#对找到的文件执行操作)
- [3.5 压缩和解压：tar、gzip、zip](https://xiaolinnote.com/linux/03-file-operations.html#_3-5-压缩和解压-tar、gzip、zip)
- [tar：打包文件（不压缩）](https://xiaolinnote.com/linux/03-file-operations.html#tar-打包文件-不压缩)
- [gzip 和 gunzip：压缩和解压](https://xiaolinnote.com/linux/03-file-operations.html#gzip-和-gunzip-压缩和解压)
- [tar + gzip：打包并压缩](https://xiaolinnote.com/linux/03-file-operations.html#tar-gzip-打包并压缩)
- [zip 和 unzip：跨平台压缩格式](https://xiaolinnote.com/linux/03-file-operations.html#zip-和-unzip-跨平台压缩格式)
- [文件校验：md5sum 和 sha256sum](https://xiaolinnote.com/linux/03-file-operations.html#文件校验-md5sum-和-sha256sum)
- [练习题](https://xiaolinnote.com/linux/03-file-operations.html#练习题)
- [速记卡](https://xiaolinnote.com/linux/03-file-operations.html#速记卡)
- [常见坑](https://xiaolinnote.com/linux/03-file-operations.html#常见坑)
- [章节总结](https://xiaolinnote.com/linux/03-file-operations.html#章节总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
