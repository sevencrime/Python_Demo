#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-07 14:21:24
# @Author  : onedi (onedi@qq.com)
# @Link    : ${link}
# @Version : $Id$

import logging


# 获取logger对象，设置日志级别
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# 获取文件处理器，并设置级别
handler = logging.FileHandler("log.txt")
# handler = logging.FileHandler("./logs/log.csv")
handler.setLevel(logging.INFO)

# 获取并设置文件处理器的日志格式
formatter = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
handler.setFormatter(formatter)

# 设置日志处理器
logger.addHandler(handler)

# 打印日志
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")


