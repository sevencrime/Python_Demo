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
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from PageElement import LoginPage


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

        login_page = LoginPage.LoginPage(self.driver, self.url, "Eddid")

        # 打开浏览器
        login_page.open()
        # 输入用户名密码
        login_page.input_username("admin")
        login_page.input_password("abcd1234")
        # 点击登录
        login_page.click_submit()
        # 断言userid
        self.assertEqual("admin", login_page.show_userid(), "userid与登录账户不一致")


if __name__ == '__main__':
    unittest.main()
