def find(arr,n):
    low,high=0,n-1
    ans=float('inf')
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
arr=[4,5,6,7,1,2]
print(find(arr,len(arr)))          