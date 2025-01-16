#S5_2669_직사각형 네개의 합집합의 면적 구하기

a=[[0]*101 for _ in range(101)]
for _ in range(4):
 x1,y1,x2,y2=map(int,input().split())
 for i in range(x1,x2):
  for j in range(y1,y2):a[i][j]=1
print(sum(sum(row)for row in a))
