#!/usr/bin/env python
#encoding: utf-8

import mytest
import unittest
import myclass
import pytest

class ch_test(mytest.mytest):

	def test_sum(self):
	    self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')
	    
	    
	def test_sub(self):
	    self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')   


if __name__ =='__main__':
    unittest.main()
    # pytest.main()