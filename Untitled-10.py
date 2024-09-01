def substr(str,n):
    if len(str)>=2:
        return((str[:2])*n)
    else:
        return(str*n)

str=input('enter any string\n')
n=int(input('enter any number\n'))
print(substr(str,n))