#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-07 18:16:38
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ***
# @Version : $Id$

from selenium import webdriver
import time
import unittest


class Test_Login(unittest.TestCase):

    def __init__(self):

        self.driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')

        self.driver.get("http://eddid-bos-feature.ntdev.be/login")


        time.sleep(5)
        print('结束脚本')       
        self.driver.quit()
    






if __name__ == '__main__' :
    Test_Login()
