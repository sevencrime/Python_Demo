#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
from readexcel import ExcelUtil
from writeexcel import copy_excel, Write_excel

# 作者：上海-悠悠
# QQ群：226296743


def send_requests(s, testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    # print(params)
    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
        print("请求头部：%s" % headers)
    except:
        headers = None
    # print(headers)
    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url: %s" % (method, url))
    print("请求params：%s" % params)

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}
    # print(bodydata)
    # 判断传data数据还是json,get请求传data，post请求传json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post" or "POST": 
        print("post请求body类型为：%s ,body内容为：%s" % (type, body))

    verify = False
    res = {}   # 接收返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                       )
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        print(testdata['rowNum'])
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        # print(res['text'])
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        # print(res['times'])
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""

        #检验期望结果checkpoint和resp是否一致，对比数据，下面需要改

        print(testdata['checkpoint'])
        print(res['text'])
        # print(type(testdata['checkpoint']))
        # print(type(res['text']))
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"


            
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res

def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub, 8, result['statuscode'])       # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 9, result['times'])            # 耗时
    wt.write(row_nub, 10, result['error'])            # 状态码非200时的返回信息
    wt.write(row_nub, 12, result['result'])           # 测试结果 pass 还是fail
    wt.write(row_nub, 13, result['msg'])           # 抛异常

if __name__ == "__main__":
    data = ExcelUtil('F:/Python_Demo/excelddtdriver/case/debug_api.xlsx').dict_data()
    print(data[0])      # data[0]得到数据驱动第一行的数据
    s = requests.session()      #创建一个session对象
    res = send_requests(s, data[0])     
    print(res)
    copy_excel("F:/Python_Demo/excelddtdriver/case/debug_api.xlsx", "F:/Python_Demo/excelddtdriver/report/result.xlsx")
    wirte_result(res, filename="F:/Python_Demo/excelddtdriver/report/result.xlsx")