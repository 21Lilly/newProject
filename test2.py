#coding:utf-8
import time
# name = raw_input('input your name:')
#
# print('hello,%s' %name)
#
# for i in range(1,5):
#     m = '%03d' %i
#     print(m)
#
# a = int(raw_input('input number:'))
#
# list=[10,2,3]
# list.append(a)
# list.sort()
# print(list)
''' n=m[:]  列表n复制列表m全部数据'''
# list1 = [10,2,4]
# list2 = []
#
# list2 = list1[:]
#
# print('list2数据是：%s' %list2)
#
# a = int(raw_input('a:'))
# b = int(raw_input('b:'))
#
# if a%b==0:
#     print('a能被b整除')
#
# else:
#     c=a/b#a/b获得相除后的值（非余数）
#     print('a/b= %i' %c)
#

'''列表组合后抛开重复值，排序'''
# list1=[1,2,3,4,5,6]
# list2=[2,4,5,7,8,9]
# list3=list1+list2
#
# list4=[]
#
# for x in list3:
#     if x not in list4:
#         list4.append(x)
#
# print(list3)
# print(list4)

'''判断是否是字符、数字、空格'''
# str1 = 'hekodjk'
# print(str1.isalpha())
#
# num = '123'
# print(num.isalnum())
# print(num.isdigit())
#
# b = ' '
# print(b.isspace())
#
# '''求列表组合值'''
# svn = [1,3,8]
# print('列表组合值：%s' %sum(svn))

'''求1！+2！+3！'''
# s = 0
# def fact(n):
#     if n==1:
#         return n
#     return n*fact(n-1)
#
# for n in range(1,4):
#     a = fact(n)
#     s+=a
#
# print(s)

'''递归调用，自定义方法，实现倒叙字符串'''
#
# def out(s,l):
#     if l==0:
#         return
#     print(s[l-1])
#     out(s,l-1)
#
# s = raw_input('输入数字：')
# l = len(s)
# out(s,l)

'''切片'''
# qp = ['one','two','three']
# print(qp[0:2])#显示序号2之前的数据
# print(qp[::-1])#数据倒叙
# print(qp[::2])#间隔显示数据
#
# '''函数调用'''
# def hello(i):
#     if i < 3:
#         print('yes')
#     else:
#         print('no')
# if __name__ == '__main__':
#     hello(0)

'''排序操作'''
# px = [1,10,45,32,78,2]
# pxb = int(raw_input('输入数字：'))
# px.append(pxb)
# # time.sleep(1)
# px.sort()
# print(px)

# px=[23,54,13,45,34,78,89,43]
# px.sort()
# print(px)
# px.reverse()
# print(px)


'''变量作用域'''
# anum = 2
# def autofunc():
#     anum = 1
#     print('inner num==%d' %anum)
#
# for i in range(3):
#     print('the num=%d' %anum)
#     anum += 1
#     autofunc()

'''嵌套列表相加'''
# x=[[1,2,3],[4,5,6]]
# y=[[3,5,6],[7,3,5]]
#
# z=[]
#输出两个列表
# for i in range(2):
#     z.append([])
#     for j in range(3):
#         z[i].append(x[i][j]+y[i][j])
#
# print(z)

'''变量值互换'''
# def exchange(a,b):
#     a,b = b,a
#     return (a,b)
#
# if __name__ == '__main__':
#     n = exchange(2,9)
#     print(n)

'''计算字符串长度'''
# str1 = 'anjmjfr'
# print(len(str1))

'''列表中的最小和最大值'''
# a = [5,8,3,1,6,7,8,56,90,-1]
# print(max(a))
# print(min(a))

'''连接两个表'''
# a1 = [1,2,3]
# b1 = [3,8,0]
# print(a1+b1)
'''字典最大值'''
# person = {"li":18,"wang":90,"zhang":20,"sun":22}
# print(max(person.values()))

'''列表生成式'''
# print(range(1,22))

'''生成器'''
#在Python中，这种一边循环一边计算的机制，成为生成器（Generator）

# 方法一：把一个列表生成式的[]改为（），就创建了一个generator
#生成式
# L = [x * x for x in range(10)]
# print(L)
#生成器
# g = (x * x for x in range(10))
# print(g)
# print(g.next())
# print(g.next())
# print(g.next())
# print(g.next())

#方法二：通过特殊函数创建：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#例如：递归斐波那契数列
#普通函数
# def fib(n):
#     if n < 2:
#         return (1)
#     else:
#         return (fib(n-1)+fib(n+2))
#
# n = int(raw_input("请输入需要计算的个数："))
# for i in range(n):
#     print(fib(i))


#generator
'''
ps:函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
# def fab(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b  #yield 实现Fibonacci数列
#         a,b = b,a+b
#         n = n+1
# m = int(raw_input('num:'))
# s = fab(m)
# print(s)

def odd():
    print('step1')
    yield 1
    print('step2')
    yield 2
    print('step3')
    yield 5

s = odd()
s.next()
s.next()
s.next()

'''迭代器'''
dict = {'Alice':'1','Beth':'2','Cecil':'3'}
for i in dict.iteritems():
    print(i)
