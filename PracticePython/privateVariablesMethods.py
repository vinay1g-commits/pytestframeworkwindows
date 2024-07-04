class A:
    __a=23 # this is a private variable
    def __privmeth(self):
        print("private method example")

    def proper(self):
        print(self.__a)
        self.__privmeth()

obj = A() # use class to create the instance/object
obj.proper() # use object referrer to access class methods
