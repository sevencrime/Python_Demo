#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-05 20:52:45
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for vel in level:
                print(vel)
                print ("[{level}]: enter function {func}()".format(
                    level=vel,
                    func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

lists = ["INFO", "ERROR"]
# @logging(level='INFO')
@logging(lists)
def say(*args, **kwargs):
    print ("say {}!".format(*args, **kwargs))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print ("do {}...".format(something))

if __name__ == '__main__':
    say('hello')
    # do("my work")