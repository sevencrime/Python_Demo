# -*- codeing: utf-8 -*-

# def funA(arg) :
#     print('A')
#     a = arg()
# @funA
# def funB():
#     print('B')

def data(times):

    if times <= 1440 and times >=0:
        hour = int(((int(times)/60))) #取小时
        minx = int(((int(times)%60))) #取分钟
        if minx == 0:
            return ("标准时间是%d:00"%(hour))
        if minx != 0:
            return ("标准时间是%d:%d"%(hour,minx))
if __name__ == "__main__":
    print(data(500))


