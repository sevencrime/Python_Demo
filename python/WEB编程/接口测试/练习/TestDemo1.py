#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class TestDemo() :

    url = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm'
    data = {'tel' : '15089514626'}
    response = requests.post(url, data=data)
    print(response)
    print(response.text)




