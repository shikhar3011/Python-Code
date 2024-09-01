# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
def more(lst):
    new=[]
    for i in lst:
        if lst.index(i)>4 and i>=1 and i<=30:
            new.append(i**2)
    return new

lst = [0,1,2,3,4,5,6,7,8,9,32]
print(more(lst))

