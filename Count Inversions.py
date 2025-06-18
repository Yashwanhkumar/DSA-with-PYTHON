def mergesort(arr, low, high):
    if low >= high:
        return 0
    mid = (low + high) // 2
    inv_count = mergesort(arr, low, mid)
    inv_count += mergesort(arr, mid + 1, high)
    
    inv_count += merge(arr, low, mid, high)
    return inv_count

def merge(arr, low, mid, high):
    cnt = 0
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += mid - left + 1
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[low + i] = temp[i]
    return cnt

arr = [12, 44, 3, 42, 889, 9]
n = len(arr)
inv_count = mergesort(arr, 0, n - 1)
print(arr)
print("Inversion count:", inv_count)
