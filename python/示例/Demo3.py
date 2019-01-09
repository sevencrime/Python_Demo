#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-09 11:32:51
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$



import xlrd,xlwt
from hanziconv import HanziConv

class reads:

    def read(self):
        # 获取excel接口文档的路径
        # path = read_conf().read()
        path = 'D:/Python_Demo/python/示例/444.xls'
        # print(path)
        # 打开excel文件
        workbook = xlrd.open_workbook(path)
        # 打开excel表
        table = workbook.sheets()[0]
        # 获取excel行数
        nrows = table.nrows
        # print(nrows)
        # 获取excel列数
        ncols = table.ncols
        # print(ncols)

        newbook = xlwt.Workbook(encoding = 'utf-8')
        newsheet = newbook.add_sheet('My worksheet')

        for i in range(nrows):
            # if i != 0:

            for j in range(ncols):
                rows = table.cell(i,j).value
                # print(rows)
                if rows != '' and type(rows) == str :
                    if u'\u4e00' <= rows <= u'\u9fff' :
                
                        # print(rows)
                        Conversion = HanziConv.toTraditional(rows)
                        newsheet.write(i, j, Conversion)
                        continue

                newsheet.write(i, j, rows)


        newbook.save('D:/Python_Demo/python/示例/newbook.xls')



if __name__ == "__main__":
    reads().read()
    