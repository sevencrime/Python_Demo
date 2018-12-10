#!/usr/bin/env python
# -*- coding: utf-8 -*-
class NotFlask():

    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            return f

        return decorator

app = NotFlask()

@app.route("/")
def hello():
    return "Hello World !"