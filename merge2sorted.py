nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
n=3
m=3
left=n-1
right=0
while left >= 0 and right < m:
    if nums1[left]>nums2[right]:
        nums1[left],nums2[right]=nums2[right],nums1[left]
        left-=1
        right+=1
    else:
        break
for i in range(m+1):
    nums1[n]=nums2[right]
    n+=1 
    right+=1 
print(nums1)



