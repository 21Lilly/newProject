# -*- coding:utf-8 -*-
'''
@project:newProject
@file:selenium4.py
@ide:PyCharm
@author:lvy
@time:2020-07-10 09:42:02
@month:七月
'''
from selenium import webdriver
import time
driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
driver.get("http://mail.163.com/")
driver.implicitly_wait(3)
#切换到登录的iFrame
iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]//iFrame')
driver.switch_to.frame(iframe)

driver.find_element_by_name("email").send_keys('123')
driver.find_element_by_name("password").send_keys('a1234')
time.sleep(6)
#释放iframe
driver.switch_to.default_content()
print("释放iframe")
driver.quit()
