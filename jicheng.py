# -*- coding:utf-8 -*-
'''
@project:newProject
@file:jicheng.py
@ide:PyCharm
@author:lvy
@time:2020-07-09 10:05:42
@month:七月
'''

class A(object):
    def __init__(self,name):
        self.name = name
        print(self.name)

    def run(self):
        print('测试测试测试')
        print(self.name)

class B(A):
    def __init__(self,age):
        self.age = age
        super().__init__('lily')  #调用父类中的init方法
        # super(B,self).__init__('lily')   #另外一种调用方法，跟上面一样

    def test(self):
        super().run()
        print('test')

ret = B('22')
ret.run()
ret.test()