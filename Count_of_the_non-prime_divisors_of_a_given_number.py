def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input())
c = 0
for i in range(1,n+1):
    if n%i == 0 and not fun(i):
        c+=1
print(c)