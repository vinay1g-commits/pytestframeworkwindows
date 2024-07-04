class car:
    def initialize(self,model,price,mileage):
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

audi = car()
audi.initialize("audi","1000000","5kmpl")
audi.start_car()
audi.stop_car()
audi.car_details()

lamborghini = car()
lamborghini.initialize("lamborghini","10000000","2kmpl")
lamborghini.start_car()
lamborghini.stop_car()
lamborghini.car_details()