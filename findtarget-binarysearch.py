def target(arr,tar,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==tar:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=tar and tar<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=tar and tar<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1    
arr=[7,8,9,1,2,3,4,5,6]
print(target(arr,1,len(arr)))