# coding:utf-8
import time
import unittest
from selenium import webdriver

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        '''
        测试固件的setUp（）的代码，主要是测试的前提准备工作
        :return:
        '''
        self.driver = webdriver.Chrome("E:\\tool\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get('http://www.baidu.com')


    def testSearch(self):

        '''
         这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        '''

        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)

        try:
            assert 'selenium' in self.driver.title
            print('Test pass')

        except Exception as e:
            print('Test Fail',format(e))
    def tearDown(self):
        '''
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        '''
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()