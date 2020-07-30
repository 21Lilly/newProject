# -*- coding:utf-8 -*-
'''
@project:newProject
@file:ssss.py
@ide:PyCharm
@author:lvy
@time:2020-07-10 10:30:01
@month:七月
'''

from selenium import webdriver
import time
url = 'E:\\PycharmProject\\newProject\\ssss.html'
driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
driver.get(url)
time.sleep(3)

#alert
driver.find_element_by_id('alert').click()

time.sleep(3)
t = driver.switch_to.alert

print(t.text)

t.accept()

time.sleep(3)



#confirm
driver.find_element_by_id('confirm').click()

time.sleep(3)
c=driver.switch_to.alert
print(c.text)
t.dismiss()
time.sleep(3)

