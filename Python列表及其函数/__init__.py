# 列表，列表的数据项不需要具有相同的类型，只要把逗号分隔的不同的数据项使用方括号括起来即可

list1 = ['Google', 'Runnoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# 访问列表中的值
print('list1[0] = ', list1[0])
print('list2[1:5] = ', list2[1:5])

# 更新列表: 可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，

print('第三个元素为: ', list1[2])
list1[2] = 2001
print("更新后列表为 : ", list1)

# 删除列表元素
print('原始列表: ', list1)
del list1[2]
print ("删除第三个元素 : ", list1)

# Python列表脚本操作符

# 长度
print(len([1, 2, 3]))
# 组合
print([1, 2, 3] + [4, 5, 6])
# 重复
print(['Hi!'] * 4)
# 元素是否存在于列表中
print(3 in [1, 2, 3])

# Python列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
squares = [1, 4, 9, 16, 25]
squares += L
print(squares)

# 嵌套列表
a = ['a', 'b', 'c']
m = [1, 2, 3]
x = [a, m]
print(x)
print(x[1])

# Python列表函数&方法
'''
len(list)
列表元素个数

max(list)
列表中元素最大值

min(list)
列表中元素最小值

list(seq)
将元组转换为列表

list.append(obj)
在列表末尾添加新对象

list.count(obj)
统计某个元素在列表中出现的次数

list.extend(seq)
用新列表扩展原来的列表

list.index(obj)
从列表中找出某个值第一个匹配项的索引位置

list.insert(index, obj)
将对象插入列表

list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

list.remove(obj)
移除列表中某个值的第一个匹配项

list.reverse()
反向列表中元素

list.sort( key=None, reverse=False)
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。

list.clear()
清空列表

list.copy()
复制列表
'''

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print("list2 列表: ", list2)

list2[1] = 'Netease'
print("修改后的 list2 列表: ", list2)
print("修改后的 list1 列表: ", list1) # 不影响原列表


aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print( "aList : ", aList)

# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
# 输出结果
print('降序输出:', vowels )


def takesecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takesecond)

# 输出类别
print ('排序列表：', random)


'''
目录：
1，将列表当做堆栈使用
2, 把列表当做队列使用
3, 列表推导式
4，嵌套列表解析
'''

# 1，将列表当做堆栈使用
stack = [3, 4, 5]
stack.append(7)
stack.append(9)
print('stack = ', stack)
stack.pop()
print('pop()后的栈 = ', stack)


# 2, 把列表当做队列使用
from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')

queue.popleft()
print('popleft = ', queue)
queue.popleft()
print('popleft = ', queue)


# 3, 列表推导式
'''
每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号
'''

vec = [2, 4, 6]
newlist = [3*x for x in vec]
print(newlist)

newlist = [[x, x ** 2] for x in vec]
print(newlist)

# 对序列里每一个元素逐个调用某方法：
fresh_fruit = ['   banana  ', '    loganberry', '  passion fruit  ']
newlist = [weapon.strip() for weapon in fresh_fruit]
print(newlist)

# 可以用 if 子句作为过滤器
newlist = [3 * x for x in vec if x > 3]
print(newlist)

# 4，嵌套列表解析

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 将3x4的矩阵 转换 成 4x3的列表
newlist1 = [[row[i] for row in matrix] for i in range(4)]
print(newlist1)

# 相当于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 相当于
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)









































