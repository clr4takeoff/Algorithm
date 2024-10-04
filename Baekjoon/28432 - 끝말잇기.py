#S5_28432_끝말잇기

li=[]
idx=-1

n=int(input())
for i in range(n):
  s=input()
  li.append(s)
  if s=="?":
    idx=i
    
prev=li[idx-1] if idx>0 else None
next=li[idx+1] if idx<n-1 else None

for _ in range(int(input())):
  a=input()

  if prev and prev[-1]!=a[0]:
    continue
   
  if next and next[0]!=a[-1]:
    continue

  if a in li:
    continue

  print(a)
  break
