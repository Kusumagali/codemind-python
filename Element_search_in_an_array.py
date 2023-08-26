n = int(input())
arr = list(map(int,input().split()))
k = int(input())
def fun(arr,k):
    return k in arr
print(fun(arr,k))