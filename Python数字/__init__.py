import cmath
import math

# cmath 模块包含了一些用于复数运算的函数。
listCmath = dir(cmath)
print(listCmath)

# math 模块提供了许多对浮点数的数学运算函数。
listMath = dir(math)
print(listMath)

print(cmath.sqrt(-1))
print(cmath.sqrt(9))
print(cmath.sin(1))

# 数学函数
# abs 一个数的绝对值
print('abs(-40)  = ', abs(-40))
print('abs(100.10)  = ', abs(100.10))

# ceil 返回一个大于或等于 x 的的最小整数
print('math.ceil(-45.17) = ', math.ceil(-45.17))
print('math.ceil(100.12) = ', math.ceil(100.12))
print('math.ceil(math.pi) = ', math.ceil(math.pi))

# exp 返回x的指数,e^x。
print('math.exp(-2) = ', math.exp(-2))
print('math.exp(10) = ', math.exp(10))
print('math.exp(4) = ', math.exp(4))

'''
abs() 函数类似于 abs() 函数，但是他有两点区别:
abs() 是内置函数。 fabs() 函数在 math 模块中定义。
fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中。
'''
print('math.fabs(-40)  = ', math.fabs(-40))
print('abs(100.10)  = ', math.fabs(100.10))

# floor 返回小于或等于 x 的整数
print('math.floor(-45.17) = ', math.floor(-45.17))
print('math.floor(100.12) = ', math.floor(100.12))
print('math.floor(100.72) = ', math.floor(100.72))
print('math.floor(math.pi) = ', math.floor(math.pi))

# log 返回x的自然对数，x>0。
print('math.log(100) = ', math.log(100))
print('math.log(math.e) = ', math.log(math.e))
print('math.log(100,10) = ', math.log(100, 10))
print('math.log(1000000,10) = ', math.log(1000000, 10))

# log10
print("math.log10(100.12) : ", math.log10(100.12))
print("math.log10(100) : ", math.log10(100))
print("math.log10(119) : ", math.log10(119))
print("math.log10(math.pi) : ", math.log10(math.pi))

# max
print('max(10, 100, 1000) = ', max(80, 100, 1000))
print('max(-20, 100, 400) = ', max(-20, 100, 400))
print('max(-80, -20, -10) = ', max(-80, -20, -10))

# min
print('min(10, 100, 1000) = ', min(80, 100, 1000))
print('min(-20, 100, 400) = ', min(-20, 100, 400))
print('min(-80, -20, -10) = ', min(-80, -20, -10))

# pow
print('math.pow(100,2) = ', math.pow(100, 2))
print('math.pow(2, 4) = ', math.pow(2, 4))

'''
其他 数学函数
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根。
'''

# 随机函数
import random

# choice
print('从 range(100) 中返回一个随机数 = ', random.choice(range(100)))
print('从列表中 [1, 2, 3, 5, 9] 返回一个随机数 = ', random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# random 随机生成的一个实数，它在[0,1)范围内。
print("random() : ", random.random())

# seed
random.seed(10)
print('Random number with seed 10 : ', random.random())

# 生成同一个随机数
random.seed( 10 )
print("Random number with seed 10 : ", random.random())

# 生成同一个随机数
random.seed( 10 )
print("Random number with seed 10 : ", random.random())


# shuffle 随机排列
list = [10, 16, 10, 5]
random.shuffle(list)
print('随机排序列表 : ', list)

random.shuffle(list)
print('随机排序列表 : ', list)

# uniform  随机生成下一个实数，它在[x,y]范围内。
print('uniform(5, 10) 的随机浮点数 : ', random.uniform(5, 10))

print('uniform(7, 14) 的随机浮点数 ：', random.uniform(14, 7))

'''
三角函数
import math
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''






























