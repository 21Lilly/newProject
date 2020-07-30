# -*- coding:utf-8 -*-
'''
@project:newProject
@file:selenium3.py
@ide:PyCharm
@author:lvy
@time:2020-07-10 09:03:55
@month:七月
'''

from selenium  import webdriver
driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
driver.get('http://bj.ganji.com/')
driver.maximize_window()
current_handle = driver.current_window_handle

print(current_handle)

driver.find_element_by_link_text('工作').click()
all_handles = driver.window_handles
print(all_handles)

#方法一：判断句柄，不等于首页就切换
# for one in all_handles:
#     if one != current_handle:
#         driver.switch_to.window(one)
#         print(driver.title)

#方法二获取list里面第二个切换
driver.switch_to.window(all_handles[1])
print(driver.title)

driver.close()

driver.switch_to.window(current_handle)
print(driver.title)

driver.quit()