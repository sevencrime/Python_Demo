#! /usr/bin/env python
# -*- coding: utf-8 -*-

#WWIFI模块

import time
import subprocess
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

#wifi开关压力
def switch(x,sum):
	while 1 :
		x += 1 
		print("打开WIFI")
		driver.find_element_by_id('com.android.settings:id/switch_widget').click()
		print("关闭WIFI")
		time.sleep(5)
		driver.find_element_by_id('com.android.settings:id/switch_widget').click()
		time.sleep(3)
		if x >= sum :
			break

#登录WIFI并判断是否连上
def connection_wifi():
	'''
	3.find_elements_by_定位方式(value)返回元素数组
	用法与find_element_by_方式(value)一致，但是返回一个数组。
	可以通过数组的索引来访问具体的某个结果

	'''
	item_list = driver.find_elements_by_class_name('android.widget.TextView')
	#遍历item_list
	for i in item_list :
		print(i.text)
		#连接WIFI
		if i.text == "Magifun":
			i.click()
			psw = driver.find_element_by_id("com.android.settings:id/password")
			psw.send_keys("mgf2016518")
			time.sleep(5) 
			but = driver.find_element_by_id("android:id/button1").click()
			break
	time.sleep(5)
	summary = driver.find_element_by_id("android:id/summary")
	print(summary.text)

#进入浏览器
def Browser() :
	driver.start_activity("com.android.browser",".BrowserActivity")

	firistFlag = True
	secondFlag = False 

	testMethod(firistFlag,secondFlag)

# 输入网址,检查网络是否正常
def testMethod(firistFlag,secondFlag):
	try:
		if firistFlag:
			url = driver.find_element_by_id("com.android.browser:id/url").send_keys("www.yohoo.com")
			driver.keyevent(66)
			secondFlag = True
			driver.manage().timeouts().pageLoadTimeout(5, TimeUnit.SECONDS);

		if secondFlag:
			url = driver.find_element_by_id("com.android.browser:id/url").send_keys("www.baidu.com")
			driver.keyevent(66)
		
			secondFlag = False
			driver.manage().timeouts().pageLoadTimeout(5, TimeUnit.SECONDS);
		
	except AttributeError:
		#print("拋出異常")
		if driver.page_source.find(u"百度") != -1 or driver.page_source.find(u"Search") != -1:
			print("网页加载成功") 

		firistFlag = False
		testMethod(firistFlag,secondFlag)

if __name__ == '__main__':	
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '7.1.2'
	desired_caps['deviceName'] = 'ML5RRVGNSQ'
	desired_caps['noReset'] = True
	desired_caps['appPackage'] = 'com.android.settings'
	desired_caps['appActivity'] = '.Settings'
	desired_caps['unicodeKeyboard'] = True
	#desired_caps['resetKeyboard'] = True
	driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
	time.sleep(1)
	driver.find_element_by_xpath(
	            "//android.widget.TextView[contains(@text,'Wi-Fi')]")

	#设置网络模式
	if driver.network_connection != 2 and driver.network_connection != 6: #判断wifi的状态
		print("连接WIFI")
		driver.find_element_by_id('com.android.settings:id/switch_widget').click() 
		time.sleep(5)

	switch(0,10)
	connection_wifi()
	# Browser()

	time.sleep(5)
	print("脚本运行结束,退出")
	driver.quit()