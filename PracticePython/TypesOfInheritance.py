#sigle level inheritance
class A:
    a=23
class B(A):
    b=34
obj_single = B()
print(obj_single.a)
print(obj_single.b)

#Multievel Inheritance
class c:
    c=243
class d(c):
    d=78
class e(d):
    e=568
obj_multi = e()
print(obj_multi.c)
print(obj_multi.d)
print(obj_multi.e)

#Hierarchical level inheritance
class f:
    f=56
class g(f):
    g=46
class h(f):
    h=678
obj_hierar = h()
print(obj_hierar.f)
# print(obj_hierar.g) This gives error bcz h is not child of g
print(obj_hierar.h)

#multiple Inheritance
class i:
    i=54
class j:
    j=345
class k(i,j):
    k=34
obj_multipl = k()
print(obj_multipl.i)
print(obj_multipl.j)
print(obj_multipl.k)

#Hybrid Inheritance
class l:
    l=457
class m(l):
    m=456
class n(l):
    n=345
class o(m,n):
    o=678
obj_hybrid= o()
print(obj_hybrid.l)
print(obj_hybrid.m)
print(obj_hybrid.n)
print(obj_hybrid.o)