a=11
b=13
c=a+b
print("sum = ",c)
print("sum of  ",a,"  +   ",b,"     is   ",c)
print()
print()
x=None
if x:
    print("is none true")
elif x is False:    
    print("is none false")
else:
    print('none is none')
print()
print()
a,b= 4.5-7.1j,-5.4-3.9j
c=a+b
print("sum = ",c)
print("sum of  ",a,"  +   ",b,"     is   ",c)
print()
print()
print(type(a))
print(type(x))
print()
print()
p=45.2
print(p,int(p))
p1,z=33,9
print(p1,float(p1))
print(complex(z,p1))
print()
print()
n1=0b1111110
n2=0xdd
n3=0o22
print(n1,n2,n3)
print()
print()
sw='123'
sa='1100110'
saa='F83'
print(int(sw,8),int(sa,2),int(saa,16))
print()
print()
print(bin(22),oct(111),hex(33))
print()
print()
d=24<88
f=8>99
print(d+d+d-f+d-d)
print(f-f-f-f-f-d)
print(bool("cool"))
print(bool(111))
e="hi"
print(bool(e))
print()
print()
bool(["d",'f','d','e'])
bool(0)
bool("")
bool(())
print()
print()
st="welcome me and you and us"
t='welcom all'
o="""you have 'hema' hnn"""
print(o)
print(st[0])
print(st[-1])
print(st[-5:-1])
print(st[2:])
print()
print()
ele=[22,34,5,66]
print(bytes(ele))
r=bytes(ele)
print(r[0])
print()
print()
a=bytearray(ele)
for i in a:
    print(i)
a[1]=9
a[2]=0
print()
print()
l=['hi',9,'33',90.002,90+9j,'cool',True]
print(l[2:4])
print(l[-4:-1])
print(l)
p=list([l[0],l[5]])
print(p)
print()
tup=('too','late','to','regret',99,109)
print(tup[0],tup[-1:],tup[3])
print()
print()
p=tuple(tup[1])
print(p)
