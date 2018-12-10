#! /usr/bin/env python
# -*- coding: utf-8 -*-

# file_manager文件管理

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


def dele(el):
    # 短按two文件夹
    action.long_press(el).wait(1000).release().perform()
    # 点击delete
    driver.find_element_by_id("com.android.rk:id/edit_delete_text").click()
    # 点击确定按钮
    driver.find_element_by_id("android:id/button1").click()


def re_Delete():
    el_two = driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'two')]")
    el_Alarms = driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Alarms')]")

    dele(el_two)
    dele(el_Alarms)

    # 判断
    text_list = driver.find_elements_by_class_name("android.widget.TextView")
    str_list = []
    for i in text_list:
        str_list.append(i.text)
    # 判断列表中是否够元素
    if 'two' not in str_list and 'Alarms' not in str_list:
        print("删除文件夹成功")


# 移动文件夹
def re_Move():
    # 移动文件夹
    el_2 = driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'two')]")
    # touchaction方法,短按
    action.long_press(el_2).wait(1000).release().perform()
    # 点击Move
    driver.find_element_by_id("com.android.rk:id/edit_move_text").click()
    # 点击levelUP
    driver.find_element_by_id("com.android.rk:id/tool_level_up").click()
    # 点击Editor
    driver.find_element_by_id("com.android.rk:id/tool_editor").click()
    # 点击Paste
    driver.find_element_by_id("com.android.rk:id/edit_paste_text").click()
    # 判断
    text_list = driver.find_elements_by_class_name("android.widget.TextView")
    str_list = []
    for i in text_list:
        str_list.append(i.text)
    # 判断列表中是否够元素
    if 'two' in str_list and 'Alarms' in str_list:
        print("移动文件夹成功")

# 移动文件夹


def re_Name():
    # 定位控件Editor
    editor = driver.find_element_by_id("com.android.rk:id/tool_editor")
    # 定位控件Next
    re_next = driver.find_element_by_id("com.android.rk:id/tool_folder_next")
    # 移动
    action.press(editor).wait(300).move_to(re_next).release().perform()
    # 点击Home
    driver.find_element_by_id("com.android.rk:id/tool_home").click()
    # 进入Internal Memory
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Internal Memory')]").click()
    # 进入DCIM
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'DCIM')]").click()
    # 点击Alarms进入下级菜单
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Alarms')]").click()
    # 定位文件夹
    el = driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'one')]")
    # touchaction方法,短按
    action.long_press(el).wait(1000).release().perform()
    # 点击Rename
    driver.find_element_by_id("com.android.rk:id/edit_rename_text").click()
    # 定位文本框
    edit = driver.find_element_by_id("com.android.rk:id/mEdit").click()
    # 退格
    for i in range(1, 10):
        driver.keyevent(67)
    # 输入文件名
    driver.find_element_by_id("com.android.rk:id/mEdit").set_value("two")
    # 点击确定
    driver.find_element_by_id("android:id/button1").click()
    # 改名后,判断是否修改名字成功
    text_list = driver.find_elements_by_class_name("android.widget.TextView")
    for i in text_list:
        if i.text == "two":
            print("文件夹改名成功")
            break


# 创建20个文件夹
def Duplicate_folder():
    i = 0
    while 1:
        i = i + 1
        try:
            # 进入下级目录
            driver.find_element_by_id("com.android.rk:id/nor_text").click()
        except Exception as e:
            # 定位NewFolder控件并点击
            newFolder = driver.find_element_by_id(
                "com.android.rk:id/tool_new_folder").click()
            edit = driver.find_element_by_id(
                "com.android.rk:id/newdirEdit").set_value("one")
            # 点击按钮OK
            driver.find_element_by_id(
                "com.android.rk:id/newdir_dialog_ok").click()
        else:
            # 定位NewFolder控件并点击
            newFolder = driver.find_element_by_id(
                "com.android.rk:id/tool_new_folder").click()
            # 定位文本框并输入文件名
            edit = driver.find_element_by_id(
                "com.android.rk:id/newdirEdit").set_value("one")
            # 点击按钮OK
            driver.find_element_by_id(
                "com.android.rk:id/newdir_dialog_ok").click()
        finally:
            # print(i)
            if i >= 2:
                print("创建20个文件夹成功")
                break


# 新建文件夹
def newFolder():
    # 点击进入Alarms下级菜单
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Alarms')]").click()
    # 获取控件multi
    multi = driver.find_element_by_id("com.android.rk:id/tool_multi_choice")
    home = driver.find_element_by_id("com.android.rk:id/tool_home")
    # 向左滑动,使用touchaction
    action.press(multi).wait(300).move_to(home).release()
    action.perform()
    # 定位NewFolder控件并点击
    newFolder = driver.find_element_by_id(
        "com.android.rk:id/tool_new_folder").click()
    # 定位文本框并输入文件名
    edit = driver.find_element_by_id(
        "com.android.rk:id/newdirEdit").send_keys("one")
    # 点击按钮OK
    driver.find_element_by_id("com.android.rk:id/newdir_dialog_ok").click()
    # 判断newfolder是否创建成功
    text_list = driver.find_elements_by_class_name("android.widget.TextView")
    for i in text_list:
        if i.text == "one":
            print("新建文件夹成功")
            break

    # 重复创建
    Duplicate_folder()

# 复制粘贴


def paste():
    # 定位"Alarms"
    el = driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Alarms')]")
    # touchaction方法,短按
    action.long_press(el).wait(1000).perform()
    # 点击copy
    driver.find_element_by_id("com.android.rk:id/edit_copy_text").click()
    # 点击进入"DCIM"文件夹
    time.sleep(3)
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'DCIM')]").click()
    # 点击"editor"
    driver.find_element_by_id("com.android.rk:id/tool_editor").click()
    # 点击"Paste"
    driver.find_element_by_id("com.android.rk:id/edit_paste_text").click()
    # 判断文件夹是否复制成功
    text_list = driver.find_elements_by_class_name("android.widget.TextView")
    for i in text_list:
        if i.text == "Alarms":
            print("复制文件夹成功")
            break


# 进入Internal Memory
def Internal():
    # 进入Internal Memory
    driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@text,'Internal Memory')]").click()

    paste()  # 复制粘贴
    newFolder()  # 新建文件夹
    re_Name()  # 重命名文件夹
    re_Move()  # 移动文件夹
    re_Delete()  # 删除文件夹

if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = 'C8W7K6JZSX'
    desired_caps['noReset'] = True
    desired_caps['appPackage'] = 'com.android.rk'
    desired_caps['appActivity'] = '.RockExplorer'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    action = TouchAction(driver)
    Internal()

    # 关闭appium服务
    time.sleep(5)
    print("脚本运行结束,退出")
    driver.quit()
