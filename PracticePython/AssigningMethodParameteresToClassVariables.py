class car():
    wheelo = 4
    def sample1(self,tyre_type,mileage,color):
        print(tyre_type,mileage,color)
        print(self.wheelo)
        self.tyre_type = tyre_type # by adding self to variables it becomes class level and can be accessed inside any methods present in the class
        self.mileage = mileage
        self.color  = color

    def sample2(self):
        print(self.tyre_type,self.mileage,self.color)

c = car()
c.sample1("rubber","12","yellow")
c.sample2()
