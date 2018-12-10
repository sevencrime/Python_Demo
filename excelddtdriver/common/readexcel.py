#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-03 22:13:31
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import xlrd

class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath,'rb')
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                # print(s['rowNum'])
                # table.row.values() 获取一整行的数据
                values = self.table.row_values(j)
                # print(values)
                for x in list(range(self.colNum)):
                	# 此循环的作用是遍历出一行中，每一列的数据
                    s[self.keys[x]] = values[x]
                    # print(s)
                r.append(s)
                j += 1
            return r

if __name__ == "__main__":
    filepath = 'F:/Python_Demo/excelddtdriver/case/debug_api.xlsx'
    # sheetName = "Sheet1"
    data = ExcelUtil(filepath)
    resp = data.dict_data()
    print(resp)
    # print(resp[0]['id'])
    