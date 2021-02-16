# def rayz(a,b):
#     return a , b
      
# print(rayz(20,20))                


# r=[rayz(20,43) for i in range(10)]
# print(r)

# def fib(b:int)->None:
#     return b-1


# print(fib(10.5))


c=[23,23,1,3,2,3,4]
print(c)
print(c[0:4:1])

class Slovar:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.d=dict()
        self.d[self.key]=self.value
   
    def add(self):
        pass

a=Slovar('Денис',795843849)        
print(a.d)





