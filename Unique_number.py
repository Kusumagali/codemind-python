n = input()
l = []
d = {}
c = 0
for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d.values():
    if i>1:
        c=1
        break
if c == 1:
    print("Not Unique Number")
else:
    print("Unique Number")