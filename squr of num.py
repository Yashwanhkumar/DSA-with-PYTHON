def squr(n):
    low,high=1,n
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid <=n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
n=36
print(squr(n))
