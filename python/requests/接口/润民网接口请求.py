#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-23 17:17:24
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests




def userLogin(s) :

	data = {
		'appid' : 'www' ,
		'loginKey' : '15000000088' ,
		'loginPwd' : 'ss123456' ,
		'type' : '0'
	}
	# 请求登录接口
	r = s.post(localhost+'RmarketShop/account/userLogin.html',data=data)
	resp = r.json()
	print("接口userLogin的页面返回信息为: \r",resp)
	resp['data'].pop('loginTime')

	return resp['data']

# def queryAccountInfo(s,token_main) :

# 	data = {}
# 	data.update(token_main)
# 	data['appid'] = 'www'
# 	# print(data)

# 	resp = s.post(localhost+'RmarketShop/account/queryAccountInfo.html',data=data).json()
# 	# print("接口queryAccountInfo的页面返回信息为: \r",resp)


# def findMyCommodity(s,token_main):

# 	data = {}
# 	data.update(token_main)
# 	data['update_time_start'] = '2018-08-30 00:00:00'
# 	data['update_time_end'] = '2018-09-03 23:59:59'
# 	data['appid'] = 'www'
# 	data['type'] = 0
# 	print(data)

# 	resp = s.post(localhost+'RmarketShop/Commodity/findMyCommodity.html',data=data).json()

# 	# print('接口findMyCommodity返回的信息为: \r',resp)

# def findMyOrder(s,token_main):

# 	data = {}
# 	data.update(token_main)
# 	data['appid'] = 'www'
# 	data['type'] = 0
# 	# data['commodity_name'] = '测试商品支付'
# 	# data['commodity_id'] = 'CP0785'
# 	# data['order_time_start'] = '2018-08-20 00:00:00'
# 	# data['order_time_end'] = '2018-09-03 23:59:59'

# 	resp = s.post(localhost+'RmarketShop/StoreCommodityOrder/findMyOrder.html',data=data).json()
# 	print('接口findMyOrder的返回信息为: \r',resp)




if __name__ == "__main__" :
	localhost = 'http://192.168.1.3:8081/'
	# 创建一个session
	s = requests.session()

	token_main = userLogin(s)

	# queryAccountInfo(s,token_main)
	# findMyCommodity(s,token_main)
	# findMyOrder(s,token_main)



