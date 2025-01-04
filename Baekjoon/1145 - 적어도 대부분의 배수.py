#B1_1145_적어도 대부분의 배수

a=list(map(int,input().split()))
m=min(a)
while True:
 c=0
 for i in a:
  if m%i==0:c+=1
 if c>=3:break
 m+=1
print(m)
