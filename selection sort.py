arr=[12,17,6,122,7]
n=len(arr)
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[j]<arr[mini]:
            mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
print(arr)