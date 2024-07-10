#S5_3699_주차 빌딩

for t in range(int(input())):
  h,l=map(int,input().split())
  a=[]
  mx=0
  time=0
  idx=1
  xpos=[0]*h

  for i in range(h):
    b=list(map(int,input().split()))
    a.append(b)
    if mx<max(a[i]):
      mx=max(a[i])

  while True:
    if idx>mx:
      break
    else:
      for i in range(h):
        for j in range(l):
          if a[i][j]==idx:
            
            time+=i*20

            if abs(j-xpos[i])>=l/2:
              time+=(l-abs(j-xpos[i]))*5
            else:
              time+=abs(j-xpos[i])*5

            xpos[i]=j

    idx+=1

  print(time)
