#S1_1932_정수 삼각형

def hap(n,t):
  dp=[[0]*(i+1) for i in range(n)]
  dp[0][0]=t[0][0]

  for i in range(1,n):
    for j in range(i+1):
      if j==0:
        dp[i][j]=dp[i-1][j]+t[i][j]
      elif j==i:
        dp[i][j]=dp[i-1][j-1]+t[i][j]
      else:
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+t[i][j]

  return max(dp[-1])

n=int(input())
t=[]
for i in range(n):
  t.append(list(map(int,input().split())))
print(hap(n,t))
