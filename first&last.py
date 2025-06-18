def lowerbound(arr, tar, n):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= tar:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperbound(arr, tar, n):
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > tar:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1, 2, 2, 2, 3, 4, 5]
n = len(arr)
tar = 2

lb = lowerbound(arr, tar, n)
# Check if target exists in the array
if lb == n or arr[lb] != tar:
    print(-1, -1)
else:
    ub = upperbound(arr, tar, n)
    print(lb, ub - 1)  # Output: 1 3
