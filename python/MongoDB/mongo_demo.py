#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-17 18:04:49
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

import pymongo
#链接MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
# 指定数据库
db = client['test']
# 指定集合(表)
collection = db['student']

# 插入数据,返回InsertOneResult对象，调用inserted_id属性获取_id
# result = collection.insert_one({
# 		'name' : 'onedi12' ,
# 		'age' : 201 ,
# 		'gender' : 'male'
# 	})
# print(result)
# print(result.inserted_id)

#查询数据,find_one()只返回第一条数据,结果不存在会返回None
# result1 = collection.find_one({'name' : 'onedi'})
# print(result1)

#find() 返回所有数据,需要遍历出来
# result2 = collection.find({'name' : 'onedi'})
# print(result2)
# for res in result2:
# 	print(res)

# count() 统计所有数据条数
# result3 = collection.find({'name' : 'onedi'}).count()
# result3 = collection.find().count()
# print(result3)

#sort() 排序
# result4 = collection.find().sort('name' , pymongo.ASCENDING) #升序
# result4 = collection.find().sort('name' , pymongo.DESCENDING) #降序
# print([res['name'] for res in result4])

# skip() 忽略前面指定的条数
# result4 = collection.find().sort('name' , pymongo.DESCENDING).skip(4)
#limit() 只取前面指定的条数
# result4 = collection.find().sort('name' , pymongo.DESCENDING).limit(3)
# print([res['name'] for res in result4])

#update_one()
# condition = {'name' : 'onedi'}
# student = collection.find_one(condition)
# student['age'] = 25
# result5 = collection.update_one(condition, {'$set' : student})
# print(result5)
# print(result5.matched_count, result5.modified_count)

















