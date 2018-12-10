# coding = utf-8
# author:semishigure

import requests
import json

url = 'https://api.douban.com/v2/movie/search'

# 此参数类型一定为字典
params = dict(q = u'刘德华')
# params = dict(tag = u'喜剧')

r = requests.get(url,params= params)

# print(r.url)
# json.dumps()用于将dict类型的数据转成str
# ensure_ascii 编码
print('Search Parame:\n',json.dumps(params,ensure_ascii=False))
# indent=4 缩进4格
# print('Search Reaponse:\n',json.dumps(r.json(),ensure_ascii=False, indent=4))

print(len(r['subjects']))

