#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-04 14:01:39
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import unittest
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):

    # #下面的1,2,3代表我们传入的参数,每次传入一个值
    # @data(1,2,3)
    # #定义一个value用于接收我们传入的参数
    # def test_something(self,value):
    #     #对于传入的参数与2进行对比,相等就通过,否则就是不同过
    #     self.assertEqual(value, 2)


    #下面的(1,2)(2,3)代表我们传入的参数,每次传入两个值
    @data((1,2),(2,3))
    #告诉我们的测试用例传入的是两个以上的值
    @unpack
    #定义两个参数value用于接收我们传入的参数
    def test_something(self,value1,value2):
        print(value1,value2)
        #对于传入的第一个参数+1与第二个参数进行对比,相等就通过,否则就是不通过
        self.assertEqual(value2, value1+1)

if __name__ == '__main__':
    unittest.main()
