# open()方法用于打开一个文件，返回文件对象，接收两个参数：文件名file 和 模式 mode
# 语法如下
'''
open(file, mode='r')
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
'''

'''
mode 参数 有：
t    文本模式
x    写模式，新建一个文件，如果该文件已存在则会报错
b    二进制模式
+    打开一个文件进行更新(可读可写)
U    通用换行模式（不推荐）

r    以只读方式打开，文件的指针将会在文件的开头，这是默认模式
rb   以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+   打开一个文件用于读写。文件指针将会在文件的头
rb+  以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。


w    打开文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb   以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+   打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+  以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等

a    打开一个文件用于追加。如果文件存在，文件指针将会在文件的结尾。也就是说，新的内容会被写入到已有内容之后，如果文件不存在，创建新文件进行写入
ab   以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+   打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

# next(file) 文件下一行
file = open('filetest.txt', 'r')
print('文件名为：', file.name)

for index in range(5):
    line = next(file)
    print('第 %d 行 - %s ' % (index, line))

# 关闭文件
file.close()

# fileObject.read([size]); 从文件读取指定的字节数，如果未给定或为负则读取所有。
file = open('filetest.txt', 'r')
line = file.read(10)
print('读取的字符串 %s ' % line)
line1 = file.read()
print('读取的字符串 %s ' % line1)
file.close()



#fileObject.readline();  从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符
file = open("filetest.txt", "r+")

line = file.readline()
print('读取第一行 %s ' % line)

line2 = file.readline(5)
print('第二行读取 5 个字节 : %s ' % line2)

file.close()

# fileObject.seek(offset[, whence])
'''
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
'''

file = open("filetest.txt", "r+")

line = file.readline()
print('读取的数据为： %s ' % line)

# 重新设置文件读取指针到开头
file.seek(0, 0)
line = file.readline()
print('读取的数据为： %s' % line)

file.close()

# fileObject.tell()  返回文件的当前位置，即文件指针当前位置。

file = open("filetest.txt", "r+")

line = file.readline()
print('读取的数据为： %s ' % line)

# 获取当前文件位置
postion = file.tell()
print('当前位置：%d ' % postion)

file.close()

# fileObject.write( [ str ]) 向文件中写入指定字符串。
'''
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。
如果文件打开模式带 b，那么写入文件内容时，str 需要用 encode 方法转为 bytes 形式，否则报错： TypeError: a bytes-like object is required, not 'str'。
'''
file = open("filetest.txt", "r+")

string = '\n7:www.baidu.com'
# 在文件末尾写入一行
file.seek(0, 2)

line = file.write(string)

# 读取文件所有内容
file.seek(0, 0)
for index in range(6):
    line = next(file)
    print('文件行号 %d - %s ' % (index, line))

file.close()


# fileObject.writelines( [ str ]) 向文件中写入一序列的字符串。
#
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
#
# 换行需要制定换行符 \n。

file = open("filetest.txt", "a") # 追加

list = ['\n菜鸟教程 1\n', '菜鸟教程 2']
file.writelines(list)

file.close()




















