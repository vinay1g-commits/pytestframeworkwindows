class demoo():
    tyres = "apollo"
    def car_color(self):
        print("car color is grey")
    def to_access_withinClass(self): # we use self keyword to access class properties within class
        print(self.tyres)
        self.car_color()

car = demoo()
car.to_access_withinClass()