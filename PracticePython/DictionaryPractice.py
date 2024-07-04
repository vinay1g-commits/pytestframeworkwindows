bike1={
    "Honda":"Scooty",
    "Model":"Activa 6G",
    "Price":"100000",
    "Mileage":"50Kmpl"
}
bike2={
    "Honda":"Scooty",
    "Model":"Activa 6G 125cc",
    "Price":"100000",
    "Mileage":"50Kmpl"
}

print(bike2==bike1) #check if two dictionaries are equal
print(bike1!=bike2) #check if two dictionaries are not equal

print(bike1.get("Model")) #gives value of key "Model"
print(bike1["Model"]) #gives value of key "Model"

print(bike1.keys()) #getting keys
print(bike1.values()) #getting values

bike1["Model"]="Activa 5G" #updating key
print(bike1)

bike1["Total Run"] = "2500KM" #Adding a key value pair
print(bike1)

for x in bike1: #to get each key
    print(x)

for u in bike1.items(): # to get key values pairs
    print(u)

bike1.pop("Mileage")
print(bike1)

bike1.popitem()
print(bike1)

print(len(bike1))

del bike1
print(bike1)

bike1.clear()
print(bike1)