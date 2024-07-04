import re

pattern7="^vinay" # text line should start with vinay
pattern8="giri$" #text line should end with giri
pattern9="v..y" #matches any character except newline
pattern10="^vinay kumar giri$"#starts with vinay and ends with giri
pattern11="v.*y"#in between v and y anything
pattern12="v.+y"#between v and y you have to give one time something
pattern13="v.?y"#it eill accept vy also
pattern14="v.{2}y"
pattern15="[a-z]ython|[A-Z]ython"
print("Enter a text to match with the pattern")
text=input()
if re.search(pattern15,text):
    print("pattern matched with the text")
else:
    print("entered pattern didn't match with the text")