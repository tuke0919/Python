
# 变量赋值
counter = 100  # 整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(counter,miles,name)
print(counter);print(miles);print(name)

# 多个变量赋值
a = b = c = 1
b = 3
print(a,b,c)

a,b,c = 1,2,"John"
c = "Mike"
print(a,b,c)

# 标准数据类型  数字，字符串 列表 元组 和字典

# 字符串
s = "abcdef"
print(s[1:5])
print(s[1:])
print(s[:4])
print(s * 3) # * 是重复操作
print(s + " " + "TEST")

letters = ['c','h','e','c','k','i','o'] # 字符数组
print(letters[1:4:2])
letters = "checkio" # 字符串
print(letters[1:4:2])

# 列表  它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
list = ['runoob',786,2.33, 'john', 70.2]
tinylist = [123,'mike']
list2 = [456, tinylist, 'string']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
print(list2)

# 元组  是只读 List，不支持更新
tuple = ('runoob',786,2.33, 'john', 70.2)
tinytuple = (123,'mike')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

# 集合Set  可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set 可以集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b) # 差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # a和b中不同时存在的元素



# 字典
'''
列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''
dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinydict = {'name': 'john', 'code': 6725, 100: 23.14, 35.1: 'mike'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict[100])
print(tinydict[35.1])

print(tinydict.keys())
print(tinydict.values())


