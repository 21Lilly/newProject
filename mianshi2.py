#coding:utf-8
#斐波那契数列  0,1,1,2,3,5,8,13
#递推法
# def fib_loop(n):
#     a, b = 0, 1
#     while n > 0:
#         a , b = b , a+b
#         n -= 1
#     return a
#
# for i in range(3):
#     print('i = ',i)
#     print(fib_loop(i))

#生成器
#
# def fib_loop_while(max):
#     a,b = 0,1
#     while max > 0:
#         a,b = b,a+b
#         max -= 1
#         yield a
#
# for i in fib_loop_while(3):
#     print(i)


#[1,2,3,4]输出为1234
from __future__ import print_function
# lista = [1,2,3,4]
# for one in lista:
#     print(one,end = '')

#3位水仙花数是指一个三位整数，其各位数字的3次方和等于该数本身
# ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。
#
# for i in range(100,1000):
#     if pow(i//100,3) + pow(i%10,3) + pow(i//10%10,3) == i:
#         print(i,end='  ')
# num = 987
# print(num//100)
# print(num//10%10)
# print(num %10)

#回文数判断
# “回文”是指正读反读都能读通的句子。在数学中也有这样一类数字有这样的特征，称为回文数，例如121，25852等等

# n = input("请输入一个数字：")
# if n == n[::-1]:
#     print("你输入的是回文数")
# else:
#     print("你输入的不是回文数")


# 判断任意年份是否为闰年，需要满足以下条件中的任意一个：
# 　　① 该年份能被 4 整除同时不能被 100 整除；
# 　　② 该年份能被400整除。

def leap(yyyy):
    if yyyy % 4 == 0:
        if yyyy % 400 == 0:
            return True
        elif yyyy % 100 ==0:
            return False
        else:
            return True
    else:
        return False

n = int(input("请输入年份"))
if leap(n) == True:
    print("{}年是闰年".format(n))
else:
    print("{}年不是闰年".format(n))