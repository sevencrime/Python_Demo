#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'C8W7KVIEQY'
desired_caps['noReset'] = True
desired_caps['appPackage'] = 'lecar.android.view'
desired_caps['appActivity'] = '.splash.LCSplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['automationName'] = "uiautomator2"

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(5)

#点击定位弹框
# driver.find_element_by_id('lecar.android.view:id/right_btn').click()
#点击定位弹框
driver.find_element_by_id('lecar.android.view:id/lef_btn').click()

#点击热门活动选项
# driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'热门活动')]").click()
# time.sleep(3)

'''
#打开H5界面后,获取所有环境
contexts = driver.contexts
# print(contexts)
#切换到webview,           switch_to() 切换环境
driver.switch_to.context(contexts[1])
#获取当前环境,看是否切换成功
# now = driver.current_context
# print(now)

weblist = driver.find_elements_by_class_name('form-wrap')
weblist[1].click()
time.sleep(3)
#切换回APP
driver.switch_to.context(contexts[0])
'''

#定位底下的4S按钮
driver.find_element_by_android_uiautomator(
    'new UiSelector().text("4S店").resourceId("lecar.android.view:id/tab_txt")').click()

driver.find_element_by_xpath('//android.widget.TextView[contains(@text,"推荐排序")]').click()


time.sleep(3)
print("脚本运行结束,退出")
driver.quit()






