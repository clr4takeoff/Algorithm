#S1_6064_Cain Calendar

def valid(m,n,x,y):
  k=x
  res=False
  while k<m*n+1:
    if (k-1)%n+1==y:
      return k
    k+=m
  return -1

for _ in range(int(input())):
  m,n,x,y=map(int,input().split())
  print(valid(m,n,x,y))
