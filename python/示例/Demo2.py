#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 20:56:22
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import xlrd 

excel_dir = 'F:/Python_Demo/excelddtdriver/case/debug_api.xlsx'
data = xlrd.open_workbook(excel_dir)
table = data.sheet_by_name(u'Sheet1')
nrows = table.nrows
ncols = table.ncols
keys = table.row_values(0)
# print(keys)
# print(keys[1])


# 创建一个空字典，往字典里面加入键值对
# 其中，键excel中每一列的表示作为名字，value用下面用例的值
# 用循环来遍历出所有的用例
# 最后吗，把字典加入一个列表，形成一个二维数组

r = []
j = 1
for i in range(nrows):
	s = {}
	# print(i)
	value = table.row_values(j)
	# print(value)
	s[keys[1]] = value[1]
	s[keys[2]] = value[2]
	print(s)
	print(len(s))
	r.append(s)
	# print(r)

