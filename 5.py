# Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(lst1,lst2):
    result=False
    for i in lst1:
        for j in lst2:
            if i==j:
                result= True
    return result
                
print(common_member([1,2,3,4],[5,6,7,8]))
print(common_member([1,2,3,4],[4,6,7,8]))