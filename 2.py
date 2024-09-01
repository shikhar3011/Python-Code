# Write a Python program to remove duplicates from a list
def remove_duplicate(lst):
    for i in lst:
        if lst.count(i)>1:
            lst.remove(i)
    return lst

print(remove_duplicate([10,20,30,20,10,50,60,40,80,50,40]))

