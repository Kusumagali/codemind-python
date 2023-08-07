a = int(input())
b = int(input())
l1,l2 = [],[]
for i in range(1,a):
    if a%i==0:
        l1.append(i)
for j in range(1,b):
    if b%j == 0:
        l2.append(j)
if sum(l1) == b and sum(l2) == a:
    print("Amicable")
else:
    print("Not Amicable")