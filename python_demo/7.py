#! /usr/bin/env python
# -*- coding: utf-8 -*-

#利用方差对比两张图片的差异

from PIL import Image
#Ê¹ÓÃµÚÈý·½¿â£ºPillow
import math
import operator
from functools import reduce

image1=Image.open('C://Users//Administrator//Desktop//脚本文件//11.png')
image3=Image.open('C://Users//Administrator//Desktop//脚本文件//22.png')
#°ÑÍ¼Ïñ¶ÔÏó×ª»»ÎªÖ±·½Í¼Êý¾Ý£¬´æÔÚlist h1¡¢h2 ÖÐ
h1=image1.histogram()
h2=image3.histogram()

result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )


print(result)
#resultµÄÖµÔ½´ó£¬ËµÃ÷Á½ÕßµÄ²î±ðÔ½´ó£»Èç¹ûresult=0,ÔòËµÃ÷Á½ÕÅÍ¼Ò»Ä£Ò»Ñù