#B4_10188_Quadrilateral 

n=int(input())
for t in range(n):
  a,b=map(int,input().split())
  
  for i in range(b):
    print("X"*a)

  if t!=n-1:
    print()
