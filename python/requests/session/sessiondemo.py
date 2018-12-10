#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

'''
# 创建一个session对象 
s = requests.Session()
# 用session对象发出get请求，设置cookies 
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')  
# 用session对象发出另外一个get请求，获取cookies
r = s.get("http://httpbin.org/cookies")  
# 显示结果  
print(r.text)
'''

s = requests.Session()

s.auth = ('user', 'pass')  

s.headers.update({'x-test': 'true'})

r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'}) 

print(r.request.headers)



