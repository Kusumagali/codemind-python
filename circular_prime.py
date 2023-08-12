def fun(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
    
n = int(input())
if fun(n) and fun(int(str(n)[::-1])):
    print("circular prime")
elif fun(n) and not fun(int(str(n)[::-1])):
    print("prime but not a circular prime")
else:
    print("not prime")