# 面向对象技术简介
'''

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：     类中定义的函数。
类变量：   类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员： 类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写： 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量： 定义在方法中的变量，只作用于当前实例的类。
实例变量： 在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承： 即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
'''


# 类对象
class MyClass:
    """一个简单的类实例"""
    i = 123456

    def fun(self):
        return 'hello world'


# 实例化类 会自动调用构造函数 __init__()
x = MyClass()
# 访问类的属性和方法
print('MyClass 类的属性 i 为：', x.i)
print('MyClass 类的方法 fun 为：', x.fun())


# __init__(),方法可以有参数，参数用过__init__()传递到类的实例化操作上，例如
class Complex:
    # 带参数的构造函数
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


# self 代表类的实例，而非类
class Test:
    def prt(self):
        print(self)
        print(self.__class__)


test = Test()
test.prt()


# 类的方法
class People:
    name = ''
    age = 0
    # 定义私有方法，私有属性在类外无法直接访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s 说：我 %d 岁.' % (self.name, self.age))


people = People('mike', 10, 20)
people.speak()


# 类的继承
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 子类要调用父类的方法
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆盖父类的方法
    def speak(self):
        print('%s 说：我 %d 岁了，我再读 %d 年级' % (self.name, self.age, self.grade))


student = Student('ken', 10, 60, 3)
student.speak()


# 类的多继承

class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.topic = t
        self.name = n

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多继承
'''
需要注意圆括号中父类的顺序，
若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''


class Sample(Speaker, Student):
    a = ''

    def __init__(self,n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample('Tim', 25, 80, 4, 'Python')
test.speak()


# 方法重写
class Parent:

    def my_method(self):
        print('调用父类方法')


class Child(Parent):

    def my_method(self):
        print('调用子类方法')


child = Child()
# 子类调用重写方法
child.my_method()

# 用子类对象调用 已被覆盖的方法
super(Child, child).my_method()


# 类的私有属性和私有方法
'''
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
'''


class Site:
    name = ''
    # 私有属性
    __url = ''

    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name: ', self.name)
        print('url: ', self.__url)

    # "私有方法"
    def __function(self):
        print('这是私有方法')

    def function(self):
        print('这是公共方法')
        self.__function()


site = Site('菜鸟教程', 'www.runoob.com')
site.who()
site.function()

'''
类的专有方法

__init__  构造函数，在生成对象时调用
__del__   析构函数，释放对象时使用
__repr__  打印，转换
__setitem__ 按照索引赋值
__getitem__ 按照索引取值
__len__  获取长度
__cmp__  比较运算
__call__ 函数调用
__add__ 加运算
__sub__ 减运算
__mul__ 乘运算
__truediv__  除运算
__mod__ 求余运算
__pow__ 乘方
'''


# 运算符重载
class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2)






























