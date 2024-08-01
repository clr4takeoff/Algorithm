#S2_30804_fruits Tanghulu

def tanghulu(fruits, n):
  if n==0:
    return 0

  cnt={}
  mx=0
  s=0

  for e in range(n):
    if fruits[e] in cnt:
      cnt[fruits[e]]+=1
    else:
      cnt[fruits[e]]=1

    while len(cnt)>2:
      cnt[fruits[s]]-=1
      if cnt[fruits[s]]==0:
        del cnt[fruits[s]]
      s+=1
    
    mx=max(mx, e-s+1)
  return mx

n=int(input())
fruits=list(map(int,input().split()))
print(tanghulu(fruits,n))
