# list is mutable whereas tuple is immutable(cannnot be updated)
# in list we use [] and for tuple we use ()

a=(1,(2,3,4,2),3,3,4,4,5)
print(a)
print(type(a))
print(a[1][2])

for i in range(len(a)): #for loop
    print(a[i])

for j in a: #for each loop
    print(j)

x=(1,[2,4,5,6],3,4,4,5,5,) # we can only update nested list inside tuple
x[1][1]=0
print(x)

z=tuple("vinay kumar giri")
print(z[6])
print(type(z))

# we can use sum et functions just like list refer notes

