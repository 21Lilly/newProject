# -*- coding:utf-8 -*-
'''
@project:newProject
@file:selenium5.py
@ide:PyCharm
@author:lvy
@time:2020-07-10 15:45:54
@month:七月
'''

from selenium import webdriver
import time

driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
driver.get('https://www.12306.cn/index/')
#去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)

#清空文本后输入值
driver.find_element_by_id("train_date").click()
driver.find_element_by_id("train_date").clear()
time.sleep(3)
driver.find_element_by_id("train_date").send_keys('2020-07-16')

# time.sleep(3)
driver.quit()
