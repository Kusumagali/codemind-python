n = input()
a = n[::-1]
c = int(n)**2
d = int(a)**2
if str(c) == str(d)[::-1]:
    print("True")
else:
    print("False")