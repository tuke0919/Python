#!usr/bin/python3
'''
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
'''

# 算数运算符

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)
c = a - b
print("2 - c 的值为：", c)
c = a * b
print("3 - c 的值为：", c)
c = a / b
print("4 - c 的值为：", c)
c = a % b
print("5 - c 的值为：", c)

a = 2
b = 3
c = a ** b # 幂 - 返回x的y次幂
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b  # 取整除 - 向下取接近除数的整数
print("7 - c 的值为：", c)

# 比较运算符
a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print('1 - a 不等于 b')

if a != b:
    print("2 - a 不等于 b")
else:
    print('2 - a 等于 b')

if a < b:
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if a > b:
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if b >= a:
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")


# 赋值运算符
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

# 位运算符
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;    # 12 = 0000 1100
print("1 - c 的值为：", c)
c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)


# 逻辑运算符  and or not
a = 10
b = 20
if a and b:
   print("1 - 变量 a 和 b 都为 true")
else:
   print("1 - 变量 a 和 b 有一个不为 true")

# 修改变量 a 的值
a = 0
if a and b:
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if a or b:
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

# 成员运算符  in ,not in
'''
测试实例中包含了一系列的成员，包括字符串，列表或元组。
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5];

if a in list:
    print('1 - 变量a 在给定的列表  list 中')
else:
    print('1 - 变量a 不在给定的列表 list 中')

# 修改变量 a 的值
a = 2
if a in list:
   print("3 - 变量 a 在给定的列表中 list 中")
else:
   print("3 - 变量 a 不在给定的列表中 list 中")



# 身份运算符 ：比较两个对象的存储单元
'''
 id() 函数用于获取对象内存地址。
'''
a = 10
b = 20

if a is b:
    print('1 - a 和 b 有相同的标识')
else:
    print('1 - a 和 b 没有相同的标识')

if id(a) == id(b):
   print("2 - a 和 b 有相同的标识")
else:
   print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# 运算符优先级
'''
**	            指数 (最高优先级)
~ + -	        按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	    乘，除，取模和取整除
+ -	            加法减法
>> <<	        右移，左移运算符
&	            位 'AND'
^ |	            位运算符
<= < > >=	    比较运算符
<> == !=	    等于运算符
= %= /= //= -= += *= **=	赋值运算符
is ,is not	    身份运算符
in ,not in	    成员运算符
and or not	    逻辑运算符
'''










