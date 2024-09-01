# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def rem(lst):
    lst.remove(lst[0])
    lst.remove(lst[4])
    lst.remove(lst[-1])
    return lst

Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(len(Sample_List))
print(rem(Sample_List))
print(len(Sample_List))


