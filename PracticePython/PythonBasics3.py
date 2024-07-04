name ="Vinay kumar Giri"
experience = 6
location = "Ballia"
print("My name is" + name +" with experience of " + str( experience) + " and my location is " + location)
#print("My name is" + name +" with experience of " + experience, + " and my location is " + location)
print("My name is {} with experience of {} and my location is {}".format(name,experience,location))
print("My name is {2} with experience of {1} and my location is {0}".format(location,experience,name))
print("My name is %s. I have experience of %d and my location is %s"%(name,experience,location)) #u can also use %f for floating point numbers or %g