#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

if __name__ == '__main__':

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'C8W7KWY897'
    desired_caps['noReset'] = True
    desired_caps['appPackage'] = 'com.android.rk'
    desired_caps['appActivity'] = '.RockExplorer'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote(
        'http://localhost:4723/wd/hub', desired_caps)

    current = driver.contexts

    print(current)
