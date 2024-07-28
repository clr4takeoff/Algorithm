#S2_1541_잃어버린 괄호

s=input()
li=s.split('-')

res=sum(map(int,li[0].split('+')))
for i in range(1,len(li)):
  res-=sum(map(int, li[i].split('+')))

print(res)
