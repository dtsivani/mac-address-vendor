dec1=629
b1=bin(dec1)
print(b1)
print('decimal',dec1,'is',b1,'in binary')
o1=oct(dec1)
print(o1)
print('decimal',dec1,'is',o1,'in octal')
h1=hex(dec1)
print(h1)
print('decimal',dec1,'is',h1,'in hexadecimal')
'''
hi this is class
'''
s="welcome to sphoorthy engineering college !!!"
print(s)
print(s[0])
print(s[12:24])
print(s[17:])
print(s[-1])
print(s[-10])
print(s[-10:-20])
print(s[-20:-10])
print(s[-10:])
print(s[:-20])
print(s[:])
ele=[1,3,4,5,23,55,78]
x=bytes(ele)
print(x[3])
print(x[4])
print(x)
y=bytearray(ele)
for i in y:
    print(i)
y[0]=88
print(y[0])
