#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-19 13:14:27
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ***
# @Version : $Id$

import sys
sys.path.append("..")
from common.read_interface_document import reads
import random


class TestData():

    def Data_Generation(self):
        interface_data = reads().read()
        # print(interface_data)
        # print(interface_data['param'])
        data_value = []  # 存放参数

        str_list = []
        int_list = []
        long_list = []
        yes_key = []
        not_key = []

        for param in interface_data['param']:
            # print(param)
            if param['required'] == "是":
                yes_key.append(param['key'])
            else:
                not_key.append(param['key'])
                # data[param["key"]] = ""

            team = []
            # 纯数字,6位数
            str1 = random.randint(100000, 999999)
            team.append(str1)
            # 纯字母,6位数
            str2 = 'abcdefghijklmnopqrstuvwxyz'
            x = random.randint(0, len(str2) - 6)
            team.append(str2[x:(x + 6)])
            # 纯符号
            str3 = ',./;[!@#]$%^%&&*()_+'
            x = random.randint(0, len(str3) - 6)
            team.append(str3[x:(x + 6)])
            # 代码标签
            # 组合字符
            str4 = str(str1) + str2 + str3
            x = random.randint(0, len(str4) - 6)
            team.append(str4[x:(x + 6)])
            # 临界值
            # 空字符串
            team.append('')

            # 判断参数类型后,制造数据
            if param['type'] == 'string' or param['type'] == 'String':
                str_list = team
                data_value.append(str_list)

            elif param['type'] == 'int' or param['type'] == 'Int' or param['type'] == 'INT':
                int_list = team
                # 零
                int_list.append(0)
                #-1
                int_list.append(-1)
                # 最大
                int_list.append(2147483647)
                # 最小值
                int_list.append(-2147483648)

                data_value.append(int_list)

            elif param['type'] == 'long' or param['type'] == 'Long':
                pass
            else:
                pass

        print(yes_key)
        print(not_key)
        print(data_value)


if __name__ == "__main__":
    TestData().Data_Generation()
