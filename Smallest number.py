# Smallest number
def small(lst):
    small=lst[0]
    for i in lst:
        if small>i:
            small=i
    return small

lst=[]
lenght=int(input('Enter lenght of list :\n'))
for i in range (0,lenght):
    print('Enter element number',i,':')
    value=int(input())
    lst.append(value)
print('Your list :',lst)
print('smallest element is',small(lst))
