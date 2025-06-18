import math
def sol(arr,mid):
    n=len(arr)
    su=0
    for i in range(n):
        su+=math.ceil(arr[i]/mid)
    return su
def koko(arr,h):
    low,high=1,max(arr)
    ans=float('inf')
    while low <= high:
        mid=(low+high)//2
        if sol(arr,mid)<=h:
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return low
arr=[30,11,23,4,20]
h=5
print(koko(arr,h))        

