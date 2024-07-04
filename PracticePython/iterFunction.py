a=[1,2,3,4]
str = iter(a)
print(next(str))
print(next(str))
print(next(str))
print(next(str))

b=[1,2,3,4]
str = iter(b)
for some in str:
    print(some)