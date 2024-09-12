#B1_2033_반올림

n=input()
res=list(n)

for i in range(len(n)-1,0,-1):
  if int(res[i])>4:
    res[i-1]=str(int(res[i-1])+1)
  res[i]="0"

if res[0]=="10":
  res[0]="0"
  res.insert(0,"1")

print("".join(res))
