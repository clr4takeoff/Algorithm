#B4_13866_팀 나누기

a,b,c,d=map(int,input().split())
s1=abs((a+b)-(c+d))
s2=abs((a+c)-(b+d))
s3=abs((a+d)-(b+c))
print(min(s1,s2,s3))
