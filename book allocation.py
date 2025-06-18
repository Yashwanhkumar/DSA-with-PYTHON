def sol(arr,mid):
    n=len(arr)
    stu=1
    su=0
    for i in range(n):
        if su+arr[i]>mid:
            stu+=1
            su=arr[i]
        else:
            su+=arr[i]
    return stu
def bs(arr,stu):
    low=max(arr)
    high=sum(arr)
    ans=0
    while low <= high:
        mid=(low+high)//2
        if sol(arr,mid) >stu:
            low=mid+1
        else:
            high=mid-1
    return low
arr=[25,46,28,49,24]
print(bs(arr,4))

