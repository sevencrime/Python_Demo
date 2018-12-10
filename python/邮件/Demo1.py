#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from_addr = input('17620446727@163.com')
password = input('shengqile54604')
# 输入收件人地址:
to_addr = input('zqy09@saintway.cn')
# 输入SMTP服务器地址:
smtp_server = input('smtp.163.com')

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
