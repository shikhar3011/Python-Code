# product of elements
lst=[]
lenght=int(input('Enter lenght of list :\n'))
for i in range (1,lenght+1):
    print('Enter element number',i,':')
    value=int(input())
    lst.append(value)
print('Your list :',lst)

product=1
for i in lst:
    product=product*i
print('Product is :',product)
