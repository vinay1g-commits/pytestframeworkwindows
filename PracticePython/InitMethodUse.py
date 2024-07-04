class car:
    def __init__(self,model,price,mileage):
        self.model=model
        self.price=price
        self.mileage=mileage

    def start_car(self):
        print(self.model + " has started")

    def stop_car(self):
        print(self.model + " has stopped")

    def car_details(self):
        print(self.model + " price is : " + self.price)
        print(self.model + " mileage is: " + self.mileage)
#init method is initialization method equivalent of constructors in java
#using init method we can directly pass the arguments to the init method.
audi = car("audi","1000000","5kmpl")
audi.start_car()
audi.stop_car()
audi.car_details()

lamborghini = car("lamborghini","10000000","2kmpl")
lamborghini.start_car()
lamborghini.stop_car()
lamborghini.car_details()