def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def pal(n):
    n = str(i)
    if n == n[::-1]:
        return True
    return False
    
n = int(input())
i = n+1
while 1:
    if prime(i) and pal(i):
        print(i)
        break
    else:
        i+=1