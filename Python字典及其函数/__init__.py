# 字典
'''
1，字典的每个键值对 key => value 对用冒号(:)分割，每对之间用逗号(,)分割，整个字典包括在花括号({})中
2，键必须是唯一的，但值不必
3，值可以取任何类型，但键必须是不可变的，比如字符串，数字和元组

'''
# 访问字典里的值
dict = {'name': 'jack','Age': 7, 'Class': 'First' }
print("dict['name'] = ", dict['name'])
print("dict['Age'] = ", dict['Age'] )

# 修改字典
dict['Age'] = 9           # 更新 字段
dict['School'] = '菜鸟教程' # 添加信息
print('更新之后的字典 = ', dict)

# 删除字典元素

del dict['name'] # 删除 键
#dict.clear() #清空字典
#del dict   # 删除字典
print('更新之后的字典 = ', dict)

# 字典键的特性
'''
字典值 可以是任何的Python对象，既可以是标准的对象，也可以是用户自定义的对象，但键不行
1, 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2, 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
# 1 demo
dict = {'name': 'jack', 'Age': 7, 'name': '小菜鸟'}
print("dict['name'] = ", dict['name'] )

# 字典内置方法

len(dict)
print('计算字典元素个数，即键的总数 len(dict) = ', len(dict))

str(dict)
print('输出字典，打印字符串表示 str(dict) = ', str(dict))

'''
字典的内置方法：
dict.clear()
删除字典内所有元素

dict.copy()
返回字典的浅复制

dict.fromkeys(seq[,value])
创建一个新字典，以序列seq中元素做字典的键，value为所有字典键的默认值

dict.get(key,default = None)
返回指定键的值，如果值不在字典中返回默认值 None

key in dict
键是否在字典中

dict.items()
以列表返回可遍历的(键，值) 元组数组

dict.keys()
返回一个迭代器，可以使用 list() 来转换为列表

dict.values()
返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。

dict.update(dict2)
把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里

dict.pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值

dict.popitem()
随机返回并删除字典中的一对键和值(一般删除末尾对)

'''

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print('新的字典为 = ', dict)

dict = dict.fromkeys(seq, 10)
print('新的字典为 = ', dict)

dict = {'Name': 'Runoob', 'Age': 7}
print('dict.keys() = ', dict.keys())
print('list(dict.keys()) = ', list(dict.keys()))

dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print('dict.values() = ', dict.values())
print('字典所有值为 = ', list(dict.values()))


# 字典的遍历技巧

# 字典遍历时，关键字和对应的值可以使用items方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在列表遍历时，使用enumerate 同时得到 索引位置和对应的值
for i, value in enumerate(['tic', 'tac', 'toe']):
    print(i, value)

# 同时遍历两个或者更多序列，可以使用zip()组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy gail', 'blue']

for q, a in zip(questions,answers):
    print('What is your {0}? It is {1}'.format(q, a))

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)










