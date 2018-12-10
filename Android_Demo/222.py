#!/usr/bin/env python 
# _*_ coding:utf-8 _*_
#coding=utf-8  

'''
Created on Oct 20, 2014

@author: deldong
'''
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

logFile = open("C:\\monkeyrunner_log.txt","a+")

device = MonkeyRunner.waitForConnection()
if not device:
    print("Please connect a device to start!")
    logFile.write("Please connect a device to start!\n")
else:
    print("Device Connected successfully!")
    logFile.write("Device Connected successfully!\n")
    
package = 'com.android.calculator2' 
activity = 'com.android.calculator2.Calculator'
runComponent = package + '/' + activity

print("Start calculator")
logFile.write("Start calculator")
device.startActivity(component=runComponent)

print("Wait 15s")
logFile.write("Wait 15s")
MonkeyRunner.sleep(5)

print("Get widget object")
logFile.write("Get widget object")
hierarchyviewer = device.getHierarchyViewer()

viewDigit8 = hierarchyviewer.findViewById("id/digit_8")
viewDigit9 = hierarchyviewer.findViewById("id/digit_9")
viewMul = hierarchyviewer.findViewById("id/op_mul")
viewEqual = hierarchyviewer.findViewById("id/eq")

print(viewDigit8)

print("Get location of view")
logFile.write("Get location of view")
pointViewDigit8 = hierarchyviewer.getAbsoluteCenterOfView(viewDigit8)
pointViewDigit9 = hierarchyviewer.getAbsoluteCenterOfView(viewDigit9)
pointViewMul = hierarchyviewer.getAbsoluteCenterOfView(viewMul)
pointViewEqual = hierarchyviewer.getAbsoluteCenterOfView(viewEqual)

print("touch 8*9=")
logFile.write("touch 8*9=")
MonkeyRunner.sleep(5)

print(pointViewDigit8);
print(pointViewDigit8.x);

device.touch(pointViewDigit8.x,pointViewDigit8.y,MonkeyDevice.DOWN_AND_UP)
device.touch(pointViewMul.x,pointViewMul.y,MonkeyDevice.DOWN_AND_UP)
device.touch(pointViewDigit9.x,pointViewDigit9.y,MonkeyDevice.DOWN_AND_UP)
device.touch(pointViewEqual.x,pointViewEqual.y,MonkeyDevice.DOWN_AND_UP)

logFile.close()

