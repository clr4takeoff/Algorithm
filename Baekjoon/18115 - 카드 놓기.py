#S3_18115_카드 놓기

from collections import deque

n=int(input())
a=list(map(int,input().split()))
card=deque()

for i in range(n-1,-1,-1):
  k=str(n-i)
  if a[i]==1:
    card.appendleft(k)
  elif a[i]==2:
    card.insert(1,k)
  else:
    card.append(k)

print(" ".join(card))
