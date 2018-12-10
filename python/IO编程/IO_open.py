#!/usr/bin/env python
# -*- coding: utf-8 -*-

path = 'F:/Python_Demo/python'
# try写法
# try:
#     f = open (path+'/1.txt','r',encoding = 'utf-8')
#     str_f = f.read()
#     print(str_f)
# except Exception as e:
#     raise
# else:
#     pass
# finally:
#     f.close()

# 使用with关键字

with open(path+'/1.txt' , 'a+' , encoding = 'utf-8') as f :
    f.seek(0)
    f.write("h3333333333")
    f.seek(0)
    print(f.read())






