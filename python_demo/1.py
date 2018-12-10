#coding=gbk


'''
print("hello,python")
#help(max)
a, b, c = 1, 2, 3
print("a+b+c:",a+b+c)

print(4/2)
print(4//2)
'''
'''
str = "hello"
#0 1 2 3 4 
print(str)
print(str[-1])
print(str[0:-1])
print(str[0])
print(str[2:4])
print(str*2)
print(str*2+"aaaa")
'''
'''
list = [1,2,3,4,5,"6","7","8","9"]
#print(list)
list[3] = 10 
#print(list)
del list[2]
#print(list)
'''
'''
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if('Tosm' in student):
    print("yes")
else:
    print("no")
'''

a = set('2392590235')
b = set('58513')
#print(a - b)
#print(a | b)
#print(a ^ b)
#print(a & b)

'''
c = set(["1","3","5","6"])
#print(c)
t = list(c) 
t.sort() #按原来的顺序排序sort()
print(t)


print(100%3)    #模
print(100//3)   #除法取整数
print(2**3)     #幂
'''

import calendar 

cal = calendar.month(2017,9)
#print(cal) 

#print(calendar.isleap(2017))  #判断是否为闰年
#print(calendar.month(2017,9,w=2,l=1))


def ChangeInt(a):
    
    a = 10
   # print(a)

b = 2 
ChangeInt(b)
#print(b)



def printinfo( arg1, *vartuple ):

   print(arg1)
   for var in vartuple:
      print (var)
   return;
 
# 调用printinfo 函数
#printinfo( 10 );
#printinfo( 70, 60, 50 );


import math 

content = dir(math)

#print(content)

#str = input("请输入：");
#print ("你输入的内容是: ", str)








