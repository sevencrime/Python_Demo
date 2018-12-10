#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#初始化webdriver的chromedriver
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#打开页面
driver.get('C:/Users/Administrator/Desktop/demo/2.html')
driver.maximize_window()

title = driver.find_element_by_id("w3c")
print(type(title))
titlepage = title.text
print(titlepage)
title.click()

windows = driver.window_handles

for handle in windows:
    if handle != driver.current_window_handle:
        driver.close()
    else:
        driver.switch_to.window(handle)
        print(driver.title)

        if driver.title.find(titlepage):
            print("pass")
        else:
            print("fail")
    

time.sleep(3)
driver.quit()









