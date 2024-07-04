from abc import ABC, abstractmethod


class A(ABC): # for abstract class we have to inherit from class ABC
    def __init__(self,a):
        print("constructor/initialization for pyhon")
        self.a=a
    @abstractmethod # for abstract methods we have to use abstractmethod annotation
    def method_one(self):
        pass

    @abstractmethod # for abstract methods we have to use abstractmethod annotation
    def method_two(self):
        pass

    #normal method
    def method_three(self):
        print("normal method")

class B(A):
    def method_one(self): # this is abstract class as not all abstract methods are implemented here
        print("inside method one") # implementing one of the abstract method
class C(B): # this becomes normal class as here all the abstract methods are implamented
    #and we can create its object
    def method_two(self):
        print("inside method two" ,self.a)

obj = C(23)
obj.method_one()
obj.method_two()
obj.method_three()




