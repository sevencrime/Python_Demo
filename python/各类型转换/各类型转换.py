#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一、字典
dict = {'name': 'Zara', 'age': 7}
#字典转为字符串
str(dict)
#字典可以转为元组
tuple(dict)
#字典可以转为元组
tuple(dict.values())
#字典转为列表
list(dict)
#字典转为列表
dict.values

# 二、、元组
tup=(1, 2, 3, 4, 5,6,7,8)
#元组转为字符串
tup.__str__()
#元组转为列表
list(tup)
#元组不可以转为字典

# 三、列表
nums=[1, 3, 5, 7, 9, 11, 13];
#列表转为字符串
str(nums)
#列表转为元组
tuple(nums)
#列表不可以转为字典

# 四、字符串
str="(1,2,3)"
#字符串转为元组
tuple(eval(str))
#字符串转为列表
list(eval("(1,2,3)"))
#字符串转为字典
str1="{'name':'ljq', 'age':24}"
eval(str1)