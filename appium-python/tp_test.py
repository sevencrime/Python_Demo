#! /usr/bin/env python
# -*- coding: utf-8 -*-
#测试屏幕的tp

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

BOOLEAN = False

#获取机器屏幕大小X,Y
def getSize():
	x = driver.get_window_size()['width']
	y = driver.get_window_size()['height']
	return(x,y)


#使用touchAction来移动屏幕
def toachSweip(x,y,x1,y1) :
	action = TouchAction(driver)
	action.press(x=x,y=y).wait(ms=200).move_to(x=x1,y=y1).release()
	action.perform()

#向上滑动
def swipeUp():
	#获取屏幕像素,返回一个数组
	size = getSize() 
	#global BOOLEAN
	if BOOLEAN == False :
		#上滑动
		x1 = size[0] * 0.5	
		y1 = size[1] * 0.75	
		y2 = size[1] * 0.25	
		time.sleep(1)

	if BOOLEAN == True : 
		#下滑动
		x1 = size[0] * 0.4
		y1 = size[1] * 0.35	
		y2 = size[1] * 0.75
		time.sleep(1)

	#使用swipe方法来移动
	#driver.swipe(x1,y1,x1,y2,t)
	toachSweip(x1,y1,x1,y2)

#寻找Pointer location
def Search_Pointer_location() :
	global BOOLEAN
	#下拉托盘
	driver.open_notifications()
	#进入开发者模式
	el = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'USB debugging connected')]").click()

	#循环遍历列表找到Pointer location
	while 1:
		try:
			swipeUp()
			time.sleep(1)
			#定位Pointer location
			point = driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Pointer location')]")
		except Exception as e:
			#print('没有找到元素,继续滑动')
			# driver.page_source 获取页面所有元素
			str_page_source = driver.page_source
			#判断是否滑动到页面底部,滑到底部后,向上滑动寻找元素
			if str_page_source.find('Reset ShortcutManager rate-limiting') != -1 : 
				BOOLEAN = True
			#滑到最上面,向下滑动
			if str_page_source.find('Take bug report') != -1 :
				#global BOOLEAN
				BOOLEAN = False
				
		else:
			# 得到switch,text为ON 的控件
			try:
				#print('ssssssss')
				switch = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/switch_widget").text("ON")')
				#判断switch开关是否打开
				if switch.text == 'ON' :
					print("Pointer location is already open")
					time.sleep(5)
					break

			except Exception as e:
				point.click()
				print("open Pointer location")
				break	
			
	driver.keyevent(3)

#屏幕划线
def draw_line(str1):
	size = getSize()
	
	for x in range(1,size[0],10) :
		driver.swipe(x,1,x,size[1]-10,2000)
	
	for y in range(1,size[1],10) :
		driver.swipe(1,y,size[0]-10,y,2000)
	

if __name__ == '__main__':	
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '5.1.1'
	desired_caps['deviceName'] = 'C8W7KWY897'
	desired_caps['noReset'] = True
	desired_caps['appPackage'] = 'com.android.launcher3'
	desired_caps['appActivity'] = '.Launcher'
	#desired_caps['unicodeKeyboard'] = True
	#desired_caps['resetKeyboard'] = True
	driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
	
	Search_Pointer_location()
	#划线
	draw_line(str1);


	#关闭appium服务
	time.sleep(5)
	print("脚本运行结束,退出")
	driver.quit()