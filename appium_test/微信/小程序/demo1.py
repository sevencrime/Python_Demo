#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-31 20:43:56
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = 'ee31d6d0'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyoard'] = True
desired_caps['chromeOptions'] = {'androidProcess': 'WEBVIEW_com.tencent.mm:tools'}  

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)

def login():

	driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()	#权限确定框
	driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

	driver.find_element_by_id('com.tencent.mm:id/d75').click()	#点击登录按钮
	driver.find_element_by_id('com.tencent.mm:id/hz').send_keys('17620446727')
	time.sleep(2)
	driver.find_element_by_id('com.tencent.mm:id/alr').click()	#点击登录
	time.sleep(1)
	driver.find_element_by_id('com.tencent.mm:id/hz').send_keys('shengqile54604')
	driver.find_element_by_id('com.tencent.mm:id/alr').click()
	time.sleep(10)
	driver.find_element_by_id('com.tencent.mm:id/an2').click()

x = driver.get_window_size()['width'] 
y = driver.get_window_size()['height'] 
x1 = x * 0.5
y1 = y * 0.25
y2 = y * 0.75

action = TouchAction(driver)
action.press(x=x1, y=y1).wait(ms=300).move_to(x=x1, y=y2).release().perform()
time.sleep(3)

driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'滴滴公交查询')]").click()
time.sleep(2)

# el = driver.find_element_by_android_uiautomator("new UiSelector().clickable(true).description(\"今天想吃点什么？\")").click()
# driver.find_element_by_android_uiautomator("new UiSelector().clickable(true).description(\"今天想吃点什么？\")").click()

# driver.find_element_by_android_uiautomator("new UiSelector().description(\"今天想吃点什么？\")").send_keys("早餐")
# driver.find_element_by_android_uiautomator("new UiSelector().description(\"搜索\")").click()

print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
print("切换成功")


time.sleep(10)
driver.quit()









