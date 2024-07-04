def sample(*args):
    for i in args:
        print(i)
sample(1,2,3,4)

# 2nd type we can use as

def sampletwo(a,s,c,f):
    print(a,s,c,f)
args=[11,12,13,14]
sampletwo(*args)
