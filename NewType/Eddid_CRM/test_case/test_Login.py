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

    def get_Element(self, mode, path):
        mode_list = ['id', 'name', 'class', 'xpath', 'text', 'tag', 'css']
        if mode == 'id':
            pass
        elif mode == 'name':
            pass
        elif mode == 'class':
            pass
        elif mode == 'xpath':
            pass
        elif mode == 'text':
            pass
        elif mode == 'tag':
            pass
        elif mode == 'css':
            pass
        else:
            print("输入有误")


    def test_login(self):
        # login_url = self.driver.current_url
        # print("login_url=", login_url)

        # 登录用户名
        self.el_user = self.driver.find_element_by_xpath(
            "//input[@placeholder='用户名']")
        # 登录密码
        self.el_password = self.driver.find_element_by_xpath(
            "//input[@placeholder='密码']")
        # 点击登录按钮
        self.btn_login = self.driver.find_element_by_xpath("//button")
        self.el_user.send_keys('admin')
        self.el_password.send_keys('abcd1234')
        self.btn_login.click()

        self.driver.implicitly_wait(10)
        index_url = self.driver.current_url
        print("index_url=", index_url)

        text = self.driver.find_element_by_css_selector(
            ".el-dropdown-link.el-dropdown-selfdefine ").text
        # print("text=", text)
        self.assertEquals(text, 'admin', msg='登录账户有误')


if __name__ == '__main__':
    unittest.main()
