#B2_1075_나누기

n=int(input())
f=int(input())
n=(n//100)*100
for i in range(100):
    if (n+i)%f==0:
        print(f"{i:02}")
        break
