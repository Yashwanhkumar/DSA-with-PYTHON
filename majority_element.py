arr=[1,2]
n=len(arr)
cnt1,cnt2=0,0
el1,el2=None,None
for i in range(n):
    if cnt1==0 and arr[i]!=el2:
        cnt1=1
        el1=arr[i]
    elif cnt2==0 and arr[i] != el1:
        cnt2=1
        el2=arr[i]
    elif el1==arr[i]:
        cnt1+=1
    elif el2==arr[i]:
        cnt2+=1
    else:
        cnt1-=1
        cnt2-=1
cn1,cn2=0,0
ls=[]
for i in range(n):
    if el1==arr[i]:
        cn1+=1
    elif el2==arr[i]:
        cn2+=1
if cn1 > n//3:
    ls.append(el1)
if cn2 > n//3 and el2 != el1:
    ls.append(el2)
print(ls)
    