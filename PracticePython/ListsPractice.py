a=[1,2,3,4]
b=["orange","banana","mango"]
c=[2,[6,7,4],9,4]
print(a) #print the list
print(a[3]) #print individual element from the list of index 3
print(b[1])
print(len(a)) #finds the length of the list

#for i in range(len(a)): #using for loop
    #print(a[i])

for eachelem in a:  #using for each loop
    print(eachelem)

a[1] = 1 # updating the element of the list
print(a)

a.append(12) #aapending list
print(a)

a.insert(2,2) #inserting an element in the list
print(a)

a.remove(2) #removing an element from the list
print(a)

a.pop() #popping last element of the list
print(a)

a.pop(1) #index wise poping of the element in the list
print(a)

a.clear() #clearing the list
print(a)

c.reverse() #reversing of the list
print(c)


b.sort() #sorting of the list
print(b)

q=b.index("mango") #getting index of element mentioned
print(q)

d=[2,[1,2,3,4],5,6,7] # nested list
print(d[1])
print(d[1][3])

e=[1,12.3,"qwerty",123] #list can store different type of datas
print(e[1])

f=[1,2,3,4,5,6,7,8,9]
print(f[-3]) #backward indexing
print(f[3]) #forward indexing

print(f[:]) #slicing the list
print(f[1:8])
print(f[:8])
print(f[1:])

g=[1,1,1,1,1,1,2,323,2,3,23] # to know the number of times a value in the list is repeated use count
print(g.count(1))

print(max(g)) # to get the maximum in the list

print(min(g)) # to get the minimum in the list

print(sum(g)) # to get the sum in the list

print(type(g)) # to get the type of the list

#x=[1.2,23423]
#del x
#print(x)

u=[1,1,2,3,4,23,34]
print(12 in u)

z= [12,345,5]
print(u+z)

u.extend(z)
print(u)
print(z)