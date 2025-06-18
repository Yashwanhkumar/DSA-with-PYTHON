def findmissing(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < mid + k:
            low = mid + 1
        else:
            high = mid - 1
    return low + k
arr=[2,3,4,7,11]
print(findmissing(arr, 5))  # Output: 9