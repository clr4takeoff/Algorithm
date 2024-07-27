#S3_11727_2xn 타일링 2

def tiling(n):
  if n==1:
    return 1
  elif n==2:
    return 3
  else:
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=3

    for i in range(3,n+1):
      dp[i]=dp[i-1]+dp[i-2]*2
  return dp[n]

n=int(input())
print(tiling(n)%10007)
