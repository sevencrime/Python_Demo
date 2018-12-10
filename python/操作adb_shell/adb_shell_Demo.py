#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    使用此脚本,需要打开需要测试的APK启动页面

'''


import os
import re
import time

class App_performance():

    def __init__(self):
        self.test = ""   #定义一个字符串用于保存cmd的数据
        #获取当前页面的包名和类名
        test = os.popen('adb shell dumpsys activity | findstr "mFocusedActivity"').read()
        #获取包名package
        self.package = re.findall('com.+?(?=/)', test)
        #获取类名activity
        self.activity = re.findall('com.+?(?=\s)', test)
        print("当前测试应用的包名为:",self.package,self.activity)

    #启动时间:冷启动
    def cold_start_Time(self):
        #停止APP进程,用于测试冷启动
        # os.popen('adb shell am force-stop ' + ''.join(self.package))
        time.sleep(1)
        #测试启动时间ThisTime -W:等待启动完成 -S:在开始活动之前强制停止目标应用程序。
        self.test = os.popen("adb shell am start -S -W -n " + ''.join(self.activity)).read()
        # print(self.test)
        startTime = self.getStartTime(self.test)
        print("冷启动时间为:",startTime)

    #启动时间,热启动
    def hot_start_Time(self):
        #按HOME键,测试热启动
        os.popen('adb shell input keyevent 3')
        time.sleep(1)
        #测试启动时间ThisTime
        self.test = os.popen("adb shell am start -W -n " + ''.join(self.activity)).read()
        # print(self.test)
        hotTime = self.getStartTime(self.test)
        print("热启动时间为:",hotTime)

    #用于获取启动时间
    def getStartTime(self,test):
        #使用正则提取ThisTime
        ThisTime = re.findall('Th.+e.+', self.test)
        #判断是否获取到了启动时间
        if ThisTime == [] :
            print(ThisTime,"请检查ADB连接状态")
        else:
            return ThisTime
            time.sleep(2)

    #测试app的CPU占用率
    def cpuinfo(self):

        test = os.popen('adb shell dumpsys meminfo '+''.join(self.package)).read()
        # print(test)
        #使用正则获取总内存大小
        # cpu_msg = re.findall('TO..L:.+?(?=T)', test.replace(' ',''))
        cpu_msg = re.findall('TO..L.{11}', test)
        # print(cpu_msg)
        # cpu_msg = re.findall('TO..L.+', test.replace(' ',''))
        # print(cpu_msg)
        print("APP的内存占用大小:", ''.join(cpu_msg))


if __name__ == '__main__' :
    app_per = App_performance() #实例化类App_performance
    app_per.cold_start_Time()   #获取冷启动时间
    app_per.hot_start_Time()    #获取热启动时间
    app_per.cpuinfo()             #CPU占用














