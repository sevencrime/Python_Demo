#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-12 09:38:15
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
sys.path.append("D:/Python_Demo/NewType/Eddid_CRM/Controlelement")
print(sys.path)
import elements


class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')
        cls.driver.get('http://eddid-bos-feature.ntdev.be')

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        print("结束driver")
        cls.driver.quit()

    def test_login(self):
        login_url = self.driver.current_url
        print("login_url=", login_url)
        # # 登录用户名
        # self.el_user = self.driver.find_element_by_xpath(
        #     "//input[@placeholder='用户名']")
        # # 登录密码
        # self.el_password = self.driver.find_element_by_xpath(
        #     "//input[@placeholder='密码']")
        # # 点击登录按钮
        # self.btn_login = self.driver.find_element_by_xpath("//button")
        # self.el_user.send_keys('admin')
        # self.el_password.send_keys('abcd1234')
        # self.btn_login.click()
        elements.Element(self.driver)
        element.Element.ele['el_user'].send_keys('admin')
        element.Element.ele['el_password'].send_keys('abcd1234')
        element.Element.ele['btn_login'].click()

        # self.driver.implicitly_wait(10)
        time.sleep(3)
        index_url = self.driver.current_url
        print("index_url=", index_url)
        cookie = self.driver.get_cookies()
        print("cookie=", cookie)


if __name__ == '__main__':
    unittest.main()
