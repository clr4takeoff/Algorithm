#S1_1149_RGB거리

def rgb(n,a):
  dp=[[-1]*3 for _ in range(n)]
  dp[0]=a[0][:]

  for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+a[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+a[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+a[i][2]
        
  return min(dp[n-1][0],dp[n-1][1],dp[n-1][2])
  

n=int(input())
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
print(rgb(n,a))
