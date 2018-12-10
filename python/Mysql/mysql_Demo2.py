#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql


config={
    # 'host':'localhost',
    # 'port':'3306',
    'user':'root',
    'password':'123456',
    'database':'data1_db',
}
# 连接mysql
# con = mysql.connector.connect(host='localhost', port=3306, user='root',
#     password='password',database='test_db',charset='utf-8')
con = pymysql.connect(config)
# print(con.connector_id)



