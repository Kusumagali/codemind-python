def fun(n):
    if n<2:return False
    for i in range(2,n):
        if n%i == 0:return False
    return True
    
n = int(input())
a = str(n)
c = 0
for i in a:
    if fun(int(i)):c+=1
if fun(n) and c==len(a):print("Mega Prime")
else:print("Not Mega Prime")