# major difference between set and frozenset is set is mutable(can be updated)
#whereas frozen set is immutable(cannot be updated)

s=frozenset({1,2,3,4,5,56,6,8})
print(type(s))
s.add(12)
print(s)
