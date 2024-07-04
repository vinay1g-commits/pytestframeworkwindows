import datetime

date = datetime.datetime(2024,4,11,2,34,10)
print(date)

date2= datetime.datetime.now()
print(date2)

# refer https://docs.python.org/3/library/datetime.html for formats of day month etc
date3= date2.strftime("%dth %B, %Y") #11th April,2024
print(date3)