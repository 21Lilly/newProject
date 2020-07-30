# coding:utf-8

# python中常用的内置模块
#Python模块是包含Python代码的 .py 文件

import sys
import math
import random
import datetime
import time
import json

print(time.time())

#在Python中随机化列表中的元素   使用shuffle函数

# from random import shuffle
# x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
#
# shuffle(x)
# print(x)
#
# print(random.random())
# print(random.randint(1,10))
# print(random.randrange(1,100))

#把字符串的第一个字母大写   capitalize（）函数

# str1 = 'jeiojdk'
# str2 = 'Jeiojdk'
# print(str1.capitalize())
# print(str2.capitalize())

import os
# os.system("ipconfig")

# os.system('cmd.exe')
# os.system('mspaint')
# os.system('dir /s')
# print('after call')

#阻塞式调用
import subprocess
# out_bytes = subprocess.check_output(["ping","www.baidu.com"])
# print(out_bytes.decode("gbk"))
#
# out_bytes2 = subprocess.check_output(['netstat','-a'])
# out_text = out_bytes2.decode('utf-8')
# print(out_text)

#非阻塞式调用

# child = subprocess.Popen(["ping","-c","5","www.google.com"])
# print("parent process")


#作用域
# def foo():
#     a = 99
#
#     def bar():
#         b = 66
#         def test():
#             c = 77
#         print(b)
#     print(a)
# foo()

##将函数名作为参数
def foo(func):
    print('foo')
    return  bar
    func()
def bar():
    print('bar')

foo(bar)
# foo(bar())


