
# 条件语句
flag = False
name = 'luren'
if name == 'luren':
    flag = True
    print('welcome boss')
else:
    print(name)

num = 9
if num >= 0 and num <= 10:
    print('hello')

num = 10
if num < 0 or num > 10:
    print('hello')
else:
    print('undefine')

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 5):
    print('hello')
else:
    print('undefine')

# while 循环
count = 0
while count < 9:
    print('The count is :', count);
    count = count + 1;

print("Good Bye!");

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)  #  输出双数2、4、6、8、10

# 当i大于10时跳出循环
while 1:
    print(i)
    i += 1
    if i > 10:
        break;

# while … else 在循环条件为 false 时执行 else 语句块：
count = 0
while count < 5:
    print(count, ' is less than 5')
    count += 1
else:
    print(count, 'is not less than 5')

# for 循环
for letter in 'Python':
    print('当前字母：', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in  fruits:
    print('当前水果：', fruit)

print('Good Bye!')

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果:', fruits[index])

# for else
'''
在for 循环中，如果没有从任何一个break中退出，则会执行和for对应的else
只要从break中退出了，则else部分不执行。
'''
for i in range(0, 10):
    if i > 10:
        break
else:
    print('execute for ... else ...')


for i in range(0, 10):
    if i > 5:
        break
else:
    print('this else will not executed')

# pass 语句
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

print("Good bye!")













