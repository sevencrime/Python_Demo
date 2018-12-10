#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-24 16:14:49
# @Author  : onedi (onedi@qq.com)

import configparser
import os

class read_conf():

    def read(self):
        config = configparser.ConfigParser()
        '''
        #读取ini文件
        # os.getcwd()+'/config/config.ini'只能在operating_excel.py打开
        因为os.getcwd()是运行文件的路径
        '''

        config.read(os.getcwd()+'/config/config.ini',encoding='utf-8-sig')
        # config.read('E:/郑某人/Python_Demo/接口测试框架+ddt/config/config.ini',encoding='utf-8-sig')

        #读取ini中[excel]里面的'path'的值
        path = config.get('excel', 'path')

        return path

if __name__ == '__main__':
    path = read_conf().read()
    print(path)

