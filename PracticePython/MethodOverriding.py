class A:
    a=34
    def sampleA(self):
        print("inside method A")
class B(A):
    a=567
    def sampleA(self):
        print("inside method B")
obj = B()
print(obj.a)
obj.sampleA()