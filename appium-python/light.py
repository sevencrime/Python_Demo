#! /usr/bin/env python
# -*- coding: utf-8 -*-

#閃光燈压力
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'C8W7KVIEQY'
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'com.android.camera2'
desired_caps['appActivity'] = 'com.android.camera.CameraLauncher'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.find_element_by_id("com.android.camera2:id/flash_indicator").click()
driver.find_element_by_id("com.android.camera2:id/flash_toggle_button").click()
driver.find_element_by_id("com.android.camera2:id/flash_toggle_button").click()
num = 1
while 1:
	num = num + 1
	print(num)
	driver.find_element_by_id("com.android.camera2:id/shutter_button").click()
	time.sleep(3)

driver.quit()

