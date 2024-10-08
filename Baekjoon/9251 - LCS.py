#G5_9251_LCS

def lcs(a,b):
  n=len(a)
  m=len(b)

  dp=[[0]*(m+1) for i in range(n+1)]

  for i in range(1,n+1):
    for j in range(1,m+1):
      if a[i-1]==b[j-1]:
        dp[i][j]=dp[i-1][j-1]+1

      else:
        dp[i][j]=max(dp[i][j-1], dp[i-1][j])

  return dp[-1][-1]

a=input()
b=input()
print(lcs(a,b))
