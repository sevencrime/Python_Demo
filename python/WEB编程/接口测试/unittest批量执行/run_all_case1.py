#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# def suite():
#     loader = unittest.TestLoader()
#     suite = loader.discover(r'F:\\Python_Demo\\python\\WEB编程\\接口测试\\unittest批量执行\\Test_Case')
#     return suite

# if __name__ == '__main__':
#     unittest.main(defaultTest='suite',verbosity=2)

case_dir = "F:\\Python_Demo\\python\\WEB编程\\接口测试\\unittest批量执行\\Test_Case"

def all_case():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    '''
    1.discover方法里面有三个参数：
        -case_dir:这个是待执行用例的目录。
        -pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
        -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
    2.discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，
    这样就可以用unittest里面的TextTestRunner这里类的run方法去执行
    '''
    # print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())


