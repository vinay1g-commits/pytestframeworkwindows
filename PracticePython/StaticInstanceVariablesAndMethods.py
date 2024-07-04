class car:
    wheels = 4
    def __init__(self,model,price,mileage): #non static method
        self.model=model
        self.price=price
        self.mileage=mileage

    def start_car(self): #non static method
        print(self.model + " has started")

    def stop_car(self): #non static method
        print(self.model + " has stopped")

    def car_details(self): #non static method
        print(self.model + " price is : " + self.price)
        print(self.model + " mileage is: " + self.mileage)

    @staticmethod
    def demo():
        print("static demo")

    @staticmethod
    def wheel():
        print(car.wheels)
        car.demo() # we accessed static to static
        # to access non static method inside static use
        c=car("hyundia","100000","15kmpl")
        c.start_car()

#To access non static stuff outside class we create objects like below one
audi = car("audi","1000000","5kmpl")
audi.start_car()
audi.stop_car()
audi.car_details()

lamborghini = car("lamborghini","10000000","2kmpl")
lamborghini.start_car()
lamborghini.stop_car()
lamborghini.car_details()

# To access static stuff of the class outside the class we use class name
print(car.wheels)
car.demo()
car.wheel()
print(audi.wheels)

# non static stuff can be accessed anywhere(static or nonstatic methods)
# whereas static stuff can be only accessed by static methods
# if you want to access non static instances inside static method then creaate class object reference and use it to access non static stuff inside static method.
