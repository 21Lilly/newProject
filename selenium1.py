# -*- coding:utf-8 -*-
'''
@project:newProject
@file:selenium1.py
@ide:PyCharm
@author:lvy
@time:2020-07-09 14:50:19
@month:七月
'''

from selenium import webdriver
import time

driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
driver.maximize_window()

driver.get('http://www.baidu.com')
time.sleep(2)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(5)

#将滚动条移动到底部
js1 = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js1)
time.sleep(3)

#将滚动条移动到顶部
js2 = "window.scrollTo(0,0)"
driver.execute_script(js2)
time.sleep(3)

# 聚焦元素
# target = driver.find_element_by_xxxx()
# driver.execute_script("arguments[0].scrollIntoView();", target)


driver.quit()





