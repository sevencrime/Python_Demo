#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import unittest
import json

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #接口地址
        cls.login_url = 'http://127.0.0.1:5000/login'
        cls.info_url = 'http://127.0.0.1:5000/info'
        cls.username = 'admin'
        cls.password = '123456'
        
    # @unittest.skip("do not run this case")
    def test_login(self):

        data = {
            'username' : self.username,
            'password' : self.password
        }

        # data 有两个参数,所有requests.post()返回一个字典
        response = requests.post(self.login_url,data=data).json()
        print(response)
        # print(type(response))
        # for (d,x) in response.items(): #遍历response(字典)且输出
        #     print((d,x))

        assert response['code'] == 200
        assert response['msg'] == 'success'

    def test_info(self) :

        data = {
            'username' : self.username,
            'password' : self.password
        }

        response_cookies = requests.post(self.login_url, data=data).cookies
        # print(response_cookies)
        # print(type(response_cookies))
        session = response_cookies.get('session')
        # print(session)
        assert session

        info_cookies = {
            'session': session
        }

        response = requests.get(self.info_url,cookies=info_cookies).json()

        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'

if __name__ == '__main__' :
    unittest.main()



