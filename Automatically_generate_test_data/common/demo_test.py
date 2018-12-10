#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-30 23:04:41
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


def add(num):
    result = []
    res = []
    # pdb.set_trace()
    return add_list(num, 0, res, result)


def add_list(num, t, res, result):
    if num >= 0:
        for i in two[t]:
            # 限制res的长度等于key
            if len(res) <= len(one):
                if num == len(two) - 1:
                    res = []
                    res.append(i)
                elif res[-1] in two[t] and i in two[t]:
                    if t == len(two) - 1:
                        res.append(i)
                    elif t == len(res):
                        res.append(i)
                    res[-1] = i
                else:
                    res.append(i)
            else:
                # 长度超出，替换
                res.pop()

            if num == 0:
                # print(res)
                temp = {}
                for j in range(len(one)):
                    temp[one[j]] = res[j]
                result.append(temp)
                res.pop()
            add_list(num - 1, t + 1, res, result)
    return result


if __name__ == '__main__':
    one = ['login', 'type', 'password', 'ins']
    two = [
        [227513, 'nopqrs', '%&&*()', '%^%&&*', ''],
        [287742, 'uvwxyz', '&&*()_', 'nopqrs', '', 0, -1,2147483647, -2147483648],
        [492050, 'uvwxyz', '^%&&*(', 'stuvwx', ''],
        [287742, 'uvwxyz', '&&*()_', 'nopqrs', '', 0, -1,
         2147483647, -2147483648], ]

    list1 = add(len(one) - 1)
    # print(list1)
    print(len(list1))
