#B3_10707_수도요금

a=int(input())
b=int(input())
c=int(input())
d=int(input())
p=int(input())

billX=a*p
billY=b if p<c else b+(p-c)*d 

print(min(billX,billY))
