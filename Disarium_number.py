n = input()
c = 0
for i in range(len(n)):
    c += int(n[i]) ** (i+1)
if int(n) == c:
    print("True")
else:
    print("False")