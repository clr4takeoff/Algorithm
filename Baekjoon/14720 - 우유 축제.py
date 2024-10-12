#B2_14720_우유 축제

n=int(input())
a=list(map(int,input().split()))

li=[]

for i in range(n):
  cnt=0
  milk=0
  for j in range(i,n):
    if a[j]==milk:
      cnt+=1
      milk=(milk+1)%3
  li.append(cnt)

li.sort()
print(li[-1])
