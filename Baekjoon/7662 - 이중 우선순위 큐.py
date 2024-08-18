#G4_7662_이중 우선순위 큐

import heapq,sys

input=sys.stdin.readline

def dpq(a):
  maxh=[]
  minh=[]
  visited={}
  
  for i in a:
    if i[0]=="I":
      num=int(i[1])
      heapq.heappush(minh,num)
      heapq.heappush(maxh,-num)
      if num in visited:
        visited[num]+=1
      else:
        visited[num]=1
    else:
      if maxh:
        if i[1]=="1":
          while maxh:
            num=-heapq.heappop(maxh)
            if visited[num]>0:
              visited[num]-=1
              break
        else:
          while minh:
            num=heapq.heappop(minh)
            if visited[num]>0:
              visited[num]-=1
              break


  while minh and visited[minh[0]]==0:
      heapq.heappop(minh)
  while maxh and visited[-maxh[0]]==0:
      heapq.heappop(maxh)

  if minh and maxh:
      return f"{-maxh[0]} {minh[0]}"
  else:
      return "EMPTY"

for _ in range(int(input())):
  k=int(input())
  a=[]
  for i in range(k):
    x,y=map(str,input().split())
    a.append([x,y])
  
  print(dpq(a))
