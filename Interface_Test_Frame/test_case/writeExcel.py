#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-13 21:22:12
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import xlrd,xlwt
from xlutils.copy import copy
from config.read_conf import read_conf
import time
import os

class writeExcel:

	index = 0

	def __init__(self):
		self.path = read_conf().read()		#获取用例路径
		if self.index == 0 :
			self.index += 1
			print("index:",self.index)
			self.rb = xlrd.open_workbook(self.path,formatting_info=True)
			self.wb = copy(self.rb)
			self.sheet = self.wb.get_sheet(0)

	def write(self, res):

		style = xlwt.XFStyle()
		# 设置font字体
		font = xlwt.Font()
		alignment = xlwt.Alignment()
		font.name = '宋体'	#字体样式
		font.bold = True	#粗体
		alignment.horz = 0x01
		alignment.vert = 0x00
		alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT # 自动换行
		style.alignment = alignment

		self.sheet.write((res['rowNum']-1), 12, str(res['times']),style)

		if res['result'] == 'Pass':
			#修改字体颜色
			font.colour_index = 3
			style.font = font
			#修改单元格背景色
			# style1 = xlwt.easyxf('pattern: pattern solid, fore_color light_green;')
		elif res['result'] == 'Fail':
			#修改字体颜色
			font.colour_index = 2
			style.font = font
			#修改单元格背景色
			# style1 = xlwt.easyxf('pattern: pattern solid, fore_color red;')
		else :
			#暂定
			pass
		self.sheet.write((res['rowNum']-1), 9, str(res['result']),style)
		self.sheet.write((res['rowNum']-1), 10, str(res['msg']),style)
		self.sheet.write((res['rowNum']-1), 11, str(res['actual']),style)

		t = time.strftime('%Y%m%d_%H%M',time.localtime(time.time()))
		self.wb.save(os.getcwd()+'/report/report_%s.xls' %t)

if __name__ == '__main__':

	res = {'rowNum': 2, 'times': 0.173775, 'actual': {'code': 0, 'msg': 'SUCCESS', 'data': {'mainKey': 'X+LmRVMzop8o5B1u5DhlycGIA1bYoytmki7ZY4G0Ox8=', 'tokenKey': 'C449DED168E653178630DEDACABB8157', 'loginTime': '2018-09-11 15:58:21'}}, 'msg': ['msg:SUCCESS'], 'result': 'Fail'}
	sheet_wb = writeExcel().copyFile()
	writeExcel().write(res, sheet_wb[0], sheet_wb[1])