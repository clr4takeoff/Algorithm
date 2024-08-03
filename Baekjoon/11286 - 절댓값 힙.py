#S1_11286_절댓값 힙

import sys
from heapq import heappush, heappop

def absHeap(n,num):
  h=[]

  for x in num:
    if x==0:
      if h:
        res=heappop(h)
        print(res[0]*res[1])
      else:
        print(0)
    else:
      if x<0:
        heappush(h,[abs(x),-1])
      else:
        heappush(h,[x,1])

input=sys.stdin.read
data=input().split()
n=int(data[0])
num=list(map(int,data[1:]))
absHeap(n,num)
