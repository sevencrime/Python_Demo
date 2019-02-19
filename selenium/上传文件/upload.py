#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-19 10:00:03
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

# https://www.jianshu.com/p/b03ef6ffc4a5

from selenium import webdriver
driver = webdriver.Chrome(executable_path = 'chromedriver')
driver.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = driver.find_element_by_id('file')
upload.send_keys('D:\\1.txt')  # send_keys
print(upload.get_attribute('value'))  # check value

driver.quit()