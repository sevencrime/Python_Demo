#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import unittest
import json

class TestDemo_unittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 接口参数:tel=15089514626
        cls.url = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm'

        cls.data = {
            'tel' : '15814401981'
            }

    def test1(self):

        print(self.url,'?tel=15814401981')

        # response = requests.post(self.url,data=self.data)
        response = requests.get(self.url,'tel=15814401981')

        # print(response)
        print(type(response))
        print(response.text)
        print(response.text.split('='))

        list1 = response.text.split('=')



if __name__ == '__main__' :
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemo_unittest))
    runner = unittest.TextTestRunner(verbosity=2).run(suite)







