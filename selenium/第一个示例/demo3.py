#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入selenium包
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#初始化webdriver的chromedriver
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#打开页面
driver.get('C:/Users/Administrator/Desktop/demo/index.html')
# driver.get('C:/Users/Administrator/Desktop/aquarius_v16/index.html')
#driver.title,HTML页面的title
print(driver.title)
time.sleep(3)

#多表单切换
driver.switch_to_frame("one")   #切换表单
driver.find_element_by_id("one").send_keys("sss")
time.sleep(3)
driver.switch_to.default_content() #退出表单至根页面  
driver.switch_to_frame("two")
driver.find_element_by_id("two").send_keys("two")

driver.find_element_by_id("w3c").click()
time.sleep(3)
# driver.switch_to.default_content() #退出表单至根页面  

windows = driver.window_handles #获取打开的多个窗口句柄,返回一个list
driver.switch_to.window(windows[0]) #切换窗口,-1为当前最新打开页面

driver.get('https://www.baidu.com')


time.sleep(5)
print('结束脚本')
driver.quit()
# service.stop()  #关闭进程