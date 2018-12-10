#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-05 20:52:45
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


from selenium import webdriver

driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')
driver.get('http://scm.well-cars.com:3000/')
print(driver.title)

driver.find_element_by_link_text('登录').click()




time.sleep(5)
print('结束脚本')
driver.quit()
