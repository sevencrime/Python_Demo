#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-29 14:01:07
# @Author  : onedi (onedi@qq.com)

import requests
import test_case.reads
import operator
from commans.Check_result import Check_result
import commans.Logging
from retrying import retry
from Dao.MysqlHelper import MysqlHelper

# 检验数据是否插入了数据库,用请求参数和数据库对比数据是否一致


#请求接口
class requests_test():

	logger = commans.Logging.logs()		#实例化logging
	P_actual = {}	#存放上个请求的resp
	def __init__(self):
		self.ms = MysqlHelper()
		self.res = {}

	#处理testdata
	def getData(self, s, testdata, token_main):

		# print(testdata)
		rowNum = testdata['rowNum']
		method = testdata['method']		#从excel读取method
		url = testdata['address']		#从excel中读取url
		expected = testdata['expected']		#从excel中读取期望结果
		#从excel中获取headers，判断是否为空
		try:
		    headers = eval(testdata["headers"])
		    # print("请求头部：%s"  %headers)
		except:
		    headers = None

		try:
			body = eval(testdata['data'])		#从excel中获取data，转换为json格式
		except:
			body = None

		#处理body中的sql语句
		for k,v in body.items():
			if k == 'mainKey':
				body[k] = token_main['mainKey']

			elif k == 'tokenKey':
				body[k] = token_main['tokenKey']

			elif isinstance(v, str):

				if "SELECT" in v or "select" in v:
					body[k] = '{}'.format(self.ms.Link(v))

				elif "insert" in v or "INSERT" in v or "update" in v or "UPDATE" in v or "delete" in v or "DELETE" in v :
					body[k] = '{}'.format(self.ms.change(v))

		#处理期望结果中的sql语句
		# import ast
		# for k,v in ast.literal_eval(expected).items():
		# 	if isinstance(v, str) or isinstance(v, dict):
		# 		if isinstance(v, dict):
		# 			for key,value in v.items():
		# 				if "SELECT" in v or "select" in v:
		# 					expected[k][key] = '{}'.format(self.ms.Link(value))
		# 				elif "insert" in v or "INSERT" in v or "update" in v or "UPDATE" in v or "delete" in v or "DELETE" in v :
		# 					expected[k][key] = '{}'.format(self.ms.change(value))

		# 		elif "SELECT" in v or "select" in v:
		# 			expected[k] = '{}'.format(self.ms.Link(v))
		# 		elif "insert" in v or "INSERT" in v or "update" in v or "UPDATE" in v or "delete" in v or "DELETE" in v :
		# 			expected[k] = '{}'.format(self.ms.change(v))



		self.res['rowNum'] = rowNum

		self.logger.info("***************正在执行第 %s 条用例******************" %(rowNum-1))
		self.logger.info("请求方式: {} ".format(method))
		self.logger.info("请求接口: {}".format(url))
		self.logger.info("请求参数: {} \r".format(body))
		self.res = self.request(s, method, url, headers, body, expected)

		return self.res

	#开始请求，得到response
	@retry(stop_max_attempt_number=5)	#失败重新请求5次
	def request(self, s, method, url, headers, body, expected):

		try:

			# requets请求
			response = s.request(method=method,
				             url=url,
				             headers=headers,
				             data=body			#post请求参数
			                )

			resp = response.json()

			self.P_actual = resp 	#存放resp

			self.logger.info("********************** 判断结果 *************************\r")

			# 调用Check_result判断用例结果
			self.check = Check_result()
			arr = self.check.cmps(resp, eval(expected), 0)

			if arr == [] :
				self.logger.error('用例测试通过\r')
			else :
				self.logger.error('用例测试失败')
				self.logger.error('失败原因: %s \r' %arr)

			self.logger.info("***********************************************************\r \r ")

			self.res['times'] = response.elapsed.total_seconds()		#请求时间
			self.res['actual'] = resp
			self.res['msg'] = arr
			if arr == [] :
				self.res['result'] = 'Pass'
			else:
				self.res['result'] = 'Fail'


			return self.res

		except :
			self.logger.error("接口请求失败,请检查地址和参数")



if __name__ == "__main__":
	testdata = reads.reads().read()
	session = requests.session()
	rt = requests_test()
	rt.request(session, testdata)
