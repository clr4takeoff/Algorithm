#S2_2805_나무 자르기

n,m=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
l,r=0,a[-1]

while l<=r:
    mid=(l+r)//2
    total=0
    for x in a:
        if x>mid:
            total += x-mid
    if total >= m:
        l=mid+1
    else:
        r=mid-1

print(r)
