#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 17:22:57
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# login页面元素
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from commons import basepage


class LoginPage(BasePage):

    username_loc = (By.XPATH, "//input[@placeholder='用户名']")
    password_loc = (By.XPATH, "//input[@placeholder='密码']")
    btn_login_loc = (By.XPATH, "//button")
    userid_loc = (By.CSS, ".el-dropdown-link.el-dropdown-selfdefine ")
    # 打开网页

    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.btn_login_loc).click()

    def show_userid(self):
        return self.find_element(*userid_loc).text
