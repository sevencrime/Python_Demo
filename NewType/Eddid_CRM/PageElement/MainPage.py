#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-29 15:45:32
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Commons import BasePage, Logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class MainPage(BasePage.BasePage):
    # log = Logging.Logs()

    userid_loc = (By.CSS_SELECTOR, ".el-dropdown-link.el-dropdown-selfdefine ")
    submit_loc = (By.XPATH, "//button/span[contains(text(),'提交审核')]")
    add_loc = (By.XPATH, "//button/span[contains(text(),'新增')]")
    # add_loc = (By.XPATH, "//*[@id='main']/div[1]/div[2]/button[3]/span")
    update_loc = (By.XPATH, "//button/span[contains(text(),'修改')]")
    select_loc = (By.XPATH, "//button/span[contains(text(),'查看')]")

    searchInfo_loc = {By.CLASS_NAME, ".el-input.el-input--suffix"}

    
    def show_userid(self):
        return self.find_element(*self.userid_loc).text

    def click_searchInfo(self):
        time.sleep(3)
        return self.find_element(*self.searchInfo_loc)[1].click()
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.searchInfo_loc)).click()

    def click_submit(self):
        return self.find_element(*self.submit_loc).click()

    def click_add(self):
        # self.log.info(self.find_element(*self.add_loc).text)

        # time.sleep(3)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*self.add_loc)).click()

    def click_update(self):
        return self.find_element(*self.update_loc).click()

    def click_select(self):
        return self.find_element(*self.select_loc).click()

