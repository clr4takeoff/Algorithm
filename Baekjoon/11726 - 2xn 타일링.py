#S3_11726_2xn 타일링

n=int(input())
a=[0]*1001
a[1]=1
a[2]=2

for i in range(3,n+1):
  a[i]=a[i-1]+a[i-2]

if a[n]<10007:
  print(a[n])
else:
  print(a[n]%10007)