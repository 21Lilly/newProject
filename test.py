#coding:utf-8
import time

'''
给定一个非空正整数的数组，按照数组内数字重复出现次数，从高到低排序
items()方法将字典的元素转化为了元组
key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
lambda x:y中x表示输出参数，y表示lambda函数的返回值
'''
# 1、给定一个非空正整数的数组，按照数组内数字重复出现次数，从高到低排序
# list = [1,1,1, 6, 6, 7, 3, 9]
# d = {}
# list_sorted = []
# for i in list:
#     d[i] = list.count(i)
# print(d)
# # 根据字典值的降序排序
# d_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)  # [(1, 2), (6, 2), (7, 1), (3, 1), (9, 1)]
# print(d_sorted)
# # 输出排序后的数组
# for x in d_sorted:
#     print(x)
#     for number in range(0, x[1]):
#         print(number)
#         print(x[1])
#         list_sorted.append(x[0])
# print(list_sorted)
# print("按照重复次数排序后的数字是：{}".format(list_sorted))  # [ 1, 1, 6, 6, 7, 3, 9]


# print(time.time())
# print(time.localtime())
# print(time.localtime(time.time()))
# rq1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
# rq2 = time.strftime('%Y%m%d%H%M%S', time.localtime())
# print(rq1)
# print(rq2)