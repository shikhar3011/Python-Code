# largest element
def large(lst):
    lar=0
    for i in lst:
        if i>lar:
            lar=i
    return lar

lst=[]
lenght=int(input('Enter lenght of list :\n'))
for i in range (0,lenght):
    print('Enter element number',i,':')
    value=int(input())
    lst.append(value)
print('Your list :',lst)
print('Largest element is',large(lst))

