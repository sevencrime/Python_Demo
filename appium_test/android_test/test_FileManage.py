#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from appium.webdriver.common.touch_action import TouchAction
import time
import unittest


class TestFileManage(unittest.TestCase):
    """docstring for TestFileManage"""
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '3GKL20CH95'
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = 'com.android.rk'
        desired_caps['appActivity'] = '.RockExplorer'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 运行android7.0以上必须配置的参数,否则会定位不到ID
        desired_caps['automationName'] = "uiautomator2"
        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

        cls.action = TouchAction(cls.driver)
        cls.driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"Internal Memory\")").click()

        '''''判断toast信息'''   
    def find_toast(self,message):  

        try:
            # 获取message信息
            message = '//*[@text=\'%s\']' %message
            # print(message)

            # Expected_conditions类有很多判断
            # 通过as关键词对expected_conditons重名为EC
            # 调用presence_of_element_located()判断元素是否存在。
            element = WebDriverWait(self.driver,10, 0.4).until(EC.presence_of_element_located((By.XPATH,message)))  
            # print(element.text)
            return element.text
        except Exception as e:
            print("获取toast失败",e)

    # @unittest.skip("do not run test_1")
    # 复制黏贴
    def test_1_paste(self):
        driver = self.driver
        # 定位"Alarms"
        el = driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"Alarms\")")
        # touchaction方法,短按
        self.action.long_press(el).wait(1000).perform()
        # 点击copy
        driver.find_element_by_id("com.android.rk:id/edit_copy_text").click()
        # 点击进入"DCIM"文件夹
        time.sleep(2)
        # driver.find_element_by_xpath(
        #     "//android.widget.TextView[contains(@text,'DCIM')]").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"DCIM\")").click()
        # 点击"editor"
        driver.find_element_by_id("com.android.rk:id/tool_editor").click()
        time.sleep(1)
        # 点击"Paste"
        driver.find_element_by_id("com.android.rk:id/edit_paste_text").click()

        str_toast = self.find_toast('Copy finish !')
        # print(str_toast)
        # time.sleep(2)
        # # 判断文件夹是否复制成功
        # text_list = driver.find_elements_by_class_name(
        #     "android.widget.TextView")
        # str_list = [i.text for i in text_list]
        # self.assertTrue('Alarms' in str_list)
        self.assertTrue('Copy finish !' in str_toast)



    @unittest.skip("do not run test_2_newFolder")
    # 新建文件夹
    def test_2_newFolder(self):
        driver = self.driver
        action = self.action
        # 点击进入Alarms下级菜单
        driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@text,'Alarms')]").click()
        # 获取控件multi
        multi = driver.find_element_by_id(
            "com.android.rk:id/tool_multi_choice")
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
        text_list = driver.find_elements_by_class_name(
            "android.widget.TextView")
        str_list = [i.text for i in text_list]
        self.assertTrue('one' in str_list)

    @unittest.skip("do not run test_3_duplicateFolder")
    def test_3_duplicateFolder(self):
        driver = self.driver
        i = 0
        count = 0
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
                    # print("创建20个文件夹成功")
                    count = i
                    break
        self.assertEqual(count, 20)

    @unittest.skip("do not run test_4")
    def test_4_reName(self):
        driver = self.driver
        action = self.action
        # 定位控件Editor
        editor = driver.find_element_by_id("com.android.rk:id/tool_editor")
        # 定位控件Next
        re_next = driver.find_element_by_id(
            "com.android.rk:id/tool_folder_next")
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
        # for i in range(1, 10):
        #     driver.keyevent(67)
        # 输入文件名
        driver.find_element_by_id(
            "com.android.rk:id/mEdit").clear().set_value("two")
        # 点击确定
        driver.find_element_by_id("android:id/button1").click()
        # 改名后,判断是否修改名字成功
        text_list = driver.find_elements_by_class_name(
            "android.widget.TextView")
        str_list = [i.text for i in text_list]
        self.assertTrue('two' in str_list)

    @unittest.skip("do not run test_5")
    def test_5_Move(self):
        driver = self.driver
        action = self.action
        # 移动文件夹
        # el_2 = driver.find_element_by_xpath(
        #     "//android.widget.TextView[contains(@text,'two')]")
        el_2 = driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"two\")")
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
        text_list = driver.find_elements_by_class_name(
            "android.widget.TextView")
        str_list = [i.text for i in text_list]
        self.assertTrue('Alarms' in str_list)
        self.assertTrue('two' in str_list)

    def dele(self, el):
        # 短按two文件夹
        self.action.long_press(el).wait(1000).release().perform()
        # 点击delete
        self.driver.find_element_by_id(
            "com.android.rk:id/edit_delete_text").click()
        # 点击确定按钮
        self.driver.find_element_by_id("android:id/button1").click()

    @unittest.skip("do not run test_6")
    def test_6_Delete(self):
        driver = self.driver
        #定位etwo文件夹
        # el_two = driver.find_element_by_xpath(
        #     "//android.widget.TextView[contains(@text,'two')]")
        el_two = driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"two\")")
        self.dele(el_two)
        #定位Alarms文件夹
        # el_Alarms = driver.find_element_by_xpath(
        #     "//android.widget.TextView[contains(@text,'Alarms')]")
        el_Alarms = driver.find_element_by_android_uiautomator(
            "new UiSelector().text(\"Alarms\")")
        self.dele(el_Alarms)

        time.sleep(1)
        # 判断
        text_list = driver.find_elements_by_class_name(
            "android.widget.TextView")
        str_list = [i.text for i in text_list]
        # 判断列表中是否删除元素
        self.assertTrue('Alarms' not in str_list)
        self.assertTrue('two' not in str_list)

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return(x, y)

    # 使用touchAction来移动屏幕
    def toachSweip(self, x, y, x1, y1):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).wait(ms=200).move_to(x=x1, y=y1).release()
        action.perform()

    def swipeUp(self):
        # 获取屏幕像素,返回一个数组
        size = self.getSize()
        # 上滑动
        x1 = size[0] * 0.5
        y1 = size[1] * 0.75
        y2 = size[1] * 0.25
        time.sleep(1)
        self.toachSweip(x1, y1, x1, y2)

    @classmethod
    def tearDownClass(cls):

        # driver = cls.driver
        # driver.start_activity("com.android.settings", ".Settings")
        # time.sleep(2)
        # while True:
        #     try:
        #         cls().swipeUp()
        #         time.sleep(3)
        #         driver.find_element_by_xpath(
        #             "//android.widget.TextView[contains(@text,'Languages & input')]").click()
        #     except Exception as e:
        #         print(e)
        #         # driver.page_source 获取页面所有元素
        #         str_page_source = driver.page_source
        #         # 判断是否滑动到页面底部,滑到底部后,向上滑动寻找元素
        #         if str_page_source.find('About device') == -1:
        #             break
        #     else:
        #         driver.find_element_by_xpath(
        #             "//android.widget.TextView[contains(@text,'Languages & input')]").click()
        #         driver.find_element_by_xpath(
        #             "//android.widget.TextView[contains(@text,'Languages & input')]").click()
        #         break

        time.sleep(5)
        print("脚本运行结束,退出")
        cls.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFileManage))
    runner = unittest.TextTestRunner(verbosity=2).run(suite)

    '''
    with open('HTMLReport.html', 'wb+') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)
    '''
