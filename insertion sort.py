arr=[12,17,6,122,7]
n=len(arr)
for i in range(n):
    while i>0 and arr[i-1]>arr[i]:
        arr[i],arr[i-1]=arr[i-1],arr[i]
        i-=1
print(arr)