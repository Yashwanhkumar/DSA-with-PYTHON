def median(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    if n > m:
        return median(arr2, arr1)
    low = 0
    high = n
    while low <= high:
        mid1 = (low + high) // 2
        left = (n + m + 1) // 2
        mid2 = left - mid1

        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')

        if mid1 < n:
            r1 = arr1[mid1]
        if mid2 < m:
            r2 = arr2[mid2]
        if mid1 > 0:
            l1 = arr1[mid1 - 1]
        if mid2 > 0:
            l2 = arr2[mid2 - 1]

        if l2 <= r1 and l1 <= r2:
            if (n + m) % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0.0

arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45, 60]
print("The median is", median(arr1, arr2))
