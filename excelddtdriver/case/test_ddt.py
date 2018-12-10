#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 15:20:20
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import unittest
import ddt
import os
import requests
import sys
sys.path.append('F:/Python_Demo/excelddtdriver/common')
import base_api
import readexcel
import writeexcel

# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
# print(curpath)
testxlsx = os.path.join(curpath, "debug_api.xlsx")
# print(testxlsx)
# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xlsx")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()
# print(testdata)
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了
        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self, data):
        # 先复制excel数据到report
        res = base_api.send_requests(self.s, data)

        base_api.wirte_result(res, filename=reportxlsx)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s"%res_text)
        # 断言
        self.assertDictEqual(eval(res_text),eval(check))    # 判断两个字典是否一致

if __name__ == "__main__":
    unittest.main()

