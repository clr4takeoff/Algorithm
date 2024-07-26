#S3_2579_계단 오르기

def stair(a,n):
  if n==1:
    return a[1]
  elif n==2:
    return a[1]+a[2]

  else:
    dp=[0]*(n+1)

    dp[1]=a[1]
    dp[2]=a[1]+a[2]
    dp[3]=max(a[1]+a[3], a[2]+a[3])

    for i in range(4,n+1):
      dp[i]=max(a[i]+a[i-1]+dp[i-3], a[i]+dp[i-2])
    
    return dp[n]

a=[0]
n=int(input())
for i in range(n):
  a.append(int(input()))

print(stair(a,n))
