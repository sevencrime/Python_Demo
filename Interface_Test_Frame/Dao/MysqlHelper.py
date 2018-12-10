#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-13 11:06:35
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$


import pymysql

class MysqlHelper:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    database='data1_db',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    #数据库关闭
    def __del__(self):
        self.cursor.close()
        self.conn.close()


    #增删改操作
    def change(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("操作数据库成功")
        except :
            print("操作数据库失败!请检查sql语句")


    #查询数据库
    def Link(self,sql):
        try:
            self.cursor.execute(sql)
            print("查询成功")
            values = self.cursor.fetchone()
            for v in values:
                return v
        except :
            print("查询失败!请检查sql语句")
