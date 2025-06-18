def lowerbound(arr,tar,n):
    low=0
    high=n-1
    while low<=high:
        mid=low+high//2
        if arr[mid]>=tar:
            return mid
        if arr[mid]>tar:
            high=mid-1
        else:
            low=mid+1
arr=[1,2,3,4,5,6]
print(lowerbound(arr,7,len(arr)))