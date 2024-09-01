# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def same(lst):
    count=0
    for i in lst:
        if len(lst)>1 and i[0]==i[-1]:
            count=count+1
    return count

lst = ['abc', 'xyz', 'aba', '1221']
print(same(lst))

