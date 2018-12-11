#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-11 13:37:33
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ***
# @Version : $Id$

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Test_Review:

    def __init__(self):
        self.driver = webdriver.Chrome(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')
        self.driver.get('http://eddid-bos-feature.ntdev.be')

    def Element(self):
        el_user = self.driver.find_element_by_xpath(
            "//input[@placeholder='用户名']").send_keys('admin')
        el_password = self.driver.find_element_by_xpath(
            "//input[@placeholder='密码']").send_keys('abcd1234')
        # 点击登录按钮
        btn_login = self.driver.find_element_by_xpath("//button").click()

    def __del__(self):
        time.sleep(5)
        print("结束driver")
        self.driver.quit()


if __name__ == '__main__':
    Test_Review().Element()
