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
url: "https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html"
source: "https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html"
last_checked: 2026-05-17
freshness: watch
sha256: 37e98775ccc4b2e5bef9a25999b903edd5d1f6a255d1a54fb69de48af745ef2f
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
---

# 附录A0：Shell脚本简单入门

原始链接：https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- 暂无直接对应的现有概念卡；后续如果这类题目反复出现，可以考虑补一张概念卡或面试复盘页。

## 页面正文

# 附录A0：Shell脚本简单入门

[公众号@小林面试笔记](https://xiaolinnote.com)Linux大约 30 分钟约 9005 字2025/9/2

---

# [附录A0｜Shell脚本简单入门](#附录a0-shell脚本简单入门)

大家好，我是小林。

你有没有想过，为什么有些Linux管理员看起来总是那么高效？他们似乎能在几秒钟内完成复杂的任务，而其他人可能需要几分钟甚至几小时。他们的秘密武器是什么？

答案就是**Shell脚本**！

想象一下，Shell脚本就像是给你的Linux命令行装上了"自动化引擎"。它让你能够将一系列命令组合起来，创建可重复使用的程序，大大提高工作效率。就像从手动打字进化到了使用打印机一样，这是一个质的飞跃。

在本附录中，我将带你从零开始，一步步掌握Shell脚本的基础知识。无论你是完全的新手还是有一些经验，这里都有你需要的内容。

---

## [1. 第一个Shell脚本：Hello World](#_1-第一个shell脚本-hello-world)

Shell脚本到底是什么？又该如何开始呢？

Shell脚本本质上是一个包含一系列Linux命令的文本文件。当你运行这个脚本时，系统会按顺序执行其中的命令。

为什么不直接在命令行输入命令，而要用Shell脚本呢？

**想象一下这个场景**：你每天都需要备份重要文件，步骤包括：

1. 创建备份目录
2. 复制文件到备份目录
3. 添加时间戳
4. 检查是否成功

如果每天都手动输入这些命令，不仅繁琐，还容易出错。而Shell脚本可以将这些步骤自动化，一次编写，重复使用！

让我们创建你的第一个Shell脚本：

```
# 创建脚本文件
$ nano hello.sh

# 输入以下内容
#!/bin/bash
# 这是我的第一个Shell脚本
echo "Hello, World!"
echo "当前用户：$(whoami)"
echo "当前时间：$(date)"
echo "脚本执行完成"
```

为什么第一行是 `#!/bin/bash` 而不是直接开始写命令？

`#!/bin/bash` 被称为 **shebang**，它告诉系统：

- 用哪个解释器来执行这个脚本（这里是Bash）
- 这个脚本的"语言"是什么

就像你在文件开头标注"中文文档"或"English Document"一样，让系统知道如何"阅读"这个文件。

**保存文件后，给脚本添加执行权限：**

```
$ chmod +x hello.sh
```

为什么要给脚本执行权限？不能直接运行吗？

在Linux系统中，每个文件都有权限控制。默认情况下，新创建的文本文件只有读写权限，没有执行权限。`chmod +x` 命令就是给文件添加"可执行"权限，就像给一个人颁发"许可证"，允许它作为程序运行。

**现在运行你的第一个脚本：**

```
$ ./hello.sh
# 输出
Hello, World!
当前用户：xiaolin
当前时间：2025年 09月 02日 星期二 10:30:45 CST
脚本执行完成
```

**让我们深入分析这个脚本**：

```
#!/bin/bash                    # 解释器声明：告诉系统用Bash运行
# 这是我的第一个Shell脚本      # 注释：给人看的说明，计算机忽略
echo "Hello, World!"          # 输出字符串
echo "当前用户：$(whoami)"     # 输出当前用户名
echo "当前时间：$(date)"       # 输出当前时间
echo "脚本执行完成"            # 输出完成信息
```

注意到 `$(whoami)` 和 `$(date)` 这两个命令有什么特别之处吗？

这叫做 **命令替换**！它的作用是：

- 先执行括号里的命令（whoami或date）
- 将命令的输出结果替换到原位置
- echo命令会输出这个结果

比如 `echo "当前用户：$(whoami)"` 实际上变成了：

1. 执行 `whoami` → 输出 "xiaolin"
2. 将结果替换 → `echo "当前用户：xiaolin"`
3. 执行echo → 输出 "当前用户：xiaolin"

如果不使用命令替换，我们如何实现同样的效果？

```
# 方法一：先执行命令，再输出（需要两步）
whoami > temp.txt    # 将结果存入临时文件
echo "当前用户：$(cat temp.txt)"  # 读取并输出
rm temp.txt          # 删除临时文件

# 方法二：使用变量（也是两步）
current_user=$(whoami)  # 先存入变量
echo "当前用户：$current_user"  # 再输出变量
```

看到了吗？命令替换让我们能够在一行内完成这个操作，代码更简洁，也更高效！

**小练习**：试着修改这个脚本，添加更多有用的信息，比如：

- 当前目录路径
- 系统运行时间
- 内存使用情况

提示：可以使用 `pwd`、`uptime`、`free -h` 等命令。

---

## [2. 变量：脚本的记忆单元](#_2-变量-脚本的记忆单元)

如何在脚本中存储和使用数据呢？

变量是脚本的"记忆单元"，让你能够存储文本、数字或其他数据，并在需要时使用它们。

为什么需要变量？直接在命令中写死值不是更简单吗？

让我们看一个实际的例子。假设你要写一个脚本来处理不同的用户：

```
# 不使用变量的方式（不推荐）
echo "用户 xiaolin 的家目录是 /home/xiaolin"
echo "用户 xiaolin 的配置文件是 /home/xiaolin/.config"
echo "用户 xiaolin 的日志文件是 /var/log/xiaolin.log"
```

如果现在要处理用户 "zhangsan"，你需要修改每一行！但如果使用变量：

```
# 使用变量的方式（推荐）
username="xiaolin"
echo "用户 $username 的家目录是 /home/$username"
echo "用户 $username 的配置文件是 /home/$username/.config"
echo "用户 $username 的日志文件是 /var/log/$username.log"
```

现在只需要修改第一行，所有相关的行都会自动更新！这就是变量的威力。

### [基本变量操作](#基本变量操作)

```
#!/bin/bash
# 变量示例脚本

# 定义变量（注意：等号两边不能有空格）
name="小明"
age=25
city="北京"

# 使用变量（使用$符号）
echo "姓名：$name"
echo "年龄：$age"
echo "城市：$city"

# 变量拼接
greeting="你好，$name！欢迎来到$city"
echo "$greeting"

# 数学运算
echo "明年年龄：$((age + 1))岁"
```

为什么变量定义时等号两边不能有空格？

这是一个很常见的错误！在Shell脚本中：

- `name="小明"` ✅ 正确
- `name = "小明"` ❌ 错误（会被当作命令执行）

为什么呢？因为Shell脚本的设计哲学是"一切都是命令"。当你写 `name = "小明"` 时，Shell会认为：

1. `name` 是一个命令
2. `=` 是第一个参数
3. `"小明"` 是第二个参数

这显然不是我们想要的。所以记住：**变量定义时，等号两边绝对不能有空格**！

### [特殊变量](#特殊变量)

Shell提供了一些特殊的变量，它们包含了有用的信息：

```
#!/bin/bash
# 特殊变量示例

echo "脚本名称：$0"
echo "第一个参数：$1"
echo "第二个参数：$2"
echo "所有参数：$*"
echo "参数个数：$#"
echo "当前进程ID：$$"

# 测试脚本
# 保存为 special.sh
# 运行：./special.sh 苹果 香蕉
```

这些特殊变量有什么实际用途呢？

让我们看一个实际的应用场景：

```
#!/bin/bash
# 文件备份脚本

# 检查是否提供了参数
if [ $# -eq 0 ]; then
    echo "用法：$0 <文件名>"
    echo "示例：$0 important.txt"
    exit 1
fi

# 获取文件名参数
source_file="$1"

# 检查文件是否存在
if [ ! -f "$source_file" ]; then
    echo "错误：文件不存在：$source_file"
    exit 1
fi

# 创建备份
backup_file="${source_file}.backup_$(date +%Y%m%d)"
cp "$source_file" "$backup_file"

echo "✓ 已备份：$source_file → $backup_file"
echo "备份时间：$(date)"
echo "操作进程：$$"
```

这个脚本展示了特殊变量的实际用途：

- `$0`：显示脚本名称，帮助用户正确使用
- `$#`：检查参数个数，确保用户提供了必要的参数
- `$1`：获取用户输入的文件名
- `$$`：记录进程ID，便于调试和管理

### [环境变量](#环境变量)

系统预定义了一些环境变量，你可以在脚本中使用它们：

```
#!/bin/bash
# 环境变量示例

echo "当前用户：$USER"
echo "家目录：$HOME"
echo "当前路径：$PWD"
echo "Shell类型：$SHELL"
echo "主机名：$HOSTNAME"
```

环境变量和普通变量有什么区别？

好问题！主要区别在于：

1. **作用范围**：

   - 普通变量：只在当前脚本中有效
   - 环境变量：在整个系统中有效，可以传递给子进程
2. **定义方式**：

   - 普通变量：`name="value"`
   - 环境变量：`export NAME="value"`
3. **查看方式**：

   - 普通变量：`set | grep name`
   - 环境变量：`env | grep NAME`

**实际应用示例**：

```
#!/bin/bash
# 环境变量实际应用

# 设置临时环境变量（只在脚本运行期间有效）
export BACKUP_DIR="/tmp/backups"
export LOG_LEVEL="DEBUG"

# 创建临时工作目录
work_dir="$HOME/temp_work_$$"
mkdir -p "$work_dir"

echo "工作目录：$work_dir"
echo "备份目录：$BACKUP_DIR"
echo "日志级别：$LOG_LEVEL"

# 清理函数
cleanup() {
    echo "清理临时目录：$work_dir"
    rm -rf "$work_dir"
    echo "清理完成"
}

# 注册清理函数（脚本退出时执行）
trap cleanup EXIT

echo "脚本开始执行..."
# 这里可以添加主要逻辑
echo "脚本执行完成"
```

**小练习**：

1. 创建一个脚本，接收用户名作为参数，显示该用户的家目录、Shell类型等信息
2. 修改脚本，如果用户不存在，提示错误并退出
3. 添加环境变量来控制输出格式（比如详细模式或简洁模式）

---

## [3. 条件判断：让脚本更智能](#_3-条件判断-让脚本更智能)

如何让脚本根据不同情况执行不同的操作？

条件判断让脚本能够"思考"和"决策"，这是编程的核心概念之一。

为什么需要条件判断？直接按顺序执行命令不是更简单吗？

让我们看一个真实的场景。假设你要写一个系统维护脚本：

```
# 没有条件判断的脚本（有问题）
rm -rf /tmp/old_files/*        # 删除旧文件
systemctl restart nginx        # 重启服务
echo "维护完成"
```

这个脚本有什么问题？

- 如果`/tmp/old_files/`目录不存在，`rm`命令会报错
- 如果nginx服务没有安装，`systemctl restart`会失败
- 不管前面的命令是否成功，都会显示"维护完成"

这就是为什么我们需要条件判断！

### [if语句基础](#if语句基础)

```
#!/bin/bash
# if语句示例

echo "请输入你的年龄："
read age

if [ $age -ge 18 ]; then
    echo "你已经成年了！"
    echo "可以投票和开车"
elif [ $age -ge 13 ]; then
    echo "你是青少年"
else
    echo "你还是个孩子"
fi
```

`[ $age -ge 18 ]` 这个语法是什么意思？

这是Shell脚本中的条件测试语法，让我们分解一下：

- `[` 和 `]`：实际上是 `test` 命令的另一种写法
- `$age`：变量的值
- `-ge`：比较运算符，意思是 "greater than or equal to"（大于等于）

所以 `[ $age -ge 18 ]` 实际上等同于 `test $age -ge 18`。

**常见的比较运算符**：

```
# 数值比较
-eq  # 等于 (equal)
-ne  # 不等于 (not equal)
-gt  # 大于 (greater than)
-lt  # 小于 (less than)
-ge  # 大于等于 (greater than or equal)
-le  # 小于等于 (less than or equal)

# 字符串比较
=    # 等于
!=   # 不等于
-z   # 字符串为空
-n   # 字符串不为空

# 文件测试
-f   # 文件存在且是普通文件
-d   # 目录存在
-r   # 文件可读
-w   # 文件可写
-x   # 文件可执行
-s   # 文件大小不为零
```

### [常用条件测试](#常用条件测试)

```
#!/bin/bash
# 条件测试示例

# 数值比较
num1=10
num2=20

if [ $num1 -eq $num2 ]; then
    echo "数字相等"
elif [ $num1 -lt $num2 ]; then
    echo "num1 小于 num2"
else
    echo "num1 大于 num2"
fi

# 字符串比较
str1="hello"
str2="world"

if [ "$str1" = "$str2" ]; then
    echo "字符串相同"
else
    echo "字符串不同"
fi

# 文件测试
filename="test.txt"

if [ -f "$filename" ]; then
    echo "文件存在"
    if [ -r "$filename" ]; then
        echo "文件可读"
    fi
    if [ -w "$filename" ]; then
        echo "文件可写"
    fi
else
    echo "文件不存在"
    touch "$filename"
    echo "已创建文件：$filename"
fi
```

为什么字符串比较时，变量要用双引号括起来？

这是一个非常重要的安全实践！让我们看看不使用引号会发生什么：

```
# 危险的写法
name="小明 张"
if [ $name = "小明 张" ]; then  # 这里会出错！
    echo "姓名匹配"
fi
```

Shell会把 `小明 张` 拆分成两个参数，导致语法错误。但使用双引号：

```
# 安全的写法
name="小明 张"
if [ "$name" = "小明 张" ]; then  # 正确！
    echo "姓名匹配"
fi
```

**记住这个黄金法则**：在Shell脚本中，**变量替换时总是使用双引号**，除非你有特别的理由不这样做。

### [case语句](#case语句)

当需要检查多个条件时，case语句比多个if语句更清晰：

```
#!/bin/bash
# case语句示例

echo "请选择操作："
echo "1) 启动服务"
echo "2) 停止服务"
echo "3) 重启服务"
echo "4) 查看状态"
read -p "请输入选项(1-4): " choice

case $choice in
    1)
        echo "正在启动服务..."
        systemctl start nginx
        ;;
    2)
        echo "正在停止服务..."
        systemctl stop nginx
        ;;
    3)
        echo "正在重启服务..."
        systemctl restart nginx
        ;;
    4)
        echo "服务状态："
        systemctl status nginx
        ;;
    *)
        echo "无效选项"
        exit 1
        ;;
esac
```

case语句和if-elif有什么区别？什么时候用哪个？

**case语句的优势**：

- 语法更简洁，特别适合匹配固定值
- 支持通配符匹配
- 可读性更好，像菜单一样清晰

**if-elif的优势**：

- 支持复杂的条件判断
- 可以使用不同的比较运算符
- 更灵活，适合逻辑判断

**选择建议**：

- 如果是菜单选择或模式匹配 → 用case
- 如果是复杂的逻辑判断 → 用if-elif

### [实际应用示例](#实际应用示例)

让我们看一个更复杂的实际应用：

```
#!/bin/bash
# 系统健康检查脚本

# 获取系统信息
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
memory_usage=$(free | grep Mem | awk '{printf "%.2f", $3/$2 * 100.0}')
disk_usage=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)

echo "=== 系统健康检查报告 ==="
echo "检查时间：$(date)"
echo ""

# 检查CPU使用率
if (( $(echo "$cpu_usage > 80" | bc -l) )); then
    echo "⚠️  CPU使用率过高：${cpu_usage}%"
    echo "   建议检查是否有异常进程"
elif (( $(echo "$cpu_usage > 60" | bc -l) )); then
    echo "⚠️  CPU使用率偏高：${cpu_usage}%"
    echo "   建议监控系统负载"
else
    echo "✅ CPU使用率正常：${cpu_usage}%"
fi

# 检查内存使用率
if (( $(echo "$memory_usage > 90" | bc -l) )); then
    echo "⚠️  内存使用率过高：${memory_usage}%"
    echo "   建议清理内存或增加内存"
elif (( $(echo "$memory_usage > 70" | bc -l) )); then
    echo "⚠️  内存使用率偏高：${memory_usage}%"
    echo "   建议监控内存使用情况"
else
    echo "✅ 内存使用率正常：${memory_usage}%"
fi

# 检查磁盘使用率
if [ $disk_usage -gt 90 ]; then
    echo "⚠️  磁盘使用率过高：${disk_usage}%"
    echo "   建议清理磁盘空间"
elif [ $disk_usage -gt 80 ]; then
    echo "⚠️  磁盘使用率偏高：${disk_usage}%"
    echo "   建议监控磁盘使用情况"
else
    echo "✅ 磁盘使用率正常：${disk_usage}%"
fi

echo ""
echo "=== 检查完成 ==="
```

这个脚本展示了条件判断在实际工作中的应用：

- 使用数值比较检查系统资源使用率
- 使用不同级别的警告阈值
- 提供具体的建议和解决方案

**小练习**：

1. 创建一个脚本，检查用户输入的文件扩展名，并根据扩展名执行不同的操作
2. 写一个脚本来监控日志文件，当发现错误时发送邮件通知
3. 创建一个用户管理脚本，可以添加、删除、修改用户信息

---

## [4. 循环：重复执行任务](#_4-循环-重复执行任务)

如何让脚本重复执行某些操作？

循环是编程中的另一个重要概念，它让你能够重复执行代码块。

为什么需要循环？手动重复执行命令不也可以吗？

让我们看一个真实的场景。假设你需要处理100个文件：

```
# 没有循环的方式（痛苦）
mv file1.txt processed/file1.txt
mv file2.txt processed/file2.txt
mv file3.txt processed/file3.txt
# ... 继续写97行类似的代码
```

这不仅枯燥乏味，而且容易出错。但使用循环：

```
# 使用循环的方式（优雅）
for i in {1..100}; do
    mv "file${i}.txt" "processed/file${i}.txt"
done
```

看到了吗？3行代码替代了100行代码！这就是循环的威力。

### [for循环](#for循环)

```
#!/bin/bash
# for循环示例

# 循环数字
echo "倒计时开始："
for i in {5..1}; do
    echo "$i..."
    sleep 1
done
echo "发射！"

# 循环文件
echo "当前目录的文件："
for file in *; do
    if [ -f "$file" ]; then
        echo "文件：$file"
    fi
done

# C风格for循环
echo "计算1到10的和："
sum=0
for ((i=1; i<=10; i++)); do
    sum=$((sum + i))
done
echo "总和：$sum"
```

`for i in {1..5}` 和 `for ((i=1; i<=5; i++))` 有什么区别？

这是Shell脚本中两种常见的for循环语法：

**Bash风格的for循环**：

```
for i in {1..5}; do
    echo "数字：$i"
done
```

- 语法简单直观
- 适用于遍历固定的列表
- 支持通配符和文件列表

**C风格的for循环**：

```
for ((i=1; i<=5; i++)); do
    echo "数字：$i"
done
```

- 语法类似C语言
- 适合复杂的循环条件
- 支持递增、递减、步长等

**选择建议**：

- 遍历文件、固定列表 → 用Bash风格
- 复杂的数值循环 → 用C风格

### [while循环](#while循环)

```
#!/bin/bash
# while循环示例

# 简单计数器
count=1
while [ $count -le 5 ]; do
    echo "计数：$count"
    count=$((count + 1))
done

# 读取文件行
echo "读取/etc/os-release内容："
while IFS= read -r line; do
    echo "行：$line"
done < /etc/os-release

# 无限循环（按Ctrl+C退出）
echo "按Ctrl+C退出"
while true; do
    echo "当前时间：$(date +%H:%M:%S)"
    sleep 1
done
```

`while IFS= read -r line` 这行代码有什么特别之处？

这是一个很重要的文件读取模式，让我们分解一下：

- `IFS=`：设置Internal Field Separator为空，防止行首尾的空格被去掉
- `read -r`：-r选项防止反斜杠被转义
- `line`：将读取的行存入line变量

为什么要这样做？看这个例子：

```
# 创建测试文件
cat > test.txt << 'EOF'
  这行前面有空格
这行有"引号"
这行有\反斜杠
EOF

# 不安全的方式
while read line; do
    echo "读取到：$line"
done < test.txt

# 安全的方式
while IFS= read -r line; do
    echo "读取到：$line"
done < test.txt
```

你会发现，安全的方式能够正确保留行的原始格式，包括空格、引号和反斜杠。

### [循环的实际应用](#循环的实际应用)

让我们看一个更实际的例子：批量重命名文件

```
#!/bin/bash
# 批量文件重命名脚本

# 检查参数
if [ $# -eq 0 ]; then
    echo "用法：$0 <目录> <旧扩展名> <新扩展名>"
    echo "示例：$0 ./txt txt md"
    exit 1
fi

target_dir="$1"
old_ext="$2"
new_ext="$3"

# 检查目录是否存在
if [ ! -d "$target_dir" ]; then
    echo "错误：目录不存在：$target_dir"
    exit 1
fi

# 统计需要处理的文件数量
count=0
for file in "$target_dir"/*."$old_ext; do
    if [ -f "$file" ]; then
        ((count++))
    fi
done

if [ $count -eq 0 ]; then
    echo "没有找到 .$old_ext 扩展名的文件"
    exit 0
fi

echo "找到 $count 个 .$old_ext 文件"
echo "准备将扩展名改为 .$new_ext"
echo ""

# 确认操作
read -p "继续吗？(y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "操作已取消"
    exit 0
fi

# 执行重命名
success=0
failed=0

for file in "$target_dir"/*."$old_ext; do
    if [ -f "$file" ]; then
        # 构造新文件名
        filename=$(basename "$file")
        new_filename="${filename%.$old_ext}.$new_ext"
        new_file="$target_dir/$new_filename"
        
        # 执行重命名
        if mv "$file" "$new_file"; then
            echo "✓ 重命名：$filename → $new_filename"
            ((success++))
        else
            echo "✗ 重命名失败：$filename"
            ((failed++))
        fi
    fi
done

echo ""
echo "=== 重命名完成 ==="
echo "成功：$success 个文件"
echo "失败：$failed 个文件"
```

这个脚本展示了循环在实际工作中的应用：

- 使用循环遍历文件
- 条件判断和错误处理
- 用户交互和确认
- 统计和报告结果

**循环的最佳实践**：

1. **避免无限循环**：总是确保循环有退出条件
2. **处理空文件**：循环可能不执行，要考虑这种情况
3. **错误处理**：循环中的错误要适当处理
4. **性能考虑**：大量文件时，考虑优化循环

**小练习**：

1. 创建一个脚本，监控某个目录，当有新文件时自动处理
2. 写一个脚本，批量调整图片大小
3. 创建一个进度条显示功能

---

## [5. 函数：代码的重用模块](#_5-函数-代码的重用模块)

如何避免重复编写相同的代码？

函数让你能够将代码块组织成可重用的模块，提高代码的可维护性。

什么是函数？为什么要用函数？

让我们看一个实际的例子。假设你要在脚本的多个地方检查文件是否存在：

```
# 不使用函数的方式（重复代码）
if [ ! -f "/etc/config.conf" ]; then
    echo "配置文件不存在"
    exit 1
fi

# ... 很多代码之后 ...

if [ ! -f "/tmp/lockfile" ]; then
    echo "锁文件不存在"
    exit 1
fi

# ... 更多代码之后 ...

if [ ! -f "/var/log/app.log" ]; then
    echo "日志文件不存在"
    exit 1
fi
```

这种代码重复不仅难看，而且难以维护。如果以后要修改检查逻辑，需要修改多个地方。但使用函数：

```
# 使用函数的方式（代码复用）
check_file() {
    local filename="$1"
    local description="$2"
    
    if [ ! -f "$filename" ]; then
        echo "错误：$description 不存在：$filename"
        exit 1
    fi
    echo "✓ $description 存在：$filename"
}

# 使用函数
check_file "/etc/config.conf" "配置文件"
check_file "/tmp/lockfile" "锁文件"
check_file "/var/log/app.log" "日志文件"
```

现在代码更清晰，更容易维护，而且可以复用！

### [基本函数定义和使用](#基本函数定义和使用)

```
#!/bin/bash
# 函数示例

# 定义函数
show_welcome() {
    echo "================================"
    echo "      欢迎使用系统管理工具"
    echo "================================"
}

# 带参数的函数
check_file() {
    filename=$1
    if [ -f "$filename" ]; then
        echo "✓ 文件存在：$filename"
        return 0
    else
        echo "✗ 文件不存在：$filename"
        return 1
    fi
}

# 带返回值的函数
calculate_sum() {
    local result=$(( $1 + $2 ))
    echo $result
}

# 主程序
show_welcome

# 测试文件检查函数
check_file "/etc/passwd"
check_file "/nonexistent/file"

# 测试计算函数
num1=10
num2=20
sum=$(calculate_sum $num1 $num2)
echo "$num1 + $num2 = $sum"
```

函数中的 `local` 关键字是什么意思？

`local` 用于定义局部变量，这是函数编程中的一个重要概念：

```
# 局部变量示例
test_function() {
    local local_var="我是局部变量"
    global_var="我是全局变量"
    echo "函数内部：$local_var"
    echo "函数内部：$global_var"
}

# 调用函数
test_function

# 尝试访问变量
echo "函数外部：$local_var"    # 这行会出错，局部变量在函数外部不可见
echo "函数外部：$global_var"    # 这行正常，全局变量可以在函数外部访问
```

为什么需要局部变量？

1. **避免命名冲突**：防止不同函数之间的变量互相干扰
2. **内存管理**：局部变量在函数结束时自动销毁
3. **代码清晰**：明确变量的作用范围

### [函数的高级用法](#函数的高级用法)

```
#!/bin/bash
# 高级函数示例

# 带默认参数的函数
backup_file() {
    local source_file=${1:-"default.txt"}
    local backup_dir=${2:-"./backup"}
    
    # 创建备份目录
    mkdir -p "$backup_dir"
    
    # 生成备份文件名
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="$backup_dir/$(basename $source_file).backup_$timestamp"
    
    # 执行备份
    if cp "$source_file" "$backup_file" 2>/dev/null; then
        echo "✓ 备份成功：$backup_file"
        return 0
    else
        echo "✗ 备份失败：$source_file"
        return 1
    fi
}

# 批量处理函数
process_files() {
    local directory=$1
    local operation=$2
    
    if [ ! -d "$directory" ]; then
        echo "错误：目录不存在：$directory"
        return 1
    fi
    
    case $operation in
        "list")
            echo "目录 $directory 中的文件："
            ls -la "$directory"
            ;;
        "count")
            local count=$(find "$directory" -type f | wc -l)
            echo "文件数量：$count"
            ;;
        "size")
            local size=$(du -sh "$directory" | cut -f1)
            echo "目录大小：$size"
            ;;
        *)
            echo "错误：不支持的操作：$operation"
            echo "支持的操作：list, count, size"
            return 1
            ;;
    esac
}

# 使用示例
backup_file "/etc/passwd" "./backup"
process_files "/var/log" "count"
```

`${1:-"default.txt"}` 这种语法是什么意思？

这是Shell脚本中的**参数扩展**语法，用于设置默认值：

```
# 默认值设置
${parameter:-default_word}
# 如果parameter未设置或为空，则使用default_word

# 示例
name=""
echo "姓名：${name:-"未知"}"    # 输出：姓名：未知

name="小明"
echo "姓名：${name:-"未知"}"    # 输出：姓名：小明
```

还有其他有用的参数扩展：

```
# 如果变量未设置，则报错
${parameter:?错误信息}

# 如果变量未设置，则使用默认值并赋值给变量
${parameter:=default_value}

# 获取变量长度
${#parameter}

# 提取子字符串
${parameter:offset:length}
```

### [函数的实际应用](#函数的实际应用)

让我们看一个更复杂的实际应用：系统监控脚本

```
#!/bin/bash
# 系统监控脚本

# 配置变量
LOG_FILE="/tmp/system_monitor.log"
ALERT_THRESHOLD=80
MAX_LOG_SIZE=1048576  # 1MB

# 日志函数
log_message() {
    local level=$1
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

# 检查日志文件大小
check_log_size() {
    if [ -f "$LOG_FILE" ] && [ $(stat -c%s "$LOG_FILE") -gt $MAX_LOG_SIZE ]; then
        log_message "INFO" "日志文件过大，进行轮转"
        mv "$LOG_FILE" "${LOG_FILE}.old"
        touch "$LOG_FILE"
    fi
}

# 获取CPU使用率
get_cpu_usage() {
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
    echo "$cpu_usage"
}

# 获取内存使用率
get_memory_usage() {
    local memory_usage=$(free | grep Mem | awk '{printf "%.2f", $3/$2 * 100.0}')
    echo "$memory_usage"
}

# 获取磁盘使用率
get_disk_usage() {
    local disk_usage=$(df -h / | awk 'NR==2 {print $5}' | cut -d'%' -f1)
    echo "$disk_usage"
}

# 发送警报
send_alert() {
    local component=$1
    local usage=$2
    local threshold=$3
    
    log_message "ALERT" "$component 使用率过高：${usage}% (阈值：${threshold}%)"
    
    # 这里可以添加发送邮件或短信的代码
    echo "警报：$component 使用率 ${usage}% 超过阈值 ${threshold}%"
}

# 主监控函数
monitor_system() {
    log_message "INFO" "开始系统监控"
    
    # 检查CPU
    local cpu_usage=$(get_cpu_usage)
    log_message "INFO" "CPU使用率：${cpu_usage}%"
    
    if (( $(echo "$cpu_usage > $ALERT_THRESHOLD" | bc -l) )); then
        send_alert "CPU" "$cpu_usage" "$ALERT_THRESHOLD"
    fi
    
    # 检查内存
    local memory_usage=$(get_memory_usage)
    log_message "INFO" "内存使用率：${memory_usage}%"
    
    if (( $(echo "$memory_usage > $ALERT_THRESHOLD" | bc -l) )); then
        send_alert "内存" "$memory_usage" "$ALERT_THRESHOLD"
    fi
    
    # 检查磁盘
    local disk_usage=$(get_disk_usage)
    log_message "INFO" "磁盘使用率：${disk_usage}%"
    
    if [ $disk_usage -gt $ALERT_THRESHOLD ]; then
        send_alert "磁盘" "$disk_usage" "$ALERT_THRESHOLD"
    fi
    
    log_message "INFO" "系统监控完成"
}

# 清理函数
cleanup() {
    log_message "INFO" "脚本正常退出"
}

# 错误处理
handle_error() {
    local exit_code=$?
    log_message "ERROR" "脚本执行失败，退出码：$exit_code"
    exit $exit_code
}

# 信号处理
trap handle_error ERR INT TERM
trap cleanup EXIT

# 主程序
check_log_size
monitor_system
```

这个脚本展示了函数在实际项目中的应用：

- 模块化设计，每个功能都有专门的函数
- 配置与逻辑分离
- 错误处理和日志记录
- 可维护性和可扩展性

**函数的最佳实践**：

1. **单一职责**：每个函数只做一件事
2. **清晰的命名**：函数名要表达其功能
3. **参数验证**：检查输入参数的有效性
4. **错误处理**：适当的错误处理和返回值
5. **文档注释**：为复杂函数添加说明注释

**小练习**：

1. 创建一个函数库，包含常用的文件操作函数
2. 写一个带缓存的函数，避免重复计算
3. 创建一个递归函数，实现目录树的遍历

---

## [6. 实用脚本示例](#_6-实用脚本示例)

### [系统信息收集脚本](#系统信息收集脚本)

```
#!/bin/bash
# 系统信息收集脚本

# 函数：显示系统信息
show_system_info() {
    echo "=== 系统基本信息 ==="
    echo "操作系统：$(cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2 | tr -d '\"')"
    echo "内核版本：$(uname -r)"
    echo "架构：$(uname -m)"
    echo "主机名：$(hostname)"
    echo "运行时间：$(uptime -p)"
    echo ""
}

# 函数：显示硬件信息
show_hardware_info() {
    echo "=== 硬件信息 ==="
    echo "CPU信息：$(lscpu | grep 'Model name' | cut -d: -f2 | xargs)"
    echo "CPU核心数：$(nproc)"
    echo "内存总量：$(free -h | grep Mem | awk '{print $2}')"
    echo "磁盘使用情况："
    df -h | grep -E "^/dev/"
    echo ""
}

# 函数：显示网络信息
show_network_info() {
    echo "=== 网络信息 ==="
    echo "IP地址："
    ip addr show | grep -E "inet.*scope global" | awk '{print "  " $2}'
    echo "默认网关："
    ip route show default | awk '{print "  " $3}'
    echo ""
}

# 主程序
echo "系统信息收集报告"
echo "生成时间：$(date)"
echo "================================"
echo ""

show_system_info
show_hardware_info
show_network_info

echo "信息收集完成"
```

这个脚本看起来很简单，有什么特别之处吗？

这个脚本虽然简单，但展示了几个重要的设计原则：

1. **模块化设计**：每个功能都封装在独立的函数中
2. **清晰的输出格式**：使用标题和分隔线，让输出更易读
3. **错误容忍**：即使某个命令失败，脚本也会继续执行
4. **可扩展性**：可以很容易地添加新的信息收集函数

### [日志分析脚本](#日志分析脚本)

```
#!/bin/bash
# 日志分析脚本

LOG_FILE=${1:-"/var/log/syslog"}

if [ ! -f "$LOG_FILE" ]; then
    echo "错误：日志文件不存在：$LOG_FILE"
    exit 1
fi

echo "=== 日志分析报告 ==="
echo "日志文件：$LOG_FILE"
echo "分析时间：$(date)"
echo ""

# 分析错误信息
echo "=== 错误信息统计 ==="
error_count=$(grep -i "error" "$LOG_FILE" | wc -l)
echo "错误总数：$error_count"

if [ $error_count -gt 0 ]; then
    echo "最近5个错误："
    grep -i "error" "$LOG_FILE" | tail -5 | while read line; do
        echo "  $line"
    done
fi
echo ""

# 分析警告信息
echo "=== 警告信息统计 ==="
warning_count=$(grep -i "warning" "$LOG_FILE" | wc -l)
echo "警告总数：$warning_count"
echo ""

# 分析访问最多的IP（如果是访问日志）
if echo "$LOG_FILE" | grep -q "access"; then
    echo "=== 访问统计 ==="
    echo "访问最多的IP："
    awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -5 | \
        while read count ip; do
            echo "  $ip: $count 次"
        done
    echo ""
fi

# 分析最近的活动
echo "=== 最近活动 ==="
echo "最后10行日志："
tail -10 "$LOG_FILE" | while read line; do
    echo "  $line"
done
```

这个脚本有什么实际用途？

这个日志分析脚本在实际工作中非常有用：

1. **快速故障排查**：快速查看日志中的错误和警告
2. **安全监控**：分析异常访问模式
3. **性能分析**：了解系统负载和访问模式
4. **趋势分析**：定期运行，比较不同时间的结果

### [备份脚本](#备份脚本)

```
#!/bin/bash
# 自动备份脚本

# 配置
SOURCE_DIR="/home/$USER/projects"
BACKUP_DIR="/backup/$(date +%Y%m%d)"
MAX_BACKUPS=7
LOG_FILE="/var/log/backup.log"

# 日志函数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 检查源目录
check_source() {
    if [ ! -d "$SOURCE_DIR" ]; then
        log "错误：源目录不存在：$SOURCE_DIR"
        exit 1
    fi
    log "源目录检查通过：$SOURCE_DIR"
}

# 创建备份目录
create_backup_dir() {
    mkdir -p "$BACKUP_DIR"
    log "创建备份目录：$BACKUP_DIR"
}

# 执行备份
perform_backup() {
    log "开始备份..."
    
    # 备份文件
    tar -czf "$BACKUP_DIR/files_backup.tar.gz" \
        --exclude="*.tmp" \
        --exclude="*.log" \
        --exclude="node_modules" \
        --exclude=".git" \
        "$SOURCE_DIR" 2>/dev/null
    
    if [ $? -eq 0 ]; then
        log "文件备份成功"
    else
        log "文件备份失败"
        return 1
    fi
    
    # 备份配置文件
    if [ -d "/etc/$USER" ]; then
        tar -czf "$BACKUP_DIR/config_backup.tar.gz" "/etc/$USER" 2>/dev/null
        log "配置文件备份完成"
    fi
    
    # 创建备份清单
    cat > "$BACKUP_DIR/backup_manifest.txt" << EOF
备份时间：$(date)
备份源：$SOURCE_DIR
备份内容：
- files_backup.tar.gz: 项目文件备份
- config_backup.tar.gz: 配置文件备份
排除的文件和目录：
- *.tmp 临时文件
- *.log 日志文件
- node_modules Node.js依赖
- .git Git版本控制目录
EOF
    
    log "备份清单已创建"
}

# 清理旧备份
cleanup_old_backups() {
    log "清理旧备份..."
    
    # 找到并删除超过保留数量的备份
    cd "$(dirname "$BACKUP_DIR")"
    ls -t | tail -n +$(($MAX_BACKUPS + 1)) | while read backup; do
        if [ -d "$backup" ]; then
            rm -rf "$backup"
            log "删除旧备份：$backup"
        fi
    done
}

# 验证备份
verify_backup() {
    log "验证备份完整性..."
    
    # 检查备份文件是否存在
    if [ ! -f "$BACKUP_DIR/files_backup.tar.gz" ]; then
        log "错误：文件备份不存在"
        return 1
    fi
    
    # 检查备份文件是否完整
    if ! tar -tzf "$BACKUP_DIR/files_backup.tar.gz" >/dev/null 2>&1; then
        log "错误：文件备份损坏"
        return 1
    fi
    
    # 计算备份大小
    backup_size=$(du -sh "$BACKUP_DIR" | cut -f1)
    log "备份验证成功，大小：$backup_size"
}

# 主函数
main() {
    log "=== 开始备份过程 ==="
    
    check_source
    create_backup_dir
    perform_backup
    verify_backup
    cleanup_old_backups
    
    log "=== 备份过程完成 ==="
    log "备份位置：$BACKUP_DIR"
}

# 错误处理
handle_error() {
    log "备份过程中发生错误"
    exit 1
}

trap handle_error ERR

# 执行主函数
main "$@"
```

这个备份脚本有什么特别之处？

这个脚本展示了专业级备份脚本的多个重要特性：

1. **完整的错误处理**：每个步骤都有错误检查
2. **详细的日志记录**：所有操作都有日志记录
3. **智能的文件排除**：排除不需要备份的文件
4. **备份轮转**：自动清理旧备份，节省磁盘空间
5. **备份验证**：验证备份的完整性
6. **清单生成**：创建备份清单，便于管理

---

## [7. 调试和最佳实践](#_7-调试和最佳实践)

### [调试技巧](#调试技巧)

```
#!/bin/bash
# 调试示例脚本

# 启用调试模式（取消注释以启用）
# set -x  # 显示执行的每个命令
# set -e  # 遇到错误立即退出
# set -u  # 使用未定义变量时报错

# 函数：安全的文件操作
safe_file_operation() {
    local filename=$1
    local operation=$2
    
    # 检查文件是否存在
    if [ ! -f "$filename" ]; then
        echo "错误：文件不存在：$filename" >&2
        return 1
    fi
    
    # 检查文件权限
    case $operation in
        "read")
            if [ ! -r "$filename" ]; then
                echo "错误：文件不可读：$filename" >&2
                return 1
            fi
            ;;
        "write")
            if [ ! -w "$filename" ]; then
                echo "错误：文件不可写：$filename" >&2
                return 1
            fi
            ;;
    esac
    
    return 0
}

# 使用示例
echo "调试和错误处理示例"

# 安全的文件读取
if safe_file_operation "/etc/passwd" "read"; then
    echo "成功读取文件"
    # 读取文件内容（只显示前3行）
    head -3 /etc/passwd
fi

# 错误处理示例
echo "测试错误处理："
if safe_file_operation "/nonexistent/file" "read"; then
    echo "这个不会执行"
else
    echo "文件操作失败，但程序继续运行"
fi
```

`set -x`、`set -e`、`set -u` 这些调试选项有什么用？

这些是Shell脚本中非常有用的调试选项：

1. **`set -x`**（调试模式）

   - 显示每个执行的命令
   - 显示变量的替换结果
   - 帮助理解脚本的执行流程
2. **`set -e`**（错误退出）

   - 任何命令返回非零状态码时立即退出
   - 防止错误继续传播
   - 适合生产环境使用
3. **`set -u`**（未定义变量检查）

   - 使用未定义变量时报错
   - 防止拼写错误导致的意外行为
   - 提高代码的健壮性
4. **`set -o pipefail`**（管道失败）

   - 管道中任何命令失败时，整个管道返回失败
   - 防止管道中错误被忽略

### [最佳实践](#最佳实践)

1. **添加注释**：为复杂的代码添加清晰的注释
2. **使用有意义的变量名**：避免使用 `a`, `b`, `c` 这样的变量名
3. **错误处理**：检查命令的返回值，处理可能的错误
4. **使用函数**：将重复的代码组织成函数
5. **避免硬编码**：使用变量而不是固定的值
6. **测试脚本**：在不同的环境中测试你的脚本

### [脚本模板](#脚本模板)

```
#!/bin/bash
# ================================================
# 脚本名称：[脚本功能描述]
# 作者：[你的名字]
# 创建日期：[创建日期]
# 版本：1.0
# ================================================

# 设置错误处理
set -euo pipefail

# 配置变量
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="/tmp/$(basename "$0").log"

# 日志函数
log() {
    local level=$1
    shift
    local message="$*"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$level] $message" | tee -a "$LOG_FILE"
}

# 主函数
main() {
    log "INFO" "脚本开始执行"
    
    # 在这里添加主要逻辑
    
    log "INFO" "脚本执行完成"
}

# 错误处理
handle_error() {
    local exit_code=$?
    log "ERROR" "脚本执行失败，退出码：$exit_code"
    exit $exit_code
}

# 信号处理
trap handle_error ERR INT TERM

# 执行主函数
main "$@"
```

为什么要使用这么复杂的模板？

这个模板虽然看起来复杂，但它包含了专业脚本的多个重要要素：

1. **文档头部**：清晰的脚本说明
2. **错误处理**：健壮的错误处理机制
3. **日志记录**：完整的日志记录功能
4. **配置分离**：配置与逻辑分离
5. **信号处理**：优雅的错误处理和清理
6. **模块化**：主函数和辅助函数分离

---

## [8. 学习路径和进阶资源](#_8-学习路径和进阶资源)

### [学习建议](#学习建议)

1. **从简单开始**：先编写简单的脚本，逐步增加复杂度
2. **多练习**：实践是最好的学习方法
3. **阅读优秀脚本**：学习系统中的脚本文件
4. **参与开源项目**：阅读和贡献开源项目的脚本

如何找到优秀的脚本学习？

在Linux系统中有很多优秀的脚本可以学习：

```
# 查看系统脚本
ls /etc/init.d/
ls /etc/rc.d/

# 查看软件包的脚本
ls /var/lib/dpkg/info/*.postinst
ls /var/lib/dpkg/info/*.prerm

# 查看Shell内置脚本
type -a cd
type -a pushd
```

### [进阶主题](#进阶主题)

- 数组和关联数组
- 文本处理（awk, sed）
- 进程管理和作业控制
- 信号处理
- 调试技巧
- 性能优化

### [推荐资源](#推荐资源)

1. **官方文档**：`man bash` 是最权威的参考
2. **在线教程**：Linux命令行和Shell脚本编程教程
3. **实践项目**：自动化日常任务
4. **社区**：Stack Overflow, GitHub等

---

## [总结](#总结)

Shell脚本编程是Linux系统管理的核心技能。通过本附录的学习，你已经掌握了：

- 基本语法和结构
- 变量和条件判断
- 循环和函数
- 实际应用场景
- 调试和最佳实践

如何继续提升Shell脚本技能？

记住，编写好的Shell脚本需要练习和经验。从今天开始，尝试将你日常的重复任务自动化，你会发现Shell脚本的强大威力。

**建议的下一步**：

1. 选择一个重复的手动任务，尝试用脚本自动化
2. 阅读系统中的现有脚本，学习优秀的设计模式
3. 参与开源项目，贡献自己的脚本
4. 学习更高级的文本处理和系统管理技能

祝你在Shell脚本编程的道路上越走越远！🚀

**最后的小挑战**：

- 创建一个脚本，监控系统的健康状况
- 写一个脚本，自动化你的开发环境设置
- 创建一个脚本，管理你的文件备份

记住，最好的学习方式就是实践！开始动手编写你的第一个Shell脚本吧！

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [附录A0｜Shell脚本简单入门](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#附录a0-shell脚本简单入门)
- [1. 第一个Shell脚本：Hello World](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_1-第一个shell脚本-hello-world)
- [2. 变量：脚本的记忆单元](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_2-变量-脚本的记忆单元)
- [基本变量操作](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#基本变量操作)
- [特殊变量](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#特殊变量)
- [环境变量](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#环境变量)
- [3. 条件判断：让脚本更智能](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_3-条件判断-让脚本更智能)
- [if语句基础](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#if语句基础)
- [常用条件测试](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#常用条件测试)
- [case语句](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#case语句)
- [实际应用示例](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#实际应用示例)
- [4. 循环：重复执行任务](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_4-循环-重复执行任务)
- [for循环](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#for循环)
- [while循环](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#while循环)
- [循环的实际应用](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#循环的实际应用)
- [5. 函数：代码的重用模块](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_5-函数-代码的重用模块)
- [基本函数定义和使用](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#基本函数定义和使用)
- [函数的高级用法](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#函数的高级用法)
- [函数的实际应用](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#函数的实际应用)
- [6. 实用脚本示例](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_6-实用脚本示例)
- [系统信息收集脚本](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#系统信息收集脚本)
- [日志分析脚本](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#日志分析脚本)
- [备份脚本](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#备份脚本)
- [7. 调试和最佳实践](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_7-调试和最佳实践)
- [调试技巧](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#调试技巧)
- [最佳实践](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#最佳实践)
- [脚本模板](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#脚本模板)
- [8. 学习路径和进阶资源](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#_8-学习路径和进阶资源)
- [学习建议](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#学习建议)
- [进阶主题](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#进阶主题)
- [推荐资源](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#推荐资源)
- [总结](https://xiaolinnote.com/linux/appendix-a0-shell-scripting-basics.html#总结)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
