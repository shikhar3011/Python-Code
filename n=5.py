n=5

for i in range (1,n+1):
    if (i<=2 or i==n):
        for j in range(1,i+1):
            print(j,end=' ')
    else:
        print(1,end=' ')
        for j in range(1,i+1):
            print(end=' ')
        print(i,end=' ')
    print()

# 1 
# 1 2
# 1    3
# 1      4
# 1 2 3 4 5

