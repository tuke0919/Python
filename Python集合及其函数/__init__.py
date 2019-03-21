# set 是一个无序不重复元素序列

# 使用大括号{} 或者 set() 函数创建集合，注意：创建一个空集合 必须用 set() 而不是 {}, 因为{} 是用来创建一个空字典的
# 创建格式
'''

parame = {value01, value02,....}
或者
set(value)
'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # 去重功能

# 两个集合间的运算

a = set('abracadabra')
b = set('alacazam')
print('a = ', a)
print('b = ', b)

# 在a中有，但b中没有
print('a - b = ', a - b)
# a或b中包含的元素
print('a | b = ', a | b)
# a和b中都包含的元素
print('a & b = ', a & b)
# 不同时包含于a和b的元素
print('a ^ b = ', a ^ b)



# 添加元素

# value 是 元组
thisset = set(('Google', 'Runoob', 'Taobao'))
print(thisset)

# value 是 列表
thisset = set([2, 4, 'jack'])
print(thisset)

# value 是 字典，只转换 key
thisset = set({'name':'mike', 'age': 27})
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add('Facebook')
print(thisset)

# update 也可以添加元素，且参数可以是列表，元组，字典等
thisset.update({1, 3})
print(thisset)

thisset.update([1, 4], [5, 6])
print(thisset)


# 移除元素

thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove('Taobao')
print(thisset)

# s.discard( x ) 还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误
thisset.discard('Facebook') # 不存在不会发生错误
print(thisset)

# pop() 设置随机删除集合中的一个元素
thisset.pop()
print(thisset)

# 集合长度
thisset = set(("Google", "Runoob", "Taobao"))
print('集合长度 = ', len(thisset) )


# set.difference(set)  返回集合的差集，元集合不变
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print('difference x = ', x)
print('difference z = ', z)

# set.difference_update(set) 移除两个集合中都存在的元素。
'''
difference() 方法返回一个移除相同元素的新集合 
difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
'''

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.difference_update(y)
print('difference_update x = ', x)
print('difference_update y = ', y)

# set.intersection(set1, set2 ... etc) 返回一个交集，但原集合不变
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.intersection(y)
print('intersection = ', z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print('intersection = ', result)

# set.intersection_update(set1, set2 ... etc) 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.intersection_update(y)
print('intersection_update = ', x)


# set.isdisjoint(set) 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
print('isdisjoint = ', x.isdisjoint(y))

x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
print('isdisjoint = ', x.isdisjoint(y))

# set.issubset(set)  判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print('issubset = ', z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print('issubset = ', z)

# set.issuperset(set) 判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print('issuperset = ', z)

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print('issuperset = ', z)

# set.union(set1, set2...) 返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y)
print('union = ', z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print('union = ', result)














