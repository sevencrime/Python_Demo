#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-19 10:47:37
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ***
# @Version : $Id$

import xlrd
import sys
sys.path.append("..")
from config.read_conf import read_conf


class reads:

    def read(self):
        # 获取excel接口文档的路径
        path = read_conf().read()
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

        interface = {}

        for i in range(nrows):
            if i < 4:
                interface[(table.row_values(i)[0])] = table.row_values(i)[1]
            if i == 4:
                interface[table.row_values(4)[0]] = []

            if i > 5:
                s = {}
                for j in range(ncols):

                    s[table.row_values(5)[j]] = table.row_values(i)[j]

                interface[table.row_values(4)[0]].append(s)

        # print(interface)
        return interface


if __name__ == "__main__":
    interface = reads().read()
    print(interface)
