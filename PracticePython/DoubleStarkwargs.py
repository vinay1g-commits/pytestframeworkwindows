def sample(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

sample(name="vinay",experience="6",age="36")
def sample_two(name,experience,age):
    print(name,experience,age)

dict= {"name":"daksh","experience":"2","age":2}
sample_two(**dict   )
