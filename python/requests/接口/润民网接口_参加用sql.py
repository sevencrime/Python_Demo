#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-23 17:17:24
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import pymysql

def getData(str1):

	conn = pymysql.connect(user='root', password='123456', database='data1_db')
	cursor = conn.cursor()

	try:
		cursor.execute(str1)
		values = cursor.fetchone()
		for v in values:
			return v
	except Exception as e:
		# raise e
		print("SQL语句出错")
	finally:
		cursor.close()
		conn.close()


def userLogin(s) :

	# data = {
	# 	'appid' : 'www' ,
	# 	'loginKey' : '{}'.format(getData('select name from user where id = 1'))  ,
	# 	'loginPwd' : '{}'.format(getData('select password from user where id = 1')) ,
	# 	'type' : '0'
	# }


	data = {
		'appid' : 'www' ,
		'loginKey' : 'SELECT name FROM user WHERE id = 1'  ,
		'loginPwd' : 'SELECT password FROM user WHERE id = 1' ,
		'type' : '0'
	}

	for k,v in data.items():

		if "SELECT" in v or "select" in v:
			print("sssss")
			data[k] = '{}'.format(getData(v))
		elif "insert" in v or "INSERT" in v or "update" in v or "UPDATE" in v or "delete" in v or "DELETE" in v :



	print(data)
	# 请求登录接口
	# resp = s.post(localhost+'RmarketShop/account/userLogin.html',data=data).json()
	# print("接口userLogin的页面返回信息为: \r",resp)
	# resp['data'].pop('loginTime')

	# return resp['data']







if __name__ == "__main__" :
	localhost = 'http://192.168.1.3:8081/'
	# 创建一个session
	s = requests.session()

	token_main = userLogin(s)
	print(token_main)

	# queryAccountInfo(s,token_main)
	# findMyCommodity(s,token_main)
	# findMyOrder(s,token_main)



