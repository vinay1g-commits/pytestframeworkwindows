class exceptn:
#1st try except example
    print("start")
    try:
        a=10/0
    except ZeroDivisionError as z:
        print("exception is handled",z)
    print("End")
#2nd try except example
try:
    print ("enter a number")
    num = int(input())
    if num<10:
        print("not a valid number")
    else:
        print("valid number")
except ValueError as v:
    print("Exception is handled",v)
#3rd try except example raising error
try:
    print ("type yes or no if environment is good or bad respectively:")
    b=str(input())
    if b=="yes":
        print("environment is good")

    else:
        raise EnvironmentError("environment is bad")
except EnvironmentError as v:
    print("exception got handled",v )

#name exception
#try:
    #print(y)
#except TypeError as t: # type error exception is captured as an object referenced by t
    #print("exception got handled",t)


# multiple except block
try:
    a=10
except ZeroDivisionError as z:
    print("exception is handled",z)
except ValueError as v:
    print("exception handled ",v)
except TypeError as t:
    print("exception is handled:",t)
else:
    print("no exception")

finally:
    print("end of try catch examples")