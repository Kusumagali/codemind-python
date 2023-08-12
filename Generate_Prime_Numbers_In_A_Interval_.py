def fun(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if fun(i):
        print(i)