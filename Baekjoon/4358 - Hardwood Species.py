#S2_4358_Hardwood Species

import sys

d={}

while True:
    a=sys.stdin.readline().strip()
    if not a:
        break
    if a in d:
        d[a]+=1
    else:
        d[a]=1

total=sum(d.values())
keys=sorted(d.keys())

for k in keys:
    print(f"{k} {(d[k]/total)*100:.4f}")
