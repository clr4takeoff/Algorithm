#S3_1463_1로 만들기

import math

x=int(input())
d=[0]*(x+2)
d[1]=0

for i in range(2,x+1):
  if i%3==0:
    a=d[i//3]+1
  else:
    a=math.inf
  if i%2==0:
    b=d[i//2]+1
  else:
    b=math.inf

  d[i]=min(a,b,d[i-1]+1)
  
print(d[x])  
