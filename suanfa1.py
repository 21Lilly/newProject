# -*- coding:utf-8 -*-
'''
@project:newProject
@file:suanfa1.py
@ide:PyCharm
@author:lvy
@time:2020-07-07 09:12:23
@month:七月
'''

# 题目是：有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
def stringSort(data):
    startIndex = 0
    endIndex = 0
    dataLen = len(data)
    while startIndex + endIndex < dataLen:
        if data[startIndex] == '-':
            data[startIndex],data[dataLen-endIndex-1] = data[dataLen-endIndex-1],data[startIndex]
            endIndex += 1

        else:
            startIndex += 1

    return data

data=['-','-','+','-','+','+','-','+','+','-','-','+','-']
print(stringSort(data))

# 输入一个外星人数字，输出对应的人类数字，比如外星人9数字，对应人类数字7
# 人类的数字是：1、2、3、4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20、21、22、23、24、25、26、27、28、29、30。。。。。
#
# 外星人数字是：1、2、4、5、6、7、9、10、11、12、14、15、16、17、19、20、21、22、24、25、26、27、29、41、42、44、45、46、47、49。。。。。


a = '3'
b = '8'
l = []

def func(n):
    for i in range(0,n+1):
        s = str(i)
        if (a in s) or (b in s):
            l.append(s)
    return len(l)

print(9-func(9))