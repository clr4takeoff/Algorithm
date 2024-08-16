#G5_5430_AC

import sys
from collections import deque

def func(p,li):
    qu=deque(li)
    rv = False
    
    for cmd in p:
        if cmd=="R":
            rv=not rv
        elif cmd=="D":
            if not qu:
                return "error"
            if rv:
                qu.pop()
            else:
                qu.popleft()
    
    if rv:
        qu.reverse()
    
    return list(qu)

input=sys.stdin.readline
for _ in range(int(input())):
    p=input()
    n=int(input())
    s=input().strip()
    
    if s=="[]":
        li=[]
    else:
        li=list(map(int, s.strip("[]").split(",")))
    
    res=func(p,li)
    if res=="error":
        print(res)
    else:
        print("["+",".join(map(str,res))+"]")
