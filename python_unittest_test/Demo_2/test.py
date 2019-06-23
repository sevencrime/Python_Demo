#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class AlienTest(unittest.TestCase):
    globals()['status'] = 200          # 位置一

    @classmethod
    def setUp(self):
        self.url = "http://www.baidu.com"
        # globals()['status'] = 200    # 位置二

    def test_1_alien(self):
        # globals()['status'] = 200    # 位置三
        print("test_1_status：", globals()['status'])

    def test_2_alien(self):
        globals()['status'] = 404
        print("test_2_status", globals()["status"])

    @unittest.skipUnless(globals()['status'] == 200, "status不为500，跳过测试用例")
    def test_3_alien(self):
        print("test_3_status:", globals()['status'])


if __name__ == '__main__':
    unittest.main()
