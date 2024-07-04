class A(): #method overloading is not directly supported via python only below is the way to do it.
    def methA(self,a=None,b=None): # a and b are method parameters
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a)
        else:
            print("Nothing")

obj = A()
obj.methA(5,4) # a and b values are  arguments passed to method parameters
obj.methA(5)
obj.methA()