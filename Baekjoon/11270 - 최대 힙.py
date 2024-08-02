#S2_11270_최대 힙

import sys
from heapq import heappush, heappop

def maxHeap(n,num):
  h=[]

  for x in num:
    if x==0:
      if h:
        print(-heappop(h))
      else:
        print(0)
    else:
      heappush(h,-x)

input=sys.stdin.read
data=input().split()
n=int(data[0])
num=list(map(int,data[1:]))
maxHeap(n,num)
