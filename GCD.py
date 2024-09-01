a=int(input('Enter first number\n'))
b=int(input('Enter second number\n'))
if a>b:
    mn=b
else:
    mn=a
for i in range (1, mn+1):
    if a%i==0 and b%i==0:
        d=i

print('GCD of',a,'and',b,'is',d)