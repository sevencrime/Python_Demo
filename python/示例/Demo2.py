#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 20:56:22
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$



import time
import datetime
# time='Mon, 18 Apr 2016'
# time_format=datetime.datetime.strptime(time,'%a, %d %b %Y')

time1='Mon, 22 Apr 2019 09:21:48'
time_format=datetime.datetime.strptime(time1,'%a, %d %b %Y %H:%M:%S')
print(time_format)

time='Mon, 22 Apr 2019 20:21:48 +0000'
zone = time[-5:]    #Ê±Çø
receivetime = datetime.datetime.strptime(time[:-5], '%a, %d %b %Y %H:%M:%S ')  
print(receivetime)


# a = '+8000'
# print(int(a)-int(zone))

print()

print(datetime.datetime.now())

