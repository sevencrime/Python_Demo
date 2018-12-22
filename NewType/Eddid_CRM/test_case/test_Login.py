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


class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')
        self.driver.implicitly_wait(30)
        self.url = 'http://eddid-bos-feature.ntdev.be'

    def tearDown(self):
        time.sleep(5)
        print("结束driver")
        self.driver.quit()

    def test_login(self):

        login_page = loginpage(self.driver, self.url)

    # def test_login(self):
    #     login_url = self.driver.current_url
    #     print("login_url=", login_url)

    #     # 登录用户名
    #     self.el_user = self.driver.find_element_by_xpath(
    #         "//input[@placeholder='用户名']")
    #     # 登录密码
    #     self.el_password = self.driver.find_element_by_xpath(
    #         "//input[@placeholder='密码']")
    #     # 点击登录按钮
    #     self.btn_login = self.driver.find_element_by_xpath("//button")
    #     self.el_user.send_keys('admin')
    #     self.el_password.send_keys('abcd1234')
    #     self.btn_login.click()

    #     self.driver.implicitly_wait(10)
    #     # index_url = self.driver.current_url
    #     print("index_url=", index_url)

    #     # text = self.driver.find_element_by_css_selector(
    #     #     ".el-dropdown-link.el-dropdown-selfdefine ").text
    #     text = elem['text'].text
    #     # print("text=", text)
    #     self.assertEqual(text, 'admin', msg='登录账户有误')


if __name__ == '__main__':
    unittest.main()
