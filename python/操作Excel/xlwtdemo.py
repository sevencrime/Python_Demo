#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
import datetime

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet,参数为sheet名
worksheet = workbook.add_sheet('My worksheet')

style = xlwt.XFStyle() # 初始化样式

#设置font字体
font = xlwt.Font() # 为样式创建字体
font.name = 'Times New Roman' #字体名字
font.bold = True # 黑体
font.underline = True # 下划线
font.italic = True # 斜体字
style.font = font # 设定样式

#输入日期
style.num_format_str = 'M/D/YY'  #设置时间格式

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1,0, 'this is test')
#带样式style 写入
worksheet.write(1,2, 'add style', style)

worksheet.col(1).width = 1000   #设置列的宽度
# datetime模块,需导入datetime包,datetime.now()获取当前时间
worksheet.write(2,2, datetime.datetime.now(),style)

worksheet.write(0, 0, 5) # Outputs 5
worksheet.write(0, 1, 2) # Outputs 2
worksheet.write(0, 4, xlwt.Formula('SUM(A1,B1)')) # Should output "7" (A1[5] + A2[2])

# 保存
workbook.save('Excel_test.xlsx')

