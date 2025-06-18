def peak(arr,n):
    if n==1:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    low,high=1,n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return arr[mid]
        if arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[7,8,5,8,9,0]
print(peak(arr,len(arr)))