class A:
    def __init__(self):
        print("inside init function of A" )

class B(A):
    def __init__(self):
        super().__init__()
        print("inside init function of class B")

B()


