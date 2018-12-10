#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-08 19:53:07
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import xlrd
import sys
sys.path.append("..")
from config.read_conf import read_conf

class reads:

	def read(self):

		path = read_conf().read()
		# print(path)
		# 打开excel文件,open_workbook(path),path为excel所在的路径
		workbook = xlrd.open_workbook(path)
		# 打开excel表,这里表示打开第一张表
		table = workbook.sheets()[0]

		nrows = table.nrows		# 获取excel的行数
		# print(nrows)
		ncols = table.ncols		#获取excel的列数
		# print(ncols)
		keys = table.row_values(0)		#获取第一行的值
		# print(keys)

		resp = []		#创建一个list，用于存放

		x = 1
		for i in range(nrows-1):
			s = {}
			# print(i)
			s['rowNum'] = i+2 	#加入用例的行数，用户后面写入数据
			values = table.row_values(x)
			# print(values)
			for j in range(ncols):
				# print('j=',j)
				s[keys[j]] = values[j]
			# print(s)
			resp.append(s)
			x += 1

		return resp

if __name__ == "__main__":
	path = 'E:/郑某人/Python_Demo/Interface_Test_Frame/data/data.xls'
	reads = reads()

	resp = reads.read()
	print(resp)
	# print(resp[0]['expected'])
