#B3_2975_Transactions

while 1:
 b,t,a=input().split();b,a=int(b),int(a)
 if b==0 and t=="W" and a==0:break
 if t=="W":
  if b-a<-200:print("Not allowed")
  else:b-=a;print(b)
 elif t=="D":b+=a;print(b)
