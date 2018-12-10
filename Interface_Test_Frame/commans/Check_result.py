#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 17:26:16
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import sys
sys.path.append("..")
import Logging

#对比两个json结果,返回不同的结果
class Check_result():

    logger = Logging.logs()

    def __init__(self):
        self.arr = []    #存放对比后的结果

    def cmps(self, actual, expected, key):

        if isinstance(actual, dict):
            """若为dict格式"""
            for key in expected:    #遍历出期望结果expected的key
                if key not in actual:   #判断实际结果actual是否存在期望结果中的key
                    # print("actual不存在 key:%s" %key)
                    # self.logger.error("响应结果缺少了 %s 这个key" %key)
                    self.arr.append("响应结果缺少了 %s 这个字段" %key)
            for key in actual:      #遍历出实际结果actual中的key
                if key in expected:     #判断key是否在期望结果expected里面
                    if str(key) != 'mainKey' and str(key) != 'tokenKey' and str(key) != 'loginTime':
                        self.cmps(actual[key], expected[key], key)
                else:
                    # print('expected不存在 key:%s' %key)
                    # self.logger.error('期望结果多出了 %s 这个key' %key)
                    self.arr.append('期望结果多出了 %s 这个字段' %key)
        elif isinstance(actual, list):
            """若为list格式"""
            if len(actual) != len(expected):
                print("list len: '{}' != '{}'".format(len(actual), len(expected)))
            for actual_list, expected_list in zip(sorted(actual), sorted(expected)):
                if str(key) != 'mainKey' and str(key) != 'tokenKey' and str(key) != 'loginTime':
                    self.cmps(actual_list, expected_list, actual_list)

        else:
            # global arr
            if actual != expected:
                # str1 = "%s:%s,结果不一致" %(key,actual)
                str1 = "字段 %s:%s 不一致" %(key,actual)
                # self.arr.append(str1)
                self.arr.append(str1)
                # return self.arr

        return self.arr



if __name__ == '__main__':

    actual = [{'code': 0, 'msg': 'SUCCESS1', 'data': {'mainKey': 'X+LmRVMzop8o5B1u5DhlyfNx5hgkEOyGS/Cqtz0H9kY=', 'tokenKey': '5BCCE35A4DDF0D0E4DFBBD405D3F86EC', 'loginTime': '2018-09-11 18:17:55'}},{'code': 2002, 'msg': '用户名或密码不正确', 'data': None},{'code': 2007, 'msg': '用户不存在', 'data': None}]
    expected =   [{'code': 10, 'msg': 'SUCCESS', 'data': {'mainKey': 'X+LmRVMzop8o5B1u5DhlyYW9bH5k6eJjctSB3u6K0jw=', 'tokenKey': 'C6AEAA558BBE245509EEDB4329617A8B', 'loginTime': '2018-08-27 14:56:50'}},{"msg": "用户名或密码不正确","data": None},{"code": 2007,"msg": "用户不存在","data": None}]

    Check_result().cmps(actual,expected,0)
    a = Check_result().getArr()
    print(a)

