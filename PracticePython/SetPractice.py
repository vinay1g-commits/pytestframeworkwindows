a={1,2,3,4}
b={3,4,7,8}
print(a)
print(type(a))

#union
print(a.union(b))
print(a|b)

#intersection
print(a.intersection(b))
print(a&b)



#difference
print(a.difference(b))
print(a-b)
print(b-a)

#Symmetric difference
print(a.symmetric_difference(b))
print(a ^ b)

a.add(2)
print(a)
#we cna only use for each loop in set
for e in a:
   print(e)

a.update([2,4])
print(a)

a.remove(2)
print(a)

a.discard(10)
print(a)

a.pop()
print(a)

print(12 in a)

a.clear()
print(a)

z= {1,(2,1,2,4,3),3,4,5,67 }
print(z)  #there  is no indexing in set so dont use a[1][2] like that

u=[1,2,4,5]
f=set(u)
print(type(u))
print(type(f))