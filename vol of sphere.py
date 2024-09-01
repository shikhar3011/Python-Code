import cmath
cn=input()
# cn=complex(cn)
x=int(cn[0])
y=int(cn[2])
print((x**2+y**2)**0.5)
ca=cmath.phase(y)
print(ca)