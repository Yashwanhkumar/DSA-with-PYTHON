def first(arr,tar,n):
    low=0
    high=n-1
    first=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == tar:
            first=mid
            high=mid-1
        elif arr[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return first
def last(arr,tar,n):
    low=0
    high=n-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == tar:
            last=mid
            low=mid+1
        elif arr[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return last
arr=[1,2,2,2,3,4]
fs=first(arr,5,len(arr))
if fs==-1:
    print(-1,-1)
else:
    ls=last(arr,5,len(arr))
    print(fs,ls)

    