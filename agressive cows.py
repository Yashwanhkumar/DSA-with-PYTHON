def sol(arr,mid,cows):
    n=len(arr)
    cowscnt=1
    last=arr[0]
    for i in range(n):
        if arr[i]-last>=mid:
            cowscnt+=1
            last=arr[i]
    if cowscnt >= cows:
        return True 
    else:
        return False
def bs(arr,cows):
    arr.sort()
    n=len(arr)
    low=0
    high=n-1
    ans=0
    while low<=high:
        mid=(low+high)//2
        if sol(arr,mid,cows)==True:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
arr=[0,3,4,7,9,10]
print(bs(arr,4))


