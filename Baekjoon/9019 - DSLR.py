#G4_9019_DSLR

import sys
from collections import deque
input=sys.stdin.readline
N=10000
def bfs(a,b):
    if a==b:return ""
    qu=deque([(a,"")])
    visited=[False]*N
    visited[a]=True

    while qu:
        num,ops=qu.popleft()
        d=(num*2)%N
        if d==b:return ops+"D"
        if not visited[d]:
            visited[d]=True
            qu.append((d,ops+"D"))

        s=9999 if num==0 else num-1
        if s==b:return ops+"S"
        if not visited[s]:
            visited[s]=True
            qu.append((s,ops+"S"))

        l=(num%1000)*10+num//1000
        if l==b:return ops+"L"
        if not visited[l]:
            visited[l]=True
            qu.append((l,ops+"L"))
            
        r=(num%10)*1000+num//10
        if r==b:return ops+"R"
        if not visited[r]:
            visited[r]=True
            qu.append((r,ops+"R"))
    return ""

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(bfs(a,b))
