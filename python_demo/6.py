# coding: GBK


#注释

import os 
import sys
'''
print(os.name)# 查看操作系统
print(os.environ)#查看系统环境变量
print(os.path.abspath('.')) #查看当前文件的路径
#os.mkdir('F:\Python_Demo/1',0755)
print(os.path.exists("F:\Python_Demo"))
print(os.path.exists("F:/Python_Demo/1.py"))

print(os.listdir("F:\Python_Demo"))#列出该目录下的文件名

print(os.getcwd())  #获取当前文件目录
'''


#创建文件夹
#os.makedirs('e:/assist/set')
'''
#os.makedirs('F:/Python_Demo/Screenshot')
print(os.path.exists("F:/Python_Demo/Screenshot"))
print(os.getcwd()) 

print(type(path))
print(os.path.exists(path+"/Screenshot"))
#print(path+"/Screenshot")
'''

'''
path = os.getcwd()
#判断文件夹是否存在
if os.path.exists(path+"/Screenshot") == False:
    print("sss")
    os.makedirs(path+"/Screenshot")

'''

import time

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))


print(os.path.abspath(''))














