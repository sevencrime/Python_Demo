#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

str1 = 'from=zh&to=en&query=%E6%88%91%E7%88%B1%E4%BD%A0&transtype=translang&simple_means_flag=3&sign=47194.285547&token=e0fff96448bbc2f9c972301c0a595a76'

list1 = str1.split('&')

temp = []

dict1 = {}
for i in range(0,len(list1)):
    temp = list1[i].split('=')
    print(temp)
    dict1[temp[0]] = temp[1]

# print(dict1)
json1 = json.dumps(dict1)
# print(type(json1))
# print(json1)

header = ''

host = 'http://fanyi.baidu.com/v2transapi'

response = requests.post(host, data=json1).json()

print(response)
