---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - interview
  - linux
status: inbox
created: 2026-05-07
updated: 2026-05-17
url: https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html
source: https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html
last_checked: 2026-05-17
freshness: watch
sha256: ba8faee465a88454198ddcb8b1648c0313943ec900703c516e232c4c9b487735
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 附录A2：正则表达式与通配符速查

原始链接：https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 附录A2：正则表达式与通配符速查

[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 14 分钟约 4055 字2025/9/2

---

# [附录A2｜正则表达式与通配符速查](#附录a2-正则表达式与通配符速查)

大家好，我是小林。

想象一下这样的场景：你正在处理大量的日志文件，需要找出所有符合特定格式的日期；或者你想要批量重命名数百个文件，只修改符合某种命名模式的文件。面对这样的需求，普通的字符串匹配已经不够用了，你需要更强大的模式匹配工具。

正则表达式和通配符就是 Linux 世界中的"模式匹配利器"。正则表达式让你能够用简洁的语法描述复杂的文本模式，而通配符则提供了简单直观的文件名匹配方式。掌握这两个工具，你就拥有了在文本海洋中精准"捕鱼"的能力。

这个速查表将帮助你快速掌握这两种重要的模式匹配技术，从基础语法到高级应用，让你能够轻松应对各种文本处理和文件管理的挑战。

## [通配符 (Wildcards)](#通配符-wildcards)

通配符主要用于文件名匹配，在 Shell 中进行文件名扩展。它们简单直观，适合大多数文件匹配需求。

### [基础通配符](#基础通配符)

| 通配符 | 名称 | 功能描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- | --- |
| `*` | 星号 | 匹配任意数量（包括零个）的任意字符 | `ls *.txt` | file1.txt, notes.txt, data.txt |
| `?` | 问号 | 匹配单个任意字符 | `ls file?.txt` | file1.txt, fileA.txt, file\_.txt |
| `[...]` | 字符组 | 匹配指定范围内的单个字符 | `ls file[123].txt` | file1.txt, file2.txt, file3.txt |
| `[^...]` | 排除字符组 | 匹配不在指定范围内的单个字符 | `ls file[^0-9].txt` | fileA.txt, file\_.txt |
| `[a-z]` | 字符范围 | 匹配指定字符范围内的单个字符 | `ls [a-c]*.txt` | apple.txt, banana.txt, cherry.txt |

### [实际应用示例](#实际应用示例)

```
# 匹配所有文件
*                    # 匹配当前目录下所有文件和目录
*.txt               # 匹配所有 .txt 文件
file*               # 匹配所有以 file 开头的文件
*.tar.gz            # 匹配所有 tar.gz 压缩文件

# 使用 ? 匹配单个字符
file?.txt           # 匹配 file1.txt, fileA.txt 等
report_202?.csv     # 匹配 report_2020.csv 到 report_2029.csv

# 使用字符组
file[1-3].txt       # 匹配 file1.txt, file2.txt, file3.txt
image_[png,jpg]*    # 匹配 image_png001.jpg, image_jpg_data.png
access_[0-9][0-9].log # 匹配 access_00.log 到 access_99.log

# 排除特定字符
file[^0-9].txt      # 匹配 fileA.txt, file_.txt（不匹配 file1.txt）
report_[^abc].log   # 匹配 report_d.log, report_x.log（不匹配 report_a.log）
```

### [花括号扩展](#花括号扩展)

花括号扩展不是通配符，但常与通配符配合使用，用于生成组合。

| 语法 | 功能描述 | 示例 | 展开结果 |
| --- | --- | --- | --- |
| `{a,b,c}` | 列表扩展 | `file{a,b,c}.txt` | filea.txt fileb.txt filec.txt |
| `{1..5}` | 数字序列 | `file{1..3}.txt` | file1.txt file2.txt file3.txt |
| `{a..z}` | 字母序列 | `{a..c}.txt` | a.txt b.txt c.txt |
| `{start..end..step}` | 带步长的序列 | `{1..10..2}` | 1 3 5 7 9 |

```
# 实际应用示例
# 创建多个文件
touch file_{report,data,config}_{2023,2024}.txt
# 生成：file_report_2023.txt file_report_2024.txt file_data_2023.txt 等

# 备份目录结构
cp -r project/ backup_$(date +%Y%m%d)/
mkdir -p backup_{2023,2024,2025}/Q{1,2,3,4}

# 批量重命名
for file in image_{001..100}.jpg; do
    mv "$file" "processed_$file"
done
```

## [基础正则表达式 (BRE)](#基础正则表达式-bre)

基础正则表达式主要用于 `grep`、`sed`、`awk` 等文本处理工具。它们提供了比通配符更强大的文本模式匹配能力。

### [字符匹配](#字符匹配)

| 元字符 | 名称 | 功能描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- | --- |
| `.` | 点号 | 匹配除换行符外的任意单个字符 | `grep "f.r" file.txt` | for, far, f1r, f\_r |
| `[...]` | 字符组 | 匹配指定范围内的单个字符 | `grep "f[aeiou]r" file.txt` | far, fer |
| `[^...]` | 排除字符组 | 匹配不在指定范围内的单个字符 | `grep "f[^0-9]r" file.txt` | far, fer（不匹配 f1r） |
| `^` | 脱字符 | 匹配行首位置 | `grep "^Hello" file.txt` | Hello world, Hello Linux |
| `$` | 美元符号 | 匹配行尾位置 | `grep "end$" file.txt` | this is the end |
| `*` | 星号 | 匹配前一个字符的零次或多次出现 | `grep "go*gle" file.txt` | ggle, gogle, google, goooogle |
| `\{n\}` | 精确匹配 | 匹配前一个字符恰好 n 次 | `grep "o\{2\}" file.txt` | book, look, good |
| `\{n,\}` | 至少匹配 | 匹配前一个字符至少 n 次 | `grep "o\{2,\}" file.txt` | book, look, good, fooood |
| `\{n,m\}` | 范围匹配 | 匹配前一个字符 n 到 m 次 | `grep "o\{2,3\}" file.txt` | book, look, good（不匹配 fooood） |

### [特殊字符转义](#特殊字符转义)

| 转义序列 | 匹配内容 | 示例 | 匹配结果 |
| --- | --- | --- | --- |
| `\.` | 字面量点号 | `grep "file\.txt" file.txt` | file.txt（不匹配 fileXtxt） |
| `\\` | 字面量反斜杠 | `grep "\\" file.txt` | \ |
| `\[` | 字面量左方括号 | `grep "\[" file.txt` | [ |
| `\(` | 字面量左括号 | `grep "\(" file.txt` | ( |
| `\{` | 字面量左花括号 | `grep "\{" file.txt` | { |

```
# 基础正则表达式示例
# 查找以 # 开头的注释行
grep "^#" config_file

# 查找以 . 结尾的行
grep "\.$" data.txt

# 查找包含 IP 地址格式的行
grep "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" log.txt

# 查找连续两个相同字符的单词
grep "\(.\)\1" words.txt  # 匹配 book, success, letter 等
```

## [扩展正则表达式 (ERE)](#扩展正则表达式-ere)

扩展正则表达式提供了更简洁的语法和更多的功能，通常需要在工具中指定 `-E` 选项（如 `grep -E`）或使用 `egrep`。

### [量词匹配](#量词匹配)

| 量词 | 功能描述 | BRE 等价 | ERE 示例 | 匹配结果 |
| --- | --- | --- | --- | --- |
| `?` | 匹配前一个字符零次或一次 | `\{0,1\}` | `colou?r` | color, colour |
| `+` | 匹配前一个字符一次或多次 | `\{1,\}` | `go+gle` | gogle, google, gooogle |
| `*` | 匹配前一个字符零次或多次 | `*` | `go*gle` | ggle, gogle, google |
| `{n}` | 精确匹配 n 次 | `\{n\}` | `o{2}` | book, look |
| `{n,}` | 至少匹配 n 次 | `\{n,\}` | `o{2,}` | book, look, good |
| `{n,m}` | 匹配 n 到 m 次 | `\{n,m\}` | `o{2,3}` | book, look, good |

### [分组和引用](#分组和引用)

| 语法 | 功能描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- |
| `(pattern)` | 分组 | `(ab)+` | ab, abab, ababab |
| `(a|b)` | 选择匹配 | `cat|dog` | cat, dog |
| `\1`, `\2` | 反向引用 | `(.)\1` | aa, bb, 11 |

```
# 扩展正则表达式示例
# 查找包含 color 或 colour 的行
grep -E "colou?r" document.txt

# 查找邮箱地址格式
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" emails.txt

# 查找重复的单词
grep -E "\b(\w+)\s+\1\b" document.txt  # 匹配 "the the", "is is" 等

# 查找 HTML 标签
grep -E "<[^>]+>" html_file.html

# 查找日期格式 YYYY-MM-DD
grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" dates.txt
```

### [字符类别](#字符类别)

| 类别 | 功能描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- |
| `[[:alpha:]]` | 字母字符 | `[[:alpha:]]` | a, B, 中 |
| `[[:alnum:]]` | 字母数字字符 | `[[:alnum:]]` | a, 1, B, 2 |
| `[[:digit:]]` | 数字字符 | `[[:digit:]]` | 0, 1, 2, ..., 9 |
| `[[:lower:]]` | 小写字母 | `[[:lower:]]` | a, b, c, ..., z |
| `[[:upper:]]` | 大写字母 | `[[:upper:]]` | A, B, C, ..., Z |
| `[[:space:]]` | 空白字符 | `[[:space:]]` | 空格, 制表符, 换行 |
| `[[:punct:]]` | 标点符号 | `[[:punct:]]` | !, @, #, $, %, 等 |
| `[[:xdigit:]]` | 十六进制字符 | `[[:xdigit:]]` | 0-9, a-f, A-F |

```
# 字符类别使用示例
# 查找以字母开头的行
grep "^[[:alpha:]]" data.txt

# 查找包含数字的行
grep "[[:digit:]]" mixed_content.txt

# 查找标点符号
grep "[[:punct:]]" document.txt

# 查找十六进制颜色代码
grep -E "#[[:xdigit:]]{6}" css_file.css
```

## [高级正则表达式特性](#高级正则表达式特性)

### [零宽断言](#零宽断言)

零宽断言匹配位置而不是字符，用于更复杂的模式匹配。

| 断言 | 功能描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- |
| `(?=pattern)` | 正向先行断言 | `foo(?=bar)` | foo（后面跟着 bar） |
| `(?!pattern)` | 负向先行断言 | `foo(?!bar)` | foo（后面不跟着 bar） |
| `(?<=pattern)` | 正向后行断言 | `(?<=foo)bar` | bar（前面有 foo） |
| `(?<!pattern)` | 负向后行断言 | `(?<!foo)bar` | bar（前面没有 foo） |

**注意**: 这些高级特性在 `grep` 中可能需要使用 `-P` 选项（PCRE），或者在 `perl`、`python` 等语言中使用。

```
# 高级断言示例（需要 PCRE 支持）
# 查找后面跟着 "bar" 的 "foo"
grep -P "foo(?=bar)" text.txt

# 查找不跟着 "bar" 的 "foo"
grep -P "foo(?!bar)" text.txt

# 查找前面有数字的单词
grep -P "(?<=\d)\w+" text.txt

# 查找不在单词开头的数字
grep -P "(?<!\w)\d+" text.txt
```

### [贪婪与懒惰匹配](#贪婪与懒惰匹配)

| 量词类型 | 语法 | 行为描述 | 示例 | 匹配结果 |
| --- | --- | --- | --- | --- |
| 贪婪匹配 | `.*` | 尽可能多地匹配 | `a.*b` 在 "a123b456b" 中 | a123b456b |
| 懒惰匹配 | `.*?` | 尽可能少地匹配 | `a.*?b` 在 "a123b456b" 中 | a123b |

```
# 贪婪匹配示例
echo "<div>content1</div><div>content2</div>" | grep -oP "<div>.*</div>"
# 输出：<div>content1</div><div>content2</div>

# 懒惰匹配示例
echo "<div>content1</div><div>content2</div>" | grep -oP "<div>.*?</div>"
# 输出：<div>content1</div>
```

## [实际应用场景](#实际应用场景)

### [日志分析](#日志分析)

```
# 分析 Apache 访问日志
# 提取 IP 地址
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log

# 提取访问时间
grep -oE "\[[0-9]{2}/[A-Za-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}\]" access.log

# 提取 HTTP 状态码
grep -oE "\" [0-9]{3} " access.log | grep -oE "[0-9]{3}"

# 查找 404 错误
grep -E "\" 404 " access.log

# 查找特定 User-Agent
grep -E "Mozilla/[0-9]" access.log
```

### [代码处理](#代码处理)

```
# 查找 Python 函数定义
grep -nE "def [a-zA-Z_][a-zA-Z0-9_]*" *.py

# 查找 Java 类定义
grep -nE "class [A-Za-z][A-Za-z0-9_]*" *.java

# 查找 C/C++ 注释
grep -nE "(//.*|/\*.*\*/)" *.c

# 查找未使用的变量（简单模式）
grep -nE "^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*[^;]*;" *.c
```

### [配置文件处理](#配置文件处理)

```
# 提取 Nginx 配置中的服务器名称
grep -oE "server_name\s+[^;]*;" nginx.conf

# 提取 MySQL 配置中的端口号
grep -oE "port\s*=\s*[0-9]+" my.cnf

# 查找注释掉的配置行
grep -E "^\s*#" config_file

# 查找空行
grep -E "^\s*$" config_file
```

### [数据清洗](#数据清洗)

```
# 清理 CSV 文件中的引号
sed -E 's/^"|"$/ /g' data.csv

# 标准化日期格式
sed -E 's/([0-9]{2})\/([0-9]{2})\/([0-9]{4})/\3-\1-\2/g' dates.txt

# 移除多余的空格
sed -E 's/\s+/ /g' messy_text.txt

# 提取电子邮件地址
grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" contacts.txt
```

## [工具特定的正则表达式语法](#工具特定的正则表达式语法)

### [grep](#grep)

```
# 基础正则表达式（BRE）
grep "pattern" file.txt
grep "^start" file.txt          # 行首
grep "end$" file.txt           # 行尾
grep "[0-9]\{3\}" file.txt     # 恰好3个数字

# 扩展正则表达式（ERE）
grep -E "pattern" file.txt
grep -E "(cat|dog)" file.txt   # 选择匹配
grep -E "colou?r" file.txt     # 可选字符
grep -E "[0-9]{3}" file.txt    # 恰好3个数字（更简洁）

# Perl 兼容正则表达式（PCRE）
grep -P "pattern" file.txt
grep -P "\d{3}" file.txt       # 数字简写
grep -P "(?<=prefix)\w+" file.txt  # 后行断言
```

### [sed](#sed)

```
# 替换操作
sed -E 's/old/new/g' file.txt        # 全局替换
sed -E 's/^/# /' file.txt            # 行首添加注释
sed -E 's/\s+$//' file.txt           # 删除行尾空白

# 多个命令组合
sed -E '1s/^/---\n/; $s/$/\n---/' file.txt  # 添加分隔线

# 原地编辑（谨慎使用）
sed -E -i.bak 's/foo/bar/g' file.txt  # 创建备份并修改
```

### [awk](#awk)

```
# 使用正则表达式进行模式匹配
awk '/pattern/ {action}' file.txt
awk '/^ERROR/ {print $0}' error.log   # 提取错误行
awk '$1 ~ /^[0-9]/ {print $0}' data.txt  # 第一字段以数字开头

# 使用扩展正则表达式
awk --re-interval '/[0-9]{3}/ {print $0}' file.txt

# 字段匹配
awk '$2 ~ /pattern/ {print $0}' file.txt  # 第二字段匹配模式
```

### [find](#find)

```
# 使用正则表达式查找文件名
find . -regex ".*\.(txt|md)$"           # 查找 .txt 或 .md 文件
find . -iregex ".*config.*"             # 忽略大小写查找包含 config 的文件

# 使用通配符查找文件
find . -name "*.py"                      # 查找 Python 文件
find . -name "test_[0-9]*"               # 查找 test_ 开头后跟数字的文件
find . -name "[a-c]*.log"                # 查找 a-c 开头的日志文件
```

## [常见模式和模板](#常见模式和模板)

### [验证模式](#验证模式)

```
# 邮箱地址验证
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" emails.txt

# 电话号码验证（多种格式）
grep -E "(\+[0-9]{1,3}[- ]?)?[0-9]{3}[- ]?[0-9]{3}[- ]?[0-9]{4}$" phones.txt

# URL 验证
grep -E "^(https?:\/\/)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(\/[^\s]*)?$" urls.txt

# IP 地址验证
grep -E "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" ips.txt

# 日期格式验证（YYYY-MM-DD）
grep -E "^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$" dates.txt
```

### [提取模式](#提取模式)

```
# 提取 HTML 标签内容
grep -oE '<[^>]+>([^<]+)</[^>]+>' html_file.html | grep -oE '>[^<]+<' | sed 's/[><]//g'

# 提取 JSON 中的键值对
grep -oE '"[^"]+":\s*"[^"]*"' data.json

# 提取 Markdown 链接
grep -oE '\[([^\]]+)\]\([^)]+\)' markdown.md

# 提取代码中的函数调用
grep -oE '[a-zA-Z_][a-zA-Z0-9_]*\([^)]*\)' code.py
```

### [转换模式](#转换模式)

```
# 转换大小写
sed -E 's/([a-z])/\U\1/g' file.txt    # 转大写
sed -E 's/([A-Z])/\L\1/g' file.txt    # 转小写

# 标准化空白字符
sed -E 's/[[:space:]]+/ /g' file.txt  # 多个空白转为一个空格
sed -E 's/^[[:space:]]*//' file.txt    # 删除行首空白
sed -E 's/[[:space:]]*$//' file.txt    # 删除行尾空白

# 添加行号
sed -E '=' file.txt | sed -E 'N;s/\n/\t/'
```

## [性能优化建议](#性能优化建议)

### [正则表达式优化技巧](#正则表达式优化技巧)

1. **避免回溯**: 使用更具体的模式而不是 `.*`
2. **使用字符类**: `[0-9]` 比 `[0123456789]` 更高效
3. **避免贪婪匹配**: 在可能的情况下使用惰惰匹配
4. **使用锚点**: 使用 `^` 和 `$` 来限定匹配范围
5. **预编译正则**: 在脚本中重复使用时，预编译正则表达式

```
# 不好的正则表达式（可能导致性能问题）
grep -E ".*error.*" large_file.log    # 过于宽泛
grep -E "(a|b|c|d|e).*" file.txt      # 可以用 [a-e] 替代

# 好的正则表达式（更高效）
grep -E "^[0-9]{4}-[0-9]{2}-[0-9]{2}.*error" large_file.log
grep -E "[a-e].*" file.txt
```

### [通配符使用建议](#通配符使用建议)

1. **先测试再执行**: 使用 `ls` 测试通配符模式
2. **避免危险的通配符**: 谨慎使用 `rm *` 等危险命令
3. **使用引号**: 包含通配符的路径最好用引号括起来
4. **考虑 find**: 对于复杂的文件查找，使用 `find` 命令

```
# 危险的做法
rm *.log                    # 可能删除重要日志文件

# 安全的做法
ls *.log                    # 先查看匹配的文件
rm -i *.log                 # 交互式删除
find . -name "*.log" -mtime +30 -delete  # 更精确的控制
```

## [调试技巧](#调试技巧)

### [正则表达式调试](#正则表达式调试)

1. **逐步构建**: 从简单的模式开始，逐步添加复杂性
2. **使用测试工具**: 在线正则表达式测试工具很有帮助
3. **分解问题**: 将复杂的正则表达式分解为多个简单部分
4. **验证边界**: 测试边界情况和异常输入

```
# 调试步骤示例
# 第一步：测试基本模式
grep -E "error" log.txt

# 第二步：添加上下文
grep -E "error.*time" log.txt

# 第三步：添加精确匹配
grep -E "error.*time.*[0-9]{4}" log.txt

# 第四步：优化和完善
grep -E "error.*time.*[0-9]{4}-[0-9]{2}" log.txt
```

### [通配符调试](#通配符调试)

1. **使用 echo 测试**: 先用 echo 测试通配符展开结果
2. **使用 ls 验证**: 用 ls 查看实际匹配的文件
3. **使用 set -x**: 查看 Shell 如何展开通配符

```
# 测试通配符展开
echo *.txt                  # 查看会匹配哪些文件
ls file{1..3}.txt           # 验证花括号扩展

# 查看 Shell 展开过程
set -x
ls *.txt
set +x
```

## [学习资源](#学习资源)

### [推荐练习](#推荐练习)

1. **从简单开始**: 先掌握基础通配符和简单的正则表达式
2. **实际应用**: 在日常工作中主动使用这些工具
3. **阅读手册**: 使用 `man regex` 和 `man 7 glob` 查看详细文档
4. **在线资源**: 利用在线正则表达式测试工具进行练习

### [练习项目](#练习项目)

1. **日志分析器**: 创建一个脚本来分析系统日志
2. **文件重命名工具**: 批量重命名文件的工具
3. **配置文件验证器**: 验证配置文件格式的工具
4. **数据提取器**: 从文本中提取特定格式的数据

### [常见错误避免](#常见错误避免)

1. **混淆通配符和正则表达式**: 通配符用于文件名，正则表达式用于文本匹配
2. **忘记转义特殊字符**: 在正则表达式中需要转义 `.`、`*` 等字符
3. **过度使用贪婪匹配**: 导致匹配范围过大
4. **忽略大小写问题**: 在需要时使用 `-i` 选项

记住，正则表达式和通配符是强大的工具，但需要大量练习才能熟练掌握。从简单的模式开始，逐步构建复杂的表达式，在实际项目中应用这些技能，你会逐渐发现它们的强大威力。

掌握了这些模式匹配技术，你就拥有了在 Linux 命令行世界中处理文本和文件的"超能力"。无论是简单的文件管理还是复杂的文本处理，你都能够找到优雅而高效的解决方案。

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [附录A2｜正则表达式与通配符速查](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#附录a2-正则表达式与通配符速查)
- [通配符 (Wildcards)](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#通配符-wildcards)
- [基础通配符](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#基础通配符)
- [实际应用示例](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#实际应用示例)
- [花括号扩展](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#花括号扩展)
- [基础正则表达式 (BRE)](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#基础正则表达式-bre)
- [字符匹配](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#字符匹配)
- [特殊字符转义](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#特殊字符转义)
- [扩展正则表达式 (ERE)](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#扩展正则表达式-ere)
- [量词匹配](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#量词匹配)
- [分组和引用](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#分组和引用)
- [字符类别](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#字符类别)
- [高级正则表达式特性](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#高级正则表达式特性)
- [零宽断言](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#零宽断言)
- [贪婪与懒惰匹配](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#贪婪与懒惰匹配)
- [实际应用场景](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#实际应用场景)
- [日志分析](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#日志分析)
- [代码处理](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#代码处理)
- [配置文件处理](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#配置文件处理)
- [数据清洗](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#数据清洗)
- [工具特定的正则表达式语法](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#工具特定的正则表达式语法)
- [grep](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#grep)
- [sed](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#sed)
- [awk](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#awk)
- [find](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#find)
- [常见模式和模板](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#常见模式和模板)
- [验证模式](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#验证模式)
- [提取模式](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#提取模式)
- [转换模式](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#转换模式)
- [性能优化建议](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#性能优化建议)
- [正则表达式优化技巧](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#正则表达式优化技巧)
- [通配符使用建议](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#通配符使用建议)
- [调试技巧](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#调试技巧)
- [正则表达式调试](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#正则表达式调试)
- [通配符调试](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#通配符调试)
- [学习资源](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#学习资源)
- [推荐练习](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#推荐练习)
- [练习项目](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#练习项目)
- [常见错误避免](https://xiaolinnote.com/linux/appendix-a2-regex-wildcards.html#常见错误避免)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
