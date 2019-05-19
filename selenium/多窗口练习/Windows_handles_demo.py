#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

#初始化webdriver的chromedriver
driver = webdriver.Chrome()
js='window.open("https://www.baidu.com");'
driver.execute_script(js)
#打开页面
driver.get('https://www.google.com/')
driver.maximize_window()

windows = driver.window_handles

for handle in windows:
    if handle != driver.current_window_handle:
        driver.close()
    else:
        driver.switch_to.window(handle)
        print(driver.title)


time.sleep(3)
driver.quit()









