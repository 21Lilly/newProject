# -*- coding:utf-8 -*-
'''
@project:newProject
@file:suanfa2.py
@ide:PyCharm
@author:lvy
@time:2020-07-15 16:28:17
@month:七月
'''


'''
判断用户输入的年份是否是闰年

分析：能被4整除但是不能被100整除的年份是普通闰年，能被400整除的年份是世纪闰年
'''

#方法一
# yearValue = int(input("请输入年份"))
# if yearValue%4 == 0 and yearValue%100 !=0:
#     print('{0}是普通闰年'.format(yearValue))
#
# elif yearValue % 400 == 0:
#     print('{0}是世纪闰年'.format(yearValue))
#
# else:
#     print('{0}不是闰年'.format(yearValue))

#方法二
# import calendar
# yearn = int(input('请输入年份'))
# isRun = calendar.isleap(yearn)
# if isRun == True:
#     print('{0}是闰年'.format(yearn))
# else:
#     print('{0}不是闰年'.format(yearn))

'''
判断一个数是否是质数
问题分析：除了1和它本身以外不再有其他的因数的数就是质素
算法分析：输入一个整数，如果该数大于1，则从2开始循环到该数，并整除，如果余数为0，则不是质数，如果不为0，则是质数
'''
# num = int(input('请输入一个大于2的整数'))

#方法一

# if num > 2:
#     m1 = 0
#     m2 = 0
#     for i in range(2,num):
#         if num % i == 0:
#             str = '{0}不是质数'.format(num)
#             print('{n}={a}*{b}'.format(n=num,a=i,b=int(num/i)))
#             m1 = 1;m2=1
#         elif m1 == 0:
#             print('{0}是质数'.format(num))
#             break
#     if [m1,m2].count(1) == 2:
#         print('{0}不是质数'.format(num))

#方法二
# m = 2
# while m < num:
#     s = num % m
#     if s == 0:
#         break
#     else:
#         m+=1
#
# if num == m:
#     print('{0}是质数'.format(num))
#
# else:
#     print('{0}不是质数'.format(num))

'''
首先是一个快乐的数字的定义：

快乐的数字按照如下方式确定：从一个正整数开始，用其每位数的平方之和取代该数，并重复这个过程，直到最后数字要么收敛等于1且一直等于1，要么将无休止地循环下去且最终不会收敛等于1。能够最终收敛等于1的数就是快乐的数字。使用Python编写一个算法来确定一个数字是否“快乐”

例如数字 19 就是一个快乐的数字，计算过程如下：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬

　　12 + 92 = 82

　　82 + 22 = 68

　　62 + 82 = 100

　　12 + 02 + 02 = 1   （最终收敛为1）

这里经过了分析，得出了，当循环到数字4时，那么这个数字一定不是快乐数，所以可以得出条件。设置一个循环，当循环到1（快乐数）或者4（不是快乐数）时，就终止循环，得出结果是否为快乐数
'''

#快乐数判断
# def getSumofSquars(num):
#     numstr = str(num)
#     sum = 0
#     for i in numstr:
#         sum += int(i)**2
#     return sum
#
# n = input("请输入数字")
# sumofSqrs = eval(n)  #eval() 函数用来执行一个字符串表达式，并返回表达式的值。
# while sumofSqrs !=1 and sumofSqrs != 4:
#     sumofSqrs  = getSumofSquars(sumofSqrs)
#
# else:
#     if sumofSqrs ==1:
#         print("快乐的数字")
#     else:
#         print("False")

'''
括号配对检测
用户输入一行字符串，其中可能包括小括号 ()，请检查小括号是否配对正确（本题仅限于小括号）
'''
def match_parenthese(s):
    #把一个list当做栈使用
    ls = []
    parenthese = '()'
    for i in range(len(s)):
        si = s[i]
        #如果不是括号则继续
        if parenthese.find(si) == -1:
            continue
        #左括号入栈
        if si == '(':
            ls.append(si)
            continue
        if len(ls) ==0:
            return False
        #出栈比较是否匹配
        p = ls.pop()
        if p == '(' and si == ')':
            continue
        else:
            return  False

    if len(ls) > 0:
        return False
    return True

n = input()
result = match_parenthese(n)
if result == True:
    print('配对成功')

else:
    print('配对不成功')
