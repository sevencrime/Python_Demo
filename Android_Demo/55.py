#coding=utf-8
from appium import webdriver
import time, os, re

platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

desired_caps = {
    'platformName': 'Android',
    'platformVersion': platformVersion,
    'deviceName': deviceId,
    'appPackage': 'io.newtype.eddid.app',
    'appActivity': 'com.bartech.app.main.launcher.LauncherActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver.find_element_by_id("digit_1").click()

# driver.find_element_by_id("op_add").click()

# driver.find_element_by_id("digit_2").click()

# driver.find_element_by_id("eq").click()
time.sleep(10)

driver.quit()