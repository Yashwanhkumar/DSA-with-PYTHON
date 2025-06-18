# cook your dish here
def lowerbound(arr,tar,n):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=tar:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,3,4,7,9]
print(lowerbound(arr,8,len(arr)))