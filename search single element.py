def single(arr,n):
    low,high=1,n-2
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid-1]!=arr[mid]!=arr[mid+1]:
            return arr[mid]
        if mid%2==1 and  arr[mid-1]==arr[mid] or mid%2==0 and arr[mid]==arr[mid+1]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,1,2,2,3,3,4,5,5,6,6,7,7]
print(single(arr,len(arr)))