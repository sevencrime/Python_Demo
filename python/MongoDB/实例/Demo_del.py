#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 18:21:30
# @Author  : Onedi (Onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import pymongo
from bson.objectid import ObjectId

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client['test7']
client = pymongo.MongoClient("mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")
db = client['uat']

clientinfo = db['client_info']
# result = clientinfo.find({'email':'/.*onedi.*/'}, {'accountId':1, 'applyId':1})
# result = clientinfo.find({'email':'/.*onedi.*/'})
result = clientinfo.find({'email':{"$regex":'.*yuchen.*'}},{'accountId':1, 'applyId':1})
# dels = clientinfo.delete_many({'email':{"$regex":'.*yuchen.*'}})
# print(dels.deleted_count)


# print(result)
clientlist = []
accountlist = []
applylist = []
applyinfolist = []

for res in result:
    # print(res)
    accountlist.append(res['accountId'][0])
    if res['applyId'] != [] :
        applylist.append(res['applyId'][0])

# print(accountlist)
# print("******************")
# print(applylist)

account = db['account']
# r = account.find_one({'_id':ObjectId('5c779eaf7217032b278aabc6')})
# print(r)
for ac in accountlist:
    # print(ac)
    # print(type(ac))
    res = account.find_one({'_id':ObjectId(ac)})
    dels = account.delete_many({'_id':ObjectId(ac)})
    print("************删除account***********")
    print(dels.deleted_count)



applys = db['apply']
# a = applys.find_one({'_id':ObjectId('5c779e5472170347d88a89d8')})
# print(a)
for ap in applylist:
    # print(ap)
    res = applys.find_one({'_id':ObjectId(ap)})
    dels = applys.delete_many({'_id':ObjectId(ap)})
    print("************删除apply***********")
    print(dels.deleted_count)
    if res != None:
        applyinfolist.append(res['applyInfoIds'])
    # print(res)

# print(applyinfolist)

applyinfo = db['apply_info']
for info in applyinfolist:
    # print(info)
    if len(info) > 1:
        for i in range(len(info)):
            # print(i)
            # print(info[i])
            # print("**********大于1************")
            res = applyinfo.find_one({'_id':ObjectId(info[i])})
            dels = applyinfo.delete_many({'_id':ObjectId(info[i])})
            print("************删除apply_info***********")
            print(dels.deleted_count)

    else:
        res = applyinfo.find_one({'_id':ObjectId(info[0])})
        dels = applyinfo.delete_many({'_id':ObjectId(info[0])})
        print("************删除apply_info***********")
        print(dels.deleted_count)

