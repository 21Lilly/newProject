# -*- coding:utf-8 -*-
'''
@project:newProject
@file:selenium2.py
@ide:PyCharm
@author:lvy
@time:2020-07-09 15:35:19
@month:七月
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
# #访问百度首页
# first_url = 'http://www.baidu.com'
# print("now access %s" %(first_url))
# driver.get(first_url)
# time.sleep(3)
# #访问新闻页面
# second_url = 'http://news.baidu.com'
# print("now access %s" %(second_url))
# driver.get(second_url)
# time.sleep(3)
# #返回（后退）到百度首页
# print("back to %s" %(first_url))
# driver.back()
# time.sleep(3)
# #前进到新闻页
# print("forward to %5s" %(second_url))
# driver.forward()
# time.sleep(3)

#鼠标悬停操作
#
# driver.get('http://www.baidu.cn')
# driver.maximize_window()
# #定位到要悬停的元素
# above = driver.find_element_by_id("s-usersetting-top")
# #对定位到的元素执行悬停操作
# ActionChains(driver).move_to_element(above).perform()
#
# time.sleep(3)


#键盘事件
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('seleniumm')
#删除多输入的一个m
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

#输入空格键+“教程”
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys("教程")

#全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

#剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

#通过回车键来代替单击操作
driver.find_element_by_id('su').send_keys(Keys.ENTER)
'''
send_keys(Keys.F1) 键盘 F1
send_keys(Keys.F12) 键盘 F12
'''
driver.quit()
