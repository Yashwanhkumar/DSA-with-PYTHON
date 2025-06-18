def search(arr,tar,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==tar:
            return mid
        if arr[low]==arr[mid]==arr[high]:
            low+=1
            high-=1
        elif arr[low]<=arr[mid]:
            if arr[low]<=tar<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<tar<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[3,1,2,3,3,3]
t=search(arr,1,len(arr))
print(t)