import re

pattern = "vinay"
pattern1="[Vv]ina[yY]"
pattern2="[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]inay[0,1,2]"
pattern3="[a-z]inay[0-9]"
pattern4="[a-z][A-Z][0-9]inay"
pattern5="[^0-9]inay"
pattern6="[^a-z]inay"

print("Enter a text to match with the pattern")
text=input()
if re.search(pattern6,text):
    print("pattern matched with the text")
else:
    print("entered pattern didn't match with the text")


