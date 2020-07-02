
def my_generator(n):
    for i in range(n):
        temp=yield i
        print(f'我是{temp}')
 
g=my_generator(5)
 
print(next(g)) #输出0
print(next(g)) #输出1

g = my_generator(19)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
