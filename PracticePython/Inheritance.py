class A:
    varA = 34
    def method_A(self):
        print("inside method A")

class B(A):
    varB = 44
    def method_B(self):
        print("inside method B")

obj = B()
print(obj.varB)
print(obj.varA)
obj.method_A()
obj.method_B()