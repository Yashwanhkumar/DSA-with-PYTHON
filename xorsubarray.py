arr = [4, 2, 2, 6, 4]
n = len(arr)
xr = 0
target = 6
cnt = 0
dic = {0: 1}  # Initialize with 0 XOR seen once

for i in range(n):
    xr ^= arr[i]
    x = xr ^ target
    cnt += dic.get(x, 0)  # Add all previous occurrences of x
    dic[xr] = dic.get(xr, 0) + 1  # Update frequency safely

print(cnt)  # Output: 4
