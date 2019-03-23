# 语法
'''
def 函数名（参数列表)）:
    函数体
'''


def area(width, height):
    return width * height


def print_welcome(name):
    print('Welcome : ', name)


print_welcome('Mike and Jack')
w = 5
h = 4
print("width =", w, " height =", h, " area =", area(w, h))


# 参数传递
'''
1, 不可变类型：strings, tuples, numbers 是不可更改的对象
2，可变类型： list，dict 是可以修改的对象
'''

# Python参数传递: 不可变类型(字符串，整数吗，元组)是值传递，可变类型(列表，字典)是 引用传递
# 1, 值传递


def changeint(a):
    a = 10


b = 2
changeint(b)
print(b) # b的结果是2

# 2. 引用传递


def change_name(mylist):
    mylist.append([1, 2, 3, 4])
    print('函数内的取值：', mylist)


my_list = [10, 20, 30];
change_name(my_list)
print('函数外取值：', my_list)


# 参数传递的4种方式：必须参数，关键字参数，默认参数，不定长参数
# 1, 必须参数

def print_me(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用print_me函数
#print_me() # 此处会有异常

# 2，关键字参数 ：关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

# 调用print_me函数
print_me(str = "菜鸟教程")


def print_info(name, age):
    print('名字： ', name)
    print('年龄： ', age)


print_info(age=50, name='zhangsan')

# 3,默认参数


def print_info_two(name, age = 20):
    print('名字： ', name)
    print('年龄： ', age)

print_info_two(name='lisi')

# 4. 不定长参数: *元组，**字典
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
def function_name([formal_args,] *var_args_tuple)"
    '函数文档字符串'
    function_suite
    return [expression]
'''


def print_info_tuple(args1, *vartuple):
    '打印任何传入的参数'
    print('输出：')
    print(args1)
    print(vartuple)


print_info_tuple(70, 60, 22)


def print_info_tuple_two(args1, *vartuple):
    '打印任何传入的参数'
    print('输出：')
    print(args1)
    for var in vartuple:
        print(var)


print_info_tuple_two(70, 50, 22)


def print_info_dict(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


print_info_dict(10, a=78, b=90)


# 匿名函数: lambda 来创建匿名函数
'''
1,lambda 只是一个表达式，函数体比 def 简单很多。
2,lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
3,lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
4,虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
'''

# 语法： lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda args1, arg2: args1 + arg2
print('相加后的值为： ', sum(10, 20))
print('相加后的值为： ', sum(67, 90))


# 变量作用域 ---- 重点
'''
Python的作用域一共有4种，分别是：
1, L (Local) 局部作用域
2, E (Enclosing) 闭包函数外的函数中
3, G (Global) 全局作用域
4，B （Built-in）内置作用域 （内置函数所在模块的范围）

以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
'''

g_count = 0 # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2 # 局部作用域


# global 关键字 和 nonlocal 关键字

# 如果函数体内 修改 全局变量
total = 0


def sum(arg1, arg2):
    "返回两个数的和"
    total = arg1 + arg2 # 此处相当于 值传递
    print('函数内是局部变量：', total)
    return total


# 调用sum函数
sum(10, 20)
print('函数外的全局变量: ', total)

# 1，如果内部作用域 想 修改 全局变量 使用 global关键字

num = 1


def fun_1():
    global num  # 此处相当于 传递地址
    print(num)
    num = 123
    print(num)


# 调用函数
fun_1()
# 打印全局变量
print('全局变量：', num)

# 2，如果内部作用域 想修改 Enclosing作用域，外层非全局作用域，使用 nonlocal关键字


def outer():
    num_num = 10

    def inner():
        nonlocal num_num
        num_num = 100
        print(num_num)

    inner()
    print('Enclosing作用域 : ', num_num)


# 调用函数
outer()

# 全局变量是 可变类型 list时
global_list = [1, 2, 3, 4]


def change_global_list():
    # for var in global_list:
    #     print(var)
    global_list.append(9)
    print('内部修改list：', global_list)


change_global_list()
print('输出外部list', global_list)

'''
总结：
1，局部作用域 可以 访问 全局变量 和 外层非全局变量
2，局部作用域 可以 修改 可变类型(list,dict)的 全部变量 或者 外层非全局变量 ，且不用加关键字
3，局部作用域 修改 不可变类型(string, numbers, tuple)的 全局变量      需要使用 global 关键字
4，局部作用域 修改 不可变类型(string, numbers, tuple)的 外层非全局变量 需要使用 nonlocal 关键字
'''
























