#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

key = r"<html><body><h1>hello world<h1></body></html>"

s = re.findall("<h1>(.+)<h1>", key)
print(s)

print(re.search("<h1>(.+)<h1>", key))






