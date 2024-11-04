#B4_15372_A Simple Problem.

import sys
input=sys.stdin.read

data=input().split()
t=int(data[0])
results=[]

for i in range(1, t+1):
    n=int(data[i])
    results.append(str(n*n))

sys.stdout.write("\n".join(results)+"\n")
