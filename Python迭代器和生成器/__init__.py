'''
迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退
迭代器有两个基本方法：iter() 和next()
'''

# 字符串，列表，元组对象都可以 用于创建迭代器
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))


list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print(x, end=" ")


import sys
list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 生成器

'''
在Python中，使用了yield的函数被称为 生成器
和普通函数 不同的是，生成器 是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
调用生成器运行的过程中，每次遇到 yield 时函数就会暂停并保存当前所有的运行信息，返回 yield 的值，并在下一次 执行 next()方法时从当前位置继续运行

调用一个生成器函数吗，返回的是一个 迭代器对象
'''
import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10) # f是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
















