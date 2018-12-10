# coding: GBK


#注释

count = 10  #全局变量  
  
def print_local():  
    count = 10  #局部变量，这个count覆盖了全局变量count，这2个是不同的变量。 
    if count == count:
    
        print(count)  
      
def print_global():  
    print(count) #这里的count是最上面的全局变量噢  
      
print_local()  
print_global()  



