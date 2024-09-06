#S2_11053_가장 긴 증가하는 부분 수열

def lng(n,a):
  dp=[1]*n

  for i in range(n):
    for j in range(i):
      if a[i]>a[j]:
        dp[i]=max(dp[i],dp[j]+1)

  return max(dp)

n=int(input())
a=list(map(int,input().split()))
print(lng(n,a))
