# sum of elements
lst=[]
lenght=int(input('Enter lenght of list :\n'))
for i in range (1,lenght+1):
    print('Enter element number',i,':')
    value=int(input())
    lst.append(value)
print('Your list :',lst)
print('Sum of list :',sum(lst))
# sum=0
# for i in lst:
#     sum=sum+i
# print('sum of elements of lists :',sum)