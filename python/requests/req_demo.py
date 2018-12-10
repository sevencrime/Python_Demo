# coding:utf-8

import requests
import json
import sys
import io

#改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
# 最基本的GTE请求
# r = requests.get(url='https://www.apiopen.top/femaleNameApi?page=0')
# print(json.dumps(r.json(),indent = 4).encode('utf-8').decode('unicode_escape'))



r = requests.get('https://123.com').json()
# print(json.dumps(r.json(),ensure_ascii=False, indent=4))
times = r.elapsed.total_seconds()

# print(times)
print(r)
