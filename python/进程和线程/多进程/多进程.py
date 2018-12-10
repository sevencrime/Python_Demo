#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 16:33:13
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg

    def run(self):
        print ('say hi', self.arg)
        time.sleep(1)
    
if __name__ == '__main__':

    for i in range(10):
        p = MyProcess(i)
        p.start()

