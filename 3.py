
# Write a Python program to check a list is empty or not
def empty(lst):
    if len(lst)==0:
        return 1
    else:
        return 0

lst=[1,2,3]
y=empty(lst)
if y==1:
    print('Given list is an empty list')
else:
    print('Given list is not an empty list')

