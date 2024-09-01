# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even(lst):
    for i in lst:
        if i%2==0:
            lst.remove(i)
    return lst

lst=[1,2,3,4,5,6,7,8,9,10]
print('Original list :',lst)
print('New list      :',remove_even(lst))