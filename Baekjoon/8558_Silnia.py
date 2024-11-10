#B4_8558_Silnia

n=int(input())
res=1
for i in range(1,n+1):
  res*=i
  res%=10
print(res)
