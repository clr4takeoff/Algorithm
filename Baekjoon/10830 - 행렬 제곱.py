#G4_10830_행렬 제곱

def mul(X,Y,n):
  res=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        res[i][j]+=X[i][k] * Y[k][j]
      res[i][j]%=1000
  return res

def dc(a,b,n):
  if b==1:
    return [[a[i][j]%1000 for j in range(n)] for i in range(n)]
  tmp=dc(a,b//2,n)
  if b%2:
    return mul(mul(tmp,tmp,n),a,n)
  else:
    return mul(tmp,tmp,n)
       
n,b=map(int,input().split())
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
  
res=dc(a,b,n)

for i in res:
  print(" ".join(map(str,i)))
