#G5_12865_평범한 배낭

def bag(n,k,a):
  dp=[[0]*(k+1) for _ in range(n+1)]

  for i in range(k+1):
    for j in range(1,n+1):
      w,v=a[j-1]
      if w>i:
        dp[j][i]=dp[j-1][i]
      else:
        dp[j][i]=max(dp[j-1][i],dp[j-1][i-w]+v)
  
  return dp[-1][-1]


n,k=map(int,input().split())
a=[]
for _ in range(n):
  a.append(list(map(int,input().split())))
print(bag(n,k,a))
