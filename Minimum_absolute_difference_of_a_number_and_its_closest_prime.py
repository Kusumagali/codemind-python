def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
    
n = int(input())
a = n+1
b = n-1
while 1:
    if fun(a):
        print(abs(n-a))
        break
    elif fun(b):
        print(abs(n-b))
        break
    elif fun(n):
        print(0)
        break
    a+=1
    b-=1