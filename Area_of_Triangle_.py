A,B,C=map(int,input().split())
S=(A+B+C)/2
area=(S*(S-A)*(S-B)*(S-C))**0.5
print('%0.2f'%area)