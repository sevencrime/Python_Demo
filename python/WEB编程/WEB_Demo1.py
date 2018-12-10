#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Application必须是一个可调用对象,且接受了两个参数(environ, start_response)
# environ :（WSGI 的环境信息)
# start_response :（开始响应请求的函数）

# 可调用对象是一个函数
def application(environ, start_response):
    # start_response也是一个 callable，接受两个必须的参数，\n
    # status（HTTP状态）和 response_headers（响应消息的头）
    start_response('200 OK', [('Content-Type','text/html')])
    return [b'<h1>Hello, web! </h1>']

# 可调用对象是一个类
class AppClass :
    def __init__(self, environ , start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self) :
        self.start('200 OK', [('Content-Type', 'text/html')])
        yield "Hello world! \n"
        # return [b'<h1>PYTHON, web! </h1>']


