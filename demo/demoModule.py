from animal.animal_types import *
from cal.calcu import *
#Animal
Animals.cat(self=1234)
#calculator
sum = calci.sum(2,4,5)
print(sum)
sub=calci.sub(2,4,5)
print(sub)
#via object its better to call methods as it does not ask to enter self value like above.
# self implies these methods belongs to same class
obj = calci() # we can see the difference if we are using object self values are not required
# whereas on top we are requiring to enter the eslf value when we directly use class name.method name
print(obj.sum(1,2))
obj2 = Animals()
obj2.cat()
obj2.rabbit()