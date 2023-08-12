def fun(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1
    
a = int(input())
b = int(input())
c = a+b
d = c+1
while 1:
    if fun(d):
        print(abs(d-c))
        break
    d+=1