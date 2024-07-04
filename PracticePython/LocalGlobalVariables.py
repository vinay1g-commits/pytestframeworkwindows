#local Variable Example
#def local_forvar():
 #   name = "vinay"
  #  print(name)

#Global Variable
#name = "vinay"
#def global_var():
 #   name="pandit"
  #  print(name)

#print(name)

#using Global keyword
name="vinay"
def what():
    global name
    name = "pandit"
    print(name)

what()
print(name)
