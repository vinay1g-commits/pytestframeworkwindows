a=9 #initialization variable a is initialized to value 9
a=12.345 # this is not initialization for a, it is called updation
A=6
q="vinay"
k='kumar'
e=True
s,d,f=1,2,3  #stores 3 different values of same data type in 3 different variables
z=x=c=3  #stores same values in all 3 variables
my_first_name = "vinay"
print(my_first_name) #snake case lower case with underscore used here for variable name
print(z,x,c)
print(s,d,f)
print(a)
print(A)
print(q)
print(k)
print(e)
print("the value of a is:",a) # print some variable data along with text

#finding data type of variables using type() function
print(type(a))
print(type(my_first_name))
print(type(e))

#type casting
g = int(1.23)
print(g)
m = int("8")
print(m+1)
o = float(9)
print(o)
t = str(9.45)
print(t+" is a number string")

#y=int("cantconvert") #thus provide only numbers to be typecasted to int
#print(y)

#Operators :
#Arithmetic Operators
a,b=5,4
print(a+b)
print(a/b)
print(a//b) #it will not consider decimal point
print(a%b) #gives remainder
print(a**b) #2 power of 2

#Assignment Operators(compound)
a,b=5,4
a+=b # a=a+b
print(a)
a-=b #a=a-b
print(a)
a/=b
print(a)
a%=b
print(a)
a//=b
print(a)

#Relational operators :
a,b,c,d,e=5,4,5,3,9
print(a==b)
print(a!=e)
print(a>b)
print(a>c)
print(e<a)
print(a>=c)
print(a>=e)
print(a<=b)

#Logical Operators:and or not
print(True and True)
print(True and False)
print(False or False)
print(True or False)
print(not True)
print(not (a>b))

#Comments
#sdgdgf

"""
Operator precedence :
•	() have the highest priority in Python
•	Followed by ** (Exponential operator)
•	Followed by * / % // (Have the same precedence)
•	Followed by + - (Have the same precedence)
•	Same precedence operators are evaluated from left to right
"""

