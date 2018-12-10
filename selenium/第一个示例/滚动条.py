#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入selenium包
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#初始化webdriver的chromedriver
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
#打开页面
driver.get('https://www.cnblogs.com/pachongshangdexuebi/p/5313381.html')
# driver.get('C:/Users/Administrator/Desktop/aquarius_v16/index.html')
#driver.title,HTML页面的title
print(driver.title)
time.sleep(3)

#document.documentElement.scrollTop= 0 ,设置滚动条位置
js = "var q = document.documentElement.scrollTop="
driver.execute_script(js+'100000')
time.sleep(3)
driver.execute_script(js+'0')




time.sleep(5)
print('结束脚本')
driver.quit()
# service.stop()  #关闭进程