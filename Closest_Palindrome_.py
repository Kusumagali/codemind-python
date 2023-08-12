def fun(a):
    n = str(a)
    if n == n[::-1]:
        return True
    return False

n = int(input())
a = n-1
b = n+1
while 1:
    if fun(a) and fun(b):
        print(a,b)
        break
    elif fun(a):
        print(a)
        break
    elif fun(b):
        print(b)
        break
    else:
        a-=1
        b+=1
        
        
    