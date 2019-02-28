#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 18:21:30
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
db = client['uat']
clientinfo = db['client_info']
# result = clientinfo.find({'email':'/.*onedi.*/'}, {'accountId':1, 'applyId':1})
# result = clientinfo.find({'email':'/.*onedi.*/'})
result = clientinfo.find({'email':{"$regex":'.*onedi.*'}},{'accountId':1, 'applyId':1})

# print(result)
clientlist = []
accountlist = []
applylist = []

for res in result:
    # print(res)
    accountlist.append(res['accountId'][0])
    if res['applyId'] != [] :
        applylist.append(res['applyId'][0])

# print(accountlist)
# print("******************")
# print(applylist)

# account = db['account']
# # r = account.find_one({'_id':ObjectId('5c779eaf7217032b278aabc6')})
# # print(r)
# for ac in accountlist:
#     # print(ac)
#     # print(type(ac))
#     res = account.find_one({'_id':ObjectId(ac)})
#     # print(res)



applys = db['apply']
a = applys.find_one({'_id':ObjectId('5c779e5472170347d88a89d8')})
print(a)
# for ap in applys:
#     print(ap)
#     res = applys.find_one({'_id':ObjectId(ap)})
#     print(res)




