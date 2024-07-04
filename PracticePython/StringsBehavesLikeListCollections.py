# String can be stored in 3 ways in python
name1="vinay kumar giri"
name2='sanju giri'
name3=str("1234")
print(name1,name2,name3)
print(type(name1))

# Strings works like collection list

print(name1[0])
print(len(name1))
for i in range(len(name1)):
    print(name1[i])

for j in name2:
    print(j)

print("kumar" in name1)
print("kumar" in name2)

#slicing the Strings
print(name1[0:2])
print(name1[0:])
print(name1[:15])

#modifying the Stringd
print(name1.upper())
print(name1.lower())
print(name2.capitalize())
print(name2.title())

example = "     qwerty     "
print(example.strip())
print(name1.split(" "))
print(example.replace("q","u"))

""" Strings are immutable if we assign same variable name to two vlaues of string
 the strings the varaible name will simply start referencing to the 2nd value and the first value will remain as it is in the memory """
name="wetgrt"
print(id(name))
name="rgfgn"
print(id(name))
print(id(name1))
print(id(name2))
print(id(name3))
print(id(example))

repeatedWords = " vinay kumar giri giri"
print(repeatedWords.count("giri"))

# to find the first instance of the word first letter occurence in the string
print(repeatedWords.find("giri"))

#to compare the two strings
print(name1==name3)
name4 = "Daksh"
name5="daksh"
print(name4 == name5)
print(name4.casefold()==name5)

