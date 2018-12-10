#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import unittest
import xlrd

class TestLogin(unittest.TestCase):

    excel_dir = 'F:\\Python_Demo\\python\\WEB编程\\接口测试\\unittest批量执行\\data.xlsx'

    @classmethod
    def setUpClass(cls):
        #接口地址
        cls.login_url = 'http://127.0.0.1:5000/login'
        cls.info_url = 'http://127.0.0.1:5000/info'
        # cls.username = 'admin'
        # cls.password = '123456'
        cls.data = xlrd.open_workbook(cls.excel_dir)
        cls.table = cls.data.sheet_by_name(u'Sheet1')

    def test_login(self):
        table = self.table

        for i in range(table.nrows):

            rows = table.row_values(i)
            data = eval(rows[0])
            print(data)
            print(type(data))
            # data = {
            #     'username' : self.username,
            #     'password' : self.password
            # }

            try:
                # data 有两个参数,所有requests.post()返回一个字典
                response = requests.post(self.login_url,data=data).json()
            except TimeoutError:
                self.logger.error("Time out!")

            # print(type(response))
            for (d,x) in response.items(): #遍历response(字典)且输出
                print('传入参数',rows,'response:',(d,x))

            assert response['code'] == 200
            assert response['msg'] == 'success'


                


if __name__ == '__main__' :
    unittest.main()



