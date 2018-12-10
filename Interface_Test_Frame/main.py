#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-02 22:58:32
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import sys
sys.path.append("D:/郑某人/Python_Demo/Interface_Test_Frame/commans")
import src.requests_test
import unittest
import ddt
import test_case.reads
import test_case.writeExcel
import requests
from HTMLTestRunner import HTMLTestRunner

testdata = test_case.reads.reads().read()     #获取excel数据
# print(testdata)

# 使用ddt数据驱动
@ddt.ddt
class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()    #创建一个session
        cls.req = src.requests_test.requests_test()
        cls.wr = test_case.writeExcel.writeExcel()
        #先登录,获取token
        data = {
            'appid' : 'www' ,
            'loginKey' : '15000000088' ,
            'loginPwd' : 'ss123456' ,
            'type' : '0'
            }
        url = 'http://192.168.1.3:8081/RmarketShop/account/userLogin.html'
        resp = cls.s.post(url,data=data).json()
        resp['data'].pop('loginTime')
        cls.token_main = resp['data']


    @ddt.data(*testdata)
    def test_Interface(self,data):
        # 调用requests_test，进行接口请求
        res = self.req.getData(self.s, data, self.token_main)   #返回一个res
        # print(res)
        self.assertEqual(res['result'], 'Pass', res['msg'])     #断言
        # 在excel中写入res
        self.wr.write(res)


if __name__ == '__main__':

    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    unittest.TextTestRunner(verbosity=2).run(suite)


    # with open('HTMLReport.html', 'wb+') as f:
    #     runner = HTMLTestRunner(stream=f,
    #                             title='接口测试报告',
    #                             description='报告信息:',
    #                             verbosity = 2
    #                             )

    #     runner.run(suite)
