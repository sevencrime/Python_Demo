#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 17:22:57
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import sys
sys.path.append("..")


class Element:

    ele = {}

    def __init__(self, driver):

        # 登录用户名
        self.ele['el_user'] = driver.find_element_by_xpath(
            "//input[@placeholder='用户名']")
        # 登录密码
        self.ele['el_password'] = driver.find_element_by_xpath(
            "//input[@placeholder='密码']")
        # 点击登录按钮
        self.els['btn_login'] = driver.find_element_by_xpath("//button")

        return ele
