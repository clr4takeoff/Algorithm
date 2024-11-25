#B1_2748_피보나치 수 2

def fibo(n):
  dp=[0]*(n+1)
  if n==0:
    return 0
  elif n==1:
    return 1

  dp[0],dp[1]=0,1

  for i in range(2, n+1):
    dp[i]=dp[i-1]+dp[i-2]

  return dp[n]

n=int(input())
print(fibo(n))
