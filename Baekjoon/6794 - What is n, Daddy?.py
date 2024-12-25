#B3_6794_What is n, Daddy?

n=int(input())
c=0
for l in range(6):
    r=n-l
    if l>=r>=0:c+=1
print(c)
