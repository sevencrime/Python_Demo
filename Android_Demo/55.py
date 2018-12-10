#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '3709b61'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("digit_1").click()

driver.find_element_by_id("op_add").click()

driver.find_element_by_id("digit_2").click()

driver.find_element_by_id("eq").click()


driver.quit()