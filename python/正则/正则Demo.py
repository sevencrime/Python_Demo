#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
'''
key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"
#我们在编译这段正则表达式
pattern1 = re.compile(p1)
#在源文本中搜索符合正则表达式的部分
matcher1 = re.search(pattern1, key)
print(matcher1.group(0))
'''
key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>.+<h1>" #我们写的正则表达式
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
p1 = r"chuxiuhong@hit\.edu\.cn"
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
'''
key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"#胡编乱造的网址，别在意
p1 = r"https*://"#看那个星号！
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
'''
# 匹配大小写, [] 代表匹配里面的字符中的任意一个
key = r"lalala<hTml>hello</Html>heiheihei"
p1 = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
'''
key = r"mat cat hat pat"
p1 = r"[^p]at"#这代表除了p以外都匹配
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
'''
key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+\."#我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+?\."#我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''
#{a,b}(代表a<=匹配次数<=b)
key = r"saas and sas and saaas"
p1 = r"sa{1,2}s"
pattern1 = re.compile(p1)
print(pattern1.findall(key))
'''






