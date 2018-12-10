#coding=utf-8  
  
import pytesseract  
from pytesser import *  
from PIL import Image,ImageEnhance,ImageFilter  
import os  
import fnmatch  
import re,time  
  
import urllib, random  
  
  
#import hashlib    
   
def getGray(image_file):  
   tmpls=[]  
   for h in range(0,  image_file.size[1]):#h  
      for w in range(0, image_file.size[0]):#w  
         tmpls.append( image_file.getpixel((w,h))  )  
            
   return tmpls  
   
def getAvg(ls):#��ȡƽ���Ҷ�ֵ  
   return sum(ls)/len(ls)  
   
def getMH(a,b):#�Ƚ�100���ַ��м����ַ���ͬ  
   dist = 0;  
   for i in range(0,len(a)):  
      if a[i]==b[i]:  
         dist=dist+1  
   return dist  
   
def getImgHash(fne):  
   image_file = Image.open(fne) # ��  
   image_file=image_file.resize((12, 12))#����ͼƬ��С��12px X 12px  
   image_file=image_file.convert("L")#ת256�Ҷ�ͼ  
   Grayls=getGray(image_file)#�Ҷȼ���  
   avg=getAvg(Grayls)#�Ҷ�ƽ��ֵ  
   bitls=''#���ջ�ȡ0��1  
   #��ȥ���1px��������  
   for h in range(1,  image_file.size[1]-1):#h  
      for w in range(1, image_file.size[0]-1):#w  
         if image_file.getpixel((w,h))>=avg:#���ص�ֵ�Ƚ�ƽ��ֵ ���ڼ�Ϊ1 С�ڼ�Ϊ0  
            bitls=bitls+'1'  
         else:  
            bitls=bitls+'0'  
   return bitls  
'''''          
   m2 = hashlib.md5()    
   m2.update(bitls) 
   print m2.hexdigest(),bitls 
   return m2.hexdigest() 
'''  
   
   
a=getImgHash(".//testpic//001n.bmp")#ͼƬ��ַ�����滻  
files = os.listdir(".//testpic")#ͼƬ�ļ��е�ַ�����滻  
for file in files:  
   b=getImgHash(".//testpic//"+str(file))  
   compare=getMH(a,b)  
   print file,u'���ƶ�',str(compare)+'%'      