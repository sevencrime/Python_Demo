#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.client

conn = http.client.HTTPSConnection('sp0.baidu.com')
# request('请求方式','请求内容')
conn.request('GET','/8bg4cTva2gU2pMbgoY3K/bdime.html?prd=www.baidu.com')
response = conn.getresponse()
temp = response.read()
conn.close()
print(temp)

