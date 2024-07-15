#S5_6752_Time on task

n=int(input())
p=[]
cnt=0
total=0
for i in range(int(input())):
  p.append(int(input()))

p.sort()

for j in range(len(p)):
  if total+p[j]<= n:
    total+=p[j]
    cnt+=1
  else:
    break

print(cnt)
