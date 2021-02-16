# def rayz(a,b):
#     return a , b
      
# print(rayz(20,20))                


# r=[rayz(20,43) for i in range(10)]
# print(r)

# def fib(b:int)->None:
#     return b-1


# print(fib(10.5))

import sys
c=[23,23,1,3,2,3,4]
print(c)
print(c[0:4:1])

class Slovar:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.d=dict()
        self.d[self.key]=self.value
   
    def add(self,re1,re2):
        self.re1=re1
        self.re2=re2
        self.d.update({self.re1:self.re2})
        print(self.d)

    def clear(self):
        r=input('Введите кого хотите удалить') 
        if r in self.d:
            del self.d[r]   
            print(self.d)
        else:
            print('Такого нет')    

a=Slovar('Денис', 795843849)   
print(str(sys.getsizeof(a)) + ' bit')    
print(a.d)
a.add('Vadim' , 49594939)
print(str(sys.getsizeof(c)) + ' bit')    
a.clear()



