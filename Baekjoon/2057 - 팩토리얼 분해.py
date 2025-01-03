#S5_2057_팩토리얼 분해

def s(n):
 if n==0:return print("NO")
 f=[1]
 for i in range(1,21):f.append(f[-1]*i)
 f=f[::-1]
 for x in f:
  if n>=x:n-=x
 print("YES"if n==0else"NO")
s(int(input()))
