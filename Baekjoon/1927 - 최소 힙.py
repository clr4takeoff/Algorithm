#S2_1927_최소 힙

import sys
import heapq

input=sys.stdin.read
data=input().split()

n=int(data[0])
operations=[int(x) for x in data[1:]]

minHeap=[]
res=[]

for op in operations:
    if op==0:
        if minHeap:
            res.append(str(heapq.heappop(minHeap)))
        else:
            res.append('0')
    else:
        heapq.heappush(minHeap,op)

print("\n".join(res))
