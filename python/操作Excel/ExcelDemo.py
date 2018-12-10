#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

excel_dir = 'F:\\Python_Demo\\python\\WEB编程\\接口测试\\unittest批量执行\\data.xlsx'
data = xlrd.open_workbook(excel_dir)

table = data.sheet_by_name(u'Sheet1')

# 获取单元格
cell_A1 = table.cell(0,0)
# cell_B1 = table.cell(0,1)
print(cell_A1)
# print(cell_B1)

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols
print(nrows)
print(ncols)

# 获取第一行的内容
rows = table.row_values(0)
# print(rows)

# count = 0 
# while True:
#     if table.nrows <= count :
#         break
#     rows = table.row_values(count)
#     print('count=',count,":",rows)
#     count = count + 1

for i in range(table.nrows):
    rows = table.row_values(i)
    # print(rows)



parameter = table.row_values(0) #返回一个list
print(parameter)
print(type(parameter))
# 因为 parameter 变量类型是str 需要用eval函数转换成dict
jsoninfo = eval(parameter[0])
print(jsoninfo)


