#!/usr/bin/env python
#encoding: utf-8

import mytest
import unittest
import myclass
import pytest

# class ch_test(mytest.mytest):

# 	def test_sum(self):
# 	    self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
	    
	    
# 	def test_sub(self):
# 	    self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')   

class aa(unittest.TestCase):

    ##初始化工作
    def setUp(self):
        print("aaaaa, setUp")
        mytest.mytest.test_sub(self)
    
    #退出清理工作
    def tearDown(self):
        print("aaaaatearDown")
    
    #具体的测试用例，一定要以test开头
    def test111(self):
        print("test111")



if __name__ =='__main__':
    unittest.main()
    # pytest.main()