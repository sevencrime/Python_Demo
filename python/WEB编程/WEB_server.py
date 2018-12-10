#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 运行WSGI服务器

# 导入wsgiref
from wsgiref.simple_server import make_server
from WEB_Demo1 import AppClass,application

# 创建一个服务器,地址为'',端口为8000, 处理函数是application
# httpd = make_server('', 8000, application)
httpd = make_server('', 8000, AppClass)

print('Serving Http on port 8000 ... ')

httpd.serve_forever()



