def some_fun():
    print("some function outside class")

class obj_car():
    wheels=4
    def start(self):
        print("car started using start method")

some_fun() # it will execute function present outside class directly

# to access methods and functions inside the class create its object and reference for the object
o = obj_car()
print(o.wheels)
print(o.start())
