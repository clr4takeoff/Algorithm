#G2_11444_피보나치 수 6

def mul(A,B,MOD):
  res=[[0]*2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      res[i][j]=(A[i][0]*B[0][j] + A[i][1]*B[1][j])%MOD
  return res
  
def dc(n,mtr,MOD):
  if n==1:
    return mtr
  tmp=dc(n//2,mtr,MOD)
  tmp=mul(tmp,tmp,MOD)
  if n%2:
    tmp=mul(tmp,mtr,MOD)
  return tmp

n=int(input())
base=[[1,1],[1,0]]
MOD=1000000007
print(dc(n,base,MOD)[0][1])
