

var1 = 'hello World!'
var2 = 'Runoob'

print('var1[0]: ', var1[0])
print('var2[1:5]: ', var2[2: 5])

# 字符串更新
print('已更新字符串：', var1[:6] + 'Runoob')

# Python 转义字符
'''
\    续航符
\\   反斜杠符号
\'   单引号
\"   双引号
\a   响铃
\b   退格
\e   转义
\000  空
\n   换行
\r   回车
\f   换页
\v   纵向制表符
\t   横向制表符
\oyy  八进制数，yy代表的字符，例如：\o12代表换行
\other 其它的字符以普通格式输出
'''
# \xyy  十六进制数，yy代表的字符，例如:\x0a代表换行

# Python字符串运算符

a = 'Hello'
b = 'Python'
print('a + b : ', a + b)
print('a * 2 : ', a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

# 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
print(r'\n')
print(R'\n')

# Python 字符串格式化

print('我叫 %s 今年 %d 岁' % ('小明', 10))

'''
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写

'''

# Python 三引号
param_str = """
这是一个多行字符的实例
多行字符串可以使用制表符
TAB(\t)
也可以使用换行符[\n]
"""
print(param_str)


# Python 字符串内建函数

# capitalize() 首字母大写，其他字符小写
str = 'hello PYTHON'
print(str.capitalize())
str = "123 hello PYTHON"
print(str.capitalize())
str="@ Hello PYTHON"
print(str.capitalize())

# str.center(width[, fillchar]) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
line = '[www.runnoob.com]'
# width 小于宽度
print("line.center(4, '*') :", line.center(4, '*'))
print("line.center(40, '*') :", line.center(40, '*'))
# 默认空
print("line.center(40) :", line.center(40))


# str.count  回子字符串在字符串中出现的次数
str = 'www.runoob.com'
sub = 'o'
print("str.count('o') = ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub, 0, 10))

'''
str.decode("UTF-8")                    
解码，返回解码后的字符串 。

str.encode("UTF-8")                    
编码，返回编码后的字符串，它是一个 bytes 对象

str.endswith(suffix[, start[, end]])   
如果字符串含有指定的后缀返回True，否则返回False。

str.startswith(substr, beg=0,end=len(string)); 
如果检测到字符串则返回True，否则返回False。

str.find(str, beg=0, end=len(string))  
如果包含子字符串返回开始的索引值，否则返回-1。

str.rfind(str, beg=0 end=len(string))
类似于 find()函数，不过是从右边开始查找.


str.index(str, beg=0, end=len(string)) 
如果包含子字符串返回开始的索引值，否则抛出异常。

str.rindex(str, beg=0 end=len(string))
类似于 index()，不过是从右边开始.

str.isalnum()  
如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False。

str.isalpha()  
如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

str.isdigit() 
如果字符串只包含数字则返回 True 否则返回 False..

str.islower() 
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

str.isupper()
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

str.isnumeric()
如果字符串中只包含数字字符，则返回 True，否则返回 False

str.isspace()
如果字符串中只包含空格，则返回 True，否则返回 False.

str.join(sequence)
用于将序列中的元素以指定的字符连接生成一个新的字符串。

len( s )
返回字符串长度

str.lower()
返回将字符串中所有大写字符转换为小写后生成的字符串。

str.lstrip([chars]) chars --指定截取的字符。
返回截掉字符串左边的空格或指定字符后生成的新字符串。

str.rstrip([chars]) chars -- 指定删除的字符（默认为空格）
返回删除 string 字符串末尾的指定字符后生成的新字符串。

str.strip([chars]);
返回移除字符串头尾指定的字符序列生成的新字符串。


max(str)
返回字符串中最大的字母。

min(str)
返回字符串 str 中最小的字母。

str.replace(old, new[, max])
返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。

str.split(str="", num=string.count(str))
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有


str.swapcase();
将字符串中大写转换为小写，小写转换为大写。

str.title();
返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())

str.zfill(width)
返回长度为 width 的字符串，原字符串右对齐，前面填充0

str.isdecimal()
检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

'''






















