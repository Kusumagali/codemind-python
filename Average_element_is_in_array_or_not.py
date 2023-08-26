n = int(input())
arr = list(map(int,input().split()))
def fun(arr,k):
    return k in arr
a = sum(arr)//n
print(fun(arr,a))