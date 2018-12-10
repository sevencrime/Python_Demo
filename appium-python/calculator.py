#! /usr/bin/env python
# -*- coding: utf-8 -*-

#计算器模块

import os 
import time
import math
import sys
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'C8W7KVIEQY'
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(1)

#加法运算
def Add():
	print("加法运算")
	driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
	driver.find_element_by_id('com.android.calculator2:id/op_add').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("17");
	time.sleep(1)
	driver.find_element_by_id('com.android.calculator2:id/clr').click()


#减法运算
def Sub():
	print("减法运算")
	driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
	driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("5");
	time.sleep(1)
	driver.find_element_by_id('com.android.calculator2:id/clr').click()

#乘法运算
def Mul():
	print("乘法运算")
	driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
	driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_9').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("72");
	time.sleep(1)
	driver.find_element_by_id('com.android.calculator2:id/clr').click()

#除法运算
def Division():
	print("除法运算")
	driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
	driver.find_element_by_id('com.android.calculator2:id/op_div').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("2.5");
	time.sleep(1)
	driver.find_element_by_id('com.android.calculator2:id/clr').click()

#除0运算
def Div_zero():
	print("除0运算")
	driver.find_element_by_id('com.android.calculator2:id/digit_8').click()
	driver.find_element_by_id('com.android.calculator2:id/op_div').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_0').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("不能除以 0");
	time.sleep(1) 
	el = driver.find_element_by_id('com.android.calculator2:id/del')
	elx = el.location.get("x")
	ely = el.location.get("y")
	driver.tap([(elx,ely)],2000)	#长按按钮2000毫秒

#高级运算
def Sin():
	print("高级运算")
	driver.find_element_by_id('com.android.calculator2:id/fun_sin').click()
	driver.find_element_by_id('com.android.calculator2:id/const_pi').click()
	driver.find_element_by_id('com.android.calculator2:id/op_div').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
	driver.find_element_by_id('com.android.calculator2:id/rparen').click()
	driver.find_element_by_id('com.android.calculator2:id/op_sub').click()
	driver.find_element_by_id('com.android.calculator2:id/fun_cos').click()
	driver.find_element_by_id('com.android.calculator2:id/const_pi').click()
	driver.find_element_by_id('com.android.calculator2:id/op_div').click()
	driver.find_element_by_id('com.android.calculator2:id/digit_4').click()
	driver.find_element_by_id('com.android.calculator2:id/rparen').click()
	driver.find_element_by_id('com.android.calculator2:id/eq').click()
	Compared("0");
	time.sleep(1)
	driver.find_element_by_id('com.android.calculator2:id/clr').click()

#断言,判断结果
def Compared(value):
	s = 'com.android.calculator2:id/result'
	if driver.find_element_by_id(s).text != True:
		fm_text = driver.find_element_by_id(s).text
		#print(fm_text)
		if value == "0":
			fm_text = str(math.floor(float(fm_text)))

		if fm_text == value or fm_text == "Can't divide by 0": 
			print("正确")
			
		else:
			print("错误")
			#获取本地时间
			t = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
			#print(t)
			#获取文件所在路径
			path = sys.path[0]
			#print(path)
			if os.path.exists(path+"/Screenshot") == False: #判断是否存在文件夹
			    print("sss")
			    os.makedirs(path+"/Screenshot") #创建文件夹
			screen_save_path = path+"/Screenshot/"+t+'.png'
			#print(screen_save_path)
			driver.get_screenshot_as_file(screen_save_path) #截图并保存

	else:
		print("获取不到数据")


Add()
Sub()
Mul()
Division()
Div_zero()
Sin()

time.sleep(3)
print("脚本运行结束,退出")
driver.quit()
