# coding: GBK


#ע��

count = 10  #ȫ�ֱ���  
  
def print_local():  
    count = 10  #�ֲ����������count������ȫ�ֱ���count����2���ǲ�ͬ�ı����� 
    if count == count:
    
        print(count)  
      
def print_global():  
    print(count) #�����count���������ȫ�ֱ�����  
      
print_local()  
print_global()  



