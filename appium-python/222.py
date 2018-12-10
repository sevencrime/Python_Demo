import os
import sys
#print(os.path)

class MyClass :
    def function1(self,el) :
        print(el)

    def Demo1(self) :
        print("EEEEEEEEEEEEEEE")
        self.function1(555)
        self.function1(777777777)

    def getSize(self):
        x = 1
        y = 2
        return(x,y)

    def Demo2(self):
        size =self.getSize()

        print(size)

    @classmethod
    def tearDownClass(cls):
        size1 = cls().getSize()
        print(size1)


m = MyClass()
# m.Demo2()
m.tearDownClass()


