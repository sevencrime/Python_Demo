# coding: GBK


#ע��

import os 
import sys
'''
print(os.name)# �鿴����ϵͳ
print(os.environ)#�鿴ϵͳ��������
print(os.path.abspath('.')) #�鿴��ǰ�ļ���·��
#os.mkdir('F:\Python_Demo/1',0755)
print(os.path.exists("F:\Python_Demo"))
print(os.path.exists("F:/Python_Demo/1.py"))

print(os.listdir("F:\Python_Demo"))#�г���Ŀ¼�µ��ļ���

print(os.getcwd())  #��ȡ��ǰ�ļ�Ŀ¼
'''


#�����ļ���
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
#�ж��ļ����Ƿ����
if os.path.exists(path+"/Screenshot") == False:
    print("sss")
    os.makedirs(path+"/Screenshot")

'''

import time

print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))


print(os.path.abspath(''))














