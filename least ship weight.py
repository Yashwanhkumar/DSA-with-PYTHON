def sol(arr,mid):
    n=len(arr)
    days=1
    su=0
    for i in range(n):
        if su >  mid:
            days+=1
        else:
            su+=arr[i]
    return days
def bf(arr,h):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        if sol(arr,mid)<=h:
            high=mid-1
        else:
            low=mid+1
    return low
arr=[1,2,3,4,5,6,7,8,9,10]
print("the least capacity of ship is ",bf(arr,5))


        


