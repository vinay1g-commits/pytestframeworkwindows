class A:
    a=1
    def sample(self): #method name should be same to use super()
        print("inside sampleA")

class B(A):
    a=2
    def sample(self):  #method name of child and parent should be same to use super()
        print("inside sampleB")

    def properties(self):
        print(super().a)
        super().sample()

obj=B()
obj.properties()