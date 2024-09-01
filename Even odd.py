# n=int(input())
# lst=[]
# even=''
# odd=''
# for i in range (n):
#     s=input()
#     lst.append(s)
# # print(lst)

# for i in lst:
#     for j in range (len(i)-1):
#         if j%2==0:
#             even+=i[j]
#         else:
#             odd+=i[j]
# print(even,odd)

for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])