#!/usr/bin/env python
# -*- coding: utf-8 -*-

#导入selenium包
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#初始化webdriver的chromedriver
driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')
#打开页面
# driver.get('C:/Users/Administrator/Desktop/index.html')
driver.get('http://www.baidu.com')

#driver.title,HTML页面的title
print(driver.title)
time.sleep(3)

'''
#定位select下拉框,需要导包
# s1 = Select(driver.find_element_by_id("se"))
# s1.select_by_index(1) #index()选择下拉元素
'''

#定位下面的兄弟节点
#driver.find_element_by_xpath('//div[@class="isw-edit"]/following-sibling::ul/li/a[@class="isw-settings"]').click()

'''
#定位页面内的滚动条
mscb = driver.find_element_by_xpath('//div[contains(@style,"49px")]')
#ActionChains事件,click_and_hold()鼠标左键按住,move_to_element_with_offset(),鼠标拖动
ActionChains(driver).click_and_hold(mscb).move_to_element_with_offset(mscb, 0, 100).perform()  
'''
'''
# 点击多选框
js = "var q = document.documentElement.scrollTop="
driver.execute_script(js+'100000')
cher = driver.find_elements_by_xpath('//table[@class="table"]/tbody/tr/td/div')
print(len(cher))
for ch in cher :
    ch.click()
'''

'''
浏览器滚动条
# driver.maximize_window()
driver.find_element_by_link_text('UI elements').click()
driver.find_element_by_link_text('UI Elements').click()
time.sleep(3)
js = 'var q = document.documentElement.scrollTop='
driver.execute_script(js+'1400')
'''
'''
driver.maximize_window()
driver.find_element_by_link_text("Forms stuff").click()
time.sleep(3)
js = 'var q = document.documentElement.scrollTop='
driver.execute_script(js+'1200')

selector = driver.find_element_by_xpath('//div[contains(text(),"Simple select:")]/following-sibling::div/select')
Select(selector).select_by_value("5") #index()选择下拉元素
'''



time.sleep(5)
print('结束脚本')
driver.quit()
# service.stop()  #关闭进程