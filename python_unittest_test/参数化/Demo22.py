#!/usr/bin/env python
# -*- coding: utf-8 -*-

#nose_parameterized_demo
import unittest , pytest
from nose_parameterized import parameterized

class TestMathUnitTest(unittest.TestCase):
    
    params = [
        ("1st", 4, 5),
        ("2en", 2, 4),
        ("3rd", 3, 4),
    ]
    
    @parameterized.expand(input=params)
    def test_floor(self, *args, **kwargs):
        self.assertEqual(source + 1, expected)

if __name__ == '__main__':
    unittest.main()
    # pytest.main(["-s", "Demo22.py"])

