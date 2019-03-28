

'''
操作系统接口
'''
import os
# 返回当前目录
print(os.getcwd())

# 执行系统命令 mkdir
os.system('mkdir today')
print(dir(os))

'''
文件通配符
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
'''
import glob
print(glob.glob('*.py'))


'''
字符串正则匹配
re模块为高级字符串处理模块提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁，优化的解决方案
'''
import re
print(re.findall(r'\bf[a-z]*', 'whitch foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))

'''
数学
math模块为浮点运算提供了对底层C函数库的访问
random提供了生成随机数的工具。
'''
import  math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random
# 随机选择
print(random.choice(['apple', 'pear', 'banana']))
# 0 ~1 随机浮动点数
print(random.random())
# range(6) 中的随机整数
print(random.randrange(6))


'''
访问互联网
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib
'''

from urllib.request import urlopen

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)


'''
日期和时间
datetime 模块为日期和时间处理同时提供了简单和复杂的方法
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化的输出
该模块还支持时区处理
'''
import datetime
import time
from datetime import date
# dates are easily constructed and formatted
print('today = ', date.today())

# dates support calendar arithmetic
birthday = date(1971, 7, 31)
age = date.today() - birthday
print('age = ', age.days)

# 常用的日期和时间方法
# 今天
today = datetime.date.today()
print('today = ', today)
# 昨天
yesterday = today - datetime.timedelta(days=1)
print('yesterday = ', yesterday)

# 上个月
last_month = today.month - 1 if today.month - 1 else 12
print('last_month = ', last_month)

# 时间戳 秒级
time_stamp = time.time()
print('time_stamp = ', time_stamp)

# 日期格式化
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 补时差
diff = today + datetime.timedelta(hours=8)
print('diff = ', diff)


# 关于网络模块的补充
import urllib
from urllib.request import urlopen
from urllib.parse import urlencode

# 处理get请求，不传data，则为get请求


url = 'http://www.xxx.com/login'
data = {'username': 'admin', 'password': 123456}
# 将字典类型的请求数据转变成url编码
req_data = urlencode(data)
# 通过urlopen方法访问拼接好的url
res = urlopen(url + '?' + req_data)
# read方法时读取返回数据内容，decode是转换返回的数据bytes格式为str
response = res.read().decode()

print(response)

# 处理post 请求，如果传data，则为post请求

import urllib
from urllib.request import Request
from urllib.parse import urlencode

url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
# 将字典类型的请求数据转变为url编码
data = urlencode(data)
# 将url编码类型的请求数据转变为bytes类型
data = data.encode('ascii')
# 将url和请求数据处理为一个Request对象，供urlopen调用
req_data = Request(url, data)
with urlopen(req_data) as res:
    # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
    res = res.read().decode()
print(res)




