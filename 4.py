# Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(lst,n):
    lw=[]
    for i in lst:
        if len(i)>n:
            lw.append(i)
    return lw

n=int(input('Enter the length :\n'))
lst=['shikhar','ajay','salman','amitabh','mahesh','allu','ram']
print('The list of words that are longer than',n,'is',long_words(lst,n))
            
    