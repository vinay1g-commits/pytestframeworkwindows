# To access private members of the class outside the class we create getter setter
class A: 
    __a=23


    def set(self,a):
        A.__a=a

    def get(self):
        return A.__a

obj = A()
obj.set(12)     # we are setting then getting the method
print(obj.get())

