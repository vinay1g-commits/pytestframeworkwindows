import math
import random

import modulesCalc1 #modules are notthing but python files right click project > goto new>python>file

sum = modulesCalc1.A.add(2,3,2)
print(sum)
sub = modulesCalc1.A.sub(3,2,3)
print(sub)
mul = modulesCalc1.B.mul(2,2,3)
print(mul)
div = modulesCalc1.B.div(3,2,3)
print(div)

print(dir(modulesCalc1))

print(math.ceil(3.4))
print(math.sqrt(4))
print(math.floor(1.2))
print(math.pi)
print(math.tan(45))

list = ["qwe","vkg","sg","dg"]
print(random.choice(list))
print(random.randint(1,100))
