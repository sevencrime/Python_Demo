#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
# 连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='data1_db', charset='utf8')
cursor = conn.cursor()
# try:
#     # 创建
#     cursor.execute('create table user (id varchar(20) primary key, name varchar(20), password varchar(20))')
#     # 插入
#     cursor.execute('insert into user (id, name, password) values (%s, %s, %s)', ["1", "onedi","123456"])
# except Exception as e:
#     raise e

cursor = conn.cursor()

# cursor.execute('insert into user values ("112","5","6")')

# 提交事务(执行)
# conn.commit()

cursor.execute('SELECT * FROM user ')

# 返回数据
valuse = cursor.fetchall()
print(valuse)



cursor.close()
conn.close()

