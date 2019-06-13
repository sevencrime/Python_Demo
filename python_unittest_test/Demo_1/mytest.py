#!/usr/bin/env python
#encoding: utf-8

import unittest
import myclass

class mytest(unittest.TestCase):
    
    # 所有case执行之前准备一次环境
    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")

    # 所有case执行之后清理环境
    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")
    
    ##初始化工作
    def setUp(self):
        print("setUp")
    
    #退出清理工作
    def tearDown(self):
        print("tearDown")
    
    #具体的测试用例，一定要以test开头
    def test_sum(self):
        self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
        
        
    def test_sub(self):
        self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')   
        
        
if __name__ =='__main__':
    unittest.main()