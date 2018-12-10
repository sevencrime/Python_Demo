#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-11 11:21:01
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import unittest
import ddt

list1 = [{'rowNum': 2, 'id': 't_001', 'method': 'POST', 'url': 'http://127.0.0.1:5000/login', 'params': '', 'headers ': '', 'body': '{"username":"admin",\n"password":"123456"}', 'type': 'data', 'statuscode': '', 'times': '', 'error': '', 'checkpoint': "{'code': 200, 'msg': 'success'}", 'result': '', 'msg': ''}, {'rowNum': 3, 'id': 't_002', 'method': 'POST', 'url': 'http://127.0.0.1:5000/login', 'params': '', 'headers ': '', 'body': '{"username":"admin",\n"password":"1234567"}', 'type': 'data', 'statuscode': '', 'times': '', 'error': '', 'checkpoint': "{'code': 401, 'msg': 'Invalid password'}", 'result': '', 'msg': ''}, {'rowNum': 4, 'id': 't_003', 'method': 'POST', 'url': 'http://127.0.0.1:5000/login', 'params': '', 'headers ': '', 'body': '{"username":"admin1",\n"password":"123456"}', 'type': 'data', 'statuscode': '', 'times': '', 'error': '', 'checkpoint': "{'code': 401, 'msg': 'Invalid username'}", 'result': '', 'msg': ''}]

# print(list1)

@ddt.ddt
class MyTestCase(unittest.TestCase):

	@ddt.data(*list1)
	def test_something(self,data):
		print(data)

if __name__ == '__main__':
    unittest.main()