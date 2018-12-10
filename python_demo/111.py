#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-28 14:47:32
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import requests
import demjson


def userLogin(s) :

	data = {
		'appid' : 'www' ,
		'loginKey' : '15089514626' ,
		'loginPwd' : '1q2w3e4r5t' ,
		'type' : '0'
	}
	# 请求登录接口
	resp = s.post(localhost+'RmarketShop/account/userLogin.html',data=data).json()
	print("接口userLogin的页面返回信息为: \r",resp)
	resp['data'].pop('loginTime')

	return resp['data']

def addCommodity(s, token_main):

	data = {
		'subtitle': '瘦肉瘦肉粥',
	    'storage': 28,
	    'shelf_life': 30,
	    'part': 42,
	    'merchant_phone': '15089514626',
	    'merchant_name': '龙傲天123',
	    'is_save': 1,
	    'is_bear': 1,
	    'inventory_warning': 5,
	    'id': -1,
	    'detailed_address': '瘦肉瘦肉粥瘦肉瘦肉粥',
	    'delivery_field3': 441702,
	    'delivery_field2': 441700,
	    'delivery_field1': 440000,
	    'commoditySupply': {
	        "provinceId": 110000,
	        "cityIds": [
	            110100
	        ]
	    },
	    'commodityQualification': {
	        "id": "-1",
	        "url": "http://192.168.1.6:888/test/other/2018-08-28/67d1d58d-acc5-47c2-bcfb-4630d8a04073.zip",
	        "filename": "ScreenToGif+2(到知乎送个赞呗~).zip",
	        "ade": "0"
	    },
	    'commodityPicture': {
	        "id": "-1",
	        "picture_url": "http://192.168.1.6:888/test/goods/2018-08-28/8f02a07a-fdca-4002-88c4-785328b309d9.jpg",
	        "ade": "0"
	    },
	    'commodityNorms': {
	        "id": "-1",
	        "norms": "100",
	        "inventory": "100",
	        "price": "10",
	        "sales_quantity": "1",
	        "weight": "1.6",
	        "ade": "0"
	    },
	    'commodity_name': '瘦肉瘦肉粥',
	    'commodity_icon': 'http: //192.168.1.6: 888/test/goods/2018-08-28/8f02a07a-fdca-4002-88c4-785328b309d9.jpg',
	    'commodity_describe': '这是商品描述麻蛋不要错了',
	    'class_field1' : 19,
	    'class_field2' : 20,
	    'appid': 'www'

	}

	data.update(token_main)
	print("data的长度为:",len(data))

	r = s.post(localhost+'RmarketShop/Commodity/addCommodity.html',data=data)
	print("接口queryAccountInfo的页面返回信息为: \r",r.content.decode('utf-8'))



if __name__ == "__main__" :
	localhost = 'http://192.168.1.3:8081/'
	# 创建一个session
	s = requests.session()

	token_main = userLogin(s)

	addCommodity(s, token_main)